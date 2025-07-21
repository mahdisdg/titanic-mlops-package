import yaml

def load_config(path="titanic_mlops/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
