# -*- encoding=utf8 -*-
__author__ = "aijinka"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100",])


# script content
print("start...")

poco("t")
poco("e")
poco("s")
poco("t")
poco("e")
poco("r")
poco("3")
poco("5")
poco("0")
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)