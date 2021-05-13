import arrow
import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log=logging.getLogger(__name__)
import sys
sys.path.append("..")
import acp_times

def test_cd_less_than_0():
    time=arrow.now()
    assert acp_times.open_time(-1,200,time)=="unrecognized control point measurement"
    assert acp_times.close_time(-1,200,time)=="unrecognized control point measurement"

def test_cd_exact_0():
    time=arrow.now()
    assert acp_times.open_time(0,200,time)==time
    assert acp_times.close_time(0,200,time)==time.shift(hours=1)


def test_cd_over_bd_twenty_percent():
    time=arrow.now()
    assert acp_times.open_time(250,200,time)=="the control point is over 20% longer than the theoretical distance"
    assert acp_times.close_time(250,200,time)=="the control point is over 20% longer than the theoretical distance"

def test_cd_0_200():
    time=arrow.now()
    assert acp_times.open_time(112,200,time)==time.shift(hours=3,minutes=18)
    assert acp_times.close_time(112,200,time)==time.shift(hours=7,minutes=28)


def test_cd_200_400():
    time=arrow.now()
    assert acp_times.open_time(315,400,time)==time.shift(hours=9,minutes=29)
    assert acp_times.close_time(315,400,time)==time.shift(hours=21)


def test_cd_400_600():
    time=arrow.now()
    assert acp_times.open_time(600,600,time)==time.shift(hours=18,minutes=48)
    assert acp_times.close_time(600,600,time)==time.shift(days=1,hours=16)


def test_cd_600_1000():
    time=arrow.now()
    assert acp_times.open_time(789,1000,time)==time.shift(days=1,hours=1,minutes=33)
    assert acp_times.close_time(789,1000,time)==time.shift(days=2,hours=8,minutes=32)
