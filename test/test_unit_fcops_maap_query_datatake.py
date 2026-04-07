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
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_datatake --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'fcops_maap_query_datatake --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_GSV_L1B_OBS___(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_datatake --type L1B_OBS___ --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_csv_GSV_L1B_OBS___(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")

    import os
    import glob

    for f in glob.glob('fcops_maap_query_datatake_L1B_OBS____*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'fcops_maap_query_datatake --type L1B_OBS___ --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z --baseline 01 -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('fcops_maap_query_datatake_L1B_OBS____20230712T070000_20230712T090000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_GSV_L1C_FLXSYN(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_datatake --type L1C_FLXSYN --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_csv_GSV_L1C_FLXSYN(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")

    import os
    import glob

    for f in glob.glob('fcops_maap_query_datatake_L1C_FLXSYN*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'fcops_maap_query_datatake --type L1C_FLXSYN --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z --baseline 01 -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('fcops_maap_query_datatake_L1C_FLXSYN_20230712T070000_20230712T090000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_GSV_ANC_ROTLOS(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_datatake --type ANC_ROTLOS --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_csv_GSV_ANC_ROTLOS(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")

    import os
    import glob

    for f in glob.glob('fcops_maap_query_datatake_ANC_ROTLOS*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'fcops_maap_query_datatake --type ANC_ROTLOS --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z --baseline 01 -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('fcops_maap_query_datatake_ANC_ROTLOS_20230712T070000_20230712T090000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_GSV_ANC_ORBRES(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_datatake --type ANC_ORBRES --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_csv_GSV_ANC_ROTLOS(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")

    import os
    import glob

    for f in glob.glob('fcops_maap_query_datatake_ANC_ROTLOS*'):
        logger.debug(f'Removing previous result file: {f}')
        os.remove(f)
    cmd             = f'fcops_maap_query_datatake --type ANC_ROTLOS --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z --baseline 01 -C'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    results = glob.glob('fcops_maap_query_datatake_ANC_ROTLOS_20230712T070000_20230712T090000*')
    assert(len(results) == 1)
    logger.debug(f'Found result file: {results[0]}')

    with open(results[0], 'r') as csv_file:
        lines = csv_file.readlines()
        # Header + at least one data line
        assert(len(lines) > 1)
        for row in lines:
            logger.debug(row.strip())

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")