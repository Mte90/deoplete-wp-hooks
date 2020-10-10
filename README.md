# deoplete-wp-hooks

A [Deoplete](https://github.com/Shougo/deoplete.nvim) source for [wp-hooks](https://github.com/johnbillion/wp-hooks), the list of wordpress hooks.  
Automatically reconize actions and filters and use the right JSON file, also update the list itself on plugin update.

## Installation

With vundle

```
Plugin 'mte90/deoplete-wp-hooks', { 'do': './install.sh' }
```

Automatically will download the latest version of the JSON files.

## Parameters

`let g:wphooks_dir='your-new-path'`

To specify a custom path for the json files, there is already a default value.
