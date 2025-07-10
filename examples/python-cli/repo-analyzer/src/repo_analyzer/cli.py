"""
Main CLI interface for repo-analyzer using Click framework.

This module defines the primary command-line interface structure and
coordinates with command modules for specific functionality.
"""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table

from . import __version__
from .commands import analyze, config, history, report
from .config.manager import ConfigManager
from .utils.output import setup_logging


console = Console()


@click.group()
@click.option(
    "--config",
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file",
)
@click.option(
    "--verbose", "-v", 
    is_flag=True, 
    help="Enable verbose output"
)
@click.option(
    "--quiet", "-q", 
    is_flag=True, 
    help="Suppress non-essential output"
)
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx: click.Context, config: Optional[Path], verbose: bool, quiet: bool):
    """
    🔍 Repo Analyzer - Comprehensive repository analysis tool
    
    Analyze code quality, patterns, dependencies, and metrics across
    multiple programming languages with professional reporting capabilities.
    
    Examples:
        repo-analyzer analyze structure ./my-project
        repo-analyzer report summary --format html
        repo-analyzer config init --preset python
    """
    # Ensure context object exists
    ctx.ensure_object(dict)
    
    # Setup logging and output
    log_level = "DEBUG" if verbose else "WARNING" if quiet else "INFO"
    setup_logging(log_level)
    
    # Initialize configuration manager
    config_manager = ConfigManager()
    if config:
        ctx.obj["config"] = config_manager.load_config(config)
    else:
        ctx.obj["config"] = config_manager.get_default_config()
    
    ctx.obj["verbose"] = verbose
    ctx.obj["quiet"] = quiet


@cli.command()
@click.pass_context
def info(ctx: click.Context):
    """Display system information and configuration status."""
    config = ctx.obj["config"]
    
    # Create information table
    table = Table(title="Repo Analyzer Information", show_header=True)
    table.add_column("Property", style="cyan", width=20)
    table.add_column("Value", style="green")
    
    table.add_row("Version", __version__)
    table.add_row("Python Version", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    table.add_row("Config Source", str(config.get("config_source", "default")))
    table.add_row("Supported Languages", ", ".join(config.get("supported_languages", [])))
    
    console.print(table)


# Register command groups
cli.add_command(analyze.analyze)
cli.add_command(report.report)
cli.add_command(config.config)
cli.add_command(history.history)


def main():
    """Main entry point for the CLI application."""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()