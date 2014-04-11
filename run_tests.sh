#!/bin/bash
set PYTHONPATH=`pwd`:$PYTHONPATH
./vEnv/bin/python -m unittest discover -v test