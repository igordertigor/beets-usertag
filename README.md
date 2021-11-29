# beets-usertag

Provides user defined keyword tags for
[beets](https://github.com/sampsyo/beets). It provides three new commands to
add and remove tags and to clear all tags from a file. These are specifically:

```
beet addtag <query> -t <usertag>[ -t <other-usertag>[...]] [-a]
```

Adds one (or more) usertags to the track with the given id. Use the `-a` flag to
tag albums instead.

```
beet rmtag <query> -t <usertag>[ -t <other-usertag>[...]] [-a]
```

Removes a usertag from the track with the given id. Use the `-a` flag to remove
a tag from an album.

```
beet cleartags <query> [-a]
```

Strips all usertags from the track with the given id. Use the `-a` flag to strip
all usertags from the specified albums.

```
beet listtags [-a]
```

Lists all user defined tags and a count of tracks that used those tags. Use the 
`-a` flag to return user-defined tags and count for albums.

```
beet list usertags:my-tag
```

Query user tags as you would query any other field with the standard `list`
command. Add the `-a` flag to list user-tagged albums.

# Installation

First, install the package with `pip`:

```
pip install git+git://github.com/igordertigor/beets-usertag.git
```

Alternatively, put the `beetsplug` folder somewhere in your PYTHONPATH.

Then, activate the plugin by adding `usertag` to the list of plugins in in beets' `config.yaml` file. This is described in more detail in the [beets
documentation](https://beets.readthedocs.io/en/latest/plugins/index.html#using-plugins).
