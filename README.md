
# codeskeleton - general purpose code skeletons


## Trying it out

We will be adding an pypi package when this is a bit more stable,
but for now, clone the repo from github, and run:

```
$ python3 setup.py develop
```

You will now have the ``codeskeleton`` command available.


You can try out the example skeleton by registering the
``not_for_deploy/example_skeletons/`` directory as a skeleton
directory:

```
$ codeskeleton register --directory not_for_deploy/example_skeletons/
```

When this is done, you can use:

```
$ codeskeleton list-trees
```
to list the available directory tree skeleton IDs (only one),
and you can use:

```
$ codeskeleton create-tree <tree skeleton ID>
```
to create a directory tree from a skeleton definition.


## How to create your own skeletons
We will add in depth docs for this, but for now, take a
look at [not_for_deploy/example_skeletons/trees/django_project_skeleton](https://github.com/appressoas/codeskeleton/tree/master/not_for_deploy/example_skeletons/trees/django_project_skeleton).
The skeleton is defined in the ``codeskeleton.tree.yaml`` file,
and the other files in the directory is template files used by the
skeleton definition.

The template language is jinja2, with an extra ``{`` and ``}`` for
blocks, variables and comments to avoid problems when generating skeletons
for Django and jinja2 templates.

All you need to do to create a skeleton, is:

- Create a directory with a ``codeskeleton.tree.yaml`` file.
- Use ``codeskeleton register`` to register the directory as a
  skeleton directory (this just saves the directory  in
  ``~/.codeskeleton.config.yaml``).


## TODO

- Add support for snippets. The groundwork is already done, but
  we want to create a GUI, and a cli that can add the output
  to the clipboard.


## Develop

### Running tests

```
$ python -m unittest discover codeskeleton
```
