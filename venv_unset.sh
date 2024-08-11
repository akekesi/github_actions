#!/bin/bash

venv_name=.venv_sample_project

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv_name
