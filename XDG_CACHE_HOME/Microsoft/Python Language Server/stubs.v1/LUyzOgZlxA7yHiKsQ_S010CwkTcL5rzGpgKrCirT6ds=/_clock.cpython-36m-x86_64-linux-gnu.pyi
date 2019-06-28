import builtins as _mod_builtins
import kivy.weakmethod as _mod_kivy_weakmethod
import logging as _mod_logging

class ClockEvent(_mod_builtins.object):
    " A class that describes a callback scheduled with kivy's :attr:`Clock`.\n    This class is never created by the user; instead, kivy creates and returns\n    an instance of this class when scheduling a callback.\n\n    An event can be triggered (scheduled) by calling it. If it's already\n    scheduled, nothing will happen, otherwise it'll be scheduled. E.g.::\n\n        event = Clock.schedule_once(my_callback, .5)\n        event()  # nothing will happen since it's already scheduled.\n        event.cancel()  # cancel it\n        event()  # now it's scheduled again.\n    "
    def __call__(self):
        ' Schedules the callback associated with this instance.\n        If the callback is already scheduled, it will not be scheduled again.\n        '
        pass
    
    __class__ = ClockEvent
    def __init__(self, *args, **kwargs):
        " A class that describes a callback scheduled with kivy's :attr:`Clock`.\n    This class is never created by the user; instead, kivy creates and returns\n    an instance of this class when scheduling a callback.\n\n    An event can be triggered (scheduled) by calling it. If it's already\n    scheduled, nothing will happen, otherwise it'll be scheduled. E.g.::\n\n        event = Clock.schedule_once(my_callback, .5)\n        event()  # nothing will happen since it's already scheduled.\n        event.cancel()  # cancel it\n        event()  # now it's scheduled again.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _del_queue(self):
        pass
    
    @property
    def _dt(self):
        pass
    
    @property
    def _last_dt(self):
        pass
    
    @property
    def callback(self):
        pass
    
    def cancel(self):
        ' Cancels the callback if it was scheduled to be called. If not\n        scheduled, nothing happens.\n        '
        pass
    
    @property
    def cid(self):
        pass
    
    @property
    def clock(self):
        'The :class:`CyClockBase` instance associated with the event.\n    '
        pass
    
    def get_callback(self):
        "Returns the callback associated with the event. Callbacks get stored\n        with a indirect ref so that it doesn't keep objects alive. If the callback\n        is dead, None is returned.\n        "
        pass
    
    @property
    def is_triggered(self):
        'Returns whether the event is scheduled to have its callback executed by\n        the kivy thread.\n        '
        pass
    
    @property
    def loop(self):
        'Whether this event repeats at intervals of :attr:`timeout`.\n    '
        pass
    
    @property
    def next(self):
        'The next :class:`ClockEvent` in order they were scheduled.\n    '
        pass
    
    @property
    def prev(self):
        'The previous :class:`ClockEvent` in order they were scheduled.\n    '
        pass
    
    def release(self):
        '(internal method) Converts the callback into a indirect ref.\n        '
        pass
    
    def tick(self):
        '(internal method) Processes the event for the kivy thread.\n        '
        pass
    
    @property
    def timeout(self):
        'The duration after scheduling when the callback should be executed.\n    '
        pass
    
    @property
    def weak_callback(self):
        pass
    

class CyClockBase(_mod_builtins.object):
    'The base clock object with event support.\n    '
    __class__ = CyClockBase
    def __init__(self, *args, **kwargs):
        'The base clock object with event support.\n    '
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
    def _cap_event(self):
        'The cap event is the last event in the chain for each frame.\n    For a particular frame, events may be added dynamically after this event,\n    and the current frame should not process them.\n\n    Similarly to :attr:`_next_event`,\n    when canceling the :attr:`_cap_event`, :attr:`_cap_event` is shifted to the\n    one previous to it.\n    '
        pass
    
    @property
    def _last_event(self):
        'The last event in the chain. New events are added after this. Can be None.\n    '
        pass
    
    @property
    def _last_tick(self):
        pass
    
    @property
    def _lock(self):
        pass
    
    @property
    def _lock_acquire(self):
        pass
    
    @property
    def _lock_release(self):
        pass
    
    @property
    def _max_fps(self):
        pass
    
    @property
    def _next_event(self):
        "During frame processing when we service the events, this points to the next\n    event that will be processed. After ticking an event, we continue with\n    :attr:`_next_event`.\n\n    If a event that is canceled is the :attr:`_next_event`, :attr:`_next_event`\n    is shifted to point to the after after this, or None if it's at the end of the\n    chain.\n    "
        pass
    
    def _process_events(self):
        pass
    
    def _process_events_before_frame(self):
        pass
    
    def _release_references(self):
        pass
    
    @property
    def _root_event(self):
        'The first event in the chain. Can be None.\n    '
        pass
    
    @property
    def clock_resolution(self):
        "If the remaining time until the event timeout is less than :attr:`clock_resolution`,\n    the clock will execute the callback even if it hasn't exactly timed out.\n\n    If -1, the default, the resolution will be computed from config's ``maxfps``.\n    Otherwise, the provided value is used. Defaults to -1.\n    "
        pass
    
    def create_trigger(self):
        'Create a Trigger event. Check module documentation for more\n        information.\n\n        :returns:\n\n            A :class:`ClockEvent` instance. To schedule the callback of this\n            instance, you can call it.\n\n        .. versionadded:: 1.0.5\n\n        .. versionchanged:: 1.10.0\n\n            ``interval`` has been added. If True, it create a event that is called\n            every <timeout> seconds similar to :meth:`schedule_interval`. Defaults to\n            False.\n        '
        pass
    
    def get_events(self):
        'Returns the list of :class:`ClockEvent` instances currently scheduled.\n        '
        pass
    
    def get_min_timeout(self):
        'Returns the remaining time since the start of the current frame\n        for the event with the smallest timeout.\n        '
        pass
    
    def get_resolution(self):
        "Returns the minimum resolution the clock has. It's a function of\n        :attr:`clock_resolution` and ``maxfps`` provided at the config.\n        "
        pass
    
    @property
    def max_iteration(self):
        'The maximum number of callback iterations at the end of the frame, before the next\n    frame. If more iterations occur, a warning is issued.\n    '
        pass
    
    def on_schedule(self):
        'Function that is called internally every time an event is triggered\n        for this clock. It takes the event as a parameter.\n        '
        pass
    
    def schedule_del_safe(self):
        "Schedule a callback. Might be called from GC and cannot be cancelled.\n\n        It's unsafe to call various kinds of code, such as code with a lock,\n        from a `__del__` or `__dealloc__` methods. Since Kivy's Clock uses a\n        lock, it's generally unsafe to call from these methods. Instead,\n        use this method, which is thread safe and `__del__` or `__dealloc__`\n        safe, to schedule the callback in the kivy thread. It'll be executed\n        in order after the normal events are processed.\n\n        The callback takes no parameters and cannot be canceled.\n\n        .. versionadded:: 1.11.0\n        "
        pass
    
    def schedule_interval(self):
        'Schedule an event to be called every <timeout> seconds.\n\n        :returns:\n\n            A :class:`ClockEvent` instance. As opposed to\n            :meth:`create_trigger` which only creates the trigger event, this\n            method also schedules it.\n        '
        pass
    
    def schedule_once(self):
        'Schedule an event in <timeout> seconds. If <timeout> is unspecified\n        or 0, the callback will be called after the next frame is rendered.\n\n        :returns:\n\n            A :class:`ClockEvent` instance. As opposed to\n            :meth:`create_trigger` which only creates the trigger event, this\n            method also schedules it.\n\n        .. versionchanged:: 1.0.5\n            If the timeout is -1, the callback will be called before the next\n            frame (at :meth:`tick_draw`).\n        '
        pass
    
    def unschedule(self):
        "Remove a previously scheduled event.\n\n        :parameters:\n\n            `callback`: :class:`ClockEvent` or a callable.\n                If it's a :class:`ClockEvent` instance, then the callback\n                associated with this event will be canceled if it is\n                scheduled.\n\n                If it's a callable, then the callable will be unscheduled if it\n                was scheduled.\n\n                .. warning::\n\n                    Passing the callback function rather than the returned\n                    :class:`ClockEvent` will result in a significantly slower\n                    unscheduling.\n            `all`: bool\n                If True and if `callback` is a callable, all instances of this\n                callable will be unscheduled (i.e. if this callable was\n                scheduled multiple times). Defaults to `True`.\n\n        .. versionchanged:: 1.9.0\n            The all parameter was added. Before, it behaved as if `all` was\n            `True`.\n        "
        pass
    

class CyClockBaseFree(CyClockBase):
    'A clock class that supports scheduling free events in addition to normal\n    events.\n\n    Each of the :meth:`~CyClockBase.create_trigger`,\n    :meth:`~CyClockBase.schedule_once`, and :meth:`~CyClockBase.schedule_interval`\n    methods, which create a normal event, have a corresponding method\n    for creating a free event.\n    '
    __class__ = CyClockBaseFree
    def __init__(self, *args, **kwargs):
        'A clock class that supports scheduling free events in addition to normal\n    events.\n\n    Each of the :meth:`~CyClockBase.create_trigger`,\n    :meth:`~CyClockBase.schedule_once`, and :meth:`~CyClockBase.schedule_interval`\n    methods, which create a normal event, have a corresponding method\n    for creating a free event.\n    '
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
    
    def _process_free_events(self):
        pass
    
    def create_trigger(self):
        pass
    
    def create_trigger_free(self):
        'Similar to :meth:`~CyClockBase.create_trigger`, but instead creates\n        a free event.\n        '
        pass
    
    def get_min_free_timeout(self):
        'Returns the remaining time since the start of the current frame\n        for the *free* event with the smallest timeout.\n        '
        pass
    
    def schedule_interval(self):
        pass
    
    def schedule_interval_free(self):
        'Similar to :meth:`~CyClockBase.schedule_interval`, but instead creates\n        a free event.\n        '
        pass
    
    def schedule_once(self):
        pass
    
    def schedule_once_free(self):
        'Similar to :meth:`~CyClockBase.schedule_once`, but instead creates\n        a free event.\n        '
        pass
    

class FreeClockEvent(ClockEvent):
    'The event returned by the ``Clock.XXX_free`` methods of\n    :class:`CyClockBaseFree`. It stores whether the event was scheduled as a\n    free event.\n    '
    __class__ = FreeClockEvent
    def __init__(self, *args, **kwargs):
        'The event returned by the ``Clock.XXX_free`` methods of\n    :class:`CyClockBaseFree`. It stores whether the event was scheduled as a\n    free event.\n    '
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
    def free(self):
        'Whether this event was scheduled as a free event.\n    '
        pass
    

def Lock():
    'allocate_lock() -> lock object\n(allocate() is an obsolete synonym)\n\nCreate a new lock object. See help(type(threading.Lock())) for\ninformation about locks.'
    pass

Logger = _mod_logging.Logger()
WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = None
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/_clock.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy._clock'
__package__ = 'kivy'
def __pyx_unpickle_ClockEvent():
    pass

def __pyx_unpickle_FreeClockEvent():
    pass

__test__ = _mod_builtins.dict()
