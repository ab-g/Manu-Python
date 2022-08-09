#!/usr/bin/env bash

git add . && git commit -m "Fix function get_human_readable_path_to_node_by_id" \
  && git tag v0.30.1 -m '0.30.1 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
