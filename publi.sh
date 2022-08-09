#!/usr/bin/env bash

git add . && git commit -m "Fix function find_object_id_by_name_in_resource_pack" \
  && git tag v0.28.1 -m '0.28.1 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
