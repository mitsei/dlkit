from setuptools import setup

setup(
    name="DLKit Records",
    version="0.1.0",
    description="Digital Learning ToolKit Record Extensions",
    author="Jeff Merriman",
    author_email="birdland@mit.edu",
    url="https://mc3.mit.edu",
    license="MIT",
    install_requires=[
        "beautifulsoup4",
        "html5lib",
        "lxml",
        "sympy",
        "pymongo",
        "inflection"
    ]
)