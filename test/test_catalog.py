from unittest import TestCase

from catalog import Catalog


class TestCatalog(TestCase):
    def setUp(self):
        class TestNum(Catalog):
            _attrs = 'value', 'label', 'other'
            red = 1, 'Red', 'stuff'
            blue = 2, 'Blue', 'things'

        self.TestNum = TestNum

    def test_access_attrs(self):
        self.assertEqual(self.TestNum.red.name, 'red')
        self.assertEqual(self.TestNum.red.value, 1)
        self.assertEqual(self.TestNum.red.label, 'Red')
        self.assertEqual(self.TestNum.red.other, 'stuff')

    def test_access_by_attrs(self):
        self.assertEqual(self.TestNum(2), self.TestNum.blue)
        self.assertEqual(self.TestNum('blue', 'name'), self.TestNum.blue)
        self.assertEqual(self.TestNum(2, 'value'), self.TestNum.blue)
        self.assertEqual(self.TestNum('Blue', 'label'), self.TestNum.blue)
        self.assertEqual(self.TestNum('things', 'other'), self.TestNum.blue)

    def test_set_single_value(self):
        class TestNum(Catalog):
            red = 1
            blue = 2
        self.assertEqual(TestNum.red.value, 1)
        self.assertEqual(TestNum(2), TestNum.blue)

    def test_wrong_length_of_values(self):
        class TestNum(Catalog):
            _attrs = 'value', 'label', 'other'
            red = 1, 'Red'
            blue = 2, 'Blue', 'things', 'more'

        self.assertIsNone(TestNum.red.other)

    def test_data_model(self):
        self.assertEqual(len(self.TestNum), 2)
        self.assertTrue(self.TestNum.red in self.TestNum)
        self.assertSequenceEqual(list(self.TestNum), [self.TestNum.red, self.TestNum.blue])
        self.assertSequenceEqual(list(reversed(self.TestNum)),
                                 [self.TestNum.blue, self.TestNum.red])
        with self.assertRaises(AttributeError):
            del self.TestNum.red

    def test_zip(self):
        values = self.TestNum._zip()
        self.assertSequenceEqual(
            list(values), (('red', 1, 'Red', 'stuff'), ('blue', 2, 'Blue', 'things')))

    def test_zip_w_list(self):
        values = self.TestNum._zip('label', 'value')
        self.assertSequenceEqual(list(values), (('Red', 1), ('Blue', 2)))
