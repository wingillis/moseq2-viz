from setuptools import setup, find_packages
import codecs
import os


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='moseq2-viz',
    author='Datta Lab',
    description='To boldly go where no mouse has gone before',
    version=get_version("moseq2_viz/__init__.py"),
    packages=find_packages(),
    platforms=['mac', 'unix'],
    install_requires=[
        'click>=8.1',
        'cytoolz>=0.12',
        'dtaidistance>=2.3.13',
        'h5py>=3.13',
        'joblib>=1.4',
        'matplotlib>=3.10',
        'networkx>=3.0',
        'numpy>=2.2',
        'opencv-python-headless>=4.10',
        'pandas>=2.2',
        'psutil>=5.9',
        'pyarrow>=16.0',
        'ruamel-yaml>=0.18',
        'scikit-learn>=1.5',
        'scipy>=1.15',
        'seaborn>=0.13',
        'tqdm>=4.67',
    ],
    python_requires='>=3.12',
    entry_points={'console_scripts': ['moseq2-viz = moseq2_viz.cli:cli']}
)
