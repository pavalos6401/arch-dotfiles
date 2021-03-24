"
" ~/.config/nvim/plug-config/plug.vim
"

" Check if vim-plug is installed
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

" Install missing plugins
autocmd VimEnter *
      \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
      \|   PlugInstall --sync | q
      \| endif

" Install plugins
call plug#begin('~/.config/nvim/autoload/plugged')

" Themes
Plug 'embark-theme/vim', {'as': 'embark'}
Plug 'pineapplegiant/spaceduck', { 'branch': 'main' }
Plug 'dracula/vim', {'as': 'dracula'}
Plug 'arcticicestudio/nord-vim'

" Syntax highlighting improvement
Plug 'sheerun/vim-polyglot'

" Status bar
Plug 'itchyny/lightline.vim'

" NERD Commenter
Plug 'preservim/nerdcommenter'

call plug#end()
