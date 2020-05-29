from setuptools import find_packages, setup

from word_ladder import __version__ as version

setup(
    name="word_ladder",
    version=version,
    packages=find_packages(),
    install_requires=["click", "networkx"],
    entry_points={"console_scripts": ["word-ladder=word_ladder.cli:cli"]},
    include_package_data=True,
)
