"""
Analysis command group implementation.

Provides commands for analyzing repository structure, dependencies,
complexity, quality, patterns, and security.
"""

from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from ..analyzers.factory import AnalyzerFactory
from ..storage.database import DatabaseManager
from ..utils.file_utils import scan_repository


console = Console()


@click.group()
def analyze():
    """🔍 Repository analysis commands."""
    pass


@analyze.command()
@click.argument("repository_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--exclude", 
    multiple=True, 
    help="Patterns to exclude (can be used multiple times)"
)
@click.option(
    "--format", 
    "output_format",
    type=click.Choice(["terminal", "json"], case_sensitive=False),
    default="terminal",
    help="Output format"
)
@click.pass_context
def structure(
    ctx: click.Context, 
    repository_path: Path, 
    exclude: tuple, 
    output_format: str
):
    """
    Analyze repository structure and file organization.
    
    Examines directory structure, file types, language distribution,
    and organization patterns to provide insights into project layout.
    
    Example:
        repo-analyzer analyze structure ./my-project --exclude "*.pyc" --exclude "__pycache__"
    """
    config = ctx.obj["config"]
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Scanning repository structure...", total=None)
        
        # Scan repository files
        files = scan_repository(
            repository_path, 
            exclude_patterns=list(exclude) + config.get("exclude_patterns", [])
        )
        
        progress.update(task, description="Analyzing file types...")
        
        # Analyze file structure
        analyzer_factory = AnalyzerFactory()
        structure_analyzer = analyzer_factory.get_structure_analyzer()
        
        analysis_result = structure_analyzer.analyze_repository(
            repository_path, files
        )
        
        progress.update(task, description="Generating report...")
    
    if output_format == "json":
        import json
        console.print(json.dumps(analysis_result.to_dict(), indent=2))
    else:
        # Display terminal formatted results
        _display_structure_analysis(analysis_result)


@analyze.command()
@click.argument("repository_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--language",
    help="Filter analysis by programming language"
)
@click.option(
    "--check-vulnerabilities",
    is_flag=True,
    help="Check for known vulnerable dependencies"
)
@click.pass_context
def dependencies(
    ctx: click.Context,
    repository_path: Path,
    language: Optional[str],
    check_vulnerabilities: bool
):
    """
    Analyze package dependencies and imports.
    
    Examines dependency files (package.json, requirements.txt, etc.),
    analyzes import statements, and detects circular dependencies.
    
    Example:
        repo-analyzer analyze dependencies ./my-project --language python --check-vulnerabilities
    """
    config = ctx.obj["config"]
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Analyzing dependencies...", total=None)
        
        analyzer_factory = AnalyzerFactory()
        dep_analyzer = analyzer_factory.get_dependency_analyzer()
        
        analysis_result = dep_analyzer.analyze_repository(
            repository_path, 
            language_filter=language,
            check_vulnerabilities=check_vulnerabilities
        )
        
        progress.update(task, description="Generating dependency report...")
    
    _display_dependency_analysis(analysis_result)


@analyze.command()
@click.argument("repository_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--threshold",
    type=int,
    default=10,
    help="Complexity threshold for warnings"
)
@click.option(
    "--include-tests",
    is_flag=True,
    help="Include test files in analysis"
)
@click.pass_context
def complexity(
    ctx: click.Context,
    repository_path: Path,
    threshold: int,
    include_tests: bool
):
    """
    Analyze code complexity metrics.
    
    Calculates cyclomatic complexity, cognitive complexity, and nesting
    depth for functions and methods across supported languages.
    
    Example:
        repo-analyzer analyze complexity ./my-project --threshold 15 --include-tests
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Calculating complexity metrics...", total=None)
        
        analyzer_factory = AnalyzerFactory()
        complexity_analyzer = analyzer_factory.get_complexity_analyzer()
        
        analysis_result = complexity_analyzer.analyze_repository(
            repository_path,
            complexity_threshold=threshold,
            include_tests=include_tests
        )
        
        progress.update(task, description="Generating complexity report...")
    
    _display_complexity_analysis(analysis_result, threshold)


@analyze.command()
@click.argument("repository_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--fail-on-regression",
    is_flag=True,
    help="Exit with error code if quality has regressed"
)
@click.option(
    "--compare-with",
    help="Git commit/branch to compare against"
)
@click.pass_context
def quality(
    ctx: click.Context,
    repository_path: Path,
    fail_on_regression: bool,
    compare_with: Optional[str]
):
    """
    Analyze overall code quality metrics.
    
    Generates comprehensive quality assessment including maintainability
    index, technical debt indicators, and quality trends.
    
    Example:
        repo-analyzer analyze quality ./my-project --compare-with HEAD~10 --fail-on-regression
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Analyzing code quality...", total=None)
        
        analyzer_factory = AnalyzerFactory()
        quality_analyzer = analyzer_factory.get_quality_analyzer()
        
        analysis_result = quality_analyzer.analyze_repository(
            repository_path,
            compare_commit=compare_with
        )
        
        progress.update(task, description="Generating quality report...")
    
    _display_quality_analysis(analysis_result)
    
    # Check for regression if requested
    if fail_on_regression and analysis_result.has_regression:
        console.print("[red]Quality regression detected! Failing build.[/red]")
        raise click.Abort()


def _display_structure_analysis(analysis_result):
    """Display structure analysis results in terminal format."""
    table = Table(title="📁 Repository Structure Analysis", show_header=True)
    table.add_column("Metric", style="cyan", width=20)
    table.add_column("Value", style="green")
    
    table.add_row("Total Files", str(analysis_result.total_files))
    table.add_row("Total Directories", str(analysis_result.total_directories))
    table.add_row("Lines of Code", f"{analysis_result.total_lines:,}")
    table.add_row("Primary Language", analysis_result.primary_language)
    table.add_row("Language Count", str(len(analysis_result.languages)))
    
    console.print(table)
    
    # Language distribution
    if analysis_result.languages:
        lang_table = Table(title="Programming Languages", show_header=True)
        lang_table.add_column("Language", style="cyan")
        lang_table.add_column("Files", style="yellow")
        lang_table.add_column("Percentage", style="green")
        
        for lang, stats in analysis_result.languages.items():
            percentage = (stats["files"] / analysis_result.total_files) * 100
            lang_table.add_row(
                lang,
                str(stats["files"]),
                f"{percentage:.1f}%"
            )
        
        console.print(lang_table)


def _display_dependency_analysis(analysis_result):
    """Display dependency analysis results."""
    table = Table(title="📦 Dependency Analysis", show_header=True)
    table.add_column("Package Manager", style="cyan")
    table.add_column("Direct Dependencies", style="yellow")
    table.add_column("Total Dependencies", style="green")
    table.add_column("Vulnerabilities", style="red")
    
    for pm, stats in analysis_result.package_managers.items():
        table.add_row(
            pm,
            str(stats.get("direct", 0)),
            str(stats.get("total", 0)),
            str(stats.get("vulnerabilities", 0))
        )
    
    console.print(table)
    
    if analysis_result.circular_dependencies:
        console.print("\n[yellow]⚠️  Circular Dependencies Detected:[/yellow]")
        for cycle in analysis_result.circular_dependencies:
            console.print(f"  • {' → '.join(cycle)}")


def _display_complexity_analysis(analysis_result, threshold):
    """Display complexity analysis results."""
    table = Table(title="📊 Complexity Analysis", show_header=True)
    table.add_column("File", style="cyan")
    table.add_column("Function", style="yellow")
    table.add_column("Complexity", style="green")
    table.add_column("Status", style="magenta")
    
    high_complexity_count = 0
    
    for file_result in analysis_result.files:
        for func in file_result.functions:
            status = "✅ Good" if func.complexity <= threshold else "⚠️  High"
            if func.complexity > threshold:
                high_complexity_count += 1
            
            table.add_row(
                str(file_result.file_path.name),
                func.name,
                str(func.complexity),
                status
            )
    
    console.print(table)
    
    # Summary
    summary_table = Table(title="Complexity Summary", show_header=True)
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="green")
    
    summary_table.add_row("Average Complexity", f"{analysis_result.average_complexity:.1f}")
    summary_table.add_row("Max Complexity", str(analysis_result.max_complexity))
    summary_table.add_row("High Complexity Functions", str(high_complexity_count))
    summary_table.add_row("Complexity Threshold", str(threshold))
    
    console.print(summary_table)


def _display_quality_analysis(analysis_result):
    """Display quality analysis results."""
    table = Table(title="🔍 Quality Analysis", show_header=True)
    table.add_column("Metric", style="cyan", width=25)
    table.add_column("Score", style="green", width=10)
    table.add_column("Status", style="magenta")
    
    table.add_row(
        "Overall Quality Score",
        f"{analysis_result.overall_score:.1f}/10",
        "✅ Good" if analysis_result.overall_score >= 7.0 else "⚠️  Needs Improvement"
    )
    table.add_row(
        "Maintainability Index",
        f"{analysis_result.maintainability_index:.1f}",
        "✅ Good" if analysis_result.maintainability_index >= 20 else "⚠️  Low"
    )
    table.add_row(
        "Technical Debt Ratio",
        f"{analysis_result.technical_debt_ratio:.1%}",
        "✅ Good" if analysis_result.technical_debt_ratio <= 0.05 else "⚠️  High"
    )
    
    console.print(table)
    
    if analysis_result.recommendations:
        console.print("\n[yellow]💡 Recommendations:[/yellow]")
        for rec in analysis_result.recommendations:
            console.print(f"  • {rec}")


if __name__ == "__main__":
    analyze()