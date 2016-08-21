"""
UserTags is a plugin for beets that allows users to mark songs in their library
by personalized tags. These usertags can in turn be used to filter the library
and as a form of virtual folder system.

The UserTags plugin defines a flexible attribute "usertags" for beets items.
usertags can be added from the command line interface by

beet addtag <id> <usertag>[|<usertag>]

Individual tags can be removed in a similar way by

beet rmtag <id> <usertag>

Removing multiple tags is currently not supported.

Filtering the library by tag works in the exact same way as with other fields:

beet ls usertags:<filtertag>

copyright 2015 by Ingo Fruend (github@ingofruend.net)
"""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# TODO: tests

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.dbcore import types


def add_usertag(lib, opts, args):
    """Add a usertag"""
    items = lib.items(args)
    newtags = opts.tags
    for item in items:
        usertags = item.get('usertags', None)
        if usertags is None:
            usertags = []
        else:
            usertags = usertags.split('|')
        # usertags.append(' '.join(newtags))
        usertags.extend(newtags)
        usertags = list(set(usertags))
        if '' in usertags:
            usertags.pop(usertags.index(''))
        item.update({'usertags': '|'.join(usertags)})
        item.store()
        print('Added tags\n   {}'.format(item))
add_tag_command = Subcommand(
    'addtag',
    help='Add user defined tags.',
    aliases=('adt',))
add_tag_command.func = add_usertag
add_tag_command.parser.add_option(
    '--tag', '-t',
    action='append', dest='tags',
    help='Tag to add. '
    'Combine multiple tags by specifiing this option repeatedly.')
add_tag_command.parser.usage += '\n'\
    'Example: beet addtag artist:beatles -t favourites'


def remove_usertag(lib, opts, args):
    """Remove a usertag"""
    items = lib.items(args)
    deltags = opts.tags
    for item in items:
        usertags = item.get('usertags', None)
        if usertags is None:
            return
        usertags = item['usertags'].split('|')
        for tag in deltags:
            idx = usertags.index(tag)
            usertags.pop(idx)
        if len(usertags):
            item.update({'usertags': '|'.join(usertags)})
        else:
            item.update({'usertags': None})
        item.store()
        print('Removed tags {}\n    {}'.format(deltags, item))
rm_tag_command = Subcommand('rmtag',
                            help='remove user defined tag',
                            aliases=('rmt',))
rm_tag_command.func = remove_usertag
rm_tag_command.parser.add_option(
    '--tag', '-t',
    action='append', dest='tags',
    help='Tag to remove. '
    'Combine multiple tags by specifiing this option repeatedly.')
rm_tag_command.parser.usage += '\n'\
    'Example: beet rmtag artist:beatles -t favourites'


def clear_usertags(lib, opts, args):
    """Clear all usertags"""
    items = lib.items(args)
    for item in items:
        item.update({'usertags': None})
        item.store()
clear_tags_command = Subcommand('cleartags',
                                help='remove ALL user defined tags')
clear_tags_command.func = clear_usertags


def list_usertags(lib, opts, args):
    items = lib.items(u'')
    alltags = []
    for item in items:
        usertags = item.get('usertags', None)
        if usertags:
            alltags += usertags.split('|')
    for tag in sorted(set(alltags)):
        print(tag, len([True for t in alltags if t == tag]))
list_tags_command = Subcommand('listtags',
                               help='list all user defined tags',
                               aliases=('lst',))
list_tags_command.func = list_usertags


class UserTagsPlugin(BeetsPlugin):
    """UserTags plugin to support user defined tags"""
    item_types = {'usertags': types.STRING}

    def __init__(self):
        super(UserTagsPlugin, self).__init__()

    def commands(self):
        return [add_tag_command,
                rm_tag_command,
                clear_tags_command,
                list_tags_command]
