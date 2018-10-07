# beets-usertag

Provides user defined keyword tags for
[beets](https://github.com/sampsyo/beets). It provides three new commands to
add and remove tags and to clear all tags from a file. These are specifically:

```
beet addtag <query> -t <usertag>[ -t <other-usertag>[...]]
```

Adds one (or more) usertags to the track with the given id.

```
beet rmtag <query> -t <usertag>[ -t <other-usertag>[...]]
```

Removes a usertag from the track with the given id.

```
beet cleartags <query>
```

Strips all usertags from the track with the given id.

```
beet listtags
```

Lists all user defined tags and a count of tracks that used those tags.

```
beet list usertags:my-tag
```

Query user tags as you would query any other field with the standard `list` command.

# Installation

Put the beetsplug folder somewhere in your PYTHONPATH and activate the plugin
in beets' config.yaml file. This is described in more detail in the [beets
documentation](http://beets.readthedocs.org/en/latest/index.html).
