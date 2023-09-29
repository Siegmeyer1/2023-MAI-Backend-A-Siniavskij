import pytest

from src.cache import LRUCache


def test_lru__basic():
    cache = LRUCache()

    cache.set('some key', 'some val')
    cache.set('other key', 'other val')
    assert cache.get('some key') == 'some val'
    assert cache.get('other key') == 'other val'

    cache.rem('some key')
    assert cache.get('some key') == ''
    assert cache.get('other key') == 'other val'

    cache.set('other key', 'replaced')
    assert cache.get('other key') == 'replaced'


def test_lru__capacity_exceeded():
    cache = LRUCache(capacity=5)

    test_data = [(str(idx), str(idx) + ' val') for idx in range(8)]

    for key, val in test_data:
        cache.set(key, val)

    for i in range(3):
        assert cache.get(test_data[i][0]) == ''

    for i in range(3, 8):
        assert cache.get(test_data[i][0]) == test_data[i][1]


def test_lru__capacity_with_rem():
    cache = LRUCache(capacity=3)

    cache.set('a', 'a1')
    cache.set('b', 'b1')
    cache.set('c', 'c1')

    cache.rem('b')
    cache.rem('c')

    cache.set('d', 'd1')
    cache.set('e', 'e1')

    assert cache.get('a') == 'a1'
    assert cache.get('d') == 'd1'
    assert cache.get('e') == 'e1'

    assert cache.get('b') == ''
    assert cache.get('c') == ''
