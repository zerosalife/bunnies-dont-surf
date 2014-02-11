import math
import operator


class Vec2(object):
    """
    A 2d vector class. Modeled after
    http://www.pygame.org/wiki/2DVectorClass . Supports vector and
    scalar operators, and provides high level functions for working
    with vectors.

    Typically constructed:
    v = Vec2(1, 2)

    Can be indexed and assigned to like a list:
    v[1] == 2
    v.y == 2

    v[1] = 4
    v.y == 4

    Supports boolean comparisons, e.g.:
    v1 = Vec2(1, 2)
    v2 = Vec2(1, 2)
    v1 == v2
    """
    __slots__ = ["x", "y"]

    def __init__(self, x_or_pair, y=None):
        if y is None:                     # It's a pair of (x, y) or [x, y]
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:                             # It's x, y
            self.x = x_or_pair
            self.y = y

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vec2")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript "+str(key)+" to Vec2")

    def __repr__(self):
        return "Vec2(%s, %s)" % (self.x, self.y)

    # Comparison operations
    def __eq__(self, other):
        if hasattr(other, "__getitem__") and len(other) is 2:
            return self.x == other[0] and self.y == other[1]
        else:
            return False

    def __ne__(self, other):
        if hasattr(other, "__getitem__") and len(other) is 2:
            return self.x != other[0] and self.y != other[1]
        else:
            return True

    def __nonzero__(self):
        return bool(self.x or self.y)

    # Generic operator handlers (used by division)
    def _o2(self, other, f):
        "Any two-operator operation where the left operand is a Vec2"
        if isinstance(other, Vec2):
            return Vec2(f(self.x, other.x),
                        f(self.y, other.y))
        elif (hasattr(other, "__getitem__")):
            return Vec2(f(self.x, other[0]),
                        f(self.y, other[1]))
        else:
            return Vec2(f(self.x, other),
                        f(self.y, other))

    def _r_o2(self, other, f):
        "Any two-operator operation where the right operand is a Vec2"
        if isinstance(other, Vec2):
            return Vec2(f(other.x, self.x),
                        f(self.y, other.y))
        elif hasattr(other, "__getitem__"):
            return Vec2(f(other[0], self.x),
                        f(other[1], self.y))
        else:
            return Vec2(f(other, self.x),
                        f(other, self.y))

    def _io(self, other, f):
        "Inplace operator, like +="
        if hasattr(other, "__getitem__"):
            self.x = f(self.x, other[0])
            self.y = f(self.y, other[1])
        else:
            self.x = f(self.x, other)
            self.y = f(self.y, other)
        return self

    # Addition
    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x + other[0], self.y + other[1])
        else:
            return Vec2(self.x + other, self.y + other)
    __radd__ = __add__                    # Reverse order is the same op

    def __iadd__(self, other):
        if isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
        elif hasattr(other, "__getitem__"):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x - other[0], self.y - other[1])
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        if hasattr(other, "__getitem__"):
            return Vec2(other[0] - self.x, other[1] - self.y)
        else:
            return Vec2(other - self.x, other - self.y)

    def __isub__(self, other):
        if isinstance(other, Vec2):
            self.x -= other.x
            self.y -= other.y
        elif hasattr(other, "__getitem__"):
            self.x -= other[0]
            self.y -= other[1]
        else:
            self.x -= other
            self.y -= other
        return self

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2(self.x * other[0], self.y * other[1])
        else:
            return Vec2(self.x * other, self.y * other)
    __rmul__ = __mul__

    def __imul__(self, other):
        if isinstance(other, Vec2):
            self.x *= other.x
            self.y *= other.y
        elif hasattr(other, "__getitem__"):
            self.x *= other[0]
            self.y *= other[1]
        else:
            self.x *= other
            self.y *= other
        return self

    # Division
    def __div__(self, other):
        return self._o2(other, operator.div)

    def __rdiv__(self, other):
        return self._r_o2(other, operator.div)

    def __idiv__(self, other):
        return self._io(other, operator.div)

    def __floordiv__(self, other):
        return self._o2(other, operator.floordiv)

    def __rfloordiv__(self, other):
        return self._r_o2(other, operator.floordiv)

    def __ifloordiv__(self, other):
        return self._io(other, operator.floordiv)

    def __truediv__(self, other):
        return self._o2(other, operator.truediv)

    def __rtruediv__(self, other):
        return self._r_o2(other, operator.truediv)

    def __itruediv__(self, other):
        return self._io(other, operator.floordiv)

    # Modulo
    def __mod__(self, other):
        return self._o2(other, operator.mod)

    def __rmod__(self, other):
        return self._r_o2(other, operator.mod)

    def __divmod__(self, other):
        return self._o2(other, operator.divmod)

    def __rdivmod__(self, other):
        return self._r_o2(other, operator.divmod)

    # Exponentiation
    def __pow__(self, other):
        return self._o2(other, operator.pow)

    def __rpow__(self, other):
        return self._r_o2(other, operator.pow)

    # Bitwise operators
    def __lshift__(self, other):
        return self._o2(other, operator.lshift)

    def __rlshift__(self, other):
        return self._r_o2(other, operator.lshift)

    def __rshift__(self, other):
        return self._o2(other, operator.rshift)

    def __rrshift__(self, other):
        return self._r_o2(other, operator.rshift)

    def __and__(self, other):
        return self._o2(other, operator.and_)
    __rand__ = __and__

    # Unary operations
    def __neg__(self):
        return Vec2(operator.neg(self.x), operator.neg(self.y))

    def __pos__(self):
        return Vec2(operator.pos(self.x), operator.pos(self.y))

    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))

    def __invert__(self):
        return Vec2(-self.x, -self.y)

    # Vector methods
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __set_magnitude(self, value):
        mag = self.get_magnitude()
        self.x *= value/mag
        self.y *= value/mag
    magnitude = property(get_magnitude, __set_magnitude, None,
                         "Gets or sets the magnitude, or length, of \
                         the vector.")

    def get_distance(self, other):
        "Returns the distance between this vector and an OTHER vector."
        return math.sqrt((self.x - other[0])**2 + (self.y - other[1])**2)

    def as_tuple(self):
        return (self.x, self.y)

    def normalized(self):
        "Return a unit vector that is this vector normalized to its magnitude."
        mag = self.magnitude
        if mag != 0:
            return Vec2(self/mag)
        return Vec2(0, 0)

    def dot(self, other):
        "Return the dot product of this vector and an OTHER vector."
        return float(self.x * other[0] + self.y * other[1])

    def cross(self, other):
        "Return the cross product of this vector and an OTHER vector."
        return float(self.x * other[1] - self.y * other[0])

    def perpendicular(self):
        "Returns a (new) vector that is perpendicular to this vector."
        return Vec2(-self.y, self.x)

    def perpendicular_normal(self):
        """
        Returns a (new) normalized unit vector that is
        perpendicular to this vector.
        """
        norm = self.normalized()
        return norm.perpendicular()

    def get_angle(self):
        if self.magnitude is 0:
            return 0
        return math.degrees(math.atan2(self.y, self.x))

    def __set_angle(self, angle_degrees):
        self.x = self.magnitude
        self.y = 0
        self.rotate(angle_degrees)
    angle = property(get_angle, __set_angle, None,
                     "Gets or sets the angle of the vector")

    def get_angle_between(self, other):
        "Returns the angle between this vector and an OTHER vector."
        cross = self.cross(other)
        dot = self.dot(other)
        return math.degrees(math.atan2(cross, dot))

    def rotate(self, angle_degrees):
        "Rotate this vector by ANGLE_DEGREES degrees."
        radians = math.radians(angle_degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x = self.x*cos_angle - self.y*sin_angle
        y = self.x*sin_angle + self.y*cos_angle
        self.x = x
        self.y = y

    def rotated(self, angle_degrees):
        "Return a vector that is this vector rotated by ANGLE_DEGREES degrees."
        radians = math.radians(angle_degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x = self.x*cos_angle - self.y*sin_angle
        y = self.x*sin_angle + self.y*cos_angle
        return Vec2(x, y)

    def project(self, other):
        """
        Modify this vector so that it is the projection of this vector
        onto the vector defined by OTHER.
        """
        other_mag_sqrd = other[0]**2 + other[1]**2
        if other_mag_sqrd is not 0:
            projected_mag_times_other_mag = self.dot(other)

            self.x = other[0] * \
                (projected_mag_times_other_mag / other_mag_sqrd)

            self.y = other[1] * \
                (projected_mag_times_other_mag / other_mag_sqrd)
        else:
            self.x = 0
            self.y = 0

    def projected(self, other):
        """
        Return a vector that is the projection of this vector onto the
        vector defined by OTHER.
        """
        other_mag_sqrd = other[0]**2 + other[1]**2
        if other_mag_sqrd is not 0:
            projected_mag_times_other_mag = self.dot(other)
            return Vec2(other *
                        (projected_mag_times_other_mag / other_mag_sqrd))
        return Vec2(0, 0)

    def convert_to_basis(self, x_vector, y_vector):
        """
        Returns a vector that is the conversion of this vector from
        its space to the vector space defined by X_VECTOR and Y_VECTOR.
        """
        xv_mag_sqrd = x_vector[0]**2 + x_vector[1]**2
        yv_mag_sqrd = y_vector[0]**2 + y_vector[1]**2
        if xv_mag_sqrd is 0 or yv_mag_sqrd is 0:
            raise TypeError("The basis vectors x: %s and y: %s must have \
                             non-zero magnitude." % (x_vector, y_vector))
        return Vec2(self.dot(x_vector) / xv_mag_sqrd,
                    self.dot(y_vector) / yv_mag_sqrd)

    def lerp(self, other, range):
        """
        Returns a vector that is the linear interpolation between this
        vector and an OTHER vector, for a RANGE factor between 0 and
        1.

        If RANGE is 0, it will return this vector. If RANGE is 1, it
        will return the OTHER vector.
        """
        return Vec2(self.x + (other[0] - self.x) * range,
                    self.y + (other[1] - self.y) * range)
