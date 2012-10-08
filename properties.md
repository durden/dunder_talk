# Properties

- Managed attributes
- 'Encapsulation'
- Add behavior to attribute actions
- Simplify API

--------------------------------------------------

# Properties

    !python

    class User(object):
        def __init__(self, name, email):
            self._name = name
            self._email = None

            # Calls descriptor, verify on change and init
            self.email = email

        def set_email(self, email):
            if '@' not in email:
                raise TypeError

            self._email = email

        def get_email(self):
            return self._email

        email = property(get_email, set_email)

# Presenter Notes

- Attribute access looks like variable, can add behavior and method later
  without changing client/API

--------------------------------------------------

# Property usage

    !python
    >>> u = User('luke', 'test')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 6, in __init__
    File "<stdin>", line 9, in set_email
    TypeError

    >>> u = User('luke', 'noreply@lukelee.net')
    >>> u.email
    'noreply@lukelee.net'

    >>> u.set_email('test')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 9, in set_email
    TypeError

    >>> u.set_email('test@test.com')
    >>> u.email
    'test@test.com'

    >>> u._email = 'test'
    >>> u.email
    'test'

--------------------------------------------------

# Descriptor powered

    !python

    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)

# Presenter Notes

- owner is class instance
- Fancy wording for class that overrides attribute look up w/ dunders
- __delete__ called for descriptor attribute deletion
- __del__ called in other scenarios right before obj deleted

--------------------------------------------------

# Pure Python property

    !python

    class Property(object):
        "Emulate PyProperty_Type() in Objects/descrobject.c"

        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.__doc__ = doc

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError, "unreadable attribute"
            return self.fget(obj)

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError, "can't set attribute"
            self.fset(obj, value)

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError, "can't delete attribute"
            self.fdel(obj)

- [reference](http://docs.python.org/howto/descriptor.html)

--------------------------------------------------

# Custom Descriptor

    !python

    >>> texas = Temperature()
    >>> texas.farenheit = 98
    >>> texas.celsius
    36.666666666666664
    >>> texas.farenheit
    98.0
    >>> texas.celsius = 38
    >>> texas.farenheit
    100.4

--------------------------------------------------

# Custom Descriptor

    !python

    class Celsius(object):
        """Fundamental Temperature Descriptor."""
        def __init__(self, value=0.0):
            self.value = float(value)

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            self.value = float(value)

    class Farenheit(object):
        """Requires that the owner have a ``celsius`` attribute."""
        def __get__(self, instance, owner):
            return instance.celsius * 9 / 5 + 32

        def __set__(self, instance, value):
            instance.celsius = (float(value) - 32) * 5 / 9

    class Temperature(object):
        celsius = Celsius()
        farenheit = Farenheit()

- [reference](http://www.itmaybeahack.com/book/python-2.6/html/p03/p03c05_properties.html)


--------------------------------------------------

# Properties extended

    !python

    __getattr__(self, name)
    __setattr__(self, name, value)
    __delattr__(self, name)
    __getattribute__(self, name)

- Real encapsulation
- Not always a good idea
- Power means responsibility

# Presenter Notes

- getattr called only for missing attributes
- Useful for throwing a good error message or meta programming
- getattribute is called for all look up, be careful
