#!/bin/bash
python -m coverage run -m unittest discover test
python -m coverage report
python -m coverage html
