import json
import os


def get_resource_pack_data(game_project_dir_path):
    resource_pack_file_path = os.path.join(game_project_dir_path, 'resource-pack.json')
    with open(resource_pack_file_path, 'r') as resource_pack_file:
        resource_pack_data = json.load(resource_pack_file)
    return resource_pack_data


def get_scene_data(game_project_dir_path, scene_id):
    scene_file_path = os.path.join(game_project_dir_path, 'scenes/{0}.json'.format(scene_id))
    with open(scene_file_path, 'r') as scene_file:
        scene_data = json.load(scene_file)
    return scene_data


def get_all_scenes(game_project_dir_path):
    resource_pack_data = get_resource_pack_data(game_project_dir_path)
    scenes = []
    if 'scenes' in resource_pack_data:
        for key_value in resource_pack_data['scenes']['map']:
            scene_id = key_value['key']['uuid']
            scene_data = get_scene_data(game_project_dir_path, scene_id)
            scenes.append(scene_data)
    return scenes


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


def get_character_data(game_project_dir_path, character_id=None):
    if character_id is None:
        resource_pack_data = get_resource_pack_data(game_project_dir_path)
        character_id = resource_pack_data['defaultCharacterId']['uuid']
    character_file_path = os.path.join(game_project_dir_path, 'characters/{0}.json'.format(character_id))
    with open(character_file_path, 'r') as character_file:
        character_data = json.load(character_file)
    return character_data
