import os, fnmatch, random

def get_files(pattern, basedir):
    for path, dirs, files in os.walk(basedir):
        for fname in fnmatch.filter(files, pattern):
            yield os.path.join(path, fname)


def choose_files(path, number):
    files = os.listdir(path)
    chosenfiles = random.choices(files, k = number)
    return chosenfiles

# Run glslViewer from Python:
prod_shaders = fnmatch.filter(os.listdir('/media/john/sys2/web18/playground/visuals/frag/production'), '*.frag')

def run():
    shader = random.choice(prod_shaders)
    imgs = choose_files('/media/john/sys2/web18/playground/visuals/imgs/', 8)

    # print(imgs)


    img_str = ' '.join(imgs)
    commands = (f'cd /media/john/sys2/web18/playground/visuals/imgs/ && '
               f'glslViewer ../frag/production/{shader} '
               f'{img_str}')
    print(f'Running {shader} with {{{img_str}}}')
    os.system(commands)

if __name__ == '__main__':
    run()