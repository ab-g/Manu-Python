#!/usr/bin/env bash

git add . && git commit -m "Add function get_first_scene_id_from_resource_pack_data" && git tag v0.8.0 -m '0.8.0 tag'
git push --tags origin
rm -rf dist && python3 setup.py bdist_wheel && twine upload -r testpypi dist/*
pip3 uninstall -y manu
pip3 install --extra-index-url https://testpypi.python.org/pypi manu --user
