#!/usr/bin/env bash

git add . && git commit -m "Add function get_inserted_timelines_ids_from_animation_data" && git tag v0.22.0 -m '0.22.0 tag'
git push --force --tags origin master:master
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
