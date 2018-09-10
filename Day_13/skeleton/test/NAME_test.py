from nose.tools import *
import NAME
import os

def setup():
    file_obj = open("test.txt", "w")
    file_obj.write("Check it once")
    file_obj.close()

def teardown():
    pass
    # os.remove("test.txt")
    # print ("Tear down")

def test_basic():
    file_obj = open("test.txt", "r")
    file_obj.read()
    file_obj.close()
