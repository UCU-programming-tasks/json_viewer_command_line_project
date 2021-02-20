import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_viewer-dyaroshevych",
    version="0.0.1",
    author="Dmytro Yaroshevych",
    author_email="dyaroshevych@gmail.com",
    description="A Python module to navigate through JSON files and output particular parts information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UCU-programming-tasks/json_viewer_command_line_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
