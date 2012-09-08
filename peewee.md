# Peewee ORM

    !python

    __or__(self, rhs)
    __and__(self, rhs)
    __invert__(self, rhs)
    __add__(self, rhs)
    __sub__(self, rhs)
    __neg__(self)

    SomeModel.select().where(
        (Q(a='A') | Q(b='B')) &
        (Q(c='C') | Q(d='D'))
    )

    # generates something like:
    # SELECT * FROM some_obj
    # WHERE ((a = "A" OR b = "B") AND (c = "C" OR d = "D"))

- Heavy use of all math/logic overrides
- [peewee](https://github.com/coleifer/peewee)
- Relatively small, < 3000 lines

# Presenter Notes

- map logical '|', '&', '~' to 'OR', 'AND', 'NOT' SQL
- __neg__ is unary negation operator
