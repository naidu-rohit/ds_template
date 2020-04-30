import yaml
from pathlib import Path
import datetime
from os import listdir
from os.path import isfile, join
import shutil


def ensure_exists(p: Path) -> Path:
    """
    Helper to ensure a directory exists.
    """
    p = Path(p)
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_config(path):
    with open(path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            config = None
            print(exc)
    return config


def save_configs(dst):
    src = "configs"
    for f in listdir(src):
        if isfile(join(src, f)):
            shutil.copy(join(src, f), dst)
