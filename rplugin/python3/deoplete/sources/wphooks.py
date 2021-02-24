import os
import re
import json

from .base import Base

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'wp-hooks'
        self.mark = '[wp-hooks]'
        self.matchers = ['matcher_head']
        self.rank = 100
        self.min_pattern_length = 0
        self.wphooks_dir = os.path.expanduser("~/.vim/plugged/deoplete-wp-hooks/wp-hooks/")
        self.filetypes = ['php']
        self.is_debug_enabled = False
        self.is_volatile = True

        if self.vim.eval('exists("g:wphooks_dir")'):
            self.wphooks_dir = self.vim.eval('g:wphooks_dir')

        with open(self.wphooks_dir + "actions.json", "r") as read_file:
            self.actions = json.load(read_file)

        with open(self.wphooks_dir + "filters.json", "r") as read_file:
            self.filters = json.load(read_file)


    def gather_candidates(self, context):
        candidates = []
        hook_type = None

        if any(function in context['input'] for function in ['add_filter', 'remove_filter']):
            hook_type = 'filter'
        elif any(function in context['input'] for function in ['add_action', 'remove_action']):
            hook_type = 'action'

        text_input = context['input']
        text_input = text_input.replace('remove_action', '').replace('remove_filter', '')
        text_input = text_input.replace('add_action','').replace('add_filter', '')
        text_input = text_input.replace('"', '').replace('\'', '')
        text_input = text_input.replace('(', '').replace(')', '').strip()

        if text_input == '':
            return candidates

        self.debug('Type (%s): %s, Hook: %r', hook_type, context['complete_str'], text_input)
        if hook_type == 'action':
            for item in self.actions:
                if item['name'].startswith(text_input):
                    candidate = {
                        'word': item['name'],
                        'kind': item['type'],
                        'info': item['doc']['description'],
                        'dup': 1
                    }
                    candidates.append(candidate)

        if hook_type == 'filter':
            for item in self.filters:
                if item['name'].startswith(text_input):
                    candidate = {
                        'word': item['name'],
                        'kind': item['type'],
                        'info': item['doc']['description'],
                        'dup': 1
                    }
                    candidates.append(candidate)

        return candidates

