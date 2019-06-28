import builtins as _mod_builtins
import kivy.graphics.instructions as _mod_kivy_graphics_instructions
import logging as _mod_logging

Logger = _mod_logging.Logger()
PY2 = False
class StencilPop(_mod_kivy_graphics_instructions.Instruction):
    'Pop the stencil stack. See the module documentation for more information.\n    '
    __class__ = StencilPop
    def __init__(self, *args, **kwargs):
        'Pop the stencil stack. See the module documentation for more information.\n    '
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
    

class StencilPush(_mod_kivy_graphics_instructions.Instruction):
    'Push the stencil stack. See the module documentation for more\n    information.\n    '
    __class__ = StencilPush
    def __init__(self, *args, **kwargs):
        'Push the stencil stack. See the module documentation for more\n    information.\n    '
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
    

class StencilUnUse(_mod_kivy_graphics_instructions.Instruction):
    'Use current stencil buffer to unset the mask.\n    '
    __class__ = StencilUnUse
    def __init__(self, *args, **kwargs):
        'Use current stencil buffer to unset the mask.\n    '
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
    

class StencilUse(_mod_kivy_graphics_instructions.Instruction):
    'Use current stencil buffer as a mask. Check the module documentation for\n    more information.\n    '
    __class__ = StencilUse
    def __init__(self, *args, **kwargs):
        'Use current stencil buffer as a mask. Check the module documentation for\n    more information.\n    '
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
    def func_op(self):
        "Determine the stencil operation to use for glStencilFunc(). Can be\n        one of 'never', 'less', 'equal', 'lequal', 'greater', 'notequal',\n        'gequal' or 'always'.\n\n        By default, the operator is set to 'equal'.\n\n        .. versionadded:: 1.5.0\n        "
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = "\nStencil instructions\n====================\n\n.. versionadded:: 1.0.4\n\n.. versionchanged:: 1.3.0\n    The stencil operation has been updated to resolve some issues that appeared\n    when nested. You **must** now have a StencilUnUse and repeat the same\n    operation as you did after StencilPush.\n\nStencil instructions permit you to draw and use the current drawing as a mask.\nThey don't give as much control as pure OpenGL, but you can still do fancy\nthings!\n\nThe stencil buffer can be controlled using these 3 instructions:\n\n    - :class:`StencilPush`: push a new stencil layer.\n      Any drawing that happens after this will be used as a mask.\n    - :class:`StencilUse` : now draw the next instructions and use the stencil\n      for masking them.\n    - :class:`StencilUnUse` : stop using the stencil i.e. remove the mask and\n      draw normally.\n    - :class:`StencilPop` : pop the current stencil layer.\n\n\nYou should always respect this scheme:\n\n.. code-block:: kv\n\n    StencilPush\n\n    # PHASE 1: put any drawing instructions to use as a mask here.\n\n    StencilUse\n\n    # PHASE 2: all the drawing here will be automatically clipped by the\n    # mask created in PHASE 1.\n\n    StencilUnUse\n\n    # PHASE 3: put the same drawing instruction here as you did in PHASE 1\n\n    StencilPop\n\n    # PHASE 4: the stencil is now removed from the stack and unloaded.\n\n\nLimitations\n-----------\n\n- Drawing in PHASE 1 and PHASE 3 must not collide or you\n  will get unexpected results\n- The stencil is activated as soon as you perform a StencilPush\n- The stencil is deactivated as soon as you've correctly popped all the stencil\n  layers\n- You must not play with stencils yourself between a StencilPush / StencilPop\n- You can push another stencil after a StencilUse / before the StencilPop\n- You can push up to 128 layers of stencils (8 for kivy < 1.3.0)\n\n\nExample of stencil usage\n------------------------\n\nHere is an example, in kv style::\n\n    StencilPush\n\n    # create a rectangular mask with a pos of (100, 100) and a (100, 100) size.\n    Rectangle:\n        pos: 100, 100\n        size: 100, 100\n\n    StencilUse\n\n    # we want to show a big green rectangle, however, the previous stencil\n    # mask will crop us :)\n    Color:\n        rgb: 0, 1, 0\n    Rectangle:\n        size: 900, 900\n\n    StencilUnUse\n\n    # you must redraw the stencil mask to remove it\n    Rectangle:\n        pos: 100, 100\n        size: 100, 100\n\n    StencilPop\n\n"
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/stencil_instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.stencil_instructions'
__package__ = 'kivy.graphics'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_StencilPop():
    pass

def __pyx_unpickle_StencilPush():
    pass

def __pyx_unpickle_StencilUnUse():
    pass

def __pyx_unpickle_StencilUse():
    pass

__test__ = _mod_builtins.dict()
