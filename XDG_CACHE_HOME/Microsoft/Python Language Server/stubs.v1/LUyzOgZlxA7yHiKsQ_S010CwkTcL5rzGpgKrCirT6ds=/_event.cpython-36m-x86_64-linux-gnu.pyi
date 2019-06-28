import builtins as _mod_builtins
import collections as _mod_collections
import functools as _mod_functools
import kivy.weakmethod as _mod_kivy_weakmethod

class BoundCallback(_mod_builtins.object):
    __class__ = BoundCallback
    def __init__(self, *args, **kwargs):
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
    

class EventDispatcher(ObjectWithUid):
    'Generic event dispatcher interface.\n\n    See the module docstring for usage.\n    '
    __class__ = EventDispatcher
    def __init__(self, *args, **kwargs):
        'Generic event dispatcher interface.\n\n    See the module docstring for usage.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __proxy_getter(self):
        pass
    
    def __proxy_setter(self):
        pass
    
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
    def _kwargs_applied_init(self):
        pass
    
    def apply_property(self):
        "Adds properties at runtime to the class. The function accepts\n        keyword arguments of the form `prop_name=prop`, where `prop` is a\n        :class:`Property` instance and `prop_name` is the name of the attribute\n        of the property.\n\n        .. versionadded:: 1.9.1\n\n        .. warning::\n\n            This method is not recommended for common usage because you should\n            declare the properties in your class instead of using this method.\n\n        For example::\n\n            >>> print(wid.property('sticks', quiet=True))\n            None\n            >>> wid.apply_property(sticks=ObjectProperty(55, max=10))\n            >>> print(wid.property('sticks', quiet=True))\n            <kivy.properties.ObjectProperty object at 0x04303130>\n        "
        pass
    
    def bind(self):
        'Bind an event type or a property to a callback.\n\n        Usage::\n\n            # With properties\n            def my_x_callback(obj, value):\n                print(\'on object\', obj, \'x changed to\', value)\n            def my_width_callback(obj, value):\n                print(\'on object\', obj, \'width changed to\', value)\n            self.bind(x=my_x_callback, width=my_width_callback)\n\n            # With event\n            def my_press_callback(obj):\n                print(\'event on object\', obj)\n            self.bind(on_press=my_press_callback)\n\n        In general, property callbacks are called with 2 arguments (the\n        object and the property\'s new value) and event callbacks with\n        one argument (the object). The example above illustrates this.\n\n        The following example demonstrates various ways of using the bind\n        function in a complete application::\n\n            from kivy.uix.boxlayout import BoxLayout\n            from kivy.app import App\n            from kivy.uix.button import Button\n            from functools import partial\n\n\n            class DemoBox(BoxLayout):\n                """\n                This class demonstrates various techniques that can be used for binding to\n                events. Although parts could me made more optimal, advanced Python concepts\n                are avoided for the sake of readability and clarity.\n                """\n                def __init__(self, **kwargs):\n                    super(DemoBox, self).__init__(**kwargs)\n                    self.orientation = "vertical"\n\n                    # We start with binding to a normal event. The only argument\n                    # passed to the callback is the object which we have bound to.\n                    btn = Button(text="Normal binding to event")\n                    btn.bind(on_press=self.on_event)\n\n                    # Next, we bind to a standard property change event. This typically\n                    # passes 2 arguments: the object and the value\n                    btn2 = Button(text="Normal binding to a property change")\n                    btn2.bind(state=self.on_property)\n\n                    # Here we use anonymous functions (a.k.a lambdas) to perform binding.\n                    # Their advantage is that you can avoid declaring new functions i.e.\n                    # they offer a concise way to "redirect" callbacks.\n                    btn3 = Button(text="Using anonymous functions.")\n                    btn3.bind(on_press=lambda x: self.on_event(None))\n\n                    # You can also declare a function that accepts a variable number of\n                    # positional and keyword arguments and use introspection to determine\n                    # what is being passed in. This is very handy for debugging as well\n                    # as function re-use. Here, we use standard event binding to a function\n                    # that accepts optional positional and keyword arguments.\n                    btn4 = Button(text="Use a flexible function")\n                    btn4.bind(on_press=self.on_anything)\n\n                    # Lastly, we show how to use partial functions. They are sometimes\n                    # difficult to grasp, but provide a very flexible and powerful way to\n                    # reuse functions.\n                    btn5 = Button(text="Using partial functions. For hardcores.")\n                    btn5.bind(on_press=partial(self.on_anything, "1", "2", monthy="python"))\n\n                    for but in [btn, btn2, btn3, btn4, btn5]:\n                        self.add_widget(but)\n\n                def on_event(self, obj):\n                    print("Typical event from", obj)\n\n                def on_property(self, obj, value):\n                    print("Typical property change from", obj, "to", value)\n\n                def on_anything(self, *args, **kwargs):\n                    print(\'The flexible function has *args of\', str(args),\n                        "and **kwargs of", str(kwargs))\n\n\n            class DemoApp(App):\n                def build(self):\n                    return DemoBox()\n\n            if __name__ == "__main__":\n                DemoApp().run()\n\n        When binding a function to an event or property, a\n        :class:`kivy.weakmethod.WeakMethod` of the callback is saved, and\n        when dispatching the callback is removed if the callback reference\n        becomes invalid.\n\n        If a callback has already been bound to a given event or property,\n        it won\'t be added again.\n        '
        pass
    
    def create_property(self):
        "Create a new property at runtime.\n\n        .. versionadded:: 1.0.9\n\n        .. versionchanged:: 1.8.0\n            `value` parameter added, can be used to set the default value of the\n            property. Also, the type of the value is used to specialize the\n            created property.\n\n        .. versionchanged:: 1.9.0\n            In the past, if `value` was of type `bool`, a `NumericProperty`\n            would be created, now a `BooleanProperty` is created.\n\n            Also, now and positional and keyword arguments are passed to the\n            property when created.\n\n        .. warning::\n\n            This function is designed for the Kivy language, don't use it in\n            your code. You should declare the property in your class instead of\n            using this method.\n\n        :Parameters:\n            `name`: string\n                Name of the property\n            `value`: object, optional\n                Default value of the property. Type is also used for creating\n                more appropriate property types. Defaults to None.\n\n\n        ::\n\n            >>> mywidget = Widget()\n            >>> mywidget.create_property('custom')\n            >>> mywidget.custom = True\n            >>> print(mywidget.custom)\n            True\n        "
        pass
    
    def dispatch(self):
        'Dispatch an event across all the handlers added in bind/fbind().\n        As soon as a handler returns True, the dispatching stops.\n\n        The function collects all the positional and keyword arguments and\n        passes them on to the handlers.\n\n        .. note::\n            The handlers are called in reverse order than they were registered\n            with :meth:`bind`.\n\n        :Parameters:\n            `event_type`: basestring\n                the event name to dispatch.\n\n        .. versionchanged:: 1.9.0\n            Keyword arguments collection and forwarding was added. Before, only\n            positional arguments would be collected and forwarded.\n\n        '
        pass
    
    def dispatch_children(self):
        pass
    
    def dispatch_generic(self):
        pass
    
    def events(self):
        'Return all the events in the class. Can be used for introspection.\n\n        .. versionadded:: 1.8.0\n\n        '
        pass
    
    def fbind(self):
        'A method for advanced, and typically faster binding. This method is\n        different than :meth:`bind` and is meant for more advanced users and\n        internal usage. It can be used as long as the following points are heeded.\n\n        #. As opposed to :meth:`bind`, it does not check that this function and\n           largs/kwargs has not been bound before to this name. So binding\n           the same callback multiple times will just keep adding it.\n        #. Although :meth:`bind` creates a :class:`WeakMethod` of the callback when\n           binding to an event or property, this method stores the callback\n           directly, unless a keyword argument `ref` with value True is provided\n           and then a :class:`WeakMethod` is saved.\n           This is useful when there\'s no risk of a memory leak by storing the\n           callback directly.\n        #. This method returns a unique positive number if `name` was found and\n           bound, and `0`, otherwise. It does not raise an exception, like\n           :meth:`bind` if the property `name` is not found. If not zero,\n           the uid returned is unique to this `name` and callback and can be\n           used with :meth:`unbind_uid` for unbinding.\n\n\n        When binding a callback with largs and/or kwargs, :meth:`funbind`\n        must be used for unbinding. If no largs and kwargs are provided,\n        :meth:`unbind` may be used as well. :meth:`unbind_uid` can be used in\n        either case.\n\n        This method passes on any caught positional and/or keyword arguments to\n        the callback, removing the need to call partial. When calling the\n        callback the expended largs are passed on followed by instance/value\n        (just instance for kwargs) followed by expended kwargs.\n\n        Following is an example of usage similar to the example in\n        :meth:`bind`::\n\n            class DemoBox(BoxLayout):\n\n                def __init__(self, **kwargs):\n                    super(DemoBox, self).__init__(**kwargs)\n                    self.orientation = "vertical"\n\n                    btn = Button(text="Normal binding to event")\n                    btn.fbind(\'on_press\', self.on_event)\n\n                    btn2 = Button(text="Normal binding to a property change")\n                    btn2.fbind(\'state\', self.on_property)\n\n                    btn3 = Button(text="A: Using function with args.")\n                    btn3.fbind(\'on_press\', self.on_event_with_args, \'right\',\n                                   tree=\'birch\', food=\'apple\')\n\n                    btn4 = Button(text="Unbind A.")\n                    btn4.fbind(\'on_press\', self.unbind_a, btn3)\n\n                    btn5 = Button(text="Use a flexible function")\n                    btn5.fbind(\'on_press\', self.on_anything)\n\n                    btn6 = Button(text="B: Using flexible functions with args. For hardcores.")\n                    btn6.fbind(\'on_press\', self.on_anything, "1", "2", monthy="python")\n\n                    btn7 = Button(text="Force dispatch B with different params")\n                    btn7.fbind(\'on_press\', btn6.dispatch, \'on_press\', 6, 7, monthy="other python")\n\n                    for but in [btn, btn2, btn3, btn4, btn5, btn6, btn7]:\n                        self.add_widget(but)\n\n                def on_event(self, obj):\n                    print("Typical event from", obj)\n\n                def on_event_with_args(self, side, obj, tree=None, food=None):\n                    print("Event with args", obj, side, tree, food)\n\n                def on_property(self, obj, value):\n                    print("Typical property change from", obj, "to", value)\n\n                def on_anything(self, *args, **kwargs):\n                    print(\'The flexible function has *args of\', str(args),\n                        "and **kwargs of", str(kwargs))\n                    return True\n\n                def unbind_a(self, btn, event):\n                    btn.funbind(\'on_press\', self.on_event_with_args, \'right\',\n                                    tree=\'birch\', food=\'apple\')\n\n        .. note::\n\n            Since the kv lang uses this method to bind, one has to implement\n            this method, instead of :meth:`bind` when creating a non\n            :class:`EventDispatcher` based class used with the kv lang. See\n            :class:`Observable` for an example.\n\n        .. versionadded:: 1.9.0\n\n        .. versionchanged:: 1.9.1\n            The `ref` keyword argument has been added.\n        '
        pass
    
    def funbind(self):
        'Similar to :meth:`fbind`.\n\n        When unbinding, :meth:`unbind` will unbind all callbacks that match the\n        callback, while this method will only unbind the first.\n\n        To unbind, the same positional and keyword arguments passed to\n        :meth:`fbind` must be passed on to funbind.\n\n        .. note::\n\n            It is safe to use :meth:`funbind` to unbind a function bound with\n            :meth:`bind` as long as no keyword and positional arguments are\n            provided to :meth:`funbind`.\n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def get_property_observers(self):
        " Returns a list of methods that are bound to the property/event\n        passed as the *name* argument::\n\n            widget_instance.get_property_observers('on_release')\n\n        :Parameters:\n\n            `name`: str\n                The name of the event or property.\n            `args`: bool\n                Whether to return the bound args. To keep compatibility,\n                only the callback functions and not their provided args will\n                be returned in the list when `args` is False.\n\n                If True, each element in the list is a 5-tuple of\n                `(callback, largs, kwargs, is_ref, uid)`, where `is_ref` indicates\n                whether `callback` is a weakref, and `uid` is the uid given by\n                :meth:`fbind`, or None if :meth:`bind` was used. Defaults to `False`.\n\n        :Returns:\n            The list of bound callbacks. See `args` for details.\n\n        .. versionadded:: 1.8.0\n\n        .. versionchanged:: 1.9.0\n            `args` has been added.\n        "
        pass
    
    def getter(self):
        'Return the getter of a property.\n\n        .. versionadded:: 1.0.9\n        '
        pass
    
    def is_event_type(self):
        'Return True if the event_type is already registered.\n\n        .. versionadded:: 1.0.4\n        '
        pass
    
    def properties(self):
        'Return all the properties in the class in a dictionary of\n        key/property class. Can be used for introspection.\n\n        .. versionadded:: 1.0.9\n        '
        pass
    
    def property(self):
        'Get a property instance from the property name. If quiet is True,\n        None is returned instead of raising an exception when `name` is not a\n        property. Defaults to `False`.\n\n        .. versionadded:: 1.0.9\n\n        :return:\n\n            A :class:`~kivy.properties.Property` derived instance\n            corresponding to the name.\n\n        .. versionchanged:: 1.9.0\n            quiet was added.\n        '
        pass
    
    @property
    def proxy_ref(self):
        'Default implementation of proxy_ref, returns self.\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def register_event_type(self):
        "Register an event type with the dispatcher.\n\n        Registering event types allows the dispatcher to validate event handler\n        names as they are attached and to search attached objects for suitable\n        handlers. Each event type declaration must:\n\n            1. start with the prefix `on_`.\n            2. have a default handler in the class.\n\n        Example of creating a custom event::\n\n            class MyWidget(Widget):\n                def __init__(self, **kwargs):\n                    super(MyWidget, self).__init__(**kwargs)\n                    self.register_event_type('on_swipe')\n\n                def on_swipe(self):\n                    pass\n\n            def on_swipe_callback(*largs):\n                print('my swipe is called', largs)\n            w = MyWidget()\n            w.dispatch('on_swipe')\n        "
        pass
    
    def setter(self):
        "Return the setter of a property. Use: instance.setter('name').\n        The setter is a convenient callback function useful if you want\n        to directly bind one property to another.\n        It returns a partial function that will accept\n        (obj, value) args and results in the property 'name' of instance\n        being set to value.\n\n        .. versionadded:: 1.0.9\n\n        For example, to bind number2 to number1 in python you would do::\n\n            class ExampleWidget(Widget):\n                number1 = NumericProperty(None)\n                number2 = NumericProperty(None)\n\n                def __init__(self, **kwargs):\n                    super(ExampleWidget, self).__init__(**kwargs)\n                    self.bind(number1=self.setter('number2'))\n\n        This is equivalent to kv binding::\n\n            <ExampleWidget>:\n                number2: self.number1\n\n        "
        pass
    
    def unbind(self):
        'Unbind properties from callback functions with similar usage as\n        :meth:`bind`.\n\n        If a callback has been bound to a given event or property multiple\n        times, only the first occurrence will be unbound.\n\n        .. note::\n\n            It is safe to use :meth:`unbind` on a function bound with :meth:`fbind`\n            as long as that function was originally bound without any keyword and\n            positional arguments. Otherwise, the function will fail to be unbound\n            and you should use :meth:`funbind` instead.\n        '
        pass
    
    def unbind_uid(self):
        'Uses the uid returned by :meth:`fbind` to unbind the callback.\n\n        This method is much more efficient than :meth:`funbind`. If `uid`\n        evaluates to False (e.g. 0) a `ValueError` is raised. Also, only\n        callbacks bound with :meth:`fbind` can be unbound with this method.\n\n        Since each call to :meth:`fbind` will generate a unique `uid`,\n        only one callback will be removed. If `uid` is not found among the\n        callbacks, no error is raised.\n\n        E.g.::\n\n            btn6 = Button(text="B: Using flexible functions with args. For hardcores.")\n            uid = btn6.fbind(\'on_press\', self.on_anything, "1", "2", monthy="python")\n            if not uid:\n                raise Exception(\'Binding failed\').\n            ...\n            btn6.unbind_uid(\'on_press\', uid)\n\n        .. versionadded:: 1.9.0\n        '
        pass
    
    def unregister_event_types(self):
        'Unregister an event type in the dispatcher.\n        '
        pass
    

class EventObservers(_mod_builtins.object):
    'A class that stores observers as a doubly linked list. See dispatch\n    for more details on locking and deletion of observers.\n\n    In all instances, largs and kwargs if None or empty are all converted\n    to None internally before storing or comparing.\n    '
    __class__ = EventObservers
    def __init__(self, *args, **kwargs):
        'A class that stores observers as a doubly linked list. See dispatch\n    for more details on locking and deletion of observers.\n\n    In all instances, largs and kwargs if None or empty are all converted\n    to None internally before storing or comparing.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Binding/unbinding/dispatching while iterating can lead to invalid\n        data.\n        '
        return EventObservers()
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ObjectWithUid(_mod_builtins.object):
    '\n    (internal) This class assists in providing unique identifiers for class\n    instances. It is not intended for direct usage.\n    '
    __class__ = ObjectWithUid
    def __init__(self, *args, **kwargs):
        '\n    (internal) This class assists in providing unique identifiers for class\n    instances. It is not intended for direct usage.\n    '
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
    def uid(self):
        pass
    

class Observable(ObjectWithUid):
    ':class:`Observable` is a stub class defining the methods required\n    for binding. :class:`EventDispatcher` is (the) one example of a class that\n    implements the binding interface. See :class:`EventDispatcher` for details.\n\n    .. versionadded:: 1.9.0\n    '
    __class__ = Observable
    def __init__(self, *args, **kwargs):
        ':class:`Observable` is a stub class defining the methods required\n    for binding. :class:`EventDispatcher` is (the) one example of a class that\n    implements the binding interface. See :class:`EventDispatcher` for details.\n\n    .. versionadded:: 1.9.0\n    '
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
    
    def bind(self):
        pass
    
    def fbind(self):
        'See :meth:`EventDispatcher.fbind`.\n\n        .. note::\n\n            To keep backward compatibility with derived classes which may have\n            inherited from :class:`Observable` before, the\n            :meth:`fbind` method was added. The default implementation\n            of :meth:`fbind` is to create a partial\n            function that it passes to bind while saving the uid and largs/kwargs.\n            However, :meth:`funbind` (and :meth:`unbind_uid`) are fairly\n            inefficient since we have to first lookup this partial function\n            using the largs/kwargs or uid and then call :meth:`unbind` on\n            the returned function. It is recommended to overwrite\n            these methods in derived classes to bind directly for\n            better performance.\n\n            Similarly to :meth:`EventDispatcher.fbind`, this method returns\n            0 on failure and a positive unique uid on success. This uid can be\n            used with :meth:`unbind_uid`.\n\n        '
        pass
    
    def funbind(self):
        'See :meth:`fbind` and :meth:`EventDispatcher.funbind`.\n        '
        pass
    
    @property
    def proxy_ref(self):
        pass
    
    def unbind(self):
        pass
    
    def unbind_uid(self):
        'See :meth:`fbind` and :meth:`EventDispatcher.unbind_uid`.\n        '
        pass
    

WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nEvent dispatcher\n================\n\nAll objects that produce events in Kivy implement the :class:`EventDispatcher`\nwhich provides a consistent interface for registering and manipulating event\nhandlers.\n\n.. versionchanged:: 1.0.9\n    Property discovery and methods have been moved from the\n    :class:`~kivy.uix.widget.Widget` to the :class:`EventDispatcher`.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/_event.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy._event'
__package__ = 'kivy'
__test__ = _mod_builtins.dict()
def _get_bases():
    pass

defaultdict = _mod_collections.defaultdict
partial = _mod_functools.partial
string_types = _mod_builtins.str
