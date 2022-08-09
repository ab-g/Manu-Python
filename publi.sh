#!/usr/bin/env bash

git add . && git commit -m "Rename function make_asset_key_to_set_of_ids_dict to make_asset_key_to_set_dict" && git tag v0.10.1 -m '0.10.1 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
