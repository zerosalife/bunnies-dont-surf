import nose.tools as n

from bds import util


def test_flatten_list():
    l = [1, 2, 3]
    n.eq_(l, list(util.flatten(l)))
    l = [1, 2, 3, [4, 5]]
    n.eq_([1, 2, 3, 4, 5], list(util.flatten(l)))
