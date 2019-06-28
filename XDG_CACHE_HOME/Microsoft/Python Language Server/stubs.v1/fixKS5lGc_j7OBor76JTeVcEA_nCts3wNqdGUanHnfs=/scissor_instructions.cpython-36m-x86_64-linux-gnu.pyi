import builtins as _mod_builtins
import kivy.graphics.instructions as _mod_kivy_graphics_instructions

class Rect(_mod_builtins.object):
    'Rect class used internally by ScissorStack and ScissorPush to determine\n    correct clipping area.\n    '
    __class__ = Rect
    def __init__(self, *args, **kwargs):
        'Rect class used internally by ScissorStack and ScissorPush to determine\n    correct clipping area.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def intersect(self):
        pass
    

class ScissorPop(_mod_kivy_graphics_instructions.Instruction):
    'Pop the scissor stack. Call after ScissorPush, once you have completed\n    the drawing you wish to be clipped.\n    '
    __class__ = ScissorPop
    def __init__(self, *args, **kwargs):
        'Pop the scissor stack. Call after ScissorPush, once you have completed\n    the drawing you wish to be clipped.\n    '
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
    

class ScissorPush(_mod_kivy_graphics_instructions.Instruction):
    "Push the scissor stack. Provide kwargs of 'x', 'y', 'width', 'height'\n    to control the area and position of the scissoring region. Defaults to\n    0, 0, 100, 100\n\n    Scissor works by clipping all drawing outside of a rectangle starting at\n    int x, int y position and having sides of int width by int height in Window\n    space coordinates\n    "
    __class__ = ScissorPush
    def __init__(self, *args, **kwargs):
        "Push the scissor stack. Provide kwargs of 'x', 'y', 'width', 'height'\n    to control the area and position of the scissoring region. Defaults to\n    0, 0, 100, 100\n\n    Scissor works by clipping all drawing outside of a rectangle starting at\n    int x, int y position and having sides of int width by int height in Window\n    space coordinates\n    "
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
    def height(self):
        pass
    
    @property
    def pos(self):
        pass
    
    @property
    def size(self):
        pass
    
    @property
    def width(self):
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    

class ScissorStack(_mod_builtins.object):
    "Class used internally to keep track of the current state of\n    glScissors regions. Do not instantiate, prefer to inspect the module's\n    scissor_stack.\n    "
    __class__ = ScissorStack
    def __init__(self, *args, **kwargs):
        "Class used internally to keep track of the current state of\n    glScissors regions. Do not instantiate, prefer to inspect the module's\n    scissor_stack.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def back(self):
        pass
    
    @property
    def empty(self):
        pass
    
    def pop(self):
        pass
    
    def push(self):
        pass
    

__builtins__ = {}
__doc__ = '\nScissor Instructions\n====================\n\n.. versionadded:: 1.9.1\n\n\nScissor instructions clip your drawing area into a rectangular region.\n\n- :class:`ScissorPush`: Begins clipping, sets the bounds of the clip space\n- :class:`ScissorPop`: Ends clipping\n\nThe area provided to clip is in screenspace pixels and must be provided as\ninteger values not floats.\n\nThe following code will draw a circle ontop of our widget while clipping\nthe circle so it does not expand beyond the widget borders.\n\n.. code-block:: python\n\n    with self.canvas.after:\n        #If our widget is inside another widget that modified the coordinates\n        #spacing (such as ScrollView) we will want to convert to Window coords\n        x,y = self.to_window(*self.pos)\n        width, height = self.size\n        #We must convert from the possible float values provided by kivy\n        #widgets to an integer screenspace, in python3 round returns an int so\n        #the int cast will be unnecessary.\n        ScissorPush(x=int(round(x)), y=int(round(y)),\n            width=int(round(width)), height=int(round(height)))\n        Color(rgba=(1., 0., 0., .5))\n        Ellipse(size=(width*2., height*2.),\n            pos=self.center)\n        ScissorPop()\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/scissor_instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.scissor_instructions'
__package__ = 'kivy.graphics'
def __pyx_unpickle_Rect():
    pass

def __pyx_unpickle_ScissorPop():
    pass

def __pyx_unpickle_ScissorPush():
    pass

def __pyx_unpickle_ScissorStack():
    pass

__test__ = _mod_builtins.dict()
scissor_stack = ScissorStack()
