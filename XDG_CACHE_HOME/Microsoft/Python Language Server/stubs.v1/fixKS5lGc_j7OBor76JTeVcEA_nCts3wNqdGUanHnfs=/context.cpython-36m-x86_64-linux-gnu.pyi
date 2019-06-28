import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import kivy.cache as _mod_kivy_cache
import kivy.context as _mod_kivy_context
import kivy.weakmethod as _mod_kivy_weakmethod
import logging as _mod_logging
import os as _mod_os

weakref = _mod_builtins.type
Cache = _mod_kivy_cache.Cache
Clock = _mod_kivy_context.ProxyContext()
class Context(_mod_builtins.object):
    '\n    The Context class manages groups of graphics instructions. It can also be used to manage\n    observer callbacks. See :meth:`add_reload_observer` and :meth:`remove_reload_observer`\n    for more information.\n    '
    __class__ = Context
    def __init__(self, *args, **kwargs):
        '\n    The Context class manages groups of graphics instructions. It can also be used to manage\n    observer callbacks. See :meth:`add_reload_observer` and :meth:`remove_reload_observer`\n    for more information.\n    '
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
    
    def add_reload_observer(self):
        '(internal) Add a callback to be called after the whole graphics context has\n        been reloaded. This is where you can reupload your custom data into the\n        GPU.\n\n        :Parameters:\n            `callback`: func(context) -> return None\n                The first parameter will be the context itself\n            `before`: boolean, defaults to False\n                If True, the callback will be executed before all the\n                reloading processes. Use it if you want to clear your cache for\n                example.\n\n        .. versionchanged:: 1.4.0\n            `before` parameter added.\n        '
        pass
    
    def flag_update_canvas(self):
        pass
    
    def gl_dealloc(self):
        pass
    
    def reload(self):
        pass
    
    def remove_reload_observer(self):
        '(internal) Remove a callback from the observer list previously added by\n        :meth:`add_reload_observer`.\n        '
        pass
    
    def trigger_gl_dealloc(self):
        pass
    

Logger = _mod_logging.Logger()
WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nContext management\n==================\n\n.. versionadded:: 1.2.0\n\nThis class manages a registry of all created graphics instructions. It has\nthe ability to flush and delete them.\n\nYou can read more about Kivy graphics contexts in the :doc:`api-kivy.graphics`\nmodule documentation. These are based on\n`OpenGL graphics contexts <http://www.opengl.org/wiki/OpenGL_Context>`_.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/context.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.context'
__package__ = 'kivy.graphics'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Context():
    pass

__test__ = _mod_builtins.dict()
environ = _mod_os._Environ()
def get_context():
    pass

ref = weakref()
def time():
    'time() -> floating point number\n\nReturn the current time in seconds since the Epoch.\nFractions of a second may be present if the system clock provides them.'
    return 1.0

