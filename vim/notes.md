# VIM Basics

Three Modes in VIM

- Insert mode

- Command mode

- Last-line mode

## Command mode -

- When you run vim filename to edit a file. VIM starts in command mode.

- This means that typing characters won't send text to the file.

- `j` will move the cursor down one line.

- `dd` will delete an entire line.

| Command           | Description                                               |
| -------------     | :-------------:                                           |
| H                 | Moves the cursor one character to the left                |
| J                 | Moves the cursor down one line                            |
| K                 | Moves the cursor up one line                              |
| L                 | Moves the cursor one character to the left                |
| O                 | Moves the cursor to the beginning of the line             |
| $                 | Moves the cursor to the end of the line                   |
| W                 | Move forward one word                                     |
| B                 | Move backward one word                                    |
| G                 | Move to the end of the file                               |
| Gg                | Move to the beginning of the file                         |
| `.                | Move to the last edit                                     |
| D                 | Starts the delete operation                               |
| Dw                | Will delete a word                                        |
| Do                | Will delete to the beginning of the file                  |
| d$                | Will delete to the end of a line                          |
| Dgg               | Will delete to the beginning of the file                  |
| Dg                | Will delete to the end of the file                        |
| U                 | Will undo the last operation                              |
| Ctrl -r           | Will redo the last undo                                   |

## Insert Mode

- To enter insert mode, type "i" (for insert)
- To exit insert mode hit the Escape key
- This takes you back to command mode.
- ":" will allow you to save, exit and more…

### Saving

| Command           | Description                   |
| -------------     | :-------------:               |
| :w                | Saves file                    |
| :w filename       | Saves to a different file     |
| :q                | Quits                         |
| :q!               | To exist without verification |

### Searching and Replacing

| Command                                           | Description                                                                       |
| -------------                                     | :-------------:                                                                   |
| /                                                 | Followed by the test you want to search for                                       |
| N and n                                           | To find your search again or opposite direction                                   |
| ?                                                 | Reverse direction of your search                                                  |
| :%s/test/replacement test/g                       | Search through the entire document for test and replace it with replacement test  |
| :%s/test/replacement test/gc                      | Search through the entire document and confirm before replacing test              |

### Copying and pasting

| Command                                           | Description                           |
| -------------                                     | :-------------:                       |
| V                                                 | Highlight one character at a time
| v                                                 | Highlight one line at a time          |
| Ctrl -v                                           | Highlight by columns                  |
| P                                                 | Paste text after the current line     |
| p                                                 | Paste text on the current line        |
| y                                                 | Yank text into the copy buffer        |
