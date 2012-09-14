# Dunder Basics

- Dunder just slang for double underscore
- Sometimes called 'magic methods'
- 'Private' class methods
- Just methods!
- Poorly documented

# Presenter Notes

Lookup the args and when it's called and your good!

Use of 'magic' here is a poor choice since the Python community values
not using magic.  In fact, dunder methods are just plain old methods
that get called at specific, well-defined times.

------------------------------------------------------

# Why dunders?

- Your already using them
- Pythonic (common/idiomatic)
- Operator overloading
- Debugging tools
- Avoid custom API/object semantics
- Domain Specific Language (DSL)

# Presenter Notes

Main goal is to make your object look and act like a standard Python type.

The person using your object already knows Python and how to use standard
types so don't make them learn all new semantics.

------------------------------------------------------

# Common dunders

    !python
    __init__(self, *args, **kwargs)
    __str__(self)
    __unicode__(self)
    __len__(self)
    __repr__(self)

- [Old-style class dunder lookup](http://stackoverflow.com/questions/12223836/lookup-of-magic-methods-on-old-style-python-classes)

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
