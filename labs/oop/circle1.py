'''
>>> # Create a circle with a radius
>>> c = Circle(4)
>>> # test attribute and method access
>>> c.radius
4
>>> c.diameter
8
>>> c.get_area(places=0)
50
>>> c.circumference
25.133
>>> c2 = Circle(10)
>>> c2.radius = 10

'''



if __name__ == '__main__':
    import doctest
    doctest.testmod()
