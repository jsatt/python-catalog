Python Catalog
==============

.. image:: https://badge.fury.io/py/pycatalog.svg
    :target: https://badge.fury.io/py/pycatalog

.. image:: https://travis-ci.org/jsatt/python-catalog.svg?branch=master
    :target: https://travis-ci.org/jsatt/python-catalog

Catalog is a data structure for storing complex enumeration. It provides a clean definition pattern and several options for member lookup.

Supports Python 2.7, 3.3+

Install
-------

::

    pip install pycatalog

Usage
-----

::

    from catalog import Catalog

    class Color(Catalog):
        _attrs = 'value', 'label', 'other'
        red = 1, 'Red', 'stuff'
        blue = 2, 'Blue', 'things'

    # Access values as Attributes
    > Color.red.value
    1
    > Color.red.label
    'Red'

    # Call to look up members by attribute value
    > Color('Blue', 'label')
    Color.blue

    # Calling without attribute specified assumes first attribute defined in `_attrs`
    > Color(1)
    Color.red

Attributes
~~~~~~~~~~

``_attrs``: Defines names of attributes of members. (default: ``['value']``)

``_member_class``: Override the class used to create members. Create a custom  member class by extending ``CatalogMember``.

Methods
~~~~~~~

``_zip``: Return all members as a tuple. If attrs are provided as positional arguments, only those
attributes will be included, and in that order. Otherwise all attributes are included followed by
the member name.

::

    > Color._zip()
    (('red', 1, 'Red', 'stuff'), ('blue', 2, 'Blue', 'things'))
    > Colot._zip('value', 'label')
    ((1, 'Red'), (2, 'Blue'))

Changelog
---------

1.2.0 - Add support for Python 2. (Wrong direction. I know)

1.1.1 - Add ``_zip`` method

1.0.0 - Initial build and packaging
