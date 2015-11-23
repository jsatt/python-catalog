# Python Catalog

Data structure for storing complex enumeration

```python
class Color(Catalog):
    _attrs = 'value', 'label', 'other'
    red = 1, 'Red', 'stuff'
    blue = 2, 'Blue', 'things'
```

Access values as Attributes

```python
>> Color.red.value
<< 1
>> Color.red.label
<< 'Red'
```

Call to look up members by attribute value

```python
>> Color('Blue', 'label')
<< Color.blue
```

Calling without attribute specified assumes first attribute defined in `_attrs`

```python
>> Color(1)
<< Color.red
```

`_attrs` defaults to `['value']`.

Member class can be replaced by extending `CatalogMember` and defining on Catalog with
the `_member_class` attribute
