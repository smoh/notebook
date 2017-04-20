# Unsolicited tips in Vim

The one reason that I think I keep coming back to Vim after using other editors is probably it's composability more than anything. By this, I mean keystrokes you make in Vim are defined in such way that you compose your editing command in a declarative manner much like speaking another language.

Understanding text objects is central to this, and certainly was a leap in my Vim efficiency. [Here's a nice guide on text objects to get you started](http://blog.carbonfive.com/2011/10/17/vim-text-objects-the-definitive-guide/).

As a python user, it is very useful to have argument-like text objects (strings separated by comma in a parenthesis). When I write python scripts, I delete, change, or copy (corresponding to `d`, `c`, and `y` in vim command language) function arguments all the time, so it is super useful to have this defined as text object that I can operate any vim operation on.

For example below, if you have argument text object defined as `a`, and have cursor as indicated, you would do `yia` to copy inside the argument just as you would do for `yiw` to copy inside word(`w`)

```
def myfunction(data, option=1, option=2):
                        |
    pass
```

Plugins like [targets.vim](https://github.com/wellle/targets.vim) adds such feature among other things.

Set space as your leader, and remember that Vim has allocated **any** mappings starting with leader for the user to use. With this you can start your own system of mappings. I try to define mappings so that it is mnemonic (something I got out of spacemacs experience). For example, I have

```
"bn for go to next buffer
nnoremap <leader>bn :bnext<CR>
"bp for go to previous buffer
nnoremap <leader>bp :bnext<CR>
"bd for delete buffer (delete current buffer)
nnoremap <leader>bd :bdelete<CR>
```

Starting all my _buffer_ related mappings with `<leader>b`, _file_ related mappings with `<leader>f` and _toggling_ mappings with `<leader>t` helps me remember better. Check out [spacemacs documentation on mappings](http://spacemacs.org/doc/DOCUMENTATION.html#core-pillars) or [spacevim](https://github.com/ctjhoa/spacevim) for inspiration.

I generally prefer to increment my vimrc one by one occasionally than using someone else's distribution with a ton of things that I have to learn already defined.

## Bookmarks

- ["Your problem with Vim is that you don't grok vi."](http://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim) one of the most awesome answers on stack overflow
- [How to boost your Vim productivity](https://sheerun.net/2014/03/21/how-to-boost-your-vim-productivity/)
- [Learn Vimscript the Hard Way by Steve Losh](http://learnvimscriptthehardway.stevelosh.com/)
- [How to Do 90% of What Plugins Do (With Just Vim)
](https://www.youtube.com/watch?v=XA2WjJbmmoM)

## Plugins

I use [vim-plug](https://github.com/junegunn/vim-plug) for vim plugin management. There are many other alternatives.

There are _many_ plugins in vim already available, but I highly recommend to use some plugin for these functionalities:

1. Fuzzy finding. Something that mimics sublime text's `CTRL+P` (go to anything). e.g., junegunn/fzf.vim
2. Autocompletion e.g., roxma/nvim-completion-manager
3. Linting e.g.,[syntastic](https://github.com/vim-syntastic/syntastic), neomake/neomake, probably more important if you collaborate on larger projects where you really have to write clean, maintainable codes rather than personal small projects