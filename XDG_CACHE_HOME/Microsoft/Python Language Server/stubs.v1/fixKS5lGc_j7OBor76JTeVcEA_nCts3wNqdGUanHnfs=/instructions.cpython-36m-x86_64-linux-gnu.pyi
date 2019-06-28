import builtins as _mod_builtins
import kivy._event as _mod_kivy__event
import kivy.cache as _mod_kivy_cache
import kivy.core.image as _mod_kivy_core_image
import logging as _mod_logging

Cache = _mod_kivy_cache.Cache
class Callback(Instruction):
    ".. versionadded:: 1.0.4\n\n    A Callback is an instruction that will be called when the drawing\n    operation is performed. When adding instructions to a canvas, you can do\n    this::\n\n        with self.canvas:\n            Color(1, 1, 1)\n            Rectangle(pos=self.pos, size=self.size)\n            Callback(self.my_callback)\n\n    The definition of the callback must be::\n\n        def my_callback(self, instr):\n            print('I have been called!')\n\n    .. warning::\n\n        Note that if you perform many and/or costly calls to callbacks, you\n        might potentially slow down the rendering performance significantly.\n\n    The updating of your canvas does not occur until something new happens.\n    From your callback, you can ask for an update::\n\n        with self.canvas:\n            self.cb = Callback(self.my_callback)\n        # then later in the code\n        self.cb.ask_update()\n\n    If you use the Callback class to call rendering methods of another\n    toolkit, you will have issues with the OpenGL context. The OpenGL state may\n    have been manipulated by the other toolkit, and as soon as program flow\n    returns to Kivy, it will just break. You can have glitches, crashes, black\n    holes might occur, etc.\n    To avoid that, you can activate the :attr:`reset_context` option. It will\n    reset the OpenGL context state to make Kivy's rendering correct after the\n    call to your callback.\n\n    .. warning::\n\n        The :attr:`reset_context` is not a full OpenGL reset. If you have issues\n        regarding that, please contact us.\n\n    "
    __class__ = Callback
    def __init__(self, *args, **kwargs):
        ".. versionadded:: 1.0.4\n\n    A Callback is an instruction that will be called when the drawing\n    operation is performed. When adding instructions to a canvas, you can do\n    this::\n\n        with self.canvas:\n            Color(1, 1, 1)\n            Rectangle(pos=self.pos, size=self.size)\n            Callback(self.my_callback)\n\n    The definition of the callback must be::\n\n        def my_callback(self, instr):\n            print('I have been called!')\n\n    .. warning::\n\n        Note that if you perform many and/or costly calls to callbacks, you\n        might potentially slow down the rendering performance significantly.\n\n    The updating of your canvas does not occur until something new happens.\n    From your callback, you can ask for an update::\n\n        with self.canvas:\n            self.cb = Callback(self.my_callback)\n        # then later in the code\n        self.cb.ask_update()\n\n    If you use the Callback class to call rendering methods of another\n    toolkit, you will have issues with the OpenGL context. The OpenGL state may\n    have been manipulated by the other toolkit, and as soon as program flow\n    returns to Kivy, it will just break. You can have glitches, crashes, black\n    holes might occur, etc.\n    To avoid that, you can activate the :attr:`reset_context` option. It will\n    reset the OpenGL context state to make Kivy's rendering correct after the\n    call to your callback.\n\n    .. warning::\n\n        The :attr:`reset_context` is not a full OpenGL reset. If you have issues\n        regarding that, please contact us.\n\n    "
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
    
    def ask_update(self):
        "Inform the parent canvas that we'd like it to update on the next\n        frame. This is useful when you need to trigger a redraw due to some\n        value having changed for example.\n\n        .. versionadded:: 1.0.4\n        "
        pass
    
    @property
    def reset_context(self):
        'Set this to True if you want to reset the OpenGL context for Kivy\n        after the callback has been called.\n        '
        pass
    

class Canvas(CanvasBase):
    "The important Canvas class. Use this class to add graphics or context\n    instructions that you want to be used for drawing.\n\n    .. note::\n\n        The Canvas supports Python's ``with`` statement and its enter & exit\n        semantics.\n\n    Usage of a canvas without the ``with`` statement::\n\n        self.canvas.add(Color(1., 1., 0))\n        self.canvas.add(Rectangle(size=(50, 50)))\n\n    Usage of a canvas with Python's ``with`` statement::\n\n        with self.canvas:\n            Color(1., 1., 0)\n            Rectangle(size=(50, 50))\n    "
    __class__ = Canvas
    def __init__(self, *args, **kwargs):
        "The important Canvas class. Use this class to add graphics or context\n    instructions that you want to be used for drawing.\n\n    .. note::\n\n        The Canvas supports Python's ``with`` statement and its enter & exit\n        semantics.\n\n    Usage of a canvas without the ``with`` statement::\n\n        self.canvas.add(Color(1., 1., 0))\n        self.canvas.add(Rectangle(size=(50, 50)))\n\n    Usage of a canvas with Python's ``with`` statement::\n\n        with self.canvas:\n            Color(1., 1., 0)\n            Rectangle(size=(50, 50))\n    "
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
    
    def add(self):
        pass
    
    @property
    def after(self):
        "Property for getting the 'after' group.\n        "
        pass
    
    def ask_update(self):
        "Inform the canvas that we'd like it to update on the next frame.\n        This is useful when you need to trigger a redraw due to some value\n        having changed for example.\n        "
        pass
    
    @property
    def before(self):
        "Property for getting the 'before' group.\n        "
        pass
    
    def clear(self):
        'Clears every :class:`Instruction` in the canvas, leaving it clean.'
        pass
    
    def draw(self):
        'Apply the instruction to our window.\n        '
        pass
    
    @property
    def has_after(self):
        'Property to see if the :attr:`after` group has already been created.\n\n        .. versionadded:: 1.7.0\n        '
        pass
    
    @property
    def has_before(self):
        'Property to see if the :attr:`before` group has already been created.\n\n        .. versionadded:: 1.7.0\n        '
        pass
    
    @property
    def opacity(self):
        "Property to get/set the opacity value of the canvas.\n\n        .. versionadded:: 1.4.1\n\n        The opacity attribute controls the opacity of the canvas and its\n        children.  Be careful, it's a cumulative attribute: the value is\n        multiplied to the current global opacity and the result is applied to\n        the current context color.\n\n        For example: if your parent has an opacity of 0.5 and a child has an\n        opacity of 0.2, the real opacity of the child will be 0.5 * 0.2 = 0.1.\n\n        Then, the opacity is applied on the shader as::\n\n            frag_color = color * vec4(1.0, 1.0, 1.0, opacity);\n\n        "
        pass
    
    def remove(self):
        pass
    

class CanvasBase(InstructionGroup):
    'CanvasBase provides the context manager methods for the\n    :class:`Canvas`.'
    __class__ = CanvasBase
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'CanvasBase provides the context manager methods for the\n    :class:`Canvas`.'
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
    

class ContextInstruction(Instruction):
    "The ContextInstruction class is the base for the creation of instructions\n    that don't have a direct visual representation, but instead modify the\n    current Canvas' state, e.g. texture binding, setting color parameters,\n    matrix manipulation and so on.\n    "
    __class__ = ContextInstruction
    def __init__(self, *args, **kwargs):
        "The ContextInstruction class is the base for the creation of instructions\n    that don't have a direct visual representation, but instead modify the\n    current Canvas' state, e.g. texture binding, setting color parameters,\n    matrix manipulation and so on.\n    "
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
    

Image = _mod_kivy_core_image.Image
class Instruction(_mod_kivy__event.ObjectWithUid):
    "Represents the smallest instruction available. This class is for internal\n    usage only, don't use it directly.\n    "
    __class__ = Instruction
    def __init__(self, *args, **kwargs):
        "Represents the smallest instruction available. This class is for internal\n    usage only, don't use it directly.\n    "
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
    
    def flag_update(self):
        pass
    
    @property
    def group(self):
        pass
    
    @property
    def needs_redraw(self):
        pass
    
    @property
    def proxy_ref(self):
        'Return a proxy reference to the Instruction i.e. without creating a\n        reference of the widget. See `weakref.proxy\n        <http://docs.python.org/2/library/weakref.html?highlight=proxy#weakref.proxy>`_\n        for more information.\n\n        .. versionadded:: 1.7.2\n        '
        pass
    

class InstructionGroup(Instruction):
    'Group of :class:`Instructions <Instruction>`. Allows for the adding and\n    removing of graphics instructions. It can be used directly as follows::\n\n        blue = InstructionGroup()\n        blue.add(Color(0, 0, 1, 0.2))\n        blue.add(Rectangle(pos=self.pos, size=(100, 100)))\n\n        green = InstructionGroup()\n        green.add(Color(0, 1, 0, 0.4))\n        green.add(Rectangle(pos=(100, 100), size=(100, 100)))\n\n        # Here, self should be a Widget or subclass\n        [self.canvas.add(group) for group in [blue, green]]\n\n    '
    __class__ = InstructionGroup
    def __init__(self, *args, **kwargs):
        'Group of :class:`Instructions <Instruction>`. Allows for the adding and\n    removing of graphics instructions. It can be used directly as follows::\n\n        blue = InstructionGroup()\n        blue.add(Color(0, 0, 1, 0.2))\n        blue.add(Rectangle(pos=self.pos, size=(100, 100)))\n\n        green = InstructionGroup()\n        green.add(Color(0, 1, 0, 0.4))\n        green.add(Rectangle(pos=(100, 100), size=(100, 100)))\n\n        # Here, self should be a Widget or subclass\n        [self.canvas.add(group) for group in [blue, green]]\n\n    '
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
    
    def add(self):
        'Add a new :class:`Instruction` to our list.\n        '
        pass
    
    @property
    def children(self):
        pass
    
    def clear(self):
        'Remove all the :class:`Instructions <Instruction>`.\n        '
        pass
    
    def get_group(self):
        'Return an iterable for all the :class:`Instructions <Instruction>`\n        with a specific group name.\n        '
        pass
    
    def indexof(self):
        pass
    
    def insert(self):
        'Insert a new :class:`Instruction` into our list at index.\n        '
        pass
    
    def length(self):
        pass
    
    def remove(self):
        'Remove an existing :class:`Instruction` from our list.\n        '
        pass
    
    def remove_group(self):
        'Remove all :class:`Instructions <Instruction>` with a specific group\n        name.\n        '
        pass
    

Logger = _mod_logging.Logger()
PY2 = False
class RenderContext(Canvas):
    'The render context stores all the necessary information for drawing, i.e.:\n\n    - The vertex shader\n    - The fragment shader\n    - The default texture\n    - The state stack (color, texture, matrix...)\n    '
    __class__ = RenderContext
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'The render context stores all the necessary information for drawing, i.e.:\n\n    - The vertex shader\n    - The fragment shader\n    - The default texture\n    - The state stack (color, texture, matrix...)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def shader(self):
        'Return the shader attached to the render context.\n        '
        pass
    
    @property
    def use_parent_frag_modelview(self):
        'If True, the parent fragment modelview matrix will be used.\n\n        .. versionadded:: 1.10.1\n\n            rc = RenderContext(use_parent_frag_modelview=True)\n        '
        pass
    
    @property
    def use_parent_modelview(self):
        "If True, the parent modelview matrix will be used.\n\n        .. versionadded:: 1.7.0\n\n        Before::\n\n            rc['modelview_mat'] = Window.render_context['modelview_mat']\n\n        Now::\n\n            rc = RenderContext(use_parent_modelview=True)\n        "
        pass
    
    @property
    def use_parent_projection(self):
        "If True, the parent projection matrix will be used.\n\n        .. versionadded:: 1.7.0\n\n        Before::\n\n            rc['projection_mat'] = Window.render_context['projection_mat']\n\n        Now::\n\n            rc = RenderContext(use_parent_projection=True)\n        "
        pass
    

class VertexInstruction(Instruction):
    'The VertexInstruction class is the base for all graphics instructions\n    that have a direct visual representation on the canvas, such as Rectangles,\n    Triangles, Lines, Ellipse and so on.\n    '
    __class__ = VertexInstruction
    def __init__(self, *args, **kwargs):
        'The VertexInstruction class is the base for all graphics instructions\n    that have a direct visual representation on the canvas, such as Rectangles,\n    Triangles, Lines, Ellipse and so on.\n    '
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
    def source(self):
        "This property represents the filename to load the texture from.\n        If you want to use an image as source, do it like this::\n\n            with self.canvas:\n                Rectangle(source='mylogo.png', pos=self.pos, size=self.size)\n\n        Here's the equivalent in Kivy language:\n\n        .. code-block:: kv\n\n            <MyWidget>:\n                canvas:\n                    Rectangle:\n                        source: 'mylogo.png'\n                        pos: self.pos\n                        size: self.size\n\n        .. note::\n\n            The filename will be searched for using the\n            :func:`kivy.resources.resource_find` function.\n\n        "
        pass
    
    @property
    def tex_coords(self):
        "This property represents the texture coordinates used for drawing the\n        vertex instruction. The value must be a list of 8 values.\n\n        A texture coordinate has a position (u, v), and a size (w, h). The size\n        can be negative, and would represent the 'flipped' texture. By default,\n        the tex_coords are::\n\n            [u, v, u + w, v, u + w, v + h, u, v + h]\n\n        You can pass your own texture coordinates if you want to achieve fancy\n        effects.\n\n        .. warning::\n\n            The default values just mentioned can be negative. Depending\n            on the image and label providers, the coordinates are flipped\n            vertically because of the order in which the image is internally\n            stored. Instead of flipping the image data, we are just flipping\n            the texture coordinates to be faster.\n\n        "
        pass
    
    @property
    def texture(self):
        "Property that represents the texture used for drawing this\n        Instruction. You can set a new texture like this::\n\n            from kivy.core.image import Image\n\n            texture = Image('logo.png').texture\n            with self.canvas:\n                Rectangle(texture=texture, pos=self.pos, size=self.size)\n\n        Usually, you will use the :attr:`source` attribute instead of the\n        texture.\n        "
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nCanvas\n======\n\nThe :class:`Canvas` is the root object used for drawing by a\n:class:`~kivy.uix.widget.Widget`. Check the class documentation for more\ninformation about the usage of Canvas.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/instructions.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.instructions'
__package__ = 'kivy.graphics'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def join(a, *p):
    "Join two or more pathname components, inserting '/' as needed.\n    If any component is an absolute path, all previous path components\n    will be discarded.  An empty last part will result in a path that\n    ends with a separator."
    pass

kivy_shader_dir = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/data/glsl'
def proxy(object, callback=None):
    "proxy(object[, callback]) -- create a proxy object that weakly\nreferences 'object'.  'callback', if given, is called with a\nreference to the proxy when 'object' is about to be finalized."
    pass

