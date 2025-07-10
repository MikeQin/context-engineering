"""
Base analyzer interface and common analysis data structures.

Provides abstract base classes and data models for all analyzer implementations.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any


@dataclass
class FileAnalysis:
    """Analysis results for a single file."""
    file_path: Path
    language: str
    lines_of_code: int
    complexity_score: float = 0.0
    quality_score: float = 0.0
    functions: List[Dict[str, Any]] = field(default_factory=list)
    classes: List[Dict[str, Any]] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    issues: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class DirectoryAnalysis:
    """Analysis results for directory structure."""
    directory_path: Path
    total_files: int
    total_directories: int
    total_lines: int
    languages: Dict[str, Dict[str, int]] = field(default_factory=dict)
    primary_language: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "directory_path": str(self.directory_path),
            "total_files": self.total_files,
            "total_directories": self.total_directories,
            "total_lines": self.total_lines,
            "languages": self.languages,
            "primary_language": self.primary_language
        }


@dataclass
class MetricsResult:
    """Code quality metrics for analysis results."""
    average_complexity: float
    max_complexity: int
    maintainability_index: float
    technical_debt_ratio: float
    overall_score: float
    recommendations: List[str] = field(default_factory=list)
    has_regression: bool = False


class BaseAnalyzer(ABC):
    """Abstract base class for all code analyzers."""
    
    @abstractmethod
    def analyze_file(self, file_path: Path) -> FileAnalysis:
        """
        Analyze a single file and return analysis results.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            FileAnalysis object containing analysis results
        """
        pass
    
    @abstractmethod
    def analyze_directory(self, dir_path: Path, files: List[Path]) -> DirectoryAnalysis:
        """
        Analyze directory structure and file organization.
        
        Args:
            dir_path: Path to the directory to analyze
            files: List of files found in the directory
            
        Returns:
            DirectoryAnalysis object containing structure analysis
        """
        pass
    
    @abstractmethod
    def calculate_metrics(self, analyses: List[FileAnalysis]) -> MetricsResult:
        """
        Calculate aggregate metrics from file analyses.
        
        Args:
            analyses: List of file analysis results
            
        Returns:
            MetricsResult object containing calculated metrics
        """
        pass
    
    def supports_language(self, language: str) -> bool:
        """
        Check if this analyzer supports the given language.
        
        Args:
            language: Programming language name
            
        Returns:
            True if language is supported, False otherwise
        """
        return language.lower() in self.get_supported_languages()
    
    @abstractmethod
    def get_supported_languages(self) -> List[str]:
        """
        Get list of programming languages supported by this analyzer.
        
        Returns:
            List of supported language names
        """
        pass