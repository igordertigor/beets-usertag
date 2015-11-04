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

# TODO: tests

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.dbcore import types


def add_usertag(lib, opts, args):
    """Add a usertag"""
    id = int(args[0])
    item = lib.get_item(id)
    usertags = item.get('usertags', None)
    print(usertags)
    if usertags is None:
        usertags = []
    else:
        usertags = usertags.split('|')
    usertags.append(' '.join(args[1:]))
    usertags = list(set(usertags))
    if '' in usertags:
        usertags.pop(usertags.index(''))
    print(usertags)
    item.update({'usertags': '|'.join(usertags)})
    item.store()
add_tag_command = Subcommand('addtag',
                             help='add user defined tag',
                             aliases=('adt',))
add_tag_command.func = add_usertag


def remove_usertag(lib, opts, args):
    """Remove a usertag"""
    id = int(args[0])
    item = lib.get_item(id)
    usertags = item.get('usertags', None)
    if usertags is None:
        return
    usertags = item['usertags'].split('|')
    idx = usertags.index(' '.join(args[1:]))
    usertags.pop(idx)
    if len(usertags):
        item.update({'usertags': '|'.join(usertags)})
    else:
        item.update({'usertags': None})
    item.store()
rm_tag_command = Subcommand('rmtag',
                            help='remove user defined tag',
                            aliases=('rmt',))
rm_tag_command.func = remove_usertag


def clear_usertags(lib, opts, args):
    """Clear all usertags"""
    id = int(args[0])
    item = lib.get_item(id)
    item.update({'usertags': None})
    item.store()
clear_tags_command = Subcommand('cleartags',
                                help='remove ALL user defined tags')
clear_tags_command.func = clear_usertags


class UserTagsPlugin(BeetsPlugin):
    """UserTags plugin to support user defined tags"""
    item_types = {'usertags': types.STRING}

    def __init__(self):
        super(UserTagsPlugin, self).__init__()

    def commands(self):
        return [add_tag_command, rm_tag_command, clear_tags_command]
