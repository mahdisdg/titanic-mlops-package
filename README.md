# Titanic MLOps Package

A production‑ready Python package that implements a full MLOps workflow for the Titanic survival prediction problem.  
Features include configuration management, data cleaning, model training, unit tests, CI pipeline, and Docker containerization.

## Project Structure

titanic-mlops-package/

├── titanic_mlops/ # Python package (library code)

│ ├── init.py

│ ├── config.yaml # parameters and settings

│ ├── config.py # config loader

│ ├── data.py # data loading & cleaning

│ ├── model.py # train & save functions

│ └── utils.py # helper utilities

├── tests/ # pytest unit tests

│ ├── test_data.py

│ └── test_model.py

├── .github/

│ └── workflows/

│ └── ci.yml # GitHub Actions CI

├── Dockerfile # container definition

├── requirements.txt # pinned dependencies

├── setup.py # packaging script

└── README.md


## Installation

1. Clone the repository:  
    ```bash
    git clone https://github.com/<your-username>/titanic-mlops-package.git
    cd titanic-mlops-package
    ```
2. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
3. (Optional) Install as a package:  
    ```bash
    pip install .
    ```

## Usage

### 1. Prepare Data & Train Model

```bash
# place your raw CSV (e.g., train.csv) in data/raw/
python -m titanic_mlops.data --input data/raw/train.csv --output data/processed/titanic_clean.csv
python -m titanic_mlops.model --input data/processed/titanic_clean.csv --output models/model.pkl
```

### 2. Import & Predict in Python

```python
from titanic_mlops.data import load_and_clean
from titanic_mlops.model import train, save_model

# load and clean
df = load_and_clean("data/raw/train.csv")

# train and save
model = train(df)
save_model(model, "models/model.pkl")
```

## Configuration
All parameters live in ``titanic_mlops/config.yaml``:

``` yaml
seed: 42
features: ["Pclass", "Sex", "Age", "Fare"]
model_params:
  n_estimators: 100
  random_state: 42
```

You can override by editing ``config.yaml``.

## Testing
Run unit tests with pytest:

```bash
pytest --maxfail=1 --disable-warnings -q
```
## Continuous Integration
A GitHub Actions workflow (.github/workflows/ci.yml) will:
  1. Check out code
  2. Install dependencies
  3. Run pytest

CI runs on every push and pull request.

## Docker
Build and test in a container:

```bash
docker build -t titanic-mlops .
docker run --rm titanic-mlops
```

This runs all unit tests inside the container.
