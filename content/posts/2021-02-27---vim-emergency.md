---
title: "Vim Emergency"
date: "2021-02-27"
template: "post"
draft: false
slug: "vim-emergency"
category: "Tools"
tags:
  - "vim"
  - "cheatsheet"
  - "beginner"
description: "I have no use Vim. But I have no idea how to even start typing. Help me!"
socialImage: ""
---

Our friend Susan is debugging a _production_ issue. She figured out that a
configuration file on the production needs to be updated. Her manager asked
said, "Susan, this is a piece of cake! You can find the file in `/etc/`".

Susan ssh'd into the server. She knew that a file can be read in vim, and she
opens the file in vim. _OMG! She is trying to edit the text but nothing is
happening! What is going on_.

Susan has no time for long tutorials. She needs something crip and to the point.
If you are Susan read on ...

---

Our friend Susan needs to fix a production issue by updating a configuration
file on the production server.

She ssh'd into the server.  
She needs to edit the file and VIM is the only editor available.  
She has no clue how to edit text in vim.  

If you are Susan, read on ...

1. First of all, vim is a terminal application which means the mouse won't work.
   _You need to use the keyboard to move around._
2. Vim has a writing mode and a 'not writing mode'(called 'normal mode').
   Vim starts in normal mode, hence typing letters will not work.
3. _Use arrow keys_ to move left, right, up and down in the file.(Simple
   navigation keys are mentioned in the [next section](#moving-in-the-file).)
4. To start _inserting_ text type `i`.
5. When you are done, press `<ESC>` to stop inserting text and go back to normal
   mode.
6. To save the file, hit `<ESC>` then type `:write`.
7. To quit the file, hit `<ESC>` then type `:quit`.
8. If you think you messed up and want to _exit without saving_ the file - `:quit!`.

## Moving in the file

1. `gg`: Go to the first line.
2. `G`(Uppercase g): Go to the last line.
3. `Ctrl+u`: Page up
4. `Ctrl_d`: Page down
