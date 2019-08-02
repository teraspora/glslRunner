# run_shaders.py

# Author:   John Lynch
# Date:     August 2019
# Function: When user presses `Enter`, select a random fragment shader from
# the `production` directory, and a random set of fractal (and other?) images
# from the `imgs` directory, and run an instance of glslViewer
# with these objects as parameters. 

import os, fnmatch, random
from subprocess import Popen

SHADER_DIR = '/media/john/sys2/web18/playground/visuals/frag/production'
IMAGE_DIR = '/media/john/sys2/web18/playground/visuals/imgs/'
def get_files(pattern, basedir):
    for path, dirs, files in os.walk(basedir):
        for fname in fnmatch.filter(files, pattern):
            yield os.path.join(path, fname)


def choose_files(path, number):
    files = os.listdir(path)
    chosenfiles = random.choices(files, k = number)
    return chosenfiles

# Run glslViewer from Python:
prod_shaders = fnmatch.filter(os.listdir(SHADER_DIR), '*.frag')

def run():
    shader = random.choice(prod_shaders)
    imgs = choose_files(IMAGE_DIR, 8)
    img_str = ' '.join(imgs)
    glsl_cmd = ['glslViewer', f'{SHADER_DIR}/{shader}'] + imgs
    Popen(glsl_cmd)
    print(f'Running {shader} with {{{img_str}}}')
    return

if __name__ == '__main__':
    while True:
        input('Run?')
        run()