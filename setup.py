from setuptools import setup

setup(
    name="rf5_data",
    version="1.0.0",

    python_requires=">=3.9",
    install_requires=[
        "pydantic",
        "pyyaml",
        "pandas"
    ]
)