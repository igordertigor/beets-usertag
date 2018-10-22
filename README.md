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

First, install the package with `pip`:

```
pip install git+git://github.com/igordertigor/beets-usertag.git
```

Alternatively, put the `beetsplug` folder somewhere in your PYTHONPATH.

Then, activate the plugin by adding `usertag` to the list of plugins in in beets' `config.yaml` file. This is described in more detail in the [beets
documentation](https://beets.readthedocs.io/en/latest/plugins/index.html#using-plugins).
