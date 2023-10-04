from setuptools import setup

setup(
    name="clean_folder",
    version="0.0.1",
    py_modules=["clean_folder.clean"],
    packages=["clean_folder"],
    author="STime",
    description="Sort and clean folders",
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:main"
        ]
    }
)