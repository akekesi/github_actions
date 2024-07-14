#!/bin/bash

venv_name=.venv_github_actions

# create venv
if [ ! -d $venv_name ]; then
    python -m venv $venv_name 
fi

# activate venv
if [[ -z $VIRTUAL_ENV ]]; then
    . $venv_name/Scripts/activate
fi

# pip install
pip install -r "requirements.txt"
