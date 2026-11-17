"""
FCOPS Tools - Operations Tools

Installation:
    pip install -e . 
    pip install wheel
    python setup.py bdist_wheel

"""

from setuptools import setup, find_packages

setup(
    license_files           =   ['LICENSE'],
    python_requires         =   '>=3.12',
    name                    =   'fcops',
    version                 =   '0.0.13',
    description             =   'FLEX Core Payload Data Ground Segment Operations Service',
    author                  =   'FCOPS Team',
    long_description        =   open('README.md', encoding='utf-8').read() if False else "FLEX Mission Operations Tools",
    packages                =   ['fcops', 'fcops.data'],
    package_dir             =   {'fcops': 'src/fcops', 'fcops.data': 'src/fcops/data'},
    package_data            =   {'fcops': ['data/*']},
    include_package_data    =   True,
    scripts                 =   [
                                    'src/fcops/fcops_cams_query_collection',
                                    'src/fcops/fcops_mpf_ppf2kml',
                                    'src/fcops/fcops_time_utmtil',
                                    'src/fcops/fcops_maap_query_datatake',
                                    'src/fcops/fcops_maap_query_datatake_id',
                                    'src/fcops/fcops_maap_query_raw_anc_aux',
                                    'src/fcops/fcops_maap_query_products',
                                    'src/fcops/fcops_maap_query_product'
                                ],
    install_requires        =   [
#        'eocfi',
        'cdsapi',
        'ecmwf-datastores-client',
        'click>=7.0',
        'pystac',
        'pytest',
        'loguru',
        'lxml',
        'pyproj',
        'pystac_client',
        'pytz',
        'shapely',
    ],
    extras_require          =   {
        'dev': ['pytest', 'pytest-cov'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: European Space Agency Community License – v2.4 Permissive License (ESA-CL-2.4)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)

print("Completed setup for fcops package")
print("✓ Build wheel with: python setup.py bdist_wheel")