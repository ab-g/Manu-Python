import json
import os


def get_scene_data(game_project_dir_path, scene_id):
    scene_file_path = os.path.join(game_project_dir_path, 'scenes/{0}.json'.format(scene_id))
    with open(scene_file_path, 'r') as scene_file:
        scene_data = json.load(scene_file)
    return scene_data


def get_script_data(game_project_dir_path, script_id):
    script_file_path = os.path.join(game_project_dir_path, 'scripts/{0}.json'.format(script_id))
    with open(script_file_path, 'r') as script_file:
        script_data = json.load(script_file)
    return script_data


def get_animation_data(game_project_dir_path, animation_id):
    animation_file_path = os.path.join(game_project_dir_path, 'animations/{0}.json'.format(animation_id))
    with open(animation_file_path, 'r') as animation_file:
        animation_data = json.load(animation_file)
    return animation_data


def get_character_data(game_project_dir_path, character_id):
    character_file_path = os.path.join(game_project_dir_path, 'characters/{0}.json'.format(character_id))
    with open(character_file_path, 'r') as character_file:
        character_data = json.load(character_file)
    return character_data
