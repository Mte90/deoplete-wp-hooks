# deoplete-wp-hooks

A Deoplete source for [wp-hooks](https://github.com/johnbillion/wp-hooks), the list of wordpress hooks.  
Automatically reconize actions and filters and use the right JSON file.

## Installation

With vundle

```
Plugin 'mte90/deoplete-wp-hooks', { 'do': './install.sh' }
```

Autoamtically will download the latest version of the JSON files.

## Parameters

`let g:wphooks_dir='your-new-path'`

To specify a custom path for the json files.