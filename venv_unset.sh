#!/bin/bash

venv_name=.venv_github_actions

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv_name
