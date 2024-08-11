#!/bin/bash

# variables
venv=.venv_github_actions
python_required="Python 3.12.0"
python_current=$(python --version 2>&1)
requirements=requirements.txt

# python version
if [[ $python_current != *"$python_required"* ]]; then
    echo "Virtual environment '$venv' is not created."
    echo "Python version current:  $python_current"
    echo "Python version required: $python_required"
    return 0
fi

# create venv
if [ ! -d $venv ]; then
    python -m venv $venv
else
    echo "Virtual environment '$venv' already exists."
    return 0
fi

# activate venv
if [[ -z $VIRTUAL_ENV ]]; then
    . $venv/Scripts/activate
else
    echo "Virtual environment '$venv' is already activated."
    return 0
fi

# pip install
pip install -r $requirements > /dev/null

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# message for use
echo 
echo "Command to activate or deactivate '$venv':"
echo "Activation:   . $venv/Scripts/activate"
echo "Deactivation: deactivate"
