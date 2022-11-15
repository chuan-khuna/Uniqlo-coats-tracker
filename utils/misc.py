import yaml
import json
import os


def load_yaml(yaml_file: str) -> dict:
    with open(yaml_file, 'r') as f:
        dict_ = yaml.load(f, yaml.Loader)
    return dict_


def create_path_if_not_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)