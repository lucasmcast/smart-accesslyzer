import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import kivy.weakmethod as _mod_kivy_weakmethod
import logging as _mod_logging
import os as _mod_os

GLCAP_BGRA = 2
GLCAP_DXT1 = 4
GLCAP_ETC1 = 6
GLCAP_NPOT = 2
GLCAP_PVRTC = 5
GLCAP_S3TC = 3
GLCAP_UNPACK_SUBIMAGE = 7
Logger = _mod_logging.Logger()
class Texture(_mod_builtins.object):
    'Handle an OpenGL texture. This class can be used to create simple\n    textures or complex textures based on ImageData.'
    __class__ = Texture
    def __init__(self, *args, **kwargs):
        'Handle an OpenGL texture. This class can be used to create simple\n    textures or complex textures based on ImageData.'
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
    
    def _on_proxyimage_loaded(self):
        pass
    
    _sequenced_textures = _mod_builtins.dict()
    def add_reload_observer(self):
        'Add a callback to be called after the whole graphics context has\n        been reloaded. This is where you can reupload your custom data into\n        the GPU.\n\n        .. versionadded:: 1.2.0\n\n        :Parameters:\n            `callback`: func(context) -> return None\n                The first parameter will be the context itself.\n        '
        pass
    
    def ask_update(self):
        'Indicate that the content of the texture should be updated and the\n        callback function needs to be called when the texture will be\n        used.\n        '
        pass
    
    def bind(self):
        'Bind the texture to the current opengl state.'
        pass
    
    def blit_buffer(self):
        "Blit a buffer into the texture.\n\n        .. note::\n\n            Unless the canvas will be updated due to other changes,\n            :meth:`~kivy.graphics.instructions.Canvas.ask_update` should be\n            called in order to update the texture.\n\n        :Parameters:\n            `pbuffer`: bytes, or a class that implements the buffer interface (including memoryview).\n                A buffer containing the image data. It can be either a bytes\n                object or a instance of a class that implements the python\n                buffer interface, e.g. `array.array`, `bytearray`, numpy arrays\n                etc. If it's not a bytes object, the underlying buffer must\n                be contiguous, have only one dimension and must not be\n                readonly, even though the data is not modified, due to a cython\n                limitation. See module description for usage details.\n            `size`: tuple, defaults to texture size\n                Size of the image (width, height)\n            `colorfmt`: str, defaults to 'rgb'\n                Image format, can be one of 'rgb', 'rgba', 'bgr', 'bgra',\n                'luminance' or 'luminance_alpha'.\n            `pos`: tuple, defaults to (0, 0)\n                Position to blit in the texture.\n            `bufferfmt`: str, defaults to 'ubyte'\n                Type of the data buffer, can be one of 'ubyte', 'ushort',\n                'uint', 'byte', 'short', 'int' or 'float'.\n            `mipmap_level`: int, defaults to 0\n                Indicate which mipmap level we are going to update.\n            `mipmap_generation`: bool, defaults to True\n                Indicate if we need to regenerate the mipmap from level 0.\n\n        .. versionchanged:: 1.0.7\n\n            added `mipmap_level` and `mipmap_generation`\n\n        .. versionchanged:: 1.9.0\n            `pbuffer` can now be any class instance that implements the python\n            buffer interface and / or memoryviews thereof.\n\n        "
        pass
    
    def blit_data(self):
        'Replace a whole texture with image data.\n        '
        pass
    
    @property
    def bufferfmt(self):
        'Return the buffer format used in this texture (readonly).\n\n        .. versionadded:: 1.2.0\n        '
        pass
    
    @property
    def colorfmt(self):
        'Return the color format used in this texture (readonly).\n\n        .. versionadded:: 1.0.7\n        '
        pass
    
    @classmethod
    def create(cls):
        "Create a texture based on size.\n\n    :Parameters:\n        `size`: tuple, defaults to (128, 128)\n            Size of the texture.\n        `colorfmt`: str, defaults to 'rgba'\n            Color format of the texture. Can be 'rgba' or 'rgb',\n            'luminance' or 'luminance_alpha'. On desktop, additional values are\n            available: 'red', 'rg'.\n        `icolorfmt`: str, defaults to the value of `colorfmt`\n            Internal format storage of the texture. Can be 'rgba' or 'rgb',\n            'luminance' or 'luminance_alpha'. On desktop, additional values are\n            available: 'r8', 'rg8', 'rgba8'.\n        `bufferfmt`: str, defaults to 'ubyte'\n            Internal buffer format of the texture. Can be 'ubyte', 'ushort',\n            'uint', 'bute', 'short', 'int' or 'float'.\n        `mipmap`: bool, defaults to False\n            If True, it will automatically generate the mipmap texture.\n        `callback`: callable(), defaults to False\n            If a function is provided, it will be called when data is\n            needed in the texture.\n\n    .. versionchanged:: 1.7.0\n        :attr:`callback` has been added\n    "
        pass
    
    @classmethod
    def create_from_data(cls):
        'Create a texture from an ImageData class.\n    '
        pass
    
    def flip_horizontal(self):
        'Flip tex_coords for horizontal display.\n\n        .. versionadded:: 1.9.0\n\n        '
        pass
    
    def flip_vertical(self):
        'Flip tex_coords for vertical display.'
        pass
    
    def get_region(self):
        'Return a part of the texture defined by the rectangular arguments\n        (x, y, width, height). Returns a :class:`TextureRegion` instance.'
        pass
    
    @property
    def height(self):
        'Return the height of the texture (readonly).\n        '
        pass
    
    @property
    def id(self):
        'Return the OpenGL ID of the texture (readonly).\n        '
        pass
    
    @property
    def mag_filter(self):
        'Get/set the mag filter texture. Available values:\n\n        - linear\n        - nearest\n\n        Check the opengl documentation for more information about the behavior\n        of these values :\n        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.\n        '
        pass
    
    @property
    def min_filter(self):
        'Get/set the min filter texture. Available values:\n\n        - linear\n        - nearest\n        - linear_mipmap_linear\n        - linear_mipmap_nearest\n        - nearest_mipmap_nearest\n        - nearest_mipmap_linear\n\n        Check the opengl documentation for more information about the behavior\n        of these values :\n        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.\n        '
        pass
    
    @property
    def mipmap(self):
        'Return True if the texture has mipmap enabled (readonly).\n        '
        pass
    
    @property
    def pixels(self):
        'Get the pixels texture, in RGBA format only, unsigned byte. The\n        origin of the image is at bottom left.\n\n        .. versionadded:: 1.7.0\n        '
        pass
    
    def remove_reload_observer(self):
        'Remove a callback from the observer list, previously added by\n        :meth:`add_reload_observer`.\n\n        .. versionadded:: 1.2.0\n\n        '
        pass
    
    def save(self):
        "Save the texture content to a file. Check\n        :meth:`kivy.core.image.Image.save` for more information.\n\n        The flipped parameter flips the saved image vertically, and\n        defaults to True.\n\n        .. versionadded:: 1.7.0\n\n        .. versionchanged:: 1.8.0\n\n            Parameter `flipped` added, defaults to True. All the OpenGL Texture\n            are readed from bottom / left, it need to be flipped before saving.\n            If you don't want to flip the image, set flipped to False.\n        "
        pass
    
    @property
    def size(self):
        'Return the (width, height) of the texture (readonly).\n        '
        pass
    
    @property
    def target(self):
        'Return the OpenGL target of the texture (readonly).\n        '
        pass
    
    @property
    def tex_coords(self):
        'Return the list of tex_coords (opengl).\n        '
        pass
    
    @property
    def uvpos(self):
        'Get/set the UV position inside the texture.\n        '
        pass
    
    @property
    def uvsize(self):
        'Get/set the UV size inside the texture.\n\n        .. warning::\n            The size can be negative if the texture is flipped.\n        '
        pass
    
    @property
    def width(self):
        'Return the width of the texture (readonly).\n        '
        pass
    
    @property
    def wrap(self):
        'Get/set the wrap texture. Available values:\n\n        - repeat\n        - mirrored_repeat\n        - clamp_to_edge\n\n        Check the opengl documentation for more information about the behavior\n        of these values :\n        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.\n        '
        pass
    

class TextureRegion(Texture):
    'Handle a region of a Texture class. Useful for non power-of-2\n    texture handling.'
    __class__ = TextureRegion
    def __init__(self, *args, **kwargs):
        'Handle a region of a Texture class. Useful for non power-of-2\n    texture handling.'
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
    
    def ask_update(self):
        pass
    
    def bind(self):
        pass
    
    @property
    def pixels(self):
        pass
    

WeakMethod = _mod_kivy_weakmethod.WeakMethod
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nTexture\n=======\n\n.. versionchanged:: 1.6.0\n    Added support for paletted texture on OES: \'palette4_rgb8\',\n    \'palette4_rgba8\', \'palette4_r5_g6_b5\', \'palette4_rgba4\', \'palette4_rgb5_a1\',\n    \'palette8_rgb8\', \'palette8_rgba8\', \'palette8_r5_g6_b5\', \'palette8_rgba4\'\n    and \'palette8_rgb5_a1\'.\n\n:class:`Texture` is a class that handles OpenGL textures. Depending on the\nhardware,\nsome OpenGL capabilities might not be available (BGRA support, NPOT support,\netc.)\n\nYou cannot instantiate this class yourself. You must use the function\n:meth:`Texture.create` to create a new texture::\n\n    texture = Texture.create(size=(640, 480))\n\nWhen you create a texture, you should be aware of the default color\nand buffer format:\n\n    - the color/pixel format (:attr:`Texture.colorfmt`) that can be one of\n      \'rgb\', \'rgba\', \'luminance\', \'luminance_alpha\', \'bgr\' or \'bgra\'.\n      The default value is \'rgb\'\n    - the buffer format determines how a color component is stored into memory.\n      This can be one of \'ubyte\', \'ushort\', \'uint\', \'byte\', \'short\', \'int\' or\n      \'float\'. The default value and the most commonly used is \'ubyte\'.\n\nSo, if you want to create an RGBA texture::\n\n    texture = Texture.create(size=(640, 480), colorfmt=\'rgba\')\n\nYou can use your texture in almost all vertex instructions with the\n:attr:`kivy.graphics.VertexIntruction.texture` parameter. If you want to use\nyour texture in kv lang, you can save it in an\n:class:`~kivy.properties.ObjectProperty` inside your widget.\n\n.. warning::\n    Using Texture before OpenGL has been initialized will lead to a crash. If\n    you need to create textures before the application has started, import\n    Window first: `from kivy.core.window import Window`\n\nBlitting custom data\n--------------------\n\nYou can create your own data and blit it to the texture using\n:meth:`Texture.blit_buffer`.\n\nFor example, to blit immutable bytes data::\n\n    # create a 64x64 texture, defaults to rgba / ubyte\n    texture = Texture.create(size=(64, 64))\n\n    # create 64x64 rgb tab, and fill with values from 0 to 255\n    # we\'ll have a gradient from black to white\n    size = 64 * 64 * 3\n    buf = [int(x * 255 / size) for x in range(size)]\n\n    # then, convert the array to a ubyte string\n    buf = b\'\'.join(map(chr, buf))\n\n    # then blit the buffer\n    texture.blit_buffer(buf, colorfmt=\'rgb\', bufferfmt=\'ubyte\')\n\n    # that\'s all ! you can use it in your graphics now :)\n    # if self is a widget, you can do this\n    with self.canvas:\n        Rectangle(texture=texture, pos=self.pos, size=(64, 64))\n\nSince 1.9.0, you can blit data stored in a instance that implements the python\nbuffer interface, or a memoryview thereof, such as numpy arrays, python\n`array.array`, a `bytearray`, or a cython array. This is beneficial if you\nexpect to blit similar data, with perhaps a few changes in the data.\n\nWhen using a bytes representation of the data, for every change you have to\nregenerate the bytes instance, from perhaps a list, which is very inefficient.\nWhen using a buffer object, you can simply edit parts of the original data.\nSimilarly, unless starting with a bytes object, converting to bytes requires a\nfull copy, however, when using a buffer instance, no memory is copied, except\nto upload it to the GPU.\n\nContinuing with the example above::\n\n    from array import array\n\n    size = 64 * 64 * 3\n    buf = [int(x * 255 / size) for x in range(size)]\n    # initialize the array with the buffer values\n    arr = array(\'B\', buf)\n    # now blit the array\n    texture.blit_buffer(arr, colorfmt=\'rgb\', bufferfmt=\'ubyte\')\n\n    # now change some elements in the original array\n    arr[24] = arr[50] = 99\n    # blit again the buffer\n    texture.blit_buffer(arr, colorfmt=\'rgb\', bufferfmt=\'ubyte\')\n\n\nBGR/BGRA support\n----------------\n\nThe first time you try to create a BGR or BGRA texture, we check whether\nyour hardware supports BGR / BGRA textures by checking the extension\n\'GL_EXT_bgra\'.\n\nIf the extension is not found, the conversion to RGB / RGBA will be done in\nsoftware.\n\n\nNPOT texture\n------------\n\n.. versionchanged:: 1.0.7\n\n    If your hardware supports NPOT, no POT is created.\n\nAs the OpenGL documentation says, a texture must be power-of-two sized. That\nmeans\nyour width and height can be one of 64, 32, 256... but not 3, 68, 42. NPOT means\nnon-power-of-two. OpenGL ES 2 supports NPOT textures natively but with some\ndrawbacks. Another type of NPOT texture is called a rectangle texture.\nPOT, NPOT and textures all have their own pro/cons.\n\n================= ============= ============= =================================\n    Features           POT           NPOT                Rectangle\n----------------- ------------- ------------- ---------------------------------\nOpenGL Target     GL_TEXTURE_2D GL_TEXTURE_2D GL_TEXTURE_RECTANGLE_(NV|ARB|EXT)\nTexture coords    0-1 range     0-1 range     width-height range\nMipmapping        Supported     Partially     No\nWrap mode         Supported     Supported     No\n================= ============= ============= =================================\n\nIf you create a NPOT texture, we first check whether your hardware\nsupports it by checking the extensions GL_ARB_texture_non_power_of_two or\nOES_texture_npot. If none of these are available, we create the nearest\nPOT texture that can contain your NPOT texture. The :meth:`Texture.create` will\nreturn a :class:`TextureRegion` instead.\n\n\nTexture atlas\n-------------\n\nA texture atlas is a single texture that contains many images.\nIf you want to separate the original texture into many single ones, you don\'t\nneed to. You can get a region of the original texture. That will return the\noriginal texture with custom texture coordinates::\n\n    # for example, load a 128x128 image that contain 4 64x64 images\n    from kivy.core.image import Image\n    texture = Image(\'mycombinedimage.png\').texture\n\n    bottomleft = texture.get_region(0, 0, 64, 64)\n    bottomright = texture.get_region(0, 64, 64, 64)\n    topleft = texture.get_region(0, 64, 64, 64)\n    topright = texture.get_region(64, 64, 64, 64)\n\n\n.. _mipmap:\n\nMipmapping\n----------\n\n.. versionadded:: 1.0.7\n\nMipmapping is an OpenGL technique for enhancing the rendering of large textures\nto small surfaces. Without mipmapping, you might see pixelation when you\nrender to small surfaces.\nThe idea is to precalculate the subtexture and apply some image filter as a\nlinear filter. Then, when you render a small surface, instead of using the\nbiggest texture, it will use a lower filtered texture. The result can look\nbetter this way.\n\nTo make that happen, you need to specify mipmap=True when you create a\ntexture. Some widgets already give you the ability to create mipmapped\ntextures, such as the :class:`~kivy.uix.label.Label` and\n:class:`~kivy.uix.image.Image`.\n\nFrom the OpenGL Wiki : "So a 64x16 2D texture can have 5 mip-maps: 32x8, 16x4,\n8x2, 4x1, 2x1, and 1x1". Check http://www.opengl.org/wiki/Texture for more\ninformation.\n\n.. note::\n\n    As the table in previous section said, if your texture is NPOT, we\n    create the nearest POT texture and generate a mipmap from it. This\n    might change in the future.\n\nReloading the Texture\n---------------------\n\n.. versionadded:: 1.2.0\n\nIf the OpenGL context is lost, the Texture must be reloaded. Textures that have\na source are automatically reloaded but generated textures must\nbe reloaded by the user.\n\nUse the :meth:`Texture.add_reload_observer` to add a reloading function that\nwill be automatically called when needed::\n\n    def __init__(self, **kwargs):\n        super(...).__init__(**kwargs)\n        self.texture = Texture.create(size=(512, 512), colorfmt=\'RGB\',\n            bufferfmt=\'ubyte\')\n        self.texture.add_reload_observer(self.populate_texture)\n\n        # and load the data now.\n        self.cbuffer = \'\\x00\\xf0\\xff\' * 512 * 512\n        self.populate_texture(self.texture)\n\n    def populate_texture(self, texture):\n        texture.blit_buffer(self.cbuffer)\n\nThis way, you can use the same method for initialization and reloading.\n\n.. note::\n\n    For all text rendering with our core text renderer, the texture is generated\n    but we already bind a method to redo the text rendering and reupload\n    the text to the texture. You don\'t have to do anything.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/texture.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.texture'
__package__ = 'kivy.graphics'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Texture():
    pass

def __pyx_unpickle_TextureRegion():
    pass

__test__ = _mod_builtins.dict()
environ = _mod_os._Environ()
platform = 'linux'
def texture_create():
    "Create a texture based on size.\n\n    :Parameters:\n        `size`: tuple, defaults to (128, 128)\n            Size of the texture.\n        `colorfmt`: str, defaults to 'rgba'\n            Color format of the texture. Can be 'rgba' or 'rgb',\n            'luminance' or 'luminance_alpha'. On desktop, additional values are\n            available: 'red', 'rg'.\n        `icolorfmt`: str, defaults to the value of `colorfmt`\n            Internal format storage of the texture. Can be 'rgba' or 'rgb',\n            'luminance' or 'luminance_alpha'. On desktop, additional values are\n            available: 'r8', 'rg8', 'rgba8'.\n        `bufferfmt`: str, defaults to 'ubyte'\n            Internal buffer format of the texture. Can be 'ubyte', 'ushort',\n            'uint', 'bute', 'short', 'int' or 'float'.\n        `mipmap`: bool, defaults to False\n            If True, it will automatically generate the mipmap texture.\n        `callback`: callable(), defaults to False\n            If a function is provided, it will be called when data is\n            needed in the texture.\n\n    .. versionchanged:: 1.7.0\n        :attr:`callback` has been added\n    "
    pass

def texture_create_from_data():
    'Create a texture from an ImageData class.\n    '
    pass

