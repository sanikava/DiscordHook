@echo off
ECHO Installing the required packages!
TIMEOUT 3

py -3 -m pip install -U -r Modules.txt

ECHO Done!
PAUSE

