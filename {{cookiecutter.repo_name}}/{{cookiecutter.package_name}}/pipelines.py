import dagster as dag
import yaml
from datetime import datetime
from dagster import pipeline, PresetDefinition
from {{cookiecutter.package_name}}.tasks.features import *
from {{cookiecutter.package_name}}.tasks.preprocess import *
from {{cookiecutter.package_name}}.tasks.train import *
from {{cookiecutter.package_name}}.utils.common import *


@pipeline(
    preset_defs=[
        PresetDefinition(
            "dev", environment_dict=read_config("configs/preprocess.yaml"),
        ),
    ]
)
def preprocess_pipeline():
    pass

@pipeline(
    preset_defs=[
        PresetDefinition("dev", environment_dict=read_config("configs/features.yaml"),),
    ]
)
def feature_eng_pipeline():
    pass


@pipeline(
    preset_defs=[
        PresetDefinition("dev", environment_dict=read_config("configs/train.yaml"),),
    ]
)
def train_pipeline():
    pass


@pipeline
def predict_pipeline():
    pass