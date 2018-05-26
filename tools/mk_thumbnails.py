from pgmagick import Image, Geometry
import os
import sys


root_dir = './photography/images'
confs = [
    {'v1': 300, 'v2': 200, 'dir': '300'},
    {'v1': 610, 'v2': 410, 'dir': '610'},
    {'v1': 1080, 'v2': 720, 'dir': 'full'}
]


def check_args():
    if len(sys.argv) < 2:
        print('Usage:', sys.argv[0], 'image_path...')
        sys.exit(1)


def check_dirs():
    if not os.path.isdir('%s/%s' % (root_dir, confs[0]['dir'])):
        print('Wrong current directory')
        sys.exit(1)


def find_next_image_name():
    image_paths = os.listdir('%s/%s' % (root_dir, confs[0]['dir']))
    return max([int(path[:-4]) for path in image_paths if '.jpg' in path]) + 1


def resize_image(path, v1, v2):
    image = Image(path)
    size = image.size()
    geometry = Geometry(v1, v2) if size.width() > size.height() else Geometry(v2, v1)
    image.quality(100)
    image.scale(geometry)
    return image


def resize_images(paths):
    for path in paths:
        name = find_next_image_name()
        for conf in confs:
            image = resize_image(path, conf['v1'], conf['v2'])
            image.write('%s/%s/%s.jpg' % (root_dir, conf['dir'], name))


if __name__ == '__main__':
    check_args()
    check_dirs()
    resize_images(sys.argv[1:])
