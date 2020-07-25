# Setup Oh-My-Zsh using Antigen
source $HOME/.antigen.zsh

# Load Oh-My-Zsh library and bundles
antigen use oh-my-zsh
antigen bundle lukechilds/zsh-better-npm-completion

# Load theme
antigen theme simple

# Apply Antigen configuration
antigen apply

# User configuration
source $HOME/.ohmyzsh_config

export EDITOR='nvim'
export VISUAL='nvim'

# Additional files to include
source $HOME/.zshrc_path
source $HOME/.zshrc_aliases

# Setup pyenv
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

# Setup nodenv
if command -v nodenv 1>/dev/null 2>&1; then
  eval "$(nodenv init -)"
fi
export NODENV_VERSION=12.18.3

# Homebrew completions
if type brew &>/dev/null; then
  FPATH=$(brew --prefix)/share/zsh/site-functions:$FPATH
fi
