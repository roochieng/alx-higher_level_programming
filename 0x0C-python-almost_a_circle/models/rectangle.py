#!/usr/bin/python3
"""
Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle Class constractor
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Width Property
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        Setting Width
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """
        Height Property
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        Setting height
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """
        X- axis property
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        Setting x axis
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """
        Y axis property
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        Setting Y axis
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        Checking the integer parameter
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        Area calculator method
        """
        return self.__width * self.__height

    def display(self):
        """
        Display method
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        string method
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update method
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Dict to hold keys and values method
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
