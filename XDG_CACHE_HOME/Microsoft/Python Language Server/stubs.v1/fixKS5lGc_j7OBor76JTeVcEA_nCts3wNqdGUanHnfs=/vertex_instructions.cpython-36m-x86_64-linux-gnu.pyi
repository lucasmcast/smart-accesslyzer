import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import kivy.graphics.instructions as _mod_kivy_graphics_instructions
import logging as _mod_logging
import os as _mod_os

class Bezier(_mod_kivy_graphics_instructions.VertexInstruction):
    'A 2d Bezier curve.\n\n    .. versionadded:: 1.0.8\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...)\n        `segments`: int, defaults to 180\n            Define how many segments are needed for drawing the curve.\n            The drawing will be smoother if you have many segments.\n        `loop`: bool, defaults to False\n            Set the bezier curve to join the last point to the first.\n        `dash_length`: int\n            Length of a segment (if dashed), defaults to 1.\n        `dash_offset`: int\n            Distance between the end of a segment and the start of the\n            next one, defaults to 0. Changing this makes it dashed.\n    '
    __class__ = Bezier
    def __init__(self, *args, **kwargs):
        'A 2d Bezier curve.\n\n    .. versionadded:: 1.0.8\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...)\n        `segments`: int, defaults to 180\n            Define how many segments are needed for drawing the curve.\n            The drawing will be smoother if you have many segments.\n        `loop`: bool, defaults to False\n            Set the bezier curve to join the last point to the first.\n        `dash_length`: int\n            Length of a segment (if dashed), defaults to 1.\n        `dash_offset`: int\n            Distance between the end of a segment and the start of the\n            next one, defaults to 0. Changing this makes it dashed.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def dash_length(self):
        'Property for getting/setting the length of the dashes in the curve.\n        '
        pass
    
    @property
    def dash_offset(self):
        'Property for getting/setting the offset between the dashes in the\n        curve.\n        '
        pass
    
    @property
    def points(self):
        'Property for getting/settings the points of the triangle.\n\n        .. warning::\n\n            This will always reconstruct the whole graphic from the new points\n            list. It can be very CPU intensive.\n        '
        pass
    
    @property
    def segments(self):
        'Property for getting/setting the number of segments of the curve.\n        '
        pass
    

class BorderImage(Rectangle):
    "A 2d border image. The behavior of the border image is similar to the\n    concept of a CSS3 border-image.\n\n    :Parameters:\n        `border`: list\n            Border information in the format (bottom, right, top, left).\n            Each value is in pixels.\n\n        `auto_scale`: string\n            .. versionadded:: 1.9.1\n\n            .. versionchanged:: 1.9.2 \n\n                This used to be a bool and has been changed to be a string\n                state. \n\n            Can be one of 'off', 'both', 'x_only', 'y_only', 'y_full_x_lower',\n            'x_full_y_lower', 'both_lower'.\n\n            Autoscale controls the behavior of the 9-slice.\n\n            By default the border values are preserved exactly, meaning that\n            if the total size of the object is smaller than the border values\n            you will have some 'rendering errors' where your texture appears\n            inside out. This also makes it impossible to achieve a rounded\n            button that scales larger than the size of its source texture. The\n            various options for auto_scale will let you achieve some mixes of\n            the 2 types of rendering.\n\n            'off': is the default and behaves as BorderImage did when auto_scale\n            was False before.\n\n            'both': Scales both x and y dimension borders according to the size\n            of the BorderImage, this disables the BorderImage making it render\n            the same as a regular Image. \n\n            'x_only': The Y dimension functions as the default, and the X\n            scales to the size of the BorderImage's width.\n\n            'y_only': The X dimension functions as the default, and the Y \n            scales to the size of the BorderImage's height.\n\n            'y_full_x_lower': Y scales as in 'y_only', Y scales if the\n            size of the scaled version would be smaller than the provided\n            border only.\n\n            'x_full_y_lower': X scales as in 'x_only', Y scales if the\n            size of the scaled version would be smaller than the provided\n            border only.\n\n            'both_lower': This is what auto_scale did when it was True in 1.9.1\n            Both X and Y dimensions will be scaled if the BorderImage is\n            smaller than the source.\n\n            If the BorderImage's size is less than the sum of it's\n            borders, horizontally or vertically, and this property is\n            set to True, the borders will be rescaled to accommodate for\n            the smaller size.\n\n    "
    __class__ = BorderImage
    def __init__(self, *args, **kwargs):
        "A 2d border image. The behavior of the border image is similar to the\n    concept of a CSS3 border-image.\n\n    :Parameters:\n        `border`: list\n            Border information in the format (bottom, right, top, left).\n            Each value is in pixels.\n\n        `auto_scale`: string\n            .. versionadded:: 1.9.1\n\n            .. versionchanged:: 1.9.2 \n\n                This used to be a bool and has been changed to be a string\n                state. \n\n            Can be one of 'off', 'both', 'x_only', 'y_only', 'y_full_x_lower',\n            'x_full_y_lower', 'both_lower'.\n\n            Autoscale controls the behavior of the 9-slice.\n\n            By default the border values are preserved exactly, meaning that\n            if the total size of the object is smaller than the border values\n            you will have some 'rendering errors' where your texture appears\n            inside out. This also makes it impossible to achieve a rounded\n            button that scales larger than the size of its source texture. The\n            various options for auto_scale will let you achieve some mixes of\n            the 2 types of rendering.\n\n            'off': is the default and behaves as BorderImage did when auto_scale\n            was False before.\n\n            'both': Scales both x and y dimension borders according to the size\n            of the BorderImage, this disables the BorderImage making it render\n            the same as a regular Image. \n\n            'x_only': The Y dimension functions as the default, and the X\n            scales to the size of the BorderImage's width.\n\n            'y_only': The X dimension functions as the default, and the Y \n            scales to the size of the BorderImage's height.\n\n            'y_full_x_lower': Y scales as in 'y_only', Y scales if the\n            size of the scaled version would be smaller than the provided\n            border only.\n\n            'x_full_y_lower': X scales as in 'x_only', Y scales if the\n            size of the scaled version would be smaller than the provided\n            border only.\n\n            'both_lower': This is what auto_scale did when it was True in 1.9.1\n            Both X and Y dimensions will be scaled if the BorderImage is\n            smaller than the source.\n\n            If the BorderImage's size is less than the sum of it's\n            borders, horizontally or vertically, and this property is\n            set to True, the borders will be rescaled to accommodate for\n            the smaller size.\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def auto_scale(self):
        'Property for setting if the corners are automatically scaled\n        when the BorderImage is too small.\n        '
        pass
    
    @property
    def border(self):
        'Property for getting/setting the border of the class.\n        '
        pass
    
    @property
    def display_border(self):
        'Property for getting/setting the border display size.\n        '
        pass
    

class Ellipse(Rectangle):
    'A 2D ellipse.\n\n    .. versionchanged:: 1.0.7\n\n        Added angle_start and angle_end.\n\n    :Parameters:\n        `segments`: int, defaults to 180\n            Define how many segments are needed for drawing the ellipse.\n            The drawing will be smoother if you have many segments.\n        `angle_start`: int, defaults to 0\n            Specifies the starting angle, in degrees, of the disk portion.\n        `angle_end`: int, defaults to 360\n            Specifies the ending angle, in degrees, of the disk portion.\n    '
    __class__ = Ellipse
    def __init__(self, *args, **kwargs):
        'A 2D ellipse.\n\n    .. versionchanged:: 1.0.7\n\n        Added angle_start and angle_end.\n\n    :Parameters:\n        `segments`: int, defaults to 180\n            Define how many segments are needed for drawing the ellipse.\n            The drawing will be smoother if you have many segments.\n        `angle_start`: int, defaults to 0\n            Specifies the starting angle, in degrees, of the disk portion.\n        `angle_end`: int, defaults to 360\n            Specifies the ending angle, in degrees, of the disk portion.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def angle_end(self):
        'End angle of the ellipse in degrees, defaults to 360.\n        '
        pass
    
    @property
    def angle_start(self):
        'Start angle of the ellipse in degrees, defaults to 0.\n        '
        pass
    
    @property
    def segments(self):
        'Property for getting/setting the number of segments of the ellipse.\n        '
        pass
    

class GraphicException(_mod_builtins.Exception):
    'Exception raised when a graphics error is fired.\n    '
    __class__ = GraphicException
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised when a graphics error is fired.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kivy.graphics.vertex_instructions'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Line(_mod_kivy_graphics_instructions.VertexInstruction):
    "A 2d line.\n\n    Drawing a line can be done easily::\n\n        with self.canvas:\n            Line(points=[100, 100, 200, 100, 100, 200], width=10)\n\n    The line has 3 internal drawing modes that you should be aware of\n    for optimal results:\n\n    #. If the :attr:`width` is 1.0, then the standard GL_LINE drawing from\n       OpenGL will be used. :attr:`dash_length` and :attr:`dash_offset` will\n       work, while properties for cap and joint have no meaning here.\n    #. If the :attr:`width` is greater than 1.0, then a custom drawing method,\n       based on triangulation, will be used. :attr:`dash_length` and\n       :attr:`dash_offset` do not work in this mode.\n       Additionally, if the current color has an alpha less than 1.0, a\n       stencil will be used internally to draw the line.\n\n    .. image:: images/line-instruction.png\n        :align: center\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...)\n        `dash_length`: int\n            Length of a segment (if dashed), defaults to 1.\n        `dash_offset`: int\n            Offset between the end of a segment and the beginning of the\n            next one, defaults to 0. Changing this makes it dashed.\n        `width`: float\n            Width of the line, defaults to 1.0.\n        `cap`: str, defaults to 'round'\n            See :attr:`cap` for more information.\n        `joint`: str, defaults to 'round'\n            See :attr:`joint` for more information.\n        `cap_precision`: int, defaults to 10\n            See :attr:`cap_precision` for more information\n        `joint_precision`: int, defaults to 10\n            See :attr:`joint_precision` for more information\n            See :attr:`cap_precision` for more information.\n        `joint_precision`: int, defaults to 10\n            See :attr:`joint_precision` for more information.\n        `close`: bool, defaults to False\n            If True, the line will be closed.\n        `circle`: list\n            If set, the :attr:`points` will be set to build a circle. See\n            :attr:`circle` for more information.\n        `ellipse`: list\n            If set, the :attr:`points` will be set to build an ellipse. See\n            :attr:`ellipse` for more information.\n        `rectangle`: list\n            If set, the :attr:`points` will be set to build a rectangle. See\n            :attr:`rectangle` for more information.\n        `bezier`: list\n            If set, the :attr:`points` will be set to build a bezier line. See\n            :attr:`bezier` for more information.\n        `bezier_precision`: int, defaults to 180\n            Precision of the Bezier drawing.\n\n    .. versionchanged:: 1.0.8\n        `dash_offset` and `dash_length` have been added.\n\n    .. versionchanged:: 1.4.1\n        `width`, `cap`, `joint`, `cap_precision`, `joint_precision`, `close`,\n        `ellipse`, `rectangle` have been added.\n\n    .. versionchanged:: 1.4.1\n        `bezier`, `bezier_precision` have been added.\n\n    "
    __class__ = Line
    def __init__(self, *args, **kwargs):
        "A 2d line.\n\n    Drawing a line can be done easily::\n\n        with self.canvas:\n            Line(points=[100, 100, 200, 100, 100, 200], width=10)\n\n    The line has 3 internal drawing modes that you should be aware of\n    for optimal results:\n\n    #. If the :attr:`width` is 1.0, then the standard GL_LINE drawing from\n       OpenGL will be used. :attr:`dash_length` and :attr:`dash_offset` will\n       work, while properties for cap and joint have no meaning here.\n    #. If the :attr:`width` is greater than 1.0, then a custom drawing method,\n       based on triangulation, will be used. :attr:`dash_length` and\n       :attr:`dash_offset` do not work in this mode.\n       Additionally, if the current color has an alpha less than 1.0, a\n       stencil will be used internally to draw the line.\n\n    .. image:: images/line-instruction.png\n        :align: center\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...)\n        `dash_length`: int\n            Length of a segment (if dashed), defaults to 1.\n        `dash_offset`: int\n            Offset between the end of a segment and the beginning of the\n            next one, defaults to 0. Changing this makes it dashed.\n        `width`: float\n            Width of the line, defaults to 1.0.\n        `cap`: str, defaults to 'round'\n            See :attr:`cap` for more information.\n        `joint`: str, defaults to 'round'\n            See :attr:`joint` for more information.\n        `cap_precision`: int, defaults to 10\n            See :attr:`cap_precision` for more information\n        `joint_precision`: int, defaults to 10\n            See :attr:`joint_precision` for more information\n            See :attr:`cap_precision` for more information.\n        `joint_precision`: int, defaults to 10\n            See :attr:`joint_precision` for more information.\n        `close`: bool, defaults to False\n            If True, the line will be closed.\n        `circle`: list\n            If set, the :attr:`points` will be set to build a circle. See\n            :attr:`circle` for more information.\n        `ellipse`: list\n            If set, the :attr:`points` will be set to build an ellipse. See\n            :attr:`ellipse` for more information.\n        `rectangle`: list\n            If set, the :attr:`points` will be set to build a rectangle. See\n            :attr:`rectangle` for more information.\n        `bezier`: list\n            If set, the :attr:`points` will be set to build a bezier line. See\n            :attr:`bezier` for more information.\n        `bezier_precision`: int, defaults to 180\n            Precision of the Bezier drawing.\n\n    .. versionchanged:: 1.0.8\n        `dash_offset` and `dash_length` have been added.\n\n    .. versionchanged:: 1.4.1\n        `width`, `cap`, `joint`, `cap_precision`, `joint_precision`, `close`,\n        `ellipse`, `rectangle` have been added.\n\n    .. versionchanged:: 1.4.1\n        `bezier`, `bezier_precision` have been added.\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def bezier(self):
        'Use this property to build a bezier line, without calculating the\n        :attr:`points`. You can only set this property, not get it.\n\n        The argument must be a tuple of 2n elements, n being the number of points.\n\n        Usage::\n\n            Line(bezier=(x1, y1, x2, y2, x3, y3)\n\n        .. versionadded:: 1.4.2\n\n        .. note:: Bezier lines calculations are inexpensive for a low number of\n            points, but complexity is quadratic, so lines with a lot of points\n            can be very expensive to build, use with care!\n        '
        pass
    
    @property
    def bezier_precision(self):
        'Number of iteration for drawing the bezier between 2 segments,\n        defaults to 180. The bezier_precision must be at least 1.\n\n        .. versionadded:: 1.4.2\n        '
        pass
    
    @property
    def cap(self):
        "Determine the cap of the line, defaults to 'round'. Can be one of\n        'none', 'square' or 'round'\n\n        .. versionadded:: 1.4.1\n        "
        pass
    
    @property
    def cap_precision(self):
        'Number of iteration for drawing the "round" cap, defaults to 10.\n        The cap_precision must be at least 1.\n\n        .. versionadded:: 1.4.1\n        '
        pass
    
    @property
    def circle(self):
        "Use this property to build a circle, without calculating the\n        :attr:`points`. You can only set this property, not get it.\n\n        The argument must be a tuple of (center_x, center_y, radius, angle_start,\n        angle_end, segments):\n\n        * center_x and center_y represent the center of the circle\n        * radius represent the radius of the circle\n        * (optional) angle_start and angle_end are in degree. The default\n          value is 0 and 360.\n        * (optional) segments is the precision of the ellipse. The default\n          value is calculated from the range between angle.\n\n        Note that it's up to you to :attr:`close` the circle or not.\n\n        For example, for building a simple ellipse, in python::\n\n            # simple circle\n            Line(circle=(150, 150, 50))\n\n            # only from 90 to 180 degrees\n            Line(circle=(150, 150, 50, 90, 180))\n\n            # only from 90 to 180 degrees, with few segments\n            Line(circle=(150, 150, 50, 90, 180, 20))\n\n        .. versionadded:: 1.4.1\n        "
        pass
    
    @property
    def close(self):
        'If True, the line will be closed.\n\n        .. versionadded:: 1.4.1\n        '
        pass
    
    @property
    def dash_length(self):
        'Property for getting/setting the length of the dashes in the curve\n\n        .. versionadded:: 1.0.8\n        '
        pass
    
    @property
    def dash_offset(self):
        'Property for getting/setting the offset between the dashes in the curve\n\n        .. versionadded:: 1.0.8\n        '
        pass
    
    @property
    def ellipse(self):
        "Use this property to build an ellipse, without calculating the\n        :attr:`points`. You can only set this property, not get it.\n\n        The argument must be a tuple of (x, y, width, height, angle_start,\n        angle_end, segments):\n\n        * x and y represent the bottom left of the ellipse\n        * width and height represent the size of the ellipse\n        * (optional) angle_start and angle_end are in degree. The default\n          value is 0 and 360.\n        * (optional) segments is the precision of the ellipse. The default\n          value is calculated from the range between angle.\n\n        Note that it's up to you to :attr:`close` the ellipse or not.\n\n        For example, for building a simple ellipse, in python::\n\n            # simple ellipse\n            Line(ellipse=(0, 0, 150, 150))\n\n            # only from 90 to 180 degrees\n            Line(ellipse=(0, 0, 150, 150, 90, 180))\n\n            # only from 90 to 180 degrees, with few segments\n            Line(ellipse=(0, 0, 150, 150, 90, 180, 20))\n\n        .. versionadded:: 1.4.1\n        "
        pass
    
    @property
    def joint(self):
        "Determine the join of the line, defaults to 'round'. Can be one of\n        'none', 'round', 'bevel', 'miter'.\n\n        .. versionadded:: 1.4.1\n        "
        pass
    
    @property
    def joint_precision(self):
        'Number of iteration for drawing the "round" joint, defaults to 10.\n        The joint_precision must be at least 1.\n\n        .. versionadded:: 1.4.1\n        '
        pass
    
    @property
    def points(self):
        'Property for getting/settings points of the line\n\n        .. warning::\n\n            This will always reconstruct the whole graphics from the new points\n            list. It can be very CPU expensive.\n        '
        pass
    
    @property
    def rectangle(self):
        'Use this property to build a rectangle, without calculating the\n        :attr:`points`. You can only set this property, not get it.\n\n        The argument must be a tuple of (x, y, width, height):\n\n        * x and y represent the bottom-left position of the rectangle\n        * width and height represent the size\n\n        The line is automatically closed.\n\n        Usage::\n\n            Line(rectangle=(0, 0, 200, 200))\n\n        .. versionadded:: 1.4.1\n        '
        pass
    
    @property
    def rounded_rectangle(self):
        'Use this property to build a rectangle, without calculating the\n        :attr:`points`. You can only set this property, not get it.\n\n        The argument must be a tuple of one of the following forms:\n\n        * (x, y, width, height, corner_radius)\n        * (x, y, width, height, corner_radius, resolution)\n        * (x, y, width, height, corner_radius1, corner_radius2, corner_radius3, corner_radius4)\n        * (x, y, width, height, corner_radius1, corner_radius2, corner_radius3, corner_radius4, resolution)\n\n        * x and y represent the bottom-left position of the rectangle\n        * width and height represent the size\n        * corner_radius is the number of pixels between two borders and the center of the circle arc joining them\n        * resolution is the number of line segment that will be used to draw the circle arc at each corner (defaults to 30)\n\n        The line is automatically closed.\n\n        Usage::\n\n            Line(rounded_rectangle=(0, 0, 200, 200, 10, 20, 30, 40, 100))\n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    @property
    def width(self):
        'Determine the width of the line, defaults to 1.0.\n\n        .. versionadded:: 1.4.1\n        '
        pass
    

Logger = _mod_logging.Logger()
class Mesh(_mod_kivy_graphics_instructions.VertexInstruction):
    "A 2d mesh.\n\n    In OpenGL ES 2.0 and in our graphics implementation, you cannot have more\n    than 65535 indices.\n\n    A list of vertices is described as::\n\n        vertices = [x1, y1, u1, v1, x2, y2, u2, v2, ...]\n                    |            |  |            |\n                    +---- i1 ----+  +---- i2 ----+\n\n    If you want to draw a triangle, add 3 vertices. You can then make an\n    indices list as follows:\n\n        indices = [0, 1, 2]\n\n    .. versionadded:: 1.1.0\n\n    :Parameters:\n        `vertices`: iterable\n            List of vertices in the format (x1, y1, u1, v1, x2, y2, u2, v2...).\n        `indices`: iterable\n            List of indices in the format (i1, i2, i3...).\n        `mode`: str\n            Mode of the vbo. Check :attr:`mode` for more information. Defaults to\n            'points'.\n        `fmt`: list\n            The format for vertices, by default, each vertex is described by 2D\n            coordinates (x, y) and 2D texture coordinate (u, v).\n            Each element of the list should be a tuple or list, of the form\n\n                (variable_name, size, type)\n\n            which will allow mapping vertex data to the glsl instructions.\n\n                [(b'v_pos', 2, 'float'), (b'v_tc', 2, 'float'),]\n\n            will allow using\n\n                attribute vec2 v_pos;\n                attribute vec2 v_tc;\n\n            in glsl's vertex shader.\n\n    .. versionchanged:: 1.8.1\n        Before, `vertices` and `indices` would always be converted to a list,\n        now, they are only converted to a list if they do not implement the\n        buffer interface. So e.g. numpy arrays, python arrays etc. are used\n        in place, without creating any additional copies. However, the\n        buffers cannot be readonly (even though they are not changed, due to\n        a cython limitation) and must be contiguous in memory.\n\n    .. note::\n        When passing a memoryview or a instance that implements the buffer\n        interface, `vertices` should be a buffer of floats (`'f'` code in\n        python array) and `indices` should be a buffer of unsigned short (`'H'`\n        code in python array). Arrays in other formats will still have to be\n        converted internally, negating any potential gain.\n    "
    __class__ = Mesh
    def __init__(self, *args, **kwargs):
        "A 2d mesh.\n\n    In OpenGL ES 2.0 and in our graphics implementation, you cannot have more\n    than 65535 indices.\n\n    A list of vertices is described as::\n\n        vertices = [x1, y1, u1, v1, x2, y2, u2, v2, ...]\n                    |            |  |            |\n                    +---- i1 ----+  +---- i2 ----+\n\n    If you want to draw a triangle, add 3 vertices. You can then make an\n    indices list as follows:\n\n        indices = [0, 1, 2]\n\n    .. versionadded:: 1.1.0\n\n    :Parameters:\n        `vertices`: iterable\n            List of vertices in the format (x1, y1, u1, v1, x2, y2, u2, v2...).\n        `indices`: iterable\n            List of indices in the format (i1, i2, i3...).\n        `mode`: str\n            Mode of the vbo. Check :attr:`mode` for more information. Defaults to\n            'points'.\n        `fmt`: list\n            The format for vertices, by default, each vertex is described by 2D\n            coordinates (x, y) and 2D texture coordinate (u, v).\n            Each element of the list should be a tuple or list, of the form\n\n                (variable_name, size, type)\n\n            which will allow mapping vertex data to the glsl instructions.\n\n                [(b'v_pos', 2, 'float'), (b'v_tc', 2, 'float'),]\n\n            will allow using\n\n                attribute vec2 v_pos;\n                attribute vec2 v_tc;\n\n            in glsl's vertex shader.\n\n    .. versionchanged:: 1.8.1\n        Before, `vertices` and `indices` would always be converted to a list,\n        now, they are only converted to a list if they do not implement the\n        buffer interface. So e.g. numpy arrays, python arrays etc. are used\n        in place, without creating any additional copies. However, the\n        buffers cannot be readonly (even though they are not changed, due to\n        a cython limitation) and must be contiguous in memory.\n\n    .. note::\n        When passing a memoryview or a instance that implements the buffer\n        interface, `vertices` should be a buffer of floats (`'f'` code in\n        python array) and `indices` should be a buffer of unsigned short (`'H'`\n        code in python array). Arrays in other formats will still have to be\n        converted internally, negating any potential gain.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def indices(self):
        'Vertex indices used to specify the order when drawing the\n        mesh.\n        '
        pass
    
    @property
    def mode(self):
        "VBO Mode used for drawing vertices/indices. Can be one of 'points',\n        'line_strip', 'line_loop', 'lines', 'triangles', 'triangle_strip' or\n        'triangle_fan'.\n        "
        pass
    
    @property
    def vertices(self):
        "List of x, y, u, v coordinates used to construct the Mesh. Right now,\n        the Mesh instruction doesn't allow you to change the format of the\n        vertices, which means it's only x, y + one texture coordinate.\n        "
        pass
    

class Point(_mod_kivy_graphics_instructions.VertexInstruction):
    'A list of 2d points. Each point is represented as a square with a\n    width/height of 2 times the :attr:`pointsize`.\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...), where each pair\n            of coordinates specifies the center of a new point.\n        `pointsize`: float, defaults to 1.\n            The size of the point, measured from the center to the edge. A\n            value of 1.0 therefore means the real size will be 2.0 x 2.0.\n\n    .. warning::\n\n        Starting from version 1.0.7, vertex instruction have a limit of 65535\n        vertices (indices of vertex to be accurate).\n        2 entries in the list (x, y) will be converted to 4 vertices. So the\n        limit inside Point() class is 2^15-2.\n\n    '
    __class__ = Point
    def __init__(self, *args, **kwargs):
        'A list of 2d points. Each point is represented as a square with a\n    width/height of 2 times the :attr:`pointsize`.\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2...), where each pair\n            of coordinates specifies the center of a new point.\n        `pointsize`: float, defaults to 1.\n            The size of the point, measured from the center to the edge. A\n            value of 1.0 therefore means the real size will be 2.0 x 2.0.\n\n    .. warning::\n\n        Starting from version 1.0.7, vertex instruction have a limit of 65535\n        vertices (indices of vertex to be accurate).\n        2 entries in the list (x, y) will be converted to 4 vertices. So the\n        limit inside Point() class is 2^15-2.\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add_point(self):
        'Add a point to the current :attr:`points` list.\n\n        If you intend to add multiple points, prefer to use this method instead\n        of reassigning a new :attr:`points` list. Assigning a new :attr:`points`\n        list will recalculate and reupload the whole buffer into the GPU.\n        If you use add_point, it will only upload the changes.\n        '
        pass
    
    @property
    def points(self):
        'Property for getting/settings the center points in the points list.\n        Each pair of coordinates specifies the center of a new point.\n        '
        pass
    
    @property
    def pointsize(self):
        'Property for getting/setting point size.\n        The size is measured from the center to the edge, so a value of 1.0\n        means the real size will be 2.0 x 2.0.\n        '
        pass
    

class Quad(_mod_kivy_graphics_instructions.VertexInstruction):
    'A 2d quad.\n\n    :Parameters:\n        `points`: list\n            List of point in the format (x1, y1, x2, y2, x3, y3, x4, y4).\n    '
    __class__ = Quad
    def __init__(self, *args, **kwargs):
        'A 2d quad.\n\n    :Parameters:\n        `points`: list\n            List of point in the format (x1, y1, x2, y2, x3, y3, x4, y4).\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def points(self):
        'Property for getting/settings points of the quad.\n        '
        pass
    

class Rectangle(_mod_kivy_graphics_instructions.VertexInstruction):
    'A 2d rectangle.\n\n    :Parameters:\n        `pos`: list\n            Position of the rectangle, in the format (x, y).\n        `size`: list\n            Size of the rectangle, in the format (width, height).\n    '
    __class__ = Rectangle
    def __init__(self, *args, **kwargs):
        'A 2d rectangle.\n\n    :Parameters:\n        `pos`: list\n            Position of the rectangle, in the format (x, y).\n        `size`: list\n            Size of the rectangle, in the format (width, height).\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def pos(self):
        'Property for getting/settings the position of the rectangle.\n        '
        pass
    
    @property
    def size(self):
        'Property for getting/settings the size of the rectangle.\n        '
        pass
    

class RoundedRectangle(Rectangle):
    'A 2D rounded rectangle.\n\n    .. versionadded:: 1.9.1\n\n    :Parameters:\n        `segments`: int, defaults to 10\n            Define how many segments are needed for drawing the rounded corner.\n            The drawing will be smoother if you have many segments.\n        `radius`: list, defaults to [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]\n            Specifies the radii used for the rounded corners clockwise:\n            top-left, top-right, bottom-right, bottom-left.\n            Elements of the list can be numbers or tuples of two numbers to specify different x,y dimensions.\n            One value will define all corner radii to be of this value.\n            Four values will define each corner radius separately.\n            Higher numbers of values will be truncated to four.\n            The first value will be used for all corners if there are fewer than four values.\n    '
    __class__ = RoundedRectangle
    def __init__(self, *args, **kwargs):
        'A 2D rounded rectangle.\n\n    .. versionadded:: 1.9.1\n\n    :Parameters:\n        `segments`: int, defaults to 10\n            Define how many segments are needed for drawing the rounded corner.\n            The drawing will be smoother if you have many segments.\n        `radius`: list, defaults to [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]\n            Specifies the radii used for the rounded corners clockwise:\n            top-left, top-right, bottom-right, bottom-left.\n            Elements of the list can be numbers or tuples of two numbers to specify different x,y dimensions.\n            One value will define all corner radii to be of this value.\n            Four values will define each corner radius separately.\n            Higher numbers of values will be truncated to four.\n            The first value will be used for all corners if there are fewer than four values.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def radius(self):
        'Corner radii of the rounded rectangle, defaults to [10,].\n        '
        pass
    
    @property
    def segments(self):
        'Property for getting/setting the number of segments for each corner.\n        '
        pass
    

class SmoothLine(Line):
    'Experimental line using over-draw methods to get better anti-aliasing\n    results. It has few drawbacks:\n\n    - drawing a line with alpha will probably not have the intended result if\n      the line crosses itself.\n    - :attr:`~Line.cap`, :attr:`~Line.joint` and :attr:`~Line.dash` properties\n      are not supported.\n    - it uses a custom texture with a premultiplied alpha.\n    - lines under 1px in width are not supported: they will look the same.\n\n    .. warning::\n\n        This is an unfinished work, experimental, and subject to crashes.\n\n    .. versionadded:: 1.9.0\n    '
    __class__ = SmoothLine
    def __init__(self, *args, **kwargs):
        'Experimental line using over-draw methods to get better anti-aliasing\n    results. It has few drawbacks:\n\n    - drawing a line with alpha will probably not have the intended result if\n      the line crosses itself.\n    - :attr:`~Line.cap`, :attr:`~Line.joint` and :attr:`~Line.dash` properties\n      are not supported.\n    - it uses a custom texture with a premultiplied alpha.\n    - lines under 1px in width are not supported: they will look the same.\n\n    .. warning::\n\n        This is an unfinished work, experimental, and subject to crashes.\n\n    .. versionadded:: 1.9.0\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _smooth_reload_observer(self):
        pass
    
    @property
    def overdraw_width(self):
        'Determine the overdraw width of the line, defaults to 1.2.\n        '
        pass
    
    def premultiplied_texture(self):
        pass
    

class StripMesh(_mod_kivy_graphics_instructions.VertexInstruction):
    'A specialized 2d mesh.\n\n    (internal) Used for SVG, will be available with doc later.\n    '
    __class__ = StripMesh
    def __init__(self, *args, **kwargs):
        'A specialized 2d mesh.\n\n    (internal) Used for SVG, will be available with doc later.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Triangle(_mod_kivy_graphics_instructions.VertexInstruction):
    'A 2d triangle.\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2, x3, y3).\n    '
    __class__ = Triangle
    def __init__(self, *args, **kwargs):
        'A 2d triangle.\n\n    :Parameters:\n        `points`: list\n            List of points in the format (x1, y1, x2, y2, x3, y3).\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def points(self):
        'Property for getting/settings points of the triangle.\n        '
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = "\nVertex Instructions\n===================\n\nThis module includes all the classes for drawing simple vertex objects.\n\nUpdating properties\n-------------------\n\nThe list attributes of the graphics instruction classes (e.g.\n:attr:`Triangle.points`, :attr:`Mesh.indices` etc.) are not Kivy\nproperties but Python properties. As a consequence, the graphics will only\nbe updated when the list object itself is changed and not when list values\nare modified.\n\nFor example in python:\n\n.. code-block:: python\n\n    class MyWidget(Button):\n\n        triangle = ObjectProperty(None)\n        def __init__(self, **kwargs):\n            super(MyWidget, self).__init__(**kwargs)\n            with self.canvas:\n                self.triangle = Triangle(points=[0,0, 100,100, 200,0])\n\nand in kv:\n\n.. code-block:: kv\n\n    <MyWidget>:\n        text: 'Update'\n        on_press:\n            self.triangle.points[3] = 400\n\nAlthough pressing the button will change the triangle coordinates,\nthe graphics will not be updated because the list itself has not\nchanged. Similarly, no updates will occur using any syntax that changes\nonly elements of the list e.g. self.triangle.points[0:2] = [10,10] or\nself.triangle.points.insert(10) etc.\nTo force an update after a change, the list variable itself must be\nchanged, which in this case can be achieved with:\n\n.. code-block:: kv\n\n    <MyWidget>:\n        text: 'Update'\n        on_press:\n            self.triangle.points[3] = 400\n            self.triangle.points = self.triangle.points\n"
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/vertex_instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.vertex_instructions'
__package__ = 'kivy.graphics'
def __pyx_unpickle_Bezier():
    pass

def __pyx_unpickle_BorderImage():
    pass

def __pyx_unpickle_Ellipse():
    pass

def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Line():
    pass

def __pyx_unpickle_Point():
    pass

def __pyx_unpickle_Quad():
    pass

def __pyx_unpickle_Rectangle():
    pass

def __pyx_unpickle_RoundedRectangle():
    pass

def __pyx_unpickle_SmoothLine():
    pass

def __pyx_unpickle_StripMesh():
    pass

def __pyx_unpickle_Triangle():
    pass

__test__ = _mod_builtins.dict()
environ = _mod_os._Environ()
platform = 'linux'
