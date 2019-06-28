import builtins as _mod_builtins
import kivy.graphics.instructions as _mod_kivy_graphics_instructions

class ClearBuffers(_mod_kivy_graphics_instructions.Instruction):
    ' Clearbuffer Graphics Instruction.\n\n    .. versionadded:: 1.3.0\n\n    Clear the buffers specified by the instructions buffer mask property.\n    By default, only the coloc buffer is cleared.\n    '
    __class__ = ClearBuffers
    def __init__(self, *args, **kwargs):
        ' Clearbuffer Graphics Instruction.\n\n    .. versionadded:: 1.3.0\n\n    Clear the buffers specified by the instructions buffer mask property.\n    By default, only the coloc buffer is cleared.\n    '
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
    def clear_color(self):
        'If True, the color buffer will be cleared.\n        '
        pass
    
    @property
    def clear_depth(self):
        'If True, the depth buffer will be cleared.\n        '
        pass
    
    @property
    def clear_stencil(self):
        'If True, the stencil buffer will be cleared.\n        '
        pass
    

class ClearColor(_mod_kivy_graphics_instructions.Instruction):
    ' ClearColor Graphics Instruction.\n\n    .. versionadded:: 1.3.0\n\n    Sets the clear color used to clear buffers with the glClear function or\n    :class:`ClearBuffers` graphics instructions.\n    '
    __class__ = ClearColor
    def __init__(self, *args, **kwargs):
        ' ClearColor Graphics Instruction.\n\n    .. versionadded:: 1.3.0\n\n    Sets the clear color used to clear buffers with the glClear function or\n    :class:`ClearBuffers` graphics instructions.\n    '
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
    def r(self):
        'Red component, between 0 and 1.\n        '
        pass
    
    @property
    def rgb(self):
        'RGB color, a list of 3 values in 0-1 range where alpha will be 1.\n        '
        pass
    
    @property
    def rgba(self):
        'RGBA color used for the clear color, a list of 4 values in the 0-1\n        range.\n        '
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nGL instructions\n===============\n\n.. versionadded:: 1.3.0\n\nClearing an FBO\n---------------\n\nTo clear an FBO, you can use :class:`ClearColor` and :class:`ClearBuffers`\ninstructions like this example::\n\n    self.fbo = Fbo(size=self.size)\n    with self.fbo:\n        ClearColor(0, 0, 0, 0)\n        ClearBuffers()\n\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/gl_instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.gl_instructions'
__package__ = 'kivy.graphics'
def __pyx_unpickle_ClearBuffers():
    pass

def __pyx_unpickle_ClearColor():
    pass

__test__ = _mod_builtins.dict()
