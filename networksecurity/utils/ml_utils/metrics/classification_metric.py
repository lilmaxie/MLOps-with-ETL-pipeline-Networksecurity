import sys

from networksecurity.entity.artifact_entity import ClassificationMetricArtifact

from networksecurity.exception.exception import NetworkSecurityException

from sklearn.metrics import f1_score, precision_score, recall_score

def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    """
    Calculate classification metrics: precision, recall, and F1 score.
    
    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
        
    Returns:
        ClassificationMetricArtifact: Object containing precision, recall, and F1 score.
    """
    try:
        model_f1_score = f1_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        
        classfication_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision=model_precision_score,
            recall=model_recall_score
        )
        return classfication_metric
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)