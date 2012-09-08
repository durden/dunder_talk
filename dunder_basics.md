# Dunder Basics

- Dunder just slang for double underscore
- 'Private' class methods
- Sometimes called 'magic methods'
- Just poorly documented

# Presenter Notes

Use of 'magic' here is a poor choice since the Python community values
not using magic.  In fact, dunder methods are just plain old methods
that get called at specific, well-defined times.

------------------------------------------------------

# Why?

- Very common/widely used
- Pythonic
- Operator overloading
- Debugging tools
- Avoid custom API/object symantics
- Domain Specific Language (DSL)
- Your already using them

------------------------------------------------------

# Common dunders

    !python
    __init__(self, *args, **kwargs)
    __str__(self)
    __unicode__(self)
    __len__(self)
    __repr__(self)

# Presenter Notes

- init/creation are separate steps for a good reason.
- Initialize your class, not create
- Takes all arguments from when you create object and passes them
- Kind of like a constructor (not exactly)

- When str() is called, '%s', print, etc.
- Python starts at your object and looks for __str__.
- Goes through the MRO

- Different for old-style classes, some magic involved

- Similar in theory to __str__, called by unicode(), etc.

- [Old-style dunder lookup](http://stackoverflow.com/questions/12223836/lookup-of-magic-methods-on-old-style-python-classes)
