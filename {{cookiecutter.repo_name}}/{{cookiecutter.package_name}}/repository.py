from dagster import RepositoryDefinition
from {{cookiecutter.package_name}}.pipelines import *


def define_repo():
    return RepositoryDefinition(
        name="{{cookiecutter.package_name}}",
        pipeline_dict={
            "preprocess_pipeline": lambda: preprocess_pipeline,
            "feature_eng_pipeline": lambda: feature_eng_pipeline,
            "train_pipeline": lambda: train_pipeline,
            "predict_pipeline": lambda: predict_pipeline,
        },
    )
