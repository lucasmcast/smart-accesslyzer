import builtins as _mod_builtins
import functools as _mod_functools
import kivy.config as _mod_kivy_config
import kivy.context as _mod_kivy_context
import kivy.weakmethod as _mod_kivy_weakmethod
import logging as _mod_logging

weakref = _mod_builtins.type
class AliasProperty(Property):
    "Create a property with a custom getter and setter.\n\n    If you don't find a Property class that fits to your needs, you can make\n    your own by creating custom Python getter and setter methods.\n\n    Example from kivy/uix/widget.py::\n\n        def get_right(self):\n            return self.x + self.width\n        def set_right(self, value):\n            self.x = value - self.width\n        right = AliasProperty(get_right, set_right, bind=['x', 'width'])\n\n    :Parameters:\n        `getter`: function\n            Function to use as a property getter\n        `setter`: function\n            Function to use as a property setter. Properties listening to the\n            alias property won't be updated when the property is set (e.g.\n            `right = 10`), unless the `setter` returns `True`.\n        `bind`: list/tuple\n            Properties to observe for changes, as property name strings\n        `cache`: boolean\n            If True, the value will be cached, until one of the binded elements\n            will changes\n        `rebind`: bool, defaults to False\n            See :class:`ObjectProperty` for details.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. versionchanged:: 1.4.0\n        Parameter `cache` added.\n    "
    __class__ = AliasProperty
    def __init__(self, *args, **kwargs):
        "Create a property with a custom getter and setter.\n\n    If you don't find a Property class that fits to your needs, you can make\n    your own by creating custom Python getter and setter methods.\n\n    Example from kivy/uix/widget.py::\n\n        def get_right(self):\n            return self.x + self.width\n        def set_right(self, value):\n            self.x = value - self.width\n        right = AliasProperty(get_right, set_right, bind=['x', 'width'])\n\n    :Parameters:\n        `getter`: function\n            Function to use as a property getter\n        `setter`: function\n            Function to use as a property setter. Properties listening to the\n            alias property won't be updated when the property is set (e.g.\n            `right = 10`), unless the `setter` returns `True`.\n        `bind`: list/tuple\n            Properties to observe for changes, as property name strings\n        `cache`: boolean\n            If True, the value will be cached, until one of the binded elements\n            will changes\n        `rebind`: bool, defaults to False\n            See :class:`ObjectProperty` for details.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. versionchanged:: 1.4.0\n        Parameter `cache` added.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __read_only(self):
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get(self):
        pass
    
    def link_deps(self):
        pass
    
    @property
    def rebind(self):
        pass
    
    def set(self):
        pass
    
    def trigger_change(self):
        pass
    

class BooleanProperty(Property):
    'Property that represents only a boolean value.\n\n    :Parameters:\n        `defaultvalue`: boolean\n            Specifies the default value of the property.\n    '
    __class__ = BooleanProperty
    def __init__(self, *args, **kwargs):
        'Property that represents only a boolean value.\n\n    :Parameters:\n        `defaultvalue`: boolean\n            Specifies the default value of the property.\n    '
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
    

class BoundedNumericProperty(Property):
    'Property that represents a numeric value within a minimum bound and/or\n    maximum bound -- within a numeric range.\n\n    :Parameters:\n        `default`: numeric\n            Specifies the default value of the property.\n        `\\*\\*kwargs`: a list of keyword arguments\n            If a `min` parameter is included, this specifies the minimum\n            numeric value that will be accepted.\n            If a `max` parameter is included, this specifies the maximum\n            numeric value that will be accepted.\n    '
    __class__ = BoundedNumericProperty
    def __init__(self, *args, **kwargs):
        'Property that represents a numeric value within a minimum bound and/or\n    maximum bound -- within a numeric range.\n\n    :Parameters:\n        `default`: numeric\n            Specifies the default value of the property.\n        `\\*\\*kwargs`: a list of keyword arguments\n            If a `min` parameter is included, this specifies the minimum\n            numeric value that will be accepted.\n            If a `max` parameter is included, this specifies the maximum\n            numeric value that will be accepted.\n    '
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
    def bounds(self):
        'Return min/max of the value.\n\n        .. versionadded:: 1.0.9\n        '
        pass
    
    def get_max(self):
        'Return the maximum value acceptable for the BoundedNumericProperty\n        in `obj`. Return None if no maximum value is set. Check\n        :attr:`get_min` for a usage example.\n\n        .. versionadded:: 1.1.0\n        '
        pass
    
    def get_min(self):
        "Return the minimum value acceptable for the BoundedNumericProperty\n        in `obj`. Return None if no minimum value is set::\n\n            class MyWidget(Widget):\n                number = BoundedNumericProperty(0, min=-5, max=5)\n\n            widget = MyWidget()\n            print(widget.property('number').get_min(widget))\n            # will output -5\n\n        .. versionadded:: 1.1.0\n        "
        pass
    
    def set_max(self):
        "Change the maximum value acceptable for the BoundedNumericProperty,\n        only for the `obj` instance. Set to None if you want to disable it.\n        Check :attr:`set_min` for a usage example.\n\n        .. warning::\n\n            Changing the bounds doesn't revalidate the current value.\n\n        .. versionadded:: 1.1.0\n        "
        pass
    
    def set_min(self):
        "Change the minimum value acceptable for the BoundedNumericProperty,\n        only for the `obj` instance. Set to None if you want to disable it::\n\n            class MyWidget(Widget):\n                number = BoundedNumericProperty(0, min=-5, max=5)\n\n            widget = MyWidget()\n            # change the minimum to -10\n            widget.property('number').set_min(widget, -10)\n            # or disable the minimum check\n            widget.property('number').set_min(widget, None)\n\n        .. warning::\n\n            Changing the bounds doesn't revalidate the current value.\n\n        .. versionadded:: 1.1.0\n        "
        pass
    

Clock = _mod_kivy_context.ProxyContext()
class ColorProperty(Property):
    'Property that represents a color. The assignment can take either:\n\n    - a list of 3 to 4 float value between 0-1 (kivy default)\n    - a string in the format #rrggbb or #rrggbbaa\n\n    :Parameters:\n        `defaultvalue`: list or string, defaults to [1, 1, 1, 1]\n            Specifies the default value of the property.\n\n    .. versionadded:: 1.10.0\n    '
    __class__ = ColorProperty
    def __init__(self, *args, **kwargs):
        'Property that represents a color. The assignment can take either:\n\n    - a list of 3 to 4 float value between 0-1 (kivy default)\n    - a string in the format #rrggbb or #rrggbbaa\n\n    :Parameters:\n        `defaultvalue`: list or string, defaults to [1, 1, 1, 1]\n            Specifies the default value of the property.\n\n    .. versionadded:: 1.10.0\n    '
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
    

ConfigParser = _mod_kivy_config.ConfigParser
class ConfigParserProperty(Property):
    " Property that allows one to bind to changes in the configuration values\n    of a :class:`~kivy.config.ConfigParser` as well as to bind the ConfigParser\n    values to other properties.\n\n    A ConfigParser is composed of sections, where each section has a number of\n    keys and values associated with these keys. ConfigParserProperty lets\n    you automatically listen to and change the values of specified keys based\n    on other kivy properties.\n\n    For example, say we want to have a TextInput automatically write\n    its value, represented as an int, in the `info` section of a ConfigParser.\n    Also, the textinputs should update its values from the ConfigParser's\n    fields. Finally, their values should be displayed in a label. In py::\n\n        class Info(Label):\n\n            number = ConfigParserProperty(0, 'info', 'number', 'example',\n                                          val_type=int, errorvalue=41)\n\n            def __init__(self, **kw):\n                super(Info, self).__init__(**kw)\n                config = ConfigParser(name='example')\n\n    The above code creates a property that is connected to the `number` key in\n    the `info` section of the ConfigParser named `example`. Initially, this\n    ConfigParser doesn't exist. Then, in `__init__`, a ConfigParser is created\n    with name `example`, which is then automatically linked with this property.\n    then in kv:\n\n    .. code-block:: kv\n\n        BoxLayout:\n            TextInput:\n                id: number\n                text: str(info.number)\n            Info:\n                id: info\n                number: number.text\n                text: 'Number: {}'.format(self.number)\n\n    You'll notice that we have to do `text: str(info.number)`, this is because\n    the value of this property is always an int, because we specified `int` as\n    the `val_type`. However, we can assign anything to the property, e.g.\n    `number: number.text` which assigns a string, because it is instantly\n    converted with the `val_type` callback.\n\n    .. note::\n\n        If a file has been opened for this ConfigParser using\n        :meth:`~kivy.config.ConfigParser.read`, then\n        :meth:`~kivy.config.ConfigParser.write` will be called every property\n        change, keeping the file updated.\n\n    .. warning::\n\n        It is recommend that the config parser object be assigned to the\n        property after the kv tree has been constructed (e.g. schedule on next\n        frame from init). This is because the kv tree and its properties, when\n        constructed, are evaluated on its own order, therefore, any initial\n        values in the parser might be overwritten by objects it's bound to.\n        So in the example above, the TextInput might be initially empty,\n        and if `number: number.text` is evaluated before\n        `text: str(info.number)`, the config value will be overwritten with the\n        (empty) text value.\n\n    :Parameters:\n        `default`: object type\n            Specifies the default value for the key. If the parser associated\n            with this property doesn't have this section or key, it'll be\n            created with the current value, which is the default value\n            initially.\n        `section`: string type\n            The section in the ConfigParser where the key / value will be\n            written. Must be provided. If the section doesn't exist, it'll be\n            created.\n        `key`: string type\n            The key in section `section` where the value will be written to.\n            Must be provided. If the key doesn't exist, it'll be created and\n            the current value written to it, otherwise its value will be used.\n        `config`: string or :class:`~kivy.config.ConfigParser` instance.\n            The ConfigParser instance to associate with this property if\n            not None. If it's a string, the ConfigParser instance whose\n            :attr:`~kivy.config.ConfigParser.name` is the value of `config`\n            will be used. If no such parser exists yet, whenever a ConfigParser\n            with this name is created, it will automatically be linked to this\n            property.\n\n            Whenever a ConfigParser becomes linked with a property, if the\n            section or key doesn't exist, the current property value will be\n            used to create that key, otherwise, the existing key value will be\n            used for the property value; overwriting its current value. You can\n            change the ConfigParser associated with this property if a string\n            was used here, by changing the\n            :attr:`~kivy.config.ConfigParser.name` of an existing or new\n            ConfigParser instance. Or through :meth:`set_config`.\n        `\\*\\*kwargs`: a list of keyword arguments\n            `val_type`: a callable object\n                The key values are saved in the ConfigParser as strings. When\n                the ConfigParser value is read internally and assigned to the\n                property or when the user changes the property value directly,\n                if `val_type` is not None, it will be called with the new value\n                as input and it should return the value converted to the proper\n                type accepted ny this property. For example, if the property\n                represent ints, `val_type` can simply be `int`.\n\n                If the `val_type` callback raises a `ValueError`, `errorvalue`\n                or `errorhandler` will be used if provided. Tip: the\n                `getboolean` function of the ConfigParser might also be useful\n                here to convert to a boolean type.\n            `verify`: a callable object\n                Can be used to restrict the allowable values of the property.\n                For every value assigned to the property, if this is specified,\n                `verify` is called with the new value, and if it returns `True`\n                the value is accepted, otherwise, `errorvalue` or\n                `errorhandler` will be used if provided or a `ValueError` is\n                raised.\n\n    .. versionadded:: 1.9.0\n    "
    __class__ = ConfigParserProperty
    def __init__(self, *args, **kwargs):
        " Property that allows one to bind to changes in the configuration values\n    of a :class:`~kivy.config.ConfigParser` as well as to bind the ConfigParser\n    values to other properties.\n\n    A ConfigParser is composed of sections, where each section has a number of\n    keys and values associated with these keys. ConfigParserProperty lets\n    you automatically listen to and change the values of specified keys based\n    on other kivy properties.\n\n    For example, say we want to have a TextInput automatically write\n    its value, represented as an int, in the `info` section of a ConfigParser.\n    Also, the textinputs should update its values from the ConfigParser's\n    fields. Finally, their values should be displayed in a label. In py::\n\n        class Info(Label):\n\n            number = ConfigParserProperty(0, 'info', 'number', 'example',\n                                          val_type=int, errorvalue=41)\n\n            def __init__(self, **kw):\n                super(Info, self).__init__(**kw)\n                config = ConfigParser(name='example')\n\n    The above code creates a property that is connected to the `number` key in\n    the `info` section of the ConfigParser named `example`. Initially, this\n    ConfigParser doesn't exist. Then, in `__init__`, a ConfigParser is created\n    with name `example`, which is then automatically linked with this property.\n    then in kv:\n\n    .. code-block:: kv\n\n        BoxLayout:\n            TextInput:\n                id: number\n                text: str(info.number)\n            Info:\n                id: info\n                number: number.text\n                text: 'Number: {}'.format(self.number)\n\n    You'll notice that we have to do `text: str(info.number)`, this is because\n    the value of this property is always an int, because we specified `int` as\n    the `val_type`. However, we can assign anything to the property, e.g.\n    `number: number.text` which assigns a string, because it is instantly\n    converted with the `val_type` callback.\n\n    .. note::\n\n        If a file has been opened for this ConfigParser using\n        :meth:`~kivy.config.ConfigParser.read`, then\n        :meth:`~kivy.config.ConfigParser.write` will be called every property\n        change, keeping the file updated.\n\n    .. warning::\n\n        It is recommend that the config parser object be assigned to the\n        property after the kv tree has been constructed (e.g. schedule on next\n        frame from init). This is because the kv tree and its properties, when\n        constructed, are evaluated on its own order, therefore, any initial\n        values in the parser might be overwritten by objects it's bound to.\n        So in the example above, the TextInput might be initially empty,\n        and if `number: number.text` is evaluated before\n        `text: str(info.number)`, the config value will be overwritten with the\n        (empty) text value.\n\n    :Parameters:\n        `default`: object type\n            Specifies the default value for the key. If the parser associated\n            with this property doesn't have this section or key, it'll be\n            created with the current value, which is the default value\n            initially.\n        `section`: string type\n            The section in the ConfigParser where the key / value will be\n            written. Must be provided. If the section doesn't exist, it'll be\n            created.\n        `key`: string type\n            The key in section `section` where the value will be written to.\n            Must be provided. If the key doesn't exist, it'll be created and\n            the current value written to it, otherwise its value will be used.\n        `config`: string or :class:`~kivy.config.ConfigParser` instance.\n            The ConfigParser instance to associate with this property if\n            not None. If it's a string, the ConfigParser instance whose\n            :attr:`~kivy.config.ConfigParser.name` is the value of `config`\n            will be used. If no such parser exists yet, whenever a ConfigParser\n            with this name is created, it will automatically be linked to this\n            property.\n\n            Whenever a ConfigParser becomes linked with a property, if the\n            section or key doesn't exist, the current property value will be\n            used to create that key, otherwise, the existing key value will be\n            used for the property value; overwriting its current value. You can\n            change the ConfigParser associated with this property if a string\n            was used here, by changing the\n            :attr:`~kivy.config.ConfigParser.name` of an existing or new\n            ConfigParser instance. Or through :meth:`set_config`.\n        `\\*\\*kwargs`: a list of keyword arguments\n            `val_type`: a callable object\n                The key values are saved in the ConfigParser as strings. When\n                the ConfigParser value is read internally and assigned to the\n                property or when the user changes the property value directly,\n                if `val_type` is not None, it will be called with the new value\n                as input and it should return the value converted to the proper\n                type accepted ny this property. For example, if the property\n                represent ints, `val_type` can simply be `int`.\n\n                If the `val_type` callback raises a `ValueError`, `errorvalue`\n                or `errorhandler` will be used if provided. Tip: the\n                `getboolean` function of the ConfigParser might also be useful\n                here to convert to a boolean type.\n            `verify`: a callable object\n                Can be used to restrict the allowable values of the property.\n                For every value assigned to the property, if this is specified,\n                `verify` is called with the new value, and if it returns `True`\n                the value is accepted, otherwise, `errorvalue` or\n                `errorhandler` will be used if provided or a `ValueError` is\n                raised.\n\n    .. versionadded:: 1.9.0\n    "
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
    
    def _edit_setting(self):
        pass
    
    def link_deps(self):
        pass
    
    def set(self):
        pass
    
    def set_config(self):
        " Sets the ConfigParser object to be used by this property. Normally,\n        the ConfigParser is set when initializing the Property using the\n        `config` parameter.\n\n        :Parameters:\n            `config`: A :class:`~kivy.config.ConfigParser` instance.\n                The instance to use for listening to and saving property value\n                changes. If None, it disconnects the currently used\n                `ConfigParser`.\n\n        ::\n\n            class MyWidget(Widget):\n                username = ConfigParserProperty('', 'info', 'name', None)\n\n            widget = MyWidget()\n            widget.property('username').set_config(ConfigParser())\n        "
        pass
    

class DictProperty(Property):
    'Property that represents a dict.\n\n    :Parameters:\n        `defaultvalue`: dict, defaults to None\n            Specifies the default value of the property.\n        `rebind`: bool, defaults to False\n            See :class:`ObjectProperty` for details.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. warning::\n\n        Similar to :class:`ListProperty`, when assigning a dict to a\n        :class:`DictProperty`, the dict stored in the property is a shallow copy of the\n        dict and not the original dict. See :class:`ListProperty` for details.\n    '
    __class__ = DictProperty
    def __init__(self, *args, **kwargs):
        'Property that represents a dict.\n\n    :Parameters:\n        `defaultvalue`: dict, defaults to None\n            Specifies the default value of the property.\n        `rebind`: bool, defaults to False\n            See :class:`ObjectProperty` for details.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. warning::\n\n        Similar to :class:`ListProperty`, when assigning a dict to a\n        :class:`DictProperty`, the dict stored in the property is a shallow copy of the\n        dict and not the original dict. See :class:`ListProperty` for details.\n    '
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
    
    def link(self):
        pass
    
    @property
    def rebind(self):
        pass
    
    def set(self):
        pass
    

class ListProperty(Property):
    "Property that represents a list.\n\n    :Parameters:\n        `defaultvalue`: list, defaults to []\n            Specifies the default value of the property.\n\n    .. warning::\n\n        When assigning a list to a :class:`ListProperty`, the list stored in\n        the property is a shallow copy of the list and not the original list. This can\n        be demonstrated with the following example::\n\n            >>> class MyWidget(Widget):\n            >>>     my_list = ListProperty([])\n\n            >>> widget = MyWidget()\n            >>> my_list = [1, 5, {'hi': 'hello'}]\n            >>> widget.my_list = my_list\n            >>> print(my_list is widget.my_list)\n            False\n            >>> my_list.append(10)\n            >>> print(my_list, widget.my_list)\n            [1, 5, {'hi': 'hello'}, 10] [1, 5, {'hi': 'hello'}]\n\n        However, changes to nested levels will affect the property as well,\n        since the property uses a shallow copy of my_list.\n\n            >>> my_list[2]['hi'] = 'bye'\n            >>> print(my_list, widget.my_list)\n            [1, 5, {'hi': 'bye'}, 10] [1, 5, {'hi': 'bye'}]\n\n    "
    __class__ = ListProperty
    def __init__(self, *args, **kwargs):
        "Property that represents a list.\n\n    :Parameters:\n        `defaultvalue`: list, defaults to []\n            Specifies the default value of the property.\n\n    .. warning::\n\n        When assigning a list to a :class:`ListProperty`, the list stored in\n        the property is a shallow copy of the list and not the original list. This can\n        be demonstrated with the following example::\n\n            >>> class MyWidget(Widget):\n            >>>     my_list = ListProperty([])\n\n            >>> widget = MyWidget()\n            >>> my_list = [1, 5, {'hi': 'hello'}]\n            >>> widget.my_list = my_list\n            >>> print(my_list is widget.my_list)\n            False\n            >>> my_list.append(10)\n            >>> print(my_list, widget.my_list)\n            [1, 5, {'hi': 'hello'}, 10] [1, 5, {'hi': 'hello'}]\n\n        However, changes to nested levels will affect the property as well,\n        since the property uses a shallow copy of my_list.\n\n            >>> my_list[2]['hi'] = 'bye'\n            >>> print(my_list, widget.my_list)\n            [1, 5, {'hi': 'bye'}, 10] [1, 5, {'hi': 'bye'}]\n\n    "
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
    
    def link(self):
        pass
    
    def set(self):
        pass
    

Logger = _mod_logging.Logger()
NUMERIC_FORMATS = _mod_builtins.tuple()
class NumericProperty(Property):
    'Property that represents a numeric value.\n\n    :Parameters:\n        `defaultvalue`: int or float, defaults to 0\n            Specifies the default value of the property.\n\n    >>> wid = Widget()\n    >>> wid.x = 42\n    >>> print(wid.x)\n    42\n    >>> wid.x = "plop"\n     Traceback (most recent call last):\n       File "<stdin>", line 1, in <module>\n       File "properties.pyx", line 93, in kivy.properties.Property.__set__\n       File "properties.pyx", line 111, in kivy.properties.Property.set\n       File "properties.pyx", line 159, in kivy.properties.NumericProperty.check\n     ValueError: NumericProperty accept only int/float\n\n    .. versionchanged:: 1.4.1\n        NumericProperty can now accept custom text and tuple value to indicate a\n        type, like "in", "pt", "px", "cm", "mm", in the format: \'10pt\' or (10,\n        \'pt\').\n\n    '
    __class__ = NumericProperty
    def __init__(self, *args, **kwargs):
        'Property that represents a numeric value.\n\n    :Parameters:\n        `defaultvalue`: int or float, defaults to 0\n            Specifies the default value of the property.\n\n    >>> wid = Widget()\n    >>> wid.x = 42\n    >>> print(wid.x)\n    42\n    >>> wid.x = "plop"\n     Traceback (most recent call last):\n       File "<stdin>", line 1, in <module>\n       File "properties.pyx", line 93, in kivy.properties.Property.__set__\n       File "properties.pyx", line 111, in kivy.properties.Property.set\n       File "properties.pyx", line 159, in kivy.properties.NumericProperty.check\n     ValueError: NumericProperty accept only int/float\n\n    .. versionchanged:: 1.4.1\n        NumericProperty can now accept custom text and tuple value to indicate a\n        type, like "in", "pt", "px", "cm", "mm", in the format: \'10pt\' or (10,\n        \'pt\').\n\n    '
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
    
    def get_format(self):
        "\n        Return the format used for Numeric calculation. Default is px (mean\n        the value have not been changed at all). Otherwise, it can be one of\n        'in', 'pt', 'cm', 'mm'.\n        "
        pass
    

class ObjectProperty(Property):
    "Property that represents a Python object.\n\n    :Parameters:\n        `defaultvalue`: object type\n            Specifies the default value of the property.\n        `rebind`: bool, defaults to False\n            Whether kv rules using this object as an intermediate attribute\n            in a kv rule, will update the bound property when this object\n            changes.\n\n            That is the standard behavior is that if there's a kv rule\n            ``text: self.a.b.c.d``, where ``a``, ``b``, and ``c`` are\n            properties with ``rebind`` ``False`` and ``d`` is a\n            :class:`StringProperty`. Then when the rule is applied, ``text``\n            becomes bound only to ``d``. If ``a``, ``b``, or ``c`` change,\n            ``text`` still remains bound to ``d``. Furthermore, if any of them\n            were ``None`` when the rule was initially evaluated, e.g. ``b`` was\n            ``None``; then ``text`` is bound to ``b`` and will not become bound\n            to ``d`` even when ``b`` is changed to not be ``None``.\n\n            By setting ``rebind`` to ``True``, however, the rule will be\n            re-evaluated and all the properties rebound when that intermediate\n            property changes. E.g. in the example above, whenever ``b`` changes\n            or becomes not ``None`` if it was ``None`` before, ``text`` is\n            evaluated again and becomes rebound to ``d``. The overall result is\n            that ``text`` is now bound to all the properties among ``a``,\n            ``b``, or ``c`` that have ``rebind`` set to ``True``.\n        `\\*\\*kwargs`: a list of keyword arguments\n            `baseclass`\n                If kwargs includes a `baseclass` argument, this value will be\n                used for validation: `isinstance(value, kwargs['baseclass'])`.\n\n    .. warning::\n\n        To mark the property as changed, you must reassign a new python object.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. versionchanged:: 1.7.0\n\n        `baseclass` parameter added.\n    "
    __class__ = ObjectProperty
    def __init__(self, *args, **kwargs):
        "Property that represents a Python object.\n\n    :Parameters:\n        `defaultvalue`: object type\n            Specifies the default value of the property.\n        `rebind`: bool, defaults to False\n            Whether kv rules using this object as an intermediate attribute\n            in a kv rule, will update the bound property when this object\n            changes.\n\n            That is the standard behavior is that if there's a kv rule\n            ``text: self.a.b.c.d``, where ``a``, ``b``, and ``c`` are\n            properties with ``rebind`` ``False`` and ``d`` is a\n            :class:`StringProperty`. Then when the rule is applied, ``text``\n            becomes bound only to ``d``. If ``a``, ``b``, or ``c`` change,\n            ``text`` still remains bound to ``d``. Furthermore, if any of them\n            were ``None`` when the rule was initially evaluated, e.g. ``b`` was\n            ``None``; then ``text`` is bound to ``b`` and will not become bound\n            to ``d`` even when ``b`` is changed to not be ``None``.\n\n            By setting ``rebind`` to ``True``, however, the rule will be\n            re-evaluated and all the properties rebound when that intermediate\n            property changes. E.g. in the example above, whenever ``b`` changes\n            or becomes not ``None`` if it was ``None`` before, ``text`` is\n            evaluated again and becomes rebound to ``d``. The overall result is\n            that ``text`` is now bound to all the properties among ``a``,\n            ``b``, or ``c`` that have ``rebind`` set to ``True``.\n        `\\*\\*kwargs`: a list of keyword arguments\n            `baseclass`\n                If kwargs includes a `baseclass` argument, this value will be\n                used for validation: `isinstance(value, kwargs['baseclass'])`.\n\n    .. warning::\n\n        To mark the property as changed, you must reassign a new python object.\n\n    .. versionchanged:: 1.9.0\n        `rebind` has been introduced.\n\n    .. versionchanged:: 1.7.0\n\n        `baseclass` parameter added.\n    "
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
    def rebind(self):
        pass
    

class ObservableDict(_mod_builtins.dict):
    __class__ = ObservableDict
    def __delitem__(self, key):
        return None
    
    __dict__ = {}
    def __getattr__(self, attr):
        pass
    
    def __init__(self, *largs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kivy.properties'
    def __setattr__(self, attr, value):
        return None
    
    def __setitem__(self, key, value):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _weak_return(self, item):
        pass
    
    def clear(self, *largs):
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Returns a new dict with keys from iterable and values equal to value.'
        pass
    
    def pop(self, *largs):
        pass
    
    def popitem(self, *largs):
        pass
    
    def remove(self, *largs):
        pass
    
    def setdefault(self, *largs):
        pass
    
    def update(self, *largs):
        pass
    

class ObservableList(_mod_builtins.list):
    __class__ = ObservableList
    def __delitem__(self, key):
        return None
    
    def __delslice__(self, b, c):
        pass
    
    __dict__ = {}
    def __iadd__(self, *largs):
        return None
    
    def __imul__(self, b):
        return None
    
    def __init__(self, *largs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kivy.properties'
    def __setitem__(self, key, value):
        return None
    
    def __setslice__(self, b, c, v):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def append(self, *largs):
        pass
    
    def extend(self, *largs):
        pass
    
    def insert(self, i, x):
        pass
    
    def pop(self, *largs):
        pass
    
    def remove(self, *largs):
        pass
    
    def reverse(self, *largs):
        pass
    
    def sort(self, *largs):
        pass
    

class ObservableReferenceList(ObservableList):
    __class__ = ObservableReferenceList
    __dict__ = {}
    def __init__(self, *largs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __setitem__(self, key, value, update_properties):
        return None
    
    def __setslice__(self, start, stop, value, update_properties):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class OptionProperty(Property):
    'Property that represents a string from a predefined list of valid\n    options.\n\n    If the string set in the property is not in the list of valid options\n    (passed at property creation time), a ValueError exception will be raised.\n\n    :Parameters:\n        `default`: any valid type in the list of options\n            Specifies the default value of the property.\n        `\\*\\*kwargs`: a list of keyword arguments\n            Should include an `options` parameter specifying a list (not tuple)\n            of valid options.\n\n    For example::\n\n        class MyWidget(Widget):\n            state = OptionProperty("None", options=["On", "Off", "None"])\n\n    '
    __class__ = OptionProperty
    def __init__(self, *args, **kwargs):
        'Property that represents a string from a predefined list of valid\n    options.\n\n    If the string set in the property is not in the list of valid options\n    (passed at property creation time), a ValueError exception will be raised.\n\n    :Parameters:\n        `default`: any valid type in the list of options\n            Specifies the default value of the property.\n        `\\*\\*kwargs`: a list of keyword arguments\n            Should include an `options` parameter specifying a list (not tuple)\n            of valid options.\n\n    For example::\n\n        class MyWidget(Widget):\n            state = OptionProperty("None", options=["On", "Off", "None"])\n\n    '
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
    def options(self):
        'Return the options available.\n\n        .. versionadded:: 1.0.9\n        '
        pass
    

class Property(_mod_builtins.object):
    "Base class for building more complex properties.\n\n    This class handles all the basic setters and getters, None type handling,\n    the observer list and storage initialisation. This class should not be\n    directly instantiated.\n\n    By default, a :class:`Property` always takes a default value::\n\n        class MyObject(Widget):\n\n            hello = Property('Hello world')\n\n    The default value must be a value that agrees with the Property type. For\n    example, you can't set a list to a :class:`StringProperty` because the\n    StringProperty will check the default value.\n\n    None is a special case: you can set the default value of a Property to\n    None, but you can't set None to a property afterward.  If you really want\n    to do that, you must declare the Property with `allownone=True`::\n\n        class MyObject(Widget):\n\n            hello = ObjectProperty(None, allownone=True)\n\n        # then later\n        a = MyObject()\n        a.hello = 'bleh' # working\n        a.hello = None # working too, because allownone is True.\n\n    :Parameters:\n        `default`:\n            Specifies the default value for the property.\n        `\\*\\*kwargs`:\n            If the parameters include `errorhandler`, this should be a callable\n            which must take a single argument and return a valid substitute\n            value.\n\n            If the parameters include `errorvalue`, this should be an object.\n            If set, it will replace an invalid property value (overrides\n            errorhandler).\n\n            If the parameters include `force_dispatch`, it should be a boolean.\n            If True, no value comparison will be done, so the property event\n            will be dispatched even if the new value matches the old value (by\n            default identical values are not dispatched to avoid infinite\n            recursion in two-way binds). Be careful, this is for advanced use only.\n\n            `comparator`: callable or None\n                When not None, it's called with two values to be compared.\n                The function returns whether they are considered the same.\n\n    .. versionchanged:: 1.4.2\n        Parameters errorhandler and errorvalue added\n\n    .. versionchanged:: 1.9.0\n        Parameter force_dispatch added\n    "
    __class__ = Property
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return Property()
    
    def __init__(self, *args, **kwargs):
        "Base class for building more complex properties.\n\n    This class handles all the basic setters and getters, None type handling,\n    the observer list and storage initialisation. This class should not be\n    directly instantiated.\n\n    By default, a :class:`Property` always takes a default value::\n\n        class MyObject(Widget):\n\n            hello = Property('Hello world')\n\n    The default value must be a value that agrees with the Property type. For\n    example, you can't set a list to a :class:`StringProperty` because the\n    StringProperty will check the default value.\n\n    None is a special case: you can set the default value of a Property to\n    None, but you can't set None to a property afterward.  If you really want\n    to do that, you must declare the Property with `allownone=True`::\n\n        class MyObject(Widget):\n\n            hello = ObjectProperty(None, allownone=True)\n\n        # then later\n        a = MyObject()\n        a.hello = 'bleh' # working\n        a.hello = None # working too, because allownone is True.\n\n    :Parameters:\n        `default`:\n            Specifies the default value for the property.\n        `\\*\\*kwargs`:\n            If the parameters include `errorhandler`, this should be a callable\n            which must take a single argument and return a valid substitute\n            value.\n\n            If the parameters include `errorvalue`, this should be an object.\n            If set, it will replace an invalid property value (overrides\n            errorhandler).\n\n            If the parameters include `force_dispatch`, it should be a boolean.\n            If True, no value comparison will be done, so the property event\n            will be dispatched even if the new value matches the old value (by\n            default identical values are not dispatched to avoid infinite\n            recursion in two-way binds). Be careful, this is for advanced use only.\n\n            `comparator`: callable or None\n                When not None, it's called with two values to be compared.\n                The function returns whether they are considered the same.\n\n    .. versionchanged:: 1.4.2\n        Parameters errorhandler and errorvalue added\n\n    .. versionchanged:: 1.9.0\n        Parameter force_dispatch added\n    "
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
    
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
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
    
    def bind(self):
        'Add a new observer to be called only when the value is changed.\n        '
        pass
    
    @property
    def defaultvalue(self):
        pass
    
    def dispatch(self):
        "Dispatch the value change to all observers.\n\n        .. versionchanged:: 1.1.0\n            The method is now accessible from Python.\n\n        This can be used to force the dispatch of the property, even if the\n        value didn't change::\n\n            button = Button()\n            # get the Property class instance\n            prop = button.property('text')\n            # dispatch this property on the button instance\n            prop.dispatch(button)\n\n        "
        pass
    
    def fbind(self):
        "Similar to bind, except it doesn't check if the observer already\n        exists. It also expands and forwards largs and kwargs to the callback.\n        funbind or unbind_uid should be called when unbinding.\n        It returns a unique positive uid to be used with unbind_uid.\n        "
        pass
    
    def funbind(self):
        'Remove the observer from our widget observer list bound with\n        fbind. It removes the first match it finds, as opposed to unbind\n        which searches for all matches.\n        '
        pass
    
    def get(self):
        'Return the value of the property.\n        '
        pass
    
    def link(self):
        "Link the instance with its real name.\n\n        .. warning::\n\n            Internal usage only.\n\n        When a widget is defined and uses a :class:`Property` class, the\n        creation of the property object happens, but the instance doesn't know\n        anything about its name in the widget class::\n\n            class MyWidget(Widget):\n                uid = NumericProperty(0)\n\n        In this example, the uid will be a NumericProperty() instance, but the\n        property instance doesn't know its name. That's why :meth:`link` is\n        used in `Widget.__new__`. The link function is also used to create the\n        storage space of the property for this specific widget instance.\n        "
        pass
    
    def link_deps(self):
        pass
    
    @property
    def name(self):
        pass
    
    def set(self):
        'Set a new value for the property.\n        '
        pass
    
    def unbind(self):
        'Remove the observer from our widget observer list.\n        '
        pass
    
    def unbind_uid(self):
        'Remove the observer from our widget observer list bound with\n        fbind using the uid.\n        '
        pass
    

class PropertyStorage(_mod_builtins.object):
    __class__ = PropertyStorage
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ReferenceListProperty(Property):
    'Property that allows the creation of a tuple of other properties.\n\n    For example, if `x` and `y` are :class:`NumericProperty`\\s, we can create a\n    :class:`ReferenceListProperty` for the `pos`. If you change the value of\n    `pos`, it will automatically change the values of `x` and `y` accordingly.\n    If you read the value of `pos`, it will return a tuple with the values of\n    `x` and `y`.\n\n    For example::\n\n        class MyWidget(EventDispatcher):\n            x = NumericProperty(0)\n            y = NumericProperty(0)\n            pos = ReferenceListProperty(x, y)\n\n    '
    __class__ = ReferenceListProperty
    def __init__(self, *args, **kwargs):
        'Property that allows the creation of a tuple of other properties.\n\n    For example, if `x` and `y` are :class:`NumericProperty`\\s, we can create a\n    :class:`ReferenceListProperty` for the `pos`. If you change the value of\n    `pos`, it will automatically change the values of `x` and `y` accordingly.\n    If you read the value of `pos`, it will return a tuple with the values of\n    `x` and `y`.\n\n    For example::\n\n        class MyWidget(EventDispatcher):\n            x = NumericProperty(0)\n            y = NumericProperty(0)\n            pos = ReferenceListProperty(x, y)\n\n    '
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
    
    def get(self):
        pass
    
    def link(self):
        pass
    
    def link_deps(self):
        pass
    
    def set(self):
        pass
    
    def setitem(self):
        pass
    
    def trigger_change(self):
        pass
    

class StringProperty(Property):
    "Property that represents a string value.\n\n    :Parameters:\n        `defaultvalue`: string, defaults to ''\n            Specifies the default value of the property.\n\n    "
    __class__ = StringProperty
    def __init__(self, *args, **kwargs):
        "Property that represents a string value.\n\n    :Parameters:\n        `defaultvalue`: string, defaults to ''\n            Specifies the default value of the property.\n\n    "
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
    

class VariableListProperty(Property):
    "A ListProperty that allows you to work with a variable amount of\n    list items and to expand them to the desired list size.\n\n    For example, GridLayout's padding used to just accept one numeric value\n    which was applied equally to the left, top, right and bottom of the\n    GridLayout. Now padding can be given one, two or four values, which are\n    expanded into a length four list [left, top, right, bottom] and stored\n    in the property.\n\n    :Parameters:\n        `default`: a default list of values\n            Specifies the default values for the list.\n        `length`: int, one of 2 or 4.\n            Specifies the length of the final list. The `default` list will\n            be expanded to match a list of this length.\n        `\\*\\*kwargs`: a list of keyword arguments\n            Not currently used.\n\n    Keeping in mind that the `default` list is expanded to a list of length 4,\n    here are some examples of how VariabelListProperty's are handled.\n\n    - VariableListProperty([1]) represents [1, 1, 1, 1].\n    - VariableListProperty([1, 2]) represents [1, 2, 1, 2].\n    - VariableListProperty(['1px', (2, 'px'), 3, 4.0]) represents [1, 2, 3, 4.0].\n    - VariableListProperty(5) represents [5, 5, 5, 5].\n    - VariableListProperty(3, length=2) represents [3, 3].\n\n    .. versionadded:: 1.7.0\n    "
    __class__ = VariableListProperty
    def __init__(self, *args, **kwargs):
        "A ListProperty that allows you to work with a variable amount of\n    list items and to expand them to the desired list size.\n\n    For example, GridLayout's padding used to just accept one numeric value\n    which was applied equally to the left, top, right and bottom of the\n    GridLayout. Now padding can be given one, two or four values, which are\n    expanded into a length four list [left, top, right, bottom] and stored\n    in the property.\n\n    :Parameters:\n        `default`: a default list of values\n            Specifies the default values for the list.\n        `length`: int, one of 2 or 4.\n            Specifies the length of the final list. The `default` list will\n            be expanded to match a list of this length.\n        `\\*\\*kwargs`: a list of keyword arguments\n            Not currently used.\n\n    Keeping in mind that the `default` list is expanded to a list of length 4,\n    here are some examples of how VariabelListProperty's are handled.\n\n    - VariableListProperty([1]) represents [1, 1, 1, 1].\n    - VariableListProperty([1, 2]) represents [1, 2, 1, 2].\n    - VariableListProperty(['1px', (2, 'px'), 3, 4.0]) represents [1, 2, 3, 4.0].\n    - VariableListProperty(5) represents [5, 5, 5, 5].\n    - VariableListProperty(3, length=2) represents [3, 3].\n\n    .. versionadded:: 1.7.0\n    "
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
    def length(self):
        pass
    
    def link(self):
        pass
    

WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nProperties\n==========\n\nThe *Properties* classes are used when you create an\n:class:`~kivy.event.EventDispatcher`.\n\n.. warning::\n        Kivy\'s Properties are **not to be confused** with Python\'s\n        properties (i.e. the ``@property`` decorator and the <property> type).\n\nKivy\'s property classes support:\n\n    Value Checking / Validation\n        When you assign a new value to a property, the value is checked against\n        validation constraints. For\n        example, validation for an :class:`OptionProperty` will make sure that\n        the value is in a predefined list of possibilities. Validation for a\n        :class:`NumericProperty` will check that your value is a numeric type.\n        This prevents many errors early on.\n\n    Observer Pattern\n        You can specify what should happen when a property\'s value changes.\n        You can bind your own function as a callback to changes of a\n        :class:`Property`. If, for example, you want a piece of code to be\n        called when a widget\'s :class:`~kivy.uix.widget.Widget.pos` property\n        changes, you can :class:`~kivy.event.EventDispatcher.bind` a function\n        to it.\n\n    Better Memory Management\n        The same instance of a property is shared across multiple widget\n        instances.\n\nComparison Python vs. Kivy\n--------------------------\n\nBasic example\n~~~~~~~~~~~~~\n\nLet\'s compare Python and Kivy properties by creating a Python class with \'a\'\nas a float property::\n\n    class MyClass(object):\n        def __init__(self, a=1.0):\n            super(MyClass, self).__init__()\n            self.a = a\n\nWith Kivy, you can do::\n\n    class MyClass(EventDispatcher):\n        a = NumericProperty(1.0)\n\n\nDepth being tracked\n~~~~~~~~~~~~~~~~~~~\n\nOnly the "top level" of a nested object is being tracked. For example::\n\n    my_list_prop = ListProperty([1, {\'hi\': 0}])\n    # Changing a top level element will trigger all `on_my_list_prop` callbacks\n    my_list_prop[0] = 4\n    # Changing a deeper element will be ignored by all `on_my_list_prop` callbacks\n    my_list_prop[1][\'hi\'] = 4\n\nThe same holds true for all container-type kivy properties.\n\nValue checking\n~~~~~~~~~~~~~~\n\nIf you wanted to add a check for a minimum / maximum value allowed for a\nproperty, here is a possible implementation in Python::\n\n    class MyClass(object):\n        def __init__(self, a=1):\n            super(MyClass, self).__init__()\n            self.a_min = 0\n            self.a_max = 100\n            self.a = a\n\n        def _get_a(self):\n            return self._a\n        def _set_a(self, value):\n            if value < self.a_min or value > self.a_max:\n                raise ValueError(\'a out of bounds\')\n            self._a = value\n        a = property(_get_a, _set_a)\n\nThe disadvantage is you have to do that work yourself. And it becomes\nlaborious and complex if you have many properties.\nWith Kivy, you can simplify the process::\n\n    class MyClass(EventDispatcher):\n        a = BoundedNumericProperty(1, min=0, max=100)\n\nThat\'s all!\n\n\nError Handling\n~~~~~~~~~~~~~~\n\nIf setting a value would otherwise raise a ValueError, you have two options to\nhandle the error gracefully within the property. The first option is to use an\nerrorvalue parameter. An errorvalue is a substitute for the invalid value::\n\n    # simply returns 0 if the value exceeds the bounds\n    bnp = BoundedNumericProperty(0, min=-500, max=500, errorvalue=0)\n\nThe second option in to use an errorhandler parameter. An errorhandler is a\ncallable (single argument function or lambda) which can return a valid\nsubstitute::\n\n    # returns the boundary value when exceeded\n    bnp = BoundedNumericProperty(0, min=-500, max=500,\n        errorhandler=lambda x: 500 if x > 500 else -500)\n\nKeyword arguments and __init__()\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nWhen working with inheritance, namely with the `__init__()` of an object that\ninherits from :class:`~kivy.event.EventDispatcher` e.g. a\n:class:`~kivy.uix.widget.Widget`, the properties protect\nyou from a Python 3 object error. This error occurs when passing kwargs to the\n`object` instance through a `super()` call::\n\n    class MyClass(EventDispatcher):\n        def __init__(self, **kwargs):\n            super(MyClass, self).__init__(**kwargs)\n            self.my_string = kwargs.get(\'my_string\')\n\n    print(MyClass(my_string=\'value\').my_string)\n\nWhile this error is silenced in Python 2, it will stop the application\nin Python 3 with::\n\n    TypeError: object.__init__() takes no parameters\n\nLogically, to fix that you\'d either put `my_string` directly in the\n`__init__()` definition as a required argument or as an optional keyword\nargument with a default value i.e.::\n\n    class MyClass(EventDispatcher):\n        def __init__(self, my_string, **kwargs):\n            super(MyClass, self).__init__(**kwargs)\n            self.my_string = my_string\n\nor::\n\n    class MyClass(EventDispatcher):\n        def __init__(self, my_string=\'default\', **kwargs):\n            super(MyClass, self).__init__(**kwargs)\n            self.my_string = my_string\n\nAlternatively, you could pop the key-value pair from the `kwargs` dictionary\nbefore calling `super()`::\n\n    class MyClass(EventDispatcher):\n        def __init__(self, **kwargs):\n            self.my_string = kwargs.pop(\'my_string\')\n            super(MyClass, self).__init__(**kwargs)\n\nKivy properties are more flexible and do the required `kwargs.pop()`\nin the background automatically (within the `super()` call\nto :class:`~kivy.event.EventDispatcher`) to prevent this distraction::\n\n    class MyClass(EventDispatcher):\n        my_string = StringProperty(\'default\')\n        def __init__(self, **kwargs):\n            super(MyClass, self).__init__(**kwargs)\n\n    print(MyClass(my_string=\'value\').my_string)\n\nConclusion\n~~~~~~~~~~\n\nKivy properties are easier to use than the standard ones. See the next chapter\nfor examples of how to use them :)\n\n\nObserve Property changes\n------------------------\n\nAs we said in the beginning, Kivy\'s Properties implement the `Observer pattern\n<http://en.wikipedia.org/wiki/Observer_pattern>`_. That means you can\n:meth:`~kivy.event.EventDispatcher.bind` to a property and have your own\nfunction called when the value changes.\n\nThere are multiple ways to observe the changes.\n\nObserve using bind()\n~~~~~~~~~~~~~~~~~~~~\n\nYou can observe a property change by using the bind() method outside of the\nclass::\n\n    class MyClass(EventDispatcher):\n        a = NumericProperty(1)\n\n    def callback(instance, value):\n        print(\'My callback is call from\', instance)\n        print(\'and the a value changed to\', value)\n\n    ins = MyClass()\n    ins.bind(a=callback)\n\n    # At this point, any change to the a property will call your callback.\n    ins.a = 5    # callback called\n    ins.a = 5    # callback not called, because the value did not change\n    ins.a = -1   # callback called\n\n.. note::\n\n    Property objects live at the class level and manage the values attached\n    to instances. Re-assigning at class level will remove the Property. For\n    example, continuing with the code above, `MyClass.a = 5` replaces\n    the property object with a simple int.\n\n\nObserve using \'on_<propname>\'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nIf you defined the class yourself, you can use the \'on_<propname>\' callback::\n\n    class MyClass(EventDispatcher):\n        a = NumericProperty(1)\n\n        def on_a(self, instance, value):\n            print(\'My property a changed to\', value)\n\n.. warning::\n\n    Be careful with \'on_<propname>\'. If you are creating such a callback on a\n    property you are inheriting, you must not forget to call the superclass\n    function too.\n\nBinding to properties of properties.\n------------------------------------\n\nWhen binding to a property of a property, for example binding to a numeric\nproperty of an object saved in a object property, updating the object property\nto point to a new object will not re-bind the numeric property to the\nnew object. For example:\n\n.. code-block:: kv\n\n    <MyWidget>:\n        Label:\n            id: first\n            text: \'First label\'\n        Label:\n            id: second\n            text: \'Second label\'\n        Button:\n            label: first\n            text: self.label.text\n            on_press: self.label = second\n\nWhen clicking on the button, although the label object property has changed\nto the second widget, the button text will not change because it is bound to\nthe text property of the first label directly.\n\nIn `1.9.0`, the ``rebind`` option has been introduced that will allow the\nautomatic updating of the ``text`` when ``label`` is changed, provided it\nwas enabled. See :class:`ObjectProperty`.\n'Purge log fired. Analysing...
Purge finished!

__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/properties.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.properties'
__package__ = 'kivy'
__test__ = _mod_builtins.dict()
def dpi2px():
    pass

def get_color_from_hex(s):
    'Transform a hex string color to a kivy\n    :class:`~kivy.graphics.Color`.\n    '
    pass

partial = _mod_functools.partial
ref = weakref()
string_types = _mod_builtins.str
