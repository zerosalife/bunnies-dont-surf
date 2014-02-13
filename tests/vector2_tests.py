import math

import nose.tools as n

from bds.vector import Vec2


def test_construction_x_y_and_access():
    v = Vec2(1, 2)
    n.eq_(v.x, 1)
    n.eq_(v.y, 2)
    n.eq_(v[0], 1)
    n.eq_(v[1], 2)

    v = Vec2((1, 2))
    n.eq_(v.x, 1)
    n.eq_(v.y, 2)
    n.eq_(v[0], 1)
    n.eq_(v[1], 2)
    v[1] = 4
    n.ok_(v.x is 1 and v.y is 4)


def test_is_instance_of_class():
    v = Vec2(1, 2)
    n.ok_(isinstance(v, Vec2))


def test_length_of_class_obj():
    v = Vec2(1, 2)
    n.eq_(len(v), 2)


def test_string_repr():
    v = Vec2(1, 2)
    # Would normally be called by print v.
    n.eq_(v.__repr__(), "Vec2(1, 2)")

def test_as_tuple():
    v = Vec2(1, 2)
    n.eq_(v.as_tuple(), (v.x, v.y))


def test_comparison():
    v = Vec2(3, -2)
    flt_v = Vec2(3.0, -2.0)
    zero_v = Vec2(0, 0)
    n.eq_(v, flt_v)
    n.ok_(v is not zero_v)
    n.ok_((flt_v is zero_v) is False)
    n.ok_((flt_v != v) is False)
    n.ok_(v == (3, -2))
    n.ok_(v != [0, 0])
    n.ok_(v != 5)
    n.ok_(v != [3, -2, -4])


def test_math():
    v = Vec2(1, 2)
    n.eq_(v + 1, Vec2(2, 3))
    n.eq_(v - 2, Vec2(-1, 0))
    n.eq_(v * 3, Vec2(3, 6))
    n.eq_(v / 2.0, Vec2(0.5, 1))
    n.eq_(v / 2, [0, 1])
    n.eq_(v ** Vec2(2, 3), Vec2(1, 8))
    n.eq_(v + [-11, 78], Vec2(-10, 80))
    n.eq_(v / [10., 2], [0.1, 1])
    n.eq_(v / 2., [0.5, 1])


def test_reverse_math():
    v = Vec2(1, 2)
    n.eq_(1 + v, Vec2(2, 3))
    n.eq_(2 - v, Vec2(1, 0))
    n.eq_(3 * v, Vec2(3, 6))
    n.eq_([2, 6] / v, Vec2(2, 3))
    n.eq_([2, 3.] / v, Vec2(2, 3./2))
    n.eq_(v ** Vec2(2, 3), Vec2(1, 8))
    n.eq_([-1, 78] + v, Vec2(0, 80))


def test_inplace():
    v = Vec2(5, 13)
    ref_v = v
    v *= 0.5
    v += 0.5
    v /= (3, 6)
    v += Vec2(-1, -1)
    n.eq_(v, ref_v)


def test_magnitude():
    v = Vec2(1, 2)
    n.eq_(v.magnitude, math.sqrt(5))

    v = Vec2(0, 0)
    n.eq_(v.magnitude, 0)


def test_normalized_unit_vec():
    v = Vec2(1, 2)
    n.eq_(v.normalized().x, 1 / math.sqrt(5))
    n.eq_(v.normalized().y, 2 / math.sqrt(5))

    n.assert_almost_equal(v.normalized().magnitude, 1)

    v = Vec2(0, 0)
    n.eq_(v.normalized().x, 0.)
    n.eq_(v.normalized().y, 0.)


def test_distance_btwn_vecs():
    v1 = Vec2(1, 2)
    v2 = Vec2(2, 3)
    n.eq_(v1.get_distance(v2), math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2))
    n.eq_(v1.get_distance((2, 3)),
          math.sqrt((v1.x - 2)**2 + (v1.y - 3)**2))


def test_dot_product():
    v1 = Vec2(1, 2)
    v2 = Vec2(2, 3)
    n.eq_(v1.dot(v2), 8)

    v1 = Vec2(5.0, 0)
    v2 = Vec2(0, 0.5)
    n.eq_(v1.dot(v2), 0)


def test_perpendicular():
    v1 = Vec2(1, 2)
    n.eq_(v1.perpendicular(), Vec2(-2, 1))


def test_unary_operations():
    v = Vec2(1, 2)
    v = -v
    n.eq_(v, Vec2(-1, -2))
    v = abs(v)
    n.eq_(v, Vec2(1, 2))


def test_angles():
    v = Vec2(0, 1)
    n.eq_(v.angle, 90)
    v2 = Vec2(v)
    v.rotate(-90)
    n.eq_(v.get_angle_between(v2), 90)
    v2.angle -= 90
    n.eq_(v.magnitude, v2.magnitude)
    n.eq_(v2.angle, 0)
    n.eq_(v2, Vec2(1, 0))
    n.assert_almost_equal((v - v2).magnitude, 0)
    n.eq_(v.magnitude, v2.magnitude)
    v2.rotate(300)
    n.assert_almost_equal(v.get_angle_between(v2), -60)
    v2.rotate(v2.get_angle_between(v))
    n.assert_almost_equal(v.get_angle_between(v2), 0)


def test_high_level_ops():
    basis0 = Vec2(5, 0)
    basis1 = Vec2(0, 0.5)
    v = Vec2(10, 1)
    n.eq_(v.projected(basis0), Vec2(10, 0))
    n.eq_(v.projected(Vec2(0, 0)), Vec2(0, 0))
    n.eq_(basis0.dot(basis1), 0)
    n.eq_(v.convert_to_basis(basis0, basis1), Vec2(2, 2))

    v.project(basis0)
    n.eq_(v, Vec2(10, 0))

    basis0 = Vec2(0, 0)
    n.assert_raises(TypeError, v.convert_to_basis, [basis0, basis1])

    v1 = Vec2(1, 0)
    v2 = Vec2(0, 1)
    n.eq_(v1.lerp(v2, 0.5), Vec2(0.5, 0.5))
