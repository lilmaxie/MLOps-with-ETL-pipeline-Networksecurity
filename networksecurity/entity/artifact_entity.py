from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """Data Ingestion Artifact"""
    trained_file_path: str
    test_file_path: str