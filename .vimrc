" Inicio de configuracion de Neovim
set number
syntax enable
set relativenumber
set mouse=a
set numberwidth=1
set clipboard=unnamedplus
set showcmd
set ruler
set encoding=utf-8
set showmatch
set ts=4 sw=2
set laststatus=2
set noshowmode

"" Lugar donde va a ir a buscar mis pluggins
"call plug#begin('~/.config/nvim/plugged')
"
"" Temas
"Plug 'morhetz/gruvbox'
"
"" IDE
"Plug 'easymotion/vim-easymotion'
"Plug 'scrooloose/nerdtree'
"Plug 'christoomey/vim-tmux-navigator'
"Plug 'sheerun/vim-polyglot'
"Plug 'jiangmiao/auto-pairs'
"Plug 'alvan/vim-closetag'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
"
"call plug#end()
"
set background=dark
"let g:gruvbox_contrast_dark = 'hard'
colorscheme gruvbox

" Background transparente
" hi Normal guibg=NONE ctermbg=NONE

let mapleader=" "
nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>

