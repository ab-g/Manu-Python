#!/usr/bin/env bash

git add . && git commit -m "Add function get_character_data" && git tag v0.7.0 -m '0.7.0 tag'
git push --tags origin
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
