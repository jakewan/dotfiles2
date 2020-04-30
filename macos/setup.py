#!/usr/bin/env python3

from os import remove,symlink
from os.path import abspath, dirname, expanduser,join

ROOT_DIR = dirname(abspath(__file__))

def create_symlink(src, target):
    try:
        remove(target)
    except FileNotFoundError:
        pass
    print('Creating symlink {} to {}'.format(target, src))
    symlink(src, target)

def install_zsh_config():
    target_map = [
        ('zsh/.zshrc','.zshrc'),
        ('zsh/.zshrc_path', '.zshrc_path'),
        ('zsh/.zshrc_aliases', '.zshrc_aliases'),
        ('git/.gitconfig', '.gitconfig'),
        ('ssh/config', '.ssh/config'),
    ]
    for i in target_map:
        src = join(ROOT_DIR, i[0])
        target = join(expanduser('~'), i[1])
        create_symlink(src, target)

def run():
    install_zsh_config()

if __name__ == '__main__':
    run()


