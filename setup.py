"""
FCOPS Tools - FLEX Mission Planning File Parser and Tools

Installation:
    pip install -e . 
    pip install wheel
    python setup.py bdist_wheel

Usage:
    fcops-ppf-parser --help
"""
from setuptools import setup, find_packages

setup(
    license_files           =   ['LICENSE'],
    python_requires         =   ">=3.12",
    name                    =   "fcops",
    version                 =   "0.0.0",
    description             =   "FLEX Core Payload Data Ground Segment Operations Service",
    author                  =   "FCOPS Team",
    long_description        =   open('README.md', encoding='utf-8').read() if False else "FLEX Mission Operations Tools",
    package_dir             =   {"fcops": "src/fcops"},
    packages                =   find_packages(where="src"),
    package_data            =   {'fcops': ['data/*']},
    include_package_data    =   True,
    scripts                 = ['src/fcops/fcops_mpf_ppf2kml'],
    install_requires        =   [
#        'eocfi',
        'click>=7.0',
        'pytest',
        'loguru',
        'lxml',
        'pystac_client',
        'pytz',
    ],
    extras_require          =   {
        'dev': ['pytest', 'pytest-cov'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)

print("Completed setup for fcops package")
print("✓ Build wheel with: python setup.py bdist_wheel")