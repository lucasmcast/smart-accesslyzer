import builtins as _mod_builtins

class Matrix(_mod_builtins.object):
    '\n    Optimized matrix class for OpenGL::\n\n        >>> from kivy.graphics.transformation import Matrix\n        >>> m = Matrix()\n        >>> print(m)\n        [[ 1.000000 0.000000 0.000000 0.000000 ]\n        [ 0.000000 1.000000 0.000000 0.000000 ]\n        [ 0.000000 0.000000 1.000000 0.000000 ]\n        [ 0.000000 0.000000 0.000000 1.000000 ]]\n\n        [ 0   1   2   3]\n        [ 4   5   6   7]\n        [ 8   9  10  11]\n        [ 12  13  14  15]\n    '
    __class__ = Matrix
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, index):
        'Retrieve the value at the specified index or slice\n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def __init__(self, *args, **kwargs):
        '\n    Optimized matrix class for OpenGL::\n\n        >>> from kivy.graphics.transformation import Matrix\n        >>> m = Matrix()\n        >>> print(m)\n        [[ 1.000000 0.000000 0.000000 0.000000 ]\n        [ 0.000000 1.000000 0.000000 0.000000 ]\n        [ 0.000000 0.000000 1.000000 0.000000 ]\n        [ 0.000000 0.000000 0.000000 1.000000 ]]\n\n        [ 0   1   2   3]\n        [ 4   5   6   7]\n        [ 8   9  10  11]\n        [ 12  13  14  15]\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setitem__(self, index, value):
        'given an index and a value update the value at that location\n\n        .. versionadded:: 1.9.0\n        '
        return None
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get(self):
        'Retrieve the value of the current as a flat list.\n\n        .. versionadded:: 1.9.1\n        '
        pass
    
    def identity(self):
        'Reset the matrix to the identity matrix (inplace).\n        '
        pass
    
    def inverse(self):
        'Return the inverse of the matrix as a new Matrix.\n        '
        pass
    
    def look_at(self):
        'Returns a new lookat Matrix (similar to\n        `gluLookAt <http://www.opengl.org/sdk/docs/man2/xhtml/gluLookAt.xml>`_).\n\n        :Parameters:\n            `eyex`: float\n                Eyes X co-ordinate\n            `eyey`: float\n                Eyes Y co-ordinate\n            `eyez`: float\n                Eyes Z co-ordinate\n            `centerx`: float\n                The X position of the reference point\n            `centery`: float\n                The Y position of the reference point\n            `centerz`: float\n                The Z position of the reference point\n            `upx`: float\n                The X value up vector.\n            `upy`: float\n                The Y value up vector.\n            `upz`: float\n                The Z value up vector.\n\n        .. versionadded:: 1.6.0\n        '
        pass
    
    def multiply(self):
        'Multiply the given matrix with self (from the left)\n        i.e. we premultiply the given matrix by the current matrix and return\n        the result (not inplace)::\n\n            m.multiply(n) -> n * m\n            \n        :Parameters:\n            `ma`: Matrix\n                The matrix to multiply by\n        '
        pass
    
    def normal_matrix(self):
        'Computes the normal matrix, which is the inverse transpose\n        of the top left 3x3 modelview matrix used to transform normals\n        into eye/camera space.\n\n        .. versionadded:: 1.6.0\n        '
        pass
    
    def perspective(self):
        'Creates a perspective matrix (inplace).\n\n        :Parameters:\n            `fovy`: float\n                "Field Of View" angle\n            `aspect`: float\n                Aspect ratio\n            `zNear`: float\n                Near clipping plane\n            `zFar`: float\n                Far clippin plane\n\n        .. versionadded:: 1.6.0\n        '
        pass
    
    def project(self):
        'Project a point from 3d space into a 2d viewport.\n        \n        :Parameters:\n            `objx`: float\n                Points X co-ordinate\n            `objy`: float\n                Points Y co-ordinate\n            `objz`: float\n                Points Z co-ordinate\n            `model`: Matrix\n                The model matrix\n            `proj`: Matrix\n                The projection matrix\n            `vx`: float\n                Viewports X co-ordinate\n            `vy`: float\n                Viewports y co-ordinate\n            `vw`: float\n                Viewports width\n            `vh`: float\n                Viewports height\n\n        .. versionadded:: 1.7.0\n        '
        pass
    
    def rotate(self):
        'Rotate the matrix through the angle around the axis (x, y, z)\n        (inplace).\n\n        :Parameters:\n            `angle`: float\n                The angle through which to rotate the matrix\n            `x`: float\n                X position of the point\n            `y`: float\n                Y position of the point\n            `z`: float\n                Z position of the point\n        '
        pass
    
    def scale(self):
        'Scale the current matrix by the specified factors over\n        each dimension (inplace).\n\n        :Parameters:\n            `x`: float\n                The scale factor along the X axis         \n            `y`: float\n                The scale factor along the Y axis\n            `z`: float\n                The scale factor along the Z axis        \n        '
        pass
    
    def set(self):
        'Insert custom values into the matrix in a flat list format\n        or 4x4 array format like below::\n\n            m.set(array=[\n                [1.0, 0.0, 0.0, 0.0],\n                [0.0, 1.0, 0.0, 0.0],\n                [0.0, 0.0, 1.0, 0.0],\n                [0.0, 0.0, 0.0, 1.0]]\n            )\n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def tolist(self):
        'Retrieve the value of the current matrix in numpy format.\n        for example m.tolist() will return::\n\n            [[1.000000, 0.000000, 0.000000, 0.000000],\n            [0.000000, 1.000000, 0.000000, 0.000000],\n            [0.000000, 0.000000, 1.000000, 0.000000],\n            [0.000000, 0.000000, 0.000000, 1.000000]]\n\n        you can use this format to plug the result straight into numpy \n        in this way numpy.array(m.tolist()) \n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def transform_point(self):
        pass
    
    def translate(self):
        'Translate the matrix.\n\n        :Parameters:\n            `x`: float\n                The translation factor along the X axis         \n            `y`: float\n                The translation factor along the Y axis\n            `z`: float\n                The translation factor along the Z axis\n            '
        pass
    
    def transpose(self):
        'Return the transposed matrix as a new Matrix.\n\n        .. versionadded:: 1.6.0\n        '
        pass
    
    def view_clip(self):
        'Create a clip matrix (inplace).\n\n        :Parameters:\n            `left`: float\n                Co-ordinate\n            `right`: float\n                Co-ordinate\n            `bottom`: float\n                Co-ordinate\n            `top`: float\n                Co-ordinate\n            `near`: float\n                Co-ordinate\n            `far`: float\n                Co-ordinate\n            `perpective`: int\n                Co-ordinate\n\n        .. versionchanged:: 1.6.0\n            Enable support for perspective parameter.\n        '
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nTransformation\n==============\n\nThis module contains a Matrix class used for our Graphics calculations. We\ncurrently support:\n\n- rotation, translation and scaling matrices\n- multiplication matrix\n- clip matrix (with or without perspective)\n- transformation matrix for 3d touch\n\nFor more information on transformation matrices, please see the\n`OpenGL Matrices Tutorial <http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/>`_.\n\n.. versionchanged:: 1.6.0\n   Added :meth:`Matrix.perspective`, :meth:`Matrix.look_at` and\n   :meth:`Matrix.transpose`.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/transformation.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.transformation'
__package__ = 'kivy.graphics'
__test__ = _mod_builtins.dict()
