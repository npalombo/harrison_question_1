#!/bin/bash
#  Comment the line below at the right time
PATH=/usr/local/bin:$PATH
if [ -d "vEnv" ];
then
  	echo "vEnv exists"
else
	virtualenv --distribute vEnv
fi
source vEnv/bin/activate
pip install -r requirements.txt

export PATH
