from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """Data Ingestion Artifact"""
    trained_file_path: str
    test_file_path: str
    
@dataclass
class DataValidationArtifact:
    """Data Validation Artifact"""
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str
    
@dataclass
class DataTransformationArtifact:
    """Data Transformation Artifact"""
    transformed_train_file_path: str
    transformed_test_file_path: str
    transformed_object_file_path: str
    
@dataclass
class ClassificationMetricArtifact:
    """Classification Metric Artifact"""
    precision: float
    recall: float
    f1_score: float
    
@dataclass
class ModelTrainerArtifact:
    """Model Trainer Artifact"""
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact
