@echo off
ECHO Checking Modules then launching program

py -3 -m pip install -U -r Modules.txt
py file.py

ECHO Opened!
PAUSE

