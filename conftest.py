import pytest
from sklearn.model_selection import train_test_split
from fraud_detection_model.config.core import config
from fraud_detection_model.processing.data_manager import (

load_datasets, 

load_interim_data

) 


@pytest.fixture(scope="session")
def pipeline_inputs():
    # import the training dataset
    dataset = load_datasets(transaction=config.app_config.train_transaction, identity=config.app_config.train_identity, )
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(

dataset[config.model_config.all_features], dataset[config.model_config.target],
test_size=config.model_config.test_size,
stratify=dataset[config.model_config.target],
random_state=config.model_config.random_state)
    return X_train, X_test, y_train, y_test