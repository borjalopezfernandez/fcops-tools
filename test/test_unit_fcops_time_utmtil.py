import sys
import os
import time
import pytest
from importlib.metadata import version

from loguru import logger

@pytest.fixture(scope = "function", autouse = True)
def test_setup():
    logger.info('test')
    logger.info('----------------- test_setup() -------------------')


@pytest.fixture
def print_separator():
    logger.debug("\n=========================================================================")


def test_options(print_separator):
    """
    GIVEN
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_time_utmtil --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'fcops_time_utmtil --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_exec(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_time_utmtil -s UTC=20230712T070000 -e UTC=20230712T073000'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


