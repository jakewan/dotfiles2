#!/usr/bin/env python3

import argparse
from os import remove, symlink
from os.path import abspath, dirname, exists, expanduser, join, normpath
from pathlib import PosixPath

ROOT_DIR = dirname(abspath(__file__))
args = None
DRY_RUN_PREFIX = '(DRY RUN)'


def create_symlink(src, target):
    if args.dry_run:
        print(DRY_RUN_PREFIX, 'Creating symlink {} to {}'.format(target, src))
        return
    print('Creating symlink {} to {}'.format(target, src))
    try:
        remove(target)
    except FileNotFoundError:
        pass
    target_dir = dirname(target)
    if not exists(target_dir):
        PosixPath(target_dir).mkdir(parents=True)
    symlink(src, target)


def install_zsh_config(args):
    target_map = [
        ('zsh/.zshrc', '.zshrc'),
        ('zsh/.ohmyzsh_config', '.ohmyzsh_config'),
        ('zsh/.zshrc_path', '.zshrc_path'),
        ('zsh/.zshrc_aliases', '.zshrc_aliases'),
        ('../common/zsh/.zshrc_other', '.zshrc_other'),
        ('git/.gitconfig', '.gitconfig'),
        ('git/.gitignore_global', '.gitignore_global'),
        ('ssh/config', '.ssh/config'),
        ('../common/neovim/init.vim', '.config/nvim/init.vim'),
        ('../common/antigen/antigen.zsh', '.antigen.zsh'),
        ('../common/nodenv/version', '.nodenv/version'),
        ('../common/rbenv/version', '.rbenv/version'),
        ('../common/pyenv/version', '.pyenv/version'),
        ('tmux/.tmux.conf', '.tmux.conf'),
        ('vscode/settings.json', 'Library/Application Support/Code/User/settings.json'),
        ('../common/vscode/keybindings.json',
         'Library/Application Support/Code/User/keybindings.json'),
        ('gnupg/gpg-agent.conf', '.gnupg/gpg-agent.conf'),
    ]
    for i in target_map:
        src = normpath(join(ROOT_DIR, i[0]))
        target = join(expanduser('~'), i[1])
        create_symlink(src, target)


def run():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    install_zsh_config(args)


if __name__ == '__main__':
    run()
