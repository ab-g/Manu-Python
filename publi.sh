#!/usr/bin/env bash

git add . && git commit -m "Refactoring" \
  && git tag v0.26.6 -m '0.26.6 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
