from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="YuvarajuM",
    description="A small package for dvc dl tensorflow pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YuvarajuM/DVC_DL_Tensorflow",
    author_email="rajbonvoyage54@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'boto3'
        'botocore'
        'dvc'
        'matplotlib'
        'pandas'
        'PyYAML'
        'tensorflow'
        'tqdm'
        'joblib'
        'scipy'
    ]
)
