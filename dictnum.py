from collections import OrderedDict
from itertools import zip_longest


class DictNumMeta:
    @classmethod
    def __prepare__(metacls, cls, bases):
        return OrderedDict()  # keep member in order which they are set

    @staticmethod
    def __new__(cls, name, bases, newattrs):
        kls = super().__new__(cls)
        kls._member_map_ = OrderedDict()
        kls._member_names_ = []

        item_attrs = tuple(newattrs.get('_attrs', ['value']))

        for attr, values in newattrs.items():
            if not attr.startswith('_'):
                kls._member_names_.append(attr)
                item = DictNumItem(attr, item_attrs, values)
                kls._member_map_[attr] = item
                setattr(kls, attr, item)

        return kls

    def __call__(cls, value, key='value'):
        return next((i for i in cls._member_map_.values() if getattr(i, key) == value), None)

    def __len__(cls):
        return len(cls._member_map_)

    def __iter__(cls):
        return (cls._member_map_[name] for name in cls._member_names_)

    def __reversed__(cls):
        return (cls._member_map_[name] for name in reversed(cls._member_names_))

    def __contains__(cls, member):
        return member in cls._member_map_.values()

    def __delattr__(cls, attr):
        if attr in cls._member_map_:
            raise AttributeError("cannot delete member")
        super().__delattr__(attr)


class DictNumItem:
    def __init__(self, name, keys, values):
        if len(keys) == 1 and not isinstance(values, (list, tuple, set)):
            values = [values]
        for key, val in zip_longest(keys, values):
            if key:
                setattr(self, key, val)
        self.name = name

    def __repr__(self):
        return "<%s.%s: %r>" % (
                self.__class__.__name__, self.name, self.__dict__)

    def __str__(self):
        return "%s.%s" % (self.__class__.__name__, self.name)


class DictNum(metaclass=DictNumMeta):
    pass


class TestNum(DictNum):
    _attrs = 'value', 'label', 'other'
    red = 1, 'Red', 'stuff'
    blue = 2, 'Blue', 'things'
