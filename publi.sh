#!/usr/bin/env bash

git add . && git commit -m "Add constants KEY_TO_DIR and DIR_TO_KEY" && git tag v0.9.0 -m '0.9.0 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
