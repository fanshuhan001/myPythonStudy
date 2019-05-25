# --coding:utf-8 --

from nose.tools import *
import name

def setup():
    print("SETUP!")

def teardown():
    print("Tear down!")

def test_basic():
    print("I Ran!")
