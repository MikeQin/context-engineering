"""
CLI integration tests for repo-analyzer.

Tests the command-line interface functionality using Click's testing utilities.
"""

import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from repo_analyzer.cli import cli


class TestCLI:
    """Test suite for CLI functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_cli_help(self):
        """Test CLI help output."""
        result = self.runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Repo Analyzer" in result.output
        assert "analyze" in result.output
        assert "report" in result.output
    
    def test_cli_version(self):
        """Test version command."""
        result = self.runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "1.0.0" in result.output
    
    def test_info_command(self):
        """Test info command displays system information."""
        result = self.runner.invoke(cli, ["info"])
        assert result.exit_code == 0
        assert "Version" in result.output
        assert "Python Version" in result.output
    
    def test_analyze_help(self):
        """Test analyze command group help."""
        result = self.runner.invoke(cli, ["analyze", "--help"])
        assert result.exit_code == 0
        assert "structure" in result.output
        assert "dependencies" in result.output
        assert "complexity" in result.output
        assert "quality" in result.output


class TestAnalyzeCommands:
    """Test suite for analyze command group."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_analyze_structure_simple_project(self):
        """Test structure analysis on a simple project."""
        with self.runner.isolated_filesystem():
            # Create simple project structure
            Path("src").mkdir()
            Path("tests").mkdir()
            Path("src/main.py").write_text("print('hello world')")
            Path("src/utils.py").write_text("def helper(): pass")
            Path("tests/test_main.py").write_text("def test_main(): pass")
            Path("README.md").write_text("# Test Project")
            
            result = self.runner.invoke(cli, ["analyze", "structure", "."])
            
            assert result.exit_code == 0
            assert "Repository Structure Analysis" in result.output
            assert "Total Files" in result.output
    
    def test_analyze_structure_json_output(self):
        """Test structure analysis with JSON output format."""
        with self.runner.isolated_filesystem():
            # Create minimal project
            Path("main.py").write_text("print('hello')")
            
            result = self.runner.invoke(cli, [
                "analyze", "structure", ".", "--format", "json"
            ])
            
            assert result.exit_code == 0
            
            # Verify JSON output
            try:
                output_data = json.loads(result.output)
                assert "total_files" in output_data
                assert "total_directories" in output_data
            except json.JSONDecodeError:
                pytest.fail("Output is not valid JSON")
    
    def test_analyze_structure_with_excludes(self):
        """Test structure analysis with exclude patterns."""
        with self.runner.isolated_filesystem():
            # Create project with files to exclude
            Path("src").mkdir()
            Path("__pycache__").mkdir()
            Path("src/main.py").write_text("print('hello')")
            Path("src/main.pyc").write_text("compiled")
            Path("__pycache__/cache.pyc").write_text("cache")
            
            result = self.runner.invoke(cli, [
                "analyze", "structure", ".", 
                "--exclude", "*.pyc",
                "--exclude", "__pycache__"
            ])
            
            assert result.exit_code == 0
            assert "Repository Structure Analysis" in result.output
    
    def test_analyze_dependencies_python_project(self):
        """Test dependency analysis on Python project."""
        with self.runner.isolated_filesystem():
            # Create Python project with dependencies
            Path("requirements.txt").write_text("requests==2.28.0\\nclick>=8.0.0\\n")
            Path("main.py").write_text("import requests\\nimport click\\n")
            
            result = self.runner.invoke(cli, [
                "analyze", "dependencies", ".", "--language", "python"
            ])
            
            assert result.exit_code == 0
            assert "Dependency Analysis" in result.output
    
    def test_analyze_complexity_threshold(self):
        """Test complexity analysis with custom threshold."""
        with self.runner.isolated_filesystem():
            # Create file with complex function
            complex_code = '''
def complex_function(data):
    result = 0
    for item in data:
        if item > 0:
            if item % 2 == 0:
                result += item * 2
            else:
                result += item
        elif item < 0:
            if abs(item) > 10:
                result -= item
            else:
                result += abs(item)
    return result
'''
            Path("complex.py").write_text(complex_code)
            
            result = self.runner.invoke(cli, [
                "analyze", "complexity", ".", "--threshold", "5"
            ])
            
            assert result.exit_code == 0
            assert "Complexity Analysis" in result.output
    
    def test_analyze_quality_fail_on_regression(self):
        """Test quality analysis with regression detection."""
        with self.runner.isolated_filesystem():
            # Create minimal Python file
            Path("main.py").write_text("def hello(): print('world')")
            
            # This should pass since there's no comparison baseline
            result = self.runner.invoke(cli, [
                "analyze", "quality", ".", "--fail-on-regression"
            ])
            
            assert result.exit_code == 0
            assert "Quality Analysis" in result.output


class TestErrorHandling:
    """Test suite for error handling scenarios."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_analyze_nonexistent_directory(self):
        """Test error handling for non-existent directory."""
        result = self.runner.invoke(cli, [
            "analyze", "structure", "/nonexistent/directory"
        ])
        
        assert result.exit_code != 0
    
    def test_invalid_format_option(self):
        """Test error handling for invalid format option."""
        with self.runner.isolated_filesystem():
            Path("main.py").write_text("print('hello')")
            
            result = self.runner.invoke(cli, [
                "analyze", "structure", ".", "--format", "invalid"
            ])
            
            assert result.exit_code != 0
    
    def test_keyboard_interrupt_handling(self):
        """Test graceful handling of keyboard interrupt."""
        # This test would require mocking the analysis process
        # to simulate a KeyboardInterrupt during execution
        pass


class TestConfigIntegration:
    """Test suite for configuration integration."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()
    
    def test_custom_config_file(self):
        """Test using custom configuration file."""
        with self.runner.isolated_filesystem():
            # Create custom config
            config_content = '''
project:
  name: "Test Project"
  languages: ["python"]
  exclude_patterns: ["*.test"]

analysis:
  complexity:
    cyclomatic_threshold: 5
'''
            Path("custom.yml").write_text(config_content)
            Path("main.py").write_text("def hello(): pass")
            
            result = self.runner.invoke(cli, [
                "--config", "custom.yml",
                "analyze", "structure", "."
            ])
            
            assert result.exit_code == 0
    
    def test_verbose_output(self):
        """Test verbose output option."""
        with self.runner.isolated_filesystem():
            Path("main.py").write_text("print('hello')")
            
            result = self.runner.invoke(cli, [
                "--verbose",
                "analyze", "structure", "."
            ])
            
            assert result.exit_code == 0
    
    def test_quiet_output(self):
        """Test quiet output option."""
        with self.runner.isolated_filesystem():
            Path("main.py").write_text("print('hello')")
            
            result = self.runner.invoke(cli, [
                "--quiet",
                "analyze", "structure", "."
            ])
            
            assert result.exit_code == 0


if __name__ == "__main__":
    pytest.main([__file__])