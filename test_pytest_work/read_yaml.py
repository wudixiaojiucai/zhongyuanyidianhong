import yaml


def read_yaml(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    result = yaml.safe_load(content)
    return result
