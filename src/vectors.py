from typing import *

Number = Union[int, float]

class _Vector:
    '''
    Creates a _Vector object. Leave blank to create an empty one.
    '''
    def __init__(self, *args: Number):
        if isinstance(args[0], Iterable):
            self._values = args[0]
        else:
            self._values = list(args)
        
        for val in list(self):
            if not isinstance(val, Number):  raise TypeError(f"Tried to input a {type(val)} into a Vector")

    def __add__(self, value):
        if isinstance(value, _Vector):
            if len(self) != len(value):  raise ValueError("Vectors have different lengths")
            return _Vector([val + value[i] for i, val in enumerate(self)])
        elif isinstance(value, Number):
            return _Vector([val + value for val in list(self)])
        else:
            raise TypeError(f"Attempted to add type {type(value).__name__} to a Vector{len(self)}")
    
    def __sub__(self, value):
        if isinstance(value, _Vector):
            if len(self) != len(value):  raise ValueError("Vectors have different lengths")
            return _Vector([val - value[i] for i, val in enumerate(self)])
        elif isinstance(value, Number):
            return _Vector([val - value for val in list(self)])
        else:
            raise TypeError(f"Attempted to add type {type(value).__name__} to a Vector{len(self)}")
    
    def __mul__(self, value: Number):
        if not isinstance(value, Number):  raise TypeError(f"Attempted to multiply a Vector by type {type(value).__name__}")
        return _Vector([val * value for val in list(self)])
    
    def __truediv__(self, value: Number):
        if not isinstance(value, Number):  raise TypeError(f"Attempted to divide a Vector by type {type(value).__name__}")
        return _Vector([val / value for val in list(self)])
    
    def __mod__(self, value: Number):
        if not isinstance(value, Number):  raise TypeError(f"Attempted to use the modulo operation on a Vector with type {type(value).__name__}")
        return _Vector([val % value for val in list(self)])
    
    def __floordiv__(self, value: Number):
        if not isinstance(value, Number):  raise TypeError(f"Attempted to use the floordiv operation on a Vector with type {type(value).__name__}")
        return _Vector([val // value for val in list(self)])
    
    def __pow__(self, value: Number):
        if not isinstance(value, Number):  raise TypeError(f"Attempted to use the power operation on a Vector with type {type(value).__name__}")
        return _Vector([val ** value for val in list(self)])
    
    def __eq__(self, value):
        if not isinstance(value, _Vector):  return False
        return list(self) == list(value)
    
    def __iter__(self):
        for val in self._values:  yield val
        
    def __getitem__(self, index: int) -> Number:
        if not isinstance(index, int):  raise TypeError("Index was not of type 'int'")
        
        return list(self)[index]
    
    def __len__(self):  return len(self)
    
    def __str__(self) -> str:  return str(list(map(float, list(self))))[1:-1]
    
    
    def dot(self, vector) -> Number:
        if not issubclass(vector, _Vector):  raise TypeError("Trying to perform the dot product on a non-vector")
        if len(list(self)) != len(list(vector)):  raise ValueError("Vectors must be of the same length")

        product = 0
        for i, val in enumerate(list(self)):  product += val * list(vector)[i]
        
        return product
    
class Vector2(_Vector):
    def __init__(self, x: Number, y: Number | None = None):
        super().__init__([val for val in (x, y) if not val is None])
        
        if list(self) == []:
            self._values = [0, 0]
        elif len(self) == 1:
            self._values = [list(self)[0], list(self)[0]]
        
    @property
    def x(self) -> Number:  return self._values[0]
    @property
    def y(self) -> Number:  return self._values[1]
    
    @property
    def xy(self) -> Number:  return self.x, self.y
    @property
    def yx(self) -> Number:  return self.y, self.x

class Vector3(_Vector):
    def __init__(self, x: Number, y: Number | None = None, z: Number | None = None):
        super().__init__([val for val in (x, y, z) if not val is None])
        
        if list(self) == []:
            self._values = [0, 0, 0]
        elif len(list(self)) == 1:
            self._values = [self._values[0], self._values[0], self._values[0]]
        
    def cross(self, vector):
        if not issubclass(vector, _Vector):  raise TypeError("Trying to perform the cross product on a non-vector")
        if len(self) != 3 or len(self) != 3:  raise ValueError("Both vectors must be 3-dimensional")
        
        A = list(self)
        B = list(vector)

        X = A[1] * B[2] - A[2] * B[1]
        Y = A[2] * B[0] - A[0] * B[2]
        Z = A[0] * B[1] - A[1] * B[0]
        
        return Vector3(X, Y, Z)
        
    @property
    def x(self) -> Number:  return self._values[0]
    @property
    def y(self) -> Number:  return self._values[1]
    @property
    def z(self) -> Number:  return self._values[2]
    
    
    @property
    def xx(self) -> Number:  return self.x, self.x
    @property
    def xy(self) -> Number:  return self.x, self.y
    @property
    def xz(self) -> Number:  return self.x, self.z
    
    @property
    def yx(self) -> Number:  return self.y, self.x
    @property
    def yy(self) -> Number:  return self.y, self.y
    @property
    def yz(self) -> Number:  return self.y, self.z
    
    @property
    def zx(self) -> Number:  return self.z, self.x
    @property
    def zy(self) -> Number:  return self.z, self.y
    @property
    def zz(self) -> Number:  return self.z, self.z
    
    
    @property
    def xxx(self) -> Number:  return self.x, self.x, self.x
    @property
    def xxy(self) -> Number:  return self.x, self.x, self.y
    @property
    def xxz(self) -> Number:  return self.x, self.x, self.z
    
    @property
    def xyx(self) -> Number:  return self.x, self.y, self.x
    @property
    def xyy(self) -> Number:  return self.x, self.y, self.y
    @property
    def xyz(self) -> Number:  return self.x, self.y, self.z
    
    @property
    def xzx(self) -> Number:  return self.x, self.z, self.x
    @property
    def xzy(self) -> Number:  return self.x, self.z, self.y
    @property
    def xzz(self) -> Number:  return self.x, self.z, self.z
    
    @property
    def yxx(self) -> Number:  return self.y, self.x, self.x
    @property
    def yxy(self) -> Number:  return self.y, self.x, self.y
    @property
    def yxz(self) -> Number:  return self.y, self.x, self.z
    
    @property
    def yyx(self) -> Number:  return self.y, self.y, self.x
    @property
    def yyy(self) -> Number:  return self.y, self.y, self.y
    @property
    def yyz(self) -> Number:  return self.y, self.y, self.z
    
    @property
    def yzx(self) -> Number:  return self.y, self.z, self.x
    @property
    def yzy(self) -> Number:  return self.y, self.z, self.y
    @property
    def yzz(self) -> Number:  return self.y, self.z, self.z
    
    @property
    def zxx(self) -> Number:  return self.z, self.x, self.x
    @property
    def zxy(self) -> Number:  return self.z, self.x, self.y
    @property
    def zxz(self) -> Number:  return self.z, self.x, self.z
    
    @property
    def zyx(self) -> Number:  return self.z, self.y, self.x
    @property
    def zyy(self) -> Number:  return self.z, self.y, self.y
    @property
    def zyz(self) -> Number:  return self.z, self.y, self.z
    
    @property
    def zzx(self) -> Number:  return self.z, self.z, self.x
    @property
    def zzy(self) -> Number:  return self.z, self.z, self.y
    @property
    def zzz(self) -> Number:  return self.z, self.z, self.z
