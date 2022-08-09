import json
import os

KEY_TO_DIR = {
    'scenes': 'scenes',
    'scripts': 'scripts',
    'cameras': 'cameras',
    'meshes': 'meshes',
    'skinControllers': 'skin-controllers',
    'materials': 'materials',
    'textures2d': 'textures/2D',
    'texturesCube': 'textures/cube',
    'images': 'images',
    'lights': 'lights',
    'animations': 'animations',
    'audioSources': 'audio-sources',
    'soundSamples': 'sounds',
    'rigidBodies': 'rigid-bodies',
    'colliders': 'colliders',
    'characters': 'characters',
    'stateMachines': 'state-machines',
}

DIR_TO_KEY = {
    'scenes': 'scenes',
    'scripts': 'scripts',
    'cameras': 'cameras',
    'meshes': 'meshes',
    'skin-controllers': 'skinControllers',
    'materials': 'materials',
    'textures/2D': 'textures2d',
    'textures/cube': 'texturesCube',
    'images': 'images',
    'lights': 'lights',
    'animations': 'animations',
    'audio-sources': 'audioSources',
    'sounds': 'soundSamples',
    'rigid-bodies': 'rigidBodies',
    'colliders': 'colliders',
    'characters': 'characters',
    'state-machines': 'stateMachines',
}


def make_asset_key_to_set_dict():
    asset_key_to_set_dict = {
        'scenes': set(),
        'scripts': set(),
        'cameras': set(),
        'meshes': set(),
        'skinControllers': set(),
        'materials': set(),
        'textures2d': set(),
        'texturesCube': set(),
        'images': set(),
        'lights': set(),
        'animations': set(),
        'audioSources': set(),
        'soundSamples': set(),
        'rigidBodies': set(),
        'colliders': set(),
        'characters': set(),
        'stateMachines': set()
    }
    return asset_key_to_set_dict


def get_resource_pack_data(game_project_dir_path):
    resource_pack_file_path = os.path.join(game_project_dir_path, 'resource-pack.json')
    with open(resource_pack_file_path, 'r') as resource_pack_file:
        resource_pack_data = json.load(resource_pack_file)
    return resource_pack_data


def get_first_scene_id_from_resource_pack_data(resource_pack_data):
    return resource_pack_data['scenes']['map'][0]['value']['id']['uuid']


def get_first_state_machine_id_from_resource_pack_data(resource_pack_data):
    return resource_pack_data['stateMachines']['map'][0]['value']['id']['uuid']


def get_scene_data(game_project_dir_path, scene_id):
    scene_file_path = os.path.join(game_project_dir_path, 'scenes/{0}.json'.format(scene_id))
    with open(scene_file_path, 'r') as scene_file:
        scene_data = json.load(scene_file)
    return scene_data


def get_animation_data(game_project_dir_path, animation_id):
    animation_file_path = os.path.join(game_project_dir_path, 'animations/{0}.json'.format(animation_id))
    with open(animation_file_path, 'r') as animation_file:
        animation_data = json.load(animation_file)
    return animation_data


def find_node_by_id(nodes, node_id):
    for node in nodes:
        obj = node['object3D']
        if obj['id']['uuid'] == node_id:
            return node
    return None


def count_objects_by_name(nodes, object_name):
    cnt = 0
    for node in nodes:
        obj = node['object3D']
        if obj['name'] == object_name:
            cnt += 1
    return cnt


def find_object_id_by_name(nodes, object_name):
    for node in nodes:
        obj = node['object3D']
        if obj['name'] == object_name:
            return obj['id']['uuid']
    return '00000000-0000-0000-0000-000000000000'


def find_camera_follow_script_id(scripts):
    for script in scripts:
        if script['@class'] == 'CameraFollowScript':
            return script['id']['uuid']
    return '00000000-0000-0000-0000-000000000000'


def get_character_data(game_project_dir_path, character_id=None):
    if character_id is None:
        resource_pack_data = get_resource_pack_data(game_project_dir_path)
        character_id = resource_pack_data['defaultCharacterId']['uuid']
    character_file_path = os.path.join(game_project_dir_path, 'characters/{0}.json'.format(character_id))
    with open(character_file_path, 'r') as character_file:
        character_data = json.load(character_file)
    return character_data


def get_state_data_by_id_from_state_machine_data(state_machine_data, state_id):
    for state_machine_state in state_machine_data['states']:
        if state_machine_state['id']['uuid'] == state_id:
            return state_machine_state


def get_file_path_to_attachment_by_asset_path(path_to_asset):
    with open(path_to_asset, 'r') as asset_file:
        asset_data = json.load(asset_file)
    return asset_data['filePath']
