import builtins as _mod_builtins
import kivy.cache as _mod_kivy_cache
import kivy.core.image as _mod_kivy_core_image
import kivy.graphics.instructions as _mod_kivy_graphics_instructions
import logging as _mod_logging

class ApplyContextMatrix(_mod_kivy_graphics_instructions.ContextInstruction):
    "Pre-multiply the matrix at the top of the stack specified by\n    `target_stack` by the matrix at the top of the 'source_stack'\n\n    .. versionadded:: 1.6.0\n    "
    __class__ = ApplyContextMatrix
    def __init__(self, *args, **kwargs):
        "Pre-multiply the matrix at the top of the stack specified by\n    `target_stack` by the matrix at the top of the 'source_stack'\n\n    .. versionadded:: 1.6.0\n    "
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
    def source_stack(self):
        "Name of the matrix stack to use as a source.\n        Can be 'modelview_mat', 'projection_mat' or 'frag_modelview_mat'.\n\n        .. versionadded:: 1.6.0\n        "
        pass
    
    @property
    def target_stack(self):
        "Name of the matrix stack to use as a target.\n        Can be 'modelview_mat', 'projection_mat' or 'frag_modelview_mat'.\n\n        .. versionadded:: 1.6.0\n        "
        pass
    

class BindTexture(_mod_kivy_graphics_instructions.ContextInstruction):
    'BindTexture Graphic instruction.\n    The BindTexture Instruction will bind a texture and enable\n    GL_TEXTURE_2D for subsequent drawing.\n\n    :Parameters:\n        `texture`: Texture\n            Specifies the texture to bind to the given index.\n    '
    __class__ = BindTexture
    def __init__(self, *args, **kwargs):
        'BindTexture Graphic instruction.\n    The BindTexture Instruction will bind a texture and enable\n    GL_TEXTURE_2D for subsequent drawing.\n\n    :Parameters:\n        `texture`: Texture\n            Specifies the texture to bind to the given index.\n    '
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
    def index(self):
        pass
    
    @property
    def source(self):
        'Set/get the source (filename) to load for the texture.\n        '
        pass
    
    @property
    def texture(self):
        pass
    

Cache = _mod_kivy_cache.Cache
class ChangeState(_mod_kivy_graphics_instructions.ContextInstruction):
    'Instruction that changes the values of arbitrary states/uniforms on the\n    current render context.\n\n    .. versionadded:: 1.6.0\n    '
    __class__ = ChangeState
    def __init__(self, *args, **kwargs):
        'Instruction that changes the values of arbitrary states/uniforms on the\n    current render context.\n\n    .. versionadded:: 1.6.0\n    '
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
    def changes(self):
        pass
    

class Color(_mod_kivy_graphics_instructions.ContextInstruction):
    "\n    Instruction to set the color state for any vertices being\n    drawn after it.\n\n    This represents a color between 0 and 1, but is applied as a\n    *multiplier* to the texture of any vertex instructions following\n    it in a canvas. If no texture is set, the vertex instruction\n    takes the precise color of the Color instruction.\n\n    For instance, if a Rectangle has a texture with uniform color\n    ``(0.5, 0.5, 0.5, 1.0)`` and the preceding Color has\n    ``rgba=(1, 0.5, 2, 1)``, the actual visible color will be\n    ``(0.5, 0.25, 1.0, 1.0)`` since the Color instruction is applied as\n    a multiplier to every rgba component. In this case, a Color\n    component outside the 0-1 range gives a visible result as the\n    intensity of the blue component is doubled.\n\n    To declare a Color in Python, you can do::\n\n        from kivy.graphics import Color\n\n        # create red v\n        c = Color(1, 0, 0)\n        # create blue color\n        c = Color(0, 1, 0)\n        # create blue color with 50% alpha\n        c = Color(0, 1, 0, .5)\n\n        # using hsv mode\n        c = Color(0, 1, 1, mode='hsv')\n        # using hsv mode + alpha\n        c = Color(0, 1, 1, .2, mode='hsv')\n\n    You can also set color components that are available as properties\n    by passing them as keyword arguments::\n\n        c = Color(b=0.5)  # sets the blue component only\n\n    In kv lang you can set the color properties directly:\n\n    .. code-block:: kv\n\n        <Rule>:\n            canvas:\n                # red color\n                Color:\n                    rgb: 1, 0, 0\n                # blue color\n                Color:\n                    rgb: 0, 1, 0\n                # blue color with 50% alpha\n                Color:\n                    rgba: 0, 1, 0, .5\n\n                # using hsv mode\n                Color:\n                    hsv: 0, 1, 1\n                # using hsv mode + alpha\n                Color:\n                    hsv: 0, 1, 1\n                    a: .5\n\n    "
    __class__ = Color
    def __init__(self, *args, **kwargs):
        "\n    Instruction to set the color state for any vertices being\n    drawn after it.\n\n    This represents a color between 0 and 1, but is applied as a\n    *multiplier* to the texture of any vertex instructions following\n    it in a canvas. If no texture is set, the vertex instruction\n    takes the precise color of the Color instruction.\n\n    For instance, if a Rectangle has a texture with uniform color\n    ``(0.5, 0.5, 0.5, 1.0)`` and the preceding Color has\n    ``rgba=(1, 0.5, 2, 1)``, the actual visible color will be\n    ``(0.5, 0.25, 1.0, 1.0)`` since the Color instruction is applied as\n    a multiplier to every rgba component. In this case, a Color\n    component outside the 0-1 range gives a visible result as the\n    intensity of the blue component is doubled.\n\n    To declare a Color in Python, you can do::\n\n        from kivy.graphics import Color\n\n        # create red v\n        c = Color(1, 0, 0)\n        # create blue color\n        c = Color(0, 1, 0)\n        # create blue color with 50% alpha\n        c = Color(0, 1, 0, .5)\n\n        # using hsv mode\n        c = Color(0, 1, 1, mode='hsv')\n        # using hsv mode + alpha\n        c = Color(0, 1, 1, .2, mode='hsv')\n\n    You can also set color components that are available as properties\n    by passing them as keyword arguments::\n\n        c = Color(b=0.5)  # sets the blue component only\n\n    In kv lang you can set the color properties directly:\n\n    .. code-block:: kv\n\n        <Rule>:\n            canvas:\n                # red color\n                Color:\n                    rgb: 1, 0, 0\n                # blue color\n                Color:\n                    rgb: 0, 1, 0\n                # blue color with 50% alpha\n                Color:\n                    rgba: 0, 1, 0, .5\n\n                # using hsv mode\n                Color:\n                    hsv: 0, 1, 1\n                # using hsv mode + alpha\n                Color:\n                    hsv: 0, 1, 1\n                    a: .5\n\n    "
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
    def a(self):
        'Alpha component, between 0 and 1.\n        '
        pass
    
    @property
    def b(self):
        'Blue component, between 0 and 1.\n        '
        pass
    
    @property
    def g(self):
        'Green component, between 0 and 1.\n        '
        pass
    
    @property
    def h(self):
        'Hue component, between 0 and 1.\n        '
        pass
    
    @property
    def hsv(self):
        'HSV color, list of 3 values in 0-1 range, alpha will be 1.\n        '
        pass
    
    @property
    def r(self):
        'Red component, between 0 and 1.\n        '
        pass
    
    @property
    def rgb(self):
        'RGB color, list of 3 values in 0-1 range. The alpha will be 1.\n        '
        pass
    
    @property
    def rgba(self):
        'RGBA color, list of 4 values in 0-1 range.\n        '
        pass
    
    @property
    def s(self):
        'Saturation component, between 0 and 1.\n        '
        pass
    
    @property
    def v(self):
        'Value component, between 0 and 1.\n        '
        pass
    

Image = _mod_kivy_core_image.Image
class LineWidth(_mod_kivy_graphics_instructions.ContextInstruction):
    __class__ = LineWidth
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class LoadIdentity(_mod_kivy_graphics_instructions.ContextInstruction):
    "Load the identity Matrix into the matrix stack specified by\n    the instructions stack property (default='modelview_mat')\n\n    .. versionadded:: 1.6.0\n    "
    __class__ = LoadIdentity
    def __init__(self, *args, **kwargs):
        "Load the identity Matrix into the matrix stack specified by\n    the instructions stack property (default='modelview_mat')\n\n    .. versionadded:: 1.6.0\n    "
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
    def stack(self):
        "Name of the matrix stack to use. Can be 'modelview_mat',\n        'projection_mat' or 'frag_modelview_mat'.\n        "
        pass
    

Logger = _mod_logging.Logger()
class MatrixInstruction(_mod_kivy_graphics_instructions.ContextInstruction):
    'Base class for Matrix Instruction on the canvas.\n    '
    __class__ = MatrixInstruction
    def __init__(self, *args, **kwargs):
        'Base class for Matrix Instruction on the canvas.\n    '
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
    def matrix(self):
        ' Matrix property. Matrix from the transformation module.\n        Setting the matrix using this property when a change is made\n        is important because it will notify the context about the update.\n        '
        pass
    
    @property
    def stack(self):
        "Name of the matrix stack to use. Can be 'modelview_mat',\n        'projection_mat' or 'frag_modelview_mat'.\n\n        .. versionadded:: 1.6.0\n        "
        pass
    

PY2 = False
class PopMatrix(_mod_kivy_graphics_instructions.ContextInstruction):
    "Pop the matrix from the context's matrix stack onto the model view.\n    "
    __class__ = PopMatrix
    def __init__(self, *args, **kwargs):
        "Pop the matrix from the context's matrix stack onto the model view.\n    "
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
    def stack(self):
        "Name of the matrix stack to use. Can be 'modelview_mat',\n        'projection_mat' or 'frag_modelview_mat'.\n\n        .. versionadded:: 1.6.0\n        "
        pass
    

class PopState(_mod_kivy_graphics_instructions.ContextInstruction):
    'Instruction that pops arbitrary states/uniforms off the context\n    state stack.\n\n    .. versionadded:: 1.6.0\n    '
    __class__ = PopState
    def __init__(self, *args, **kwargs):
        'Instruction that pops arbitrary states/uniforms off the context\n    state stack.\n\n    .. versionadded:: 1.6.0\n    '
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
    def state(self):
        pass
    
    @property
    def states(self):
        pass
    

class PushMatrix(_mod_kivy_graphics_instructions.ContextInstruction):
    "Push the matrix onto the context's matrix stack.\n    "
    __class__ = PushMatrix
    def __init__(self, *args, **kwargs):
        "Push the matrix onto the context's matrix stack.\n    "
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
    def stack(self):
        "Name of the matrix stack to use. Can be 'modelview_mat',\n        'projection_mat' or 'frag_modelview_mat'.\n\n        .. versionadded:: 1.6.0\n        "
        pass
    

class PushState(_mod_kivy_graphics_instructions.ContextInstruction):
    'Instruction that pushes arbitrary states/uniforms onto the context\n    state stack.\n\n    .. versionadded:: 1.6.0\n    '
    __class__ = PushState
    def __init__(self, *args, **kwargs):
        'Instruction that pushes arbitrary states/uniforms onto the context\n    state stack.\n\n    .. versionadded:: 1.6.0\n    '
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
    def state(self):
        pass
    
    @property
    def states(self):
        pass
    

class Rotate(Transform):
    'Rotate the coordinate space by applying a rotation transformation\n    on the modelview matrix. You can set the properties of the instructions\n    afterwards with e.g. ::\n\n        rot.angle = 90\n        rot.axis = (0, 0, 1)\n    '
    __class__ = Rotate
    def __init__(self, *args, **kwargs):
        'Rotate the coordinate space by applying a rotation transformation\n    on the modelview matrix. You can set the properties of the instructions\n    afterwards with e.g. ::\n\n        rot.angle = 90\n        rot.axis = (0, 0, 1)\n    '
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
    def angle(self):
        'Property for getting/setting the angle of the rotation.\n        '
        pass
    
    @property
    def axis(self):
        'Property for getting/setting the axis of the rotation.\n\n        The format of the axis is (x, y, z).\n        '
        pass
    
    @property
    def origin(self):
        'Origin of the rotation.\n\n        .. versionadded:: 1.7.0\n\n        The format of the origin can be either (x, y) or (x, y, z).\n        '
        pass
    
    def set(self):
        "Set the angle and axis of rotation.\n\n        >>> rotationobject.set(90, 0, 0, 1)\n\n        .. deprecated:: 1.7.0\n\n            The set() method doesn't use the new :attr:`origin` property.\n        "
        pass
    

class Scale(Transform):
    'Instruction to create a non uniform scale transformation.\n\n    Create using one or three arguments::\n\n       Scale(s)         # scale all three axes the same\n       Scale(x, y, z)   # scale the axes independently\n\n    .. deprecated:: 1.6.0\n        Deprecated single scale property in favor of x, y, z, xyz axis\n        independent scaled factors.\n    '
    __class__ = Scale
    def __init__(self, *args, **kwargs):
        'Instruction to create a non uniform scale transformation.\n\n    Create using one or three arguments::\n\n       Scale(s)         # scale all three axes the same\n       Scale(x, y, z)   # scale the axes independently\n\n    .. deprecated:: 1.6.0\n        Deprecated single scale property in favor of x, y, z, xyz axis\n        independent scaled factors.\n    '
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
    def origin(self):
        'Origin of the scale.\n\n        .. versionadded:: 1.9.0\n\n        The format of the origin can be either (x, y) or (x, y, z).\n        '
        pass
    
    @property
    def scale(self):
        'Property for getting/setting the scale.\n\n        .. deprecated:: 1.6.0\n            Deprecated in favor of per axis scale properties x,y,z, xyz, etc.\n        '
        pass
    
    @property
    def x(self):
        'Property for getting/setting the scale on the X axis.\n\n        .. versionchanged:: 1.6.0\n        '
        pass
    
    @property
    def xyz(self):
        '3 tuple scale vector in 3D in x, y, and z axis.\n\n        .. versionchanged:: 1.6.0\n        '
        pass
    
    @property
    def y(self):
        'Property for getting/setting the scale on the Y axis.\n\n        .. versionchanged:: 1.6.0\n        '
        pass
    
    @property
    def z(self):
        'Property for getting/setting the scale on Z axis.\n\n        .. versionchanged:: 1.6.0\n        '
        pass
    

class Transform(MatrixInstruction):
    'Transform class. A matrix instruction class which\n    modifies the transformation matrix.\n    '
    __class__ = Transform
    def __init__(self, *args, **kwargs):
        'Transform class. A matrix instruction class which\n    modifies the transformation matrix.\n    '
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
    
    def identity(self):
        'Resets the transformation to the identity matrix.\n        '
        pass
    
    def rotate(self):
        'Rotate the transformation by matrix by *angle* degrees around the\n        axis defined by the vector ax, ay, az.\n        '
        pass
    
    def scale(self):
        'Applies a uniform scaling of s to the matrix transformation.\n        '
        pass
    
    def transform(self):
        'Multiply the instructions matrix by trans.\n        '
        pass
    
    def translate(self):
        'Translate the instructions transformation by tx, ty, tz.\n        '
        pass
    

class Translate(Transform):
    'Instruction to create a translation of the model view coordinate space.\n\n    Construct by either::\n\n        Translate(x, y)         # translate in just the two axes\n        Translate(x, y, z)      # translate in all three axes\n    '
    __class__ = Translate
    def __init__(self, *args, **kwargs):
        'Instruction to create a translation of the model view coordinate space.\n\n    Construct by either::\n\n        Translate(x, y)         # translate in just the two axes\n        Translate(x, y, z)      # translate in all three axes\n    '
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
    def x(self):
        'Property for getting/setting the translation on the X axis.\n        '
        pass
    
    @property
    def xy(self):
        '2 tuple with translation vector in 2D for x and y axis.\n        '
        pass
    
    @property
    def xyz(self):
        '3 tuple translation vector in 3D in x, y, and z axis.\n        '
        pass
    
    @property
    def y(self):
        'Property for getting/setting the translation on the Y axis.\n        '
        pass
    
    @property
    def z(self):
        'Property for getting/setting the translation on the Z axis.\n        '
        pass
    

class UpdateNormalMatrix(_mod_kivy_graphics_instructions.ContextInstruction):
    "Update the normal matrix 'normal_mat' based on the current\n    modelview matrix. This will compute 'normal_mat' uniform as:\n    `inverse( transpose( mat3(mvm) ) )`\n\n    .. versionadded:: 1.6.0\n    "
    __class__ = UpdateNormalMatrix
    def __init__(self, *args, **kwargs):
        "Update the normal matrix 'normal_mat' based on the current\n    modelview matrix. This will compute 'normal_mat' uniform as:\n    `inverse( transpose( mat3(mvm) ) )`\n\n    .. versionadded:: 1.6.0\n    "
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
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = "\nContext instructions\n====================\n\nThe context instructions represent non graphics elements such as:\n\n* Matrix manipulations (PushMatrix, PopMatrix, Rotate, Translate, Scale,\n  MatrixInstruction)\n* Color manipulations (Color)\n* Texture bindings (BindTexture)\n\n.. versionchanged:: 1.0.8\n    The LineWidth instruction has been removed. It wasn't working before and we\n    actually have no working implementation. We need to do more experimentation\n    to get it right. Check the bug\n    `#207 <https://github.com/kivy/kivy/issues/207>`_ for more information.\n\n"
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/context_instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.context_instructions'
__package__ = 'kivy.graphics'
def __pyx_unpickle_ApplyContextMatrix():
    pass

def __pyx_unpickle_BindTexture():
    pass

def __pyx_unpickle_ChangeState():
    pass

def __pyx_unpickle_Color():
    pass

def __pyx_unpickle_LoadIdentity():
    pass

def __pyx_unpickle_MatrixInstruction():
    pass

def __pyx_unpickle_PopMatrix():
    pass

def __pyx_unpickle_PopState():
    pass

def __pyx_unpickle_PushMatrix():
    pass

def __pyx_unpickle_PushState():
    pass

def __pyx_unpickle_Rotate():
    pass

def __pyx_unpickle_Scale():
    pass

def __pyx_unpickle_Transform():
    pass

def __pyx_unpickle_Translate():
    pass

def __pyx_unpickle_UpdateNormalMatrix():
    pass

__test__ = _mod_builtins.dict()
def gl_init_resources():
    pass

def join(a, *p):
    "Join two or more pathname components, inserting '/' as needed.\n    If any component is an absolute path, all previous path components\n    will be discarded.  An empty last part will result in a path that\n    ends with a separator."
    pass

kivy_shader_dir = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/data/glsl'
def resource_find(filename):
    'Search for a resource in the list of paths.\n    Use resource_add_path to add a custom path to the search.\n    '
    pass

