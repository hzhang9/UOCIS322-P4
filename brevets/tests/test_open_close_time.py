import sys
sys.path.append("..")
import app_times
import arrow
import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log=logging.getLogger(__name__)

def test_cd_less_than_0():
    time=arrow.now()
    assert acp_times.open_time(-1,200,arrow.now().isoformat())=="unrecognized control point measurement"
    assert acp_times.close_time(-1,200,arrow.now().isoformat())=="unrecognized control point measurement"

def test_cd_exact_0():
    time=arrow.now()
    assert acp_times.open_time(0,200,time.isoformat())==time
    assert acp_times.close_time(0,200,time.isoformat())==time

def test_cd_over_bd_twenty_percent():
    time=arrow.now()
    assert acp_times.open_time(250,200,time.isoformat())==
    assert acp_times.close_time(250,200,time.isoformat())==

def test_cd_0_200():
    time=arrow.now()
    assert acp_times.open_time(167,200,time.isoformat())==
    assert acp_times.close_time(167,200,time.isoformat())==


def test_cd_200_400():
    time=arrow.now()
    assert acp_times.open_time(257,400,time.isoformat())==
    assert acp_times.close_time(257,400,time.isoformat())==


def test_cd_400_600():
    time=arrow.now()
    assert acp_times.open_time(567,600,time.isoformat())==
    assert acp_times.close_time(567,600,time.isoformat())==


def test_cd_600_1000():
    time=arrow.now()
    assert acp_times.open_time(789,1000,time.isoformat())==
    assert acp_times.close_time(789,1000,time.isoformat())==
