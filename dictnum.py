from collections import Iterable


class DictNumMeta:
    @staticmethod
    def __new__(cls, name, bases, newattrs):
        kls = super().__new__(cls)

        item_attrs = tuple(newattrs.get('_attrs', ['value']))

        for attr, values in newattrs.items():
            if not attr.startswith('_'):
                setattr(kls, attr, DictNumItem(attr, item_attrs, values))

        #TODO: _lookup_by_{item_attr}

        return kls


class DictNumItem:
    def __init__(self, name, keys, values):
        if len(keys) > 1 and (isinstance(values, str) or not isinstance(values, Iterable)):
            values = [values]
        assert len(keys) == len(values), (
            'item {} must provide exactly {} values'.format(name, len(keys)))
        for key, val in zip(keys, values):
            setattr(self, key, val)


class DictNum(metaclass=DictNumMeta):
    pass
