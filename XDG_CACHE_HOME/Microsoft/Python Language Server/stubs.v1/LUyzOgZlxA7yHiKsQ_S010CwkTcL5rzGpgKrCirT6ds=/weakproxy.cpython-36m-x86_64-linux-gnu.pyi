import builtins as _mod_builtins

class WeakProxy(_mod_builtins.object):
    'Replacement for weakref.proxy to support comparisons\n    '
    def __abs__(self):
        'abs(self)'
        return WeakProxy()
    
    def __add__(self, value):
        'Return self+value.'
        return WeakProxy()
    
    def __and__(self, value):
        'Return self&value.'
        return WeakProxy()
    
    def __bool__(self):
        'self != 0'
        return False
    
    def __bytes__(self):
        pass
    
    __class__ = WeakProxy
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __dir__(self):
        return ['']
    
    def __divmod__(self, value):
        'Return divmod(self, value).'
        return (0, 0)
    
    def __enter__(self):
        return self
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __exit__(self):
        pass
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattr__(self):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __iand__(self, value):
        'Return self&=value.'
        return None
    
    def __ifloordiv__(self, value):
        'Return self//=value.'
        pass
    
    def __ilshift__(self, value):
        'Return self<<=value.'
        pass
    
    def __imod__(self, value):
        'Return self%=value.'
        pass
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        return 0
    
    def __init__(self, *args, **kwargs):
        'Replacement for weakref.proxy to support comparisons\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __invert__(self):
        '~self'
        return WeakProxy()
    
    def __ior__(self, value):
        'Return self|=value.'
        return None
    
    def __ipow__(self, value):
        'Return self**=value.'
        pass
    
    def __irshift__(self, value):
        'Return self>>=value.'
        pass
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return WeakProxy()
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __ixor__(self, value):
        'Return self^=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lshift__(self, value):
        'Return self<<value.'
        return WeakProxy()
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mod__(self, value):
        'Return self%value.'
        return WeakProxy()
    
    def __mul__(self, value):
        'Return self*value.'
        return WeakProxy()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return WeakProxy()
    
    def __or__(self, value):
        'Return self|value.'
        return WeakProxy()
    
    def __pos__(self):
        '+self'
        return WeakProxy()
    
    def __pow__(self, value, mod):
        'Return pow(self, value, mod).'
        return WeakProxy()
    
    def __radd__(self, value):
        'Return value+self.'
        return WeakProxy()
    
    def __rand__(self, value):
        'Return value&self.'
        return WeakProxy()
    
    def __rdiv__(self):
        pass
    
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        return (0, 0)
    
    def __reduce__(self):
        return ''; return ()
    
    @property
    def __ref(self):
        pass
    
    def __ref__(self):
        pass
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __reversed__(self):
        pass
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return WeakProxy()
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return WeakProxy()
    
    def __rmod__(self, value):
        'Return value%self.'
        return WeakProxy()
    
    def __rmul__(self, value):
        'Return value*self.'
        return WeakProxy()
    
    def __ror__(self, value):
        'Return value|self.'
        return WeakProxy()
    
    def __round__(self, ndigits=0):
        return WeakProxy()
    
    def __rpow__(self, value, mod):
        'Return pow(value, self, mod).'
        return WeakProxy()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return WeakProxy()
    
    def __rshift__(self, value):
        'Return self>>value.'
        return WeakProxy()
    
    def __rsub__(self, value):
        'Return value-self.'
        return WeakProxy()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return WeakProxy()
    
    def __rxor__(self, value):
        'Return value^self.'
        return WeakProxy()
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return WeakProxy()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def __unicode__(self):
        pass
    
    def __xor__(self, value):
        'Return self^value.'
        return WeakProxy()
    

__builtins__ = {}
__doc__ = '\nWeak Proxy\n==========\n\nIn order to allow garbage collection, the weak proxy provides\n`weak references <https://en.wikipedia.org/wiki/Weak_reference>`_ to objects.\nIt effectively enhances the\n`weakref.proxy <https://docs.python.org/2/library/weakref.html#weakref.proxy>`_\nby adding comparison support.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/weakproxy.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.weakproxy'
__package__ = 'kivy'
def __pyx_unpickle_WeakProxy():
    pass

__test__ = _mod_builtins.dict()
