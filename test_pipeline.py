import pandas as pd
from pandas.api.types import is_categorical_dtype, is_object_dtype
from fraud_detection_model import pipeline
from fraud_detection_model.config.core import configfrom fraud_detection_model.processing.validation import validate_inputs 


def test_pipeline_most_frequent_imputer(pipeline_inputs):
    # Given
    X_train, _, _, _ = pipeline_inputs assert all( x in X_train.loc[:, X_train.isnull().any()].columns for x in config.model_config.impute_most_freq_cols )
    # When
    X_transformed = pipeline.fraud_detection_pipe[:1].fit_transform(X_train[:50])
    # Then
    assert all( x not in X_transformed.loc[:, X_transformed.isnull().any()].columns for x in config.model_config.impute_most_freq_cols )
def test_pipeline_aggregate_categorical(pipeline_inputs):
    # Given
    X_train, _, _, _ = pipeline_inputs  

    assert X_train["R_emaildomain"].nunique() == 60
    # When
    X_transformed = pipeline.fraud_detection_pipe[:2].fit_transform(X_train[:50])
    # Then
    assert X_transformed["R_emaildomain"].nunique() == 2