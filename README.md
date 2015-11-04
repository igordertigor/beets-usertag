# beets-usertag

Provides user defined keyword tags for
[beets](https://github.com/sampsyo/beets). It provides three new commands to
add and remove tags and to clear all tags from a file. These are specifically:

```
beet addtag <id> <usertag>[|<other-usertag>[...]]
```

Adds one (or more) usertags to the track with the given id.

```
beet rmtag <id> <usertag>
```

Removes a usertag from the track with the given id.

```
beet cleartags <id>
```

Strips all usertags from the track with the given id.

# Installation

Put the beetsplug folder somewhere in your PYTHONPATH and activate tbe plugin
in beets' config.yaml file. This is described in more detail in the [beets
documentation](http://beets.readthedocs.org/en/latest/index.html).
