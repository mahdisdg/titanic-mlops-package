from setuptools import setup, find_packages

setup(
    name="titanic-mlops",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "pyyaml",
        "joblib"
    ]
)