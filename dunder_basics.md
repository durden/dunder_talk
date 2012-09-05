!SLIDE bullets

# Dunder Basics

- Dunder just slang for double underscore
- 'Private' class methods
- Sometimes called magic methods
- Just poorly documented

.notes Use of 'magic' here is a poor choice since the Python community values
.notes not using magic.  In fact, dunder methods are just plain old methods
.notes that get called at specific, well-defined times.

!SLIDE center smbullets

# Common dunders

    @@@ python
    __init__(self, *args, **kwargs)

.notes init/creation are separate steps for a good reason.
.notes Initialize your class, not create
.notes Takes all arguments from when you create object and passes them
.notes Kind of like a constructor (not exactly)

    @@@ python
    __str__(self)

.notes When str() is called, '%s', print, etc.
.notes Python starts at your object and looks for __str__.
.notes Goes through the MRO

.notes Different for old-style classes, some magic involved

    @@@ python
    __unicode__(self)

.notes Similar in theory to __str__, called by unicode(), etc.

- [Old-style dunder lookup](http://stackoverflow.com/questions/12223836/lookup-of-magic-methods-on-old-style-python-classes)

