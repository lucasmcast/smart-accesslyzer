import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import kivy.graphics.instructions as _mod_kivy_graphics_instructions
import kivy.weakmethod as _mod_kivy_weakmethod
import logging as _mod_logging
import os as _mod_os

class Fbo(_mod_kivy_graphics_instructions.RenderContext):
    'Fbo class for wrapping the OpenGL Framebuffer extension. The Fbo support\n    "with" statement.\n\n    :Parameters:\n        `clear_color`: tuple, defaults to (0, 0, 0, 0)\n            Define the default color for clearing the framebuffer\n        `size`: tuple, defaults to (1024, 1024)\n            Default size of the framebuffer\n        `push_viewport`: bool, defaults to True\n            If True, the OpenGL viewport will be set to the framebuffer size,\n            and will be automatically restored when the framebuffer released.\n        `with_depthbuffer`: bool, defaults to False\n            If True, the framebuffer will be allocated with a Z buffer.\n        `with_stencilbuffer`: bool, defaults to False\n            .. versionadded:: 1.9.0\n\n            If True, the framebuffer will be allocated with a stencil buffer.\n        `texture`: :class:`~kivy.graphics.texture.Texture`, defaults to None\n            If None, a default texture will be created.\n\n    .. note::\n        Using both of ``with_stencilbuffer`` and ``with_depthbuffer`` is not\n        supported in kivy 1.9.0\n\n    '
    __class__ = Fbo
    def __init__(self, *args, **kwargs):
        'Fbo class for wrapping the OpenGL Framebuffer extension. The Fbo support\n    "with" statement.\n\n    :Parameters:\n        `clear_color`: tuple, defaults to (0, 0, 0, 0)\n            Define the default color for clearing the framebuffer\n        `size`: tuple, defaults to (1024, 1024)\n            Default size of the framebuffer\n        `push_viewport`: bool, defaults to True\n            If True, the OpenGL viewport will be set to the framebuffer size,\n            and will be automatically restored when the framebuffer released.\n        `with_depthbuffer`: bool, defaults to False\n            If True, the framebuffer will be allocated with a Z buffer.\n        `with_stencilbuffer`: bool, defaults to False\n            .. versionadded:: 1.9.0\n\n            If True, the framebuffer will be allocated with a stencil buffer.\n        `texture`: :class:`~kivy.graphics.texture.Texture`, defaults to None\n            If None, a default texture will be created.\n\n    .. note::\n        Using both of ``with_stencilbuffer`` and ``with_depthbuffer`` is not\n        supported in kivy 1.9.0\n\n    '
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
        'Add a callback to be called after the whole graphics context has\n        been reloaded. This is where you can reupload your custom data in GPU.\n\n        .. versionadded:: 1.2.0\n\n        :Parameters:\n            `callback`: func(context) -> return None\n                The first parameter will be the context itself\n        '
        pass
    
    def bind(self):
        'Bind the FBO to the current opengl context.\n        `Bind` mean that you enable the Framebuffer, and all the drawing\n        operations will act inside the Framebuffer, until :meth:`release` is\n        called.\n\n        The bind/release operations are automatically called when you add\n        graphics objects into it. If you want to manipulate a Framebuffer\n        yourself, you can use it like this::\n\n            self.fbo = FBO()\n            self.fbo.bind()\n            # do any drawing command\n            self.fbo.release()\n\n            # then, your fbo texture is available at\n            print(self.fbo.texture)\n        '
        pass
    
    def clear_buffer(self):
        'Clear the framebuffer with the :attr:`clear_color`.\n\n        You need to bind the framebuffer yourself before calling this\n        method::\n\n            fbo.bind()\n            fbo.clear_buffer()\n            fbo.release()\n\n        '
        pass
    
    @property
    def clear_color(self):
        'Clear color in (red, green, blue, alpha) format.\n        '
        pass
    
    def get_pixel_color(self):
        'Get the color of the pixel with specified window\n        coordinates wx, wy. It returns result in RGBA format.\n\n        .. versionadded:: 1.8.0\n        '
        pass
    
    @property
    def pixels(self):
        'Get the pixels texture, in RGBA format only, unsigned byte. The\n        origin of the image is at bottom left.\n\n        .. versionadded:: 1.7.0\n        '
        pass
    
    def release(self):
        'Release the Framebuffer (unbind).\n        '
        pass
    
    def remove_reload_observer(self):
        'Remove a callback from the observer list, previously added by\n        :meth:`add_reload_observer`.\n\n        .. versionadded:: 1.2.0\n\n        '
        pass
    
    @property
    def size(self):
        'Size of the framebuffer, in (width, height) format.\n\n        If you change the size, the framebuffer content will be lost.\n        '
        pass
    
    @property
    def texture(self):
        'Return the framebuffer texture\n        '
        pass
    

Logger = _mod_logging.Logger()
PY2 = False
WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = "\nFramebuffer\n===========\n\nThe Fbo is like an offscreen window. You can activate the fbo for rendering into\na texture and use your fbo as a texture for other drawing.\n\nThe Fbo acts as a :class:`kivy.graphics.instructions.Canvas`.\n\nHere is an example of using an fbo for some colored rectangles::\n\n    from kivy.graphics import Fbo, Color, Rectangle\n\n    class FboTest(Widget):\n        def __init__(self, **kwargs):\n            super(FboTest, self).__init__(**kwargs)\n\n            # first step is to create the fbo and use the fbo texture on other\n            # rectangle\n\n            with self.canvas:\n                # create the fbo\n                self.fbo = Fbo(size=(256, 256))\n\n                # show our fbo on the widget in different size\n                Color(1, 1, 1)\n                Rectangle(size=(32, 32), texture=self.fbo.texture)\n                Rectangle(pos=(32, 0), size=(64, 64), texture=self.fbo.texture)\n                Rectangle(pos=(96, 0), size=(128, 128), texture=self.fbo.texture)\n\n            # in the second step, you can draw whatever you want on the fbo\n            with self.fbo:\n                Color(1, 0, 0, .8)\n                Rectangle(size=(256, 64))\n                Color(0, 1, 0, .8)\n                Rectangle(size=(64, 256))\n\nIf you change anything in the `self.fbo` object, it will be automatically updated.\nThe canvas where the fbo is put will be automatically updated as well.\n\nReloading the FBO content\n-------------------------\n\n.. versionadded:: 1.2.0\n\nIf the OpenGL context is lost, then the FBO is lost too. You need to reupload\ndata on it yourself. Use the :meth:`Fbo.add_reload_observer` to add a reloading\nfunction that will be automatically called when needed::\n\n    def __init__(self, **kwargs):\n        super(...).__init__(**kwargs)\n        self.fbo = Fbo(size=(512, 512))\n        self.fbo.add_reload_observer(self.populate_fbo)\n\n        # and load the data now.\n        self.populate_fbo(self.fbo)\n\n\n    def populate_fbo(self, fbo):\n        with fbo:\n            # .. put your Color / Rectangle / ... here\n\nThis way, you could use the same method for initialization and for reloading.\nBut it's up to you.\n\n"
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/fbo.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.fbo'
__package__ = 'kivy.graphics'
def __pyx_unpickle_Fbo():
    pass

__test__ = _mod_builtins.dict()
environ = _mod_os._Environ()
def py_glReadPixels():
    'See: `glReadPixels() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glReadPixels.xml>`_\n\n    We support only GL_RGB/GL_RGBA as a format and GL_UNSIGNED_BYTE as a\n    type.\n    '
    pass

