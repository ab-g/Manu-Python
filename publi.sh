#!/usr/bin/env bash

git add . && git commit -m "Add function find_node_by_id" && git tag v0.19.0 -m '0.19.0 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
