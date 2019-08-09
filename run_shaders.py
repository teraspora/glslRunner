# run_shaders.py

# Author:   John Lynch
# Date:     August 2019
# Function: When user presses any key, select a random fragment shader from
# the `production` directory, and a random set of fractal (and other?) images
# from the `imgs` directory, and run an instance of glslViewer
# with these objects as parameters. 

import os, fnmatch, random, threading
from subprocess import Popen

SHADER_DIR = '/media/john/sys2/web18/playground/visuals/frag/production'
IMAGE_DIRS = ['/media/john/sys2/web18/playground/visuals/imgs', '/media/john/sys2/web18/playground/visuals/imgs/new']
IMAGE_DIR_INDEX = 1
SHADER_CODES = {'b': 'blobacity', 'v': 'voronoi-05', 'c': 'cushion-x1', 'C': 'cushion-x2', '¢': 'cushion-x4', 'g': 'cogs-new00',
                'G': 'cogs-x3', 'd': 'deep-sea-x1', 'e': 'deep-sea-x', 'D': 'dance00', 'f': 'feb-18-03', 'F': 'feb-test',
                'O': 'trig-dreamz01', 'o': 'trig-dreamz-01', 't': 'trig-dreamz-03', 'T': 'trig-dreamz-05', 'a': 'anon091', 'A': 'anon10'}
EXTENSION = '.frag'
CMD_REDIRECT = ['>', '/dev/null', '2>&1']
TEXT_DIR = '/media/john/sys2/web18/playground/visuals/text/'
TEXT_IMGS = ['dance2048FB.png', 'bogbeats.png', 'red_heart.png', 'kiss1024.png']
def choose_files(path, number):
    files = os.listdir(path)
    chosenfiles = random.choices(files, k = number)
    return chosenfiles

shaders = fnmatch.filter(os.listdir(SHADER_DIR), '*.frag')

# Run glslViewer from Python:
def run(shader):
    IMAGE_DIR = IMAGE_DIRS[IMAGE_DIR_INDEX]
    print(shader)
    imgs = [f'{os.path.join(IMAGE_DIR, img)}' for img in choose_files(IMAGE_DIR, 8)]
    glsl_cmd = ['glslViewer -w 1920 -h 1080', f'{SHADER_DIR}/{shader}'] + imgs + CMD_REDIRECT
    if shader == 'dance00.frag':
        for index in [2, 4, 6, 8]:
            glsl_cmd[index] = TEXT_DIR + TEXT_IMGS[index // 2 - 1]
    cmd_str = ' '.join(glsl_cmd)
    Popen(cmd_str, shell=True)
    return

def process_command(command_index):
    if command_index == 0 or command_index == 1:
        IMAGE_DIR_INDEX = command_index
        print(f'IMAGE_DIR set to {IMAGE_DIRS[IMAGE_DIR_INDEX]}')

if __name__ == '__main__':
    while True:
        command = input('Run shader?') or ' '
        if command.isdigit():
            process_command(int(command))
        else:
            shader = SHADER_CODES[command[0]] + EXTENSION if command[0] in SHADER_CODES else random.choice(shaders)
            # Spawn a thread to run the shader
            runner = threading.Thread(target=run, args=(shader,), name='runner')
            runner.start()
