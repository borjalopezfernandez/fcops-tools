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
    cmd             = f'fcops_maap_query_product --version'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    cmd             = f'fcops_maap_query_product --help'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)

    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_flex_l1b_obs(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_product --id FLX_L1B_OBS____20230712T075954_20230712T080232_20260325T161900_0158_100_064_0021_01 | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_flex_l1c_flxsyn(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_product --id  FLX_L1C_FLXSYN_20230712T075954_20230712T080232_20260325T180107_0158_100_064_0021_01 | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_flex_anc_orbres(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_product --id FLX_ANC_ORBRES_20230712T080232_20230712T080251_20260325T161747_0018_100_064_0180_01 | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")


def test_flex_anc_attres(print_separator):
    """
    GIVEN test_conversion
    WHEN 
    THEN
    """
    logger.info(f"START : {sys._getframe().f_code.co_name} / {version('fcops')}")
    cmd             = f'fcops_maap_query_product --id FLX_ANC_ATTRES_20230712T080232_20230712T080251_20260325T161747_0018_100_064_0180_01 | jq .properties.updated,.properties.created,.properties.start_datetime,.properties.end_datetime'
    logger.info(cmd)
    exit = os.system(cmd)
    assert(exit == 0)
    logger.info(f"END : {sys._getframe().f_code.co_name} / {version('fcops')}")