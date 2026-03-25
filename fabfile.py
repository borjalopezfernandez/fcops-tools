import glob
import os

from fabric import task, executor
from loguru import logger


@task
def build(context):
    '''
    Build fcops binary wheel distribution
    '''
    cmd = 'python setup.py bdist_wheel'
    logger.info(cmd)
    context.run(cmd)


@task
def install(context):
    '''
    Install fcops latest built package with pip
    '''
    list_of_files   = glob.glob('dist/fcops*')
    latest_package  = max(list_of_files, key=os.path.getctime)
    cmd             = f"pip install {latest_package}"
    logger.info(cmd)
    context.run(cmd)


@task
def uninstall(context):
    '''
    Uninstall fcops package with pip
    '''
    cmd = 'pip uninstall -y fcops'
    logger.info(cmd)
    context.run(cmd)


@task
def update(context):
    '''
    Update fcops python package:
    > build 
    > uninstall
    > install
    '''
    build(context)
    uninstall(context)
    install(context)


@task
def test(context):
    '''
    Execution of unit tests:
    '''
    test_unit_parser_xml_ppf(context)
    test_unit_fcops_mpf_nppf(context)
    test_fcops_install(context)
    

@task
def test_unit_parser_xml_ppf(context):
    '''
    Execution of unit test test_parser_xml_ppf.py 
    '''
    cmd = 'python3 -m pytest test/test_parser_xml_ppf.py -v'
    logger.info(cmd)
    context.run(cmd)

@task
def test_unit_fcops_mpf_nppf(context):
    '''
    Execution of unit test:
    python -m pytest test/test_unit_fcops_mpf_ppf2kml.py::TestCLIIntegration::test_version_option -v
    python -m pytest test/test_unit_fcops_mpf_ppf2kml.py::TestCLIIntegration::test_command_file_config -v
    '''
    cmd = 'python3 -m pytest test/test_unit_fcops_mpf_ppf2kml.py -v'
    logger.info(cmd)
    context.run(cmd)

@task
def test_fcops_install(context):
    '''
    Execution of unit test test_parser_xml_ppf.py 
    '''
    cmd = 'python3 test/test_config_after_install.py'
    logger.info(cmd)
    context.run(cmd)