import pytest
from dagster import execute_pipeline, execute_solid
import yaml
from {{cookiecutter.package_name}}.utils.common import *
from {{cookiecutter.package_name}}.pipelines import *


def test_preprocess_pipeline():
    config = read_config("tests/test_configs/preprocess.yaml")
    res = execute_pipeline(preprocess_pipeline, environment_dict=config)
    assert res.success
    for solid_res in res.solid_result_list:
        assert solid_res.success


def test_feature_pipeline():
    config = read_config("tests/test_configs/features.yaml")
    res = execute_pipeline(feature_eng_pipeline, environment_dict=config)
    assert res.success
    for solid_res in res.solid_result_list:
        assert solid_res.success


def test_train_pipeline():
    config = read_config("tests/test_configs/train.yaml")
    res = execute_pipeline(train_pipeline, environment_dict=config)
    assert res.success
    for solid_res in res.solid_result_list:
        assert solid_res.success
