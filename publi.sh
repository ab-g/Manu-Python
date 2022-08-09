#!/usr/bin/env bash

git add . && git commit -m "Add function get_file_path_to_attachment_by_asset_path" && git tag v0.11.0 -m '0.11.0 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
