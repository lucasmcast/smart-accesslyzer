import builtins as _mod_builtins
import logging as _mod_logging

GLCAP_BGRA = 2
GLCAP_DXT1 = 4
GLCAP_ETC1 = 6
GLCAP_NPOT = 2
GLCAP_PVRTC = 5
GLCAP_S3TC = 3
GLCAP_UNPACK_SUBIMAGE = 7
Logger = _mod_logging.Logger()
_GL_GET_SIZE = _mod_builtins.dict()
__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nOpenGL utilities\n================\n\n.. versionadded:: 1.0.7\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/opengl_utils.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.opengl_utils'
__package__ = 'kivy.graphics'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def gl_get_extensions():
    "Return a list of OpenGL extensions available. All the names in the list\n    have the `GL_` stripped at the start (if it exists) and are in lowercase.\n\n    >>> print(gl_get_extensions())\n    ['arb_blend_func_extended', 'arb_color_buffer_float', 'arb_compatibility',\n     'arb_copy_buffer'... ]\n\n    "
    pass

def gl_get_texture_formats():
    'Return a list of texture formats recognized by kivy.\n    The texture list is informative but might not been supported by your\n    hardware. If you want a list of supported textures, you must filter that\n    list as follows::\n\n        supported_fmts = [gl_has_texture_format(x) for x in gl_get_texture_formats()]\n\n    '
    pass

def gl_get_version():
    'Return the (major, minor) OpenGL version, parsed from the GL_VERSION.\n\n    .. versionadded:: 1.2.0\n    '
    pass

def gl_get_version_major():
    'Return the major component of the OpenGL version.\n\n    .. versionadded:: 1.2.0\n    '
    pass

def gl_get_version_minor():
    'Return the minor component of the OpenGL version.\n\n    .. versionadded:: 1.2.0\n    '
    pass

def gl_has_capability():
    'Return the status of a OpenGL Capability. This is a wrapper that\n    auto-discovers all the capabilities that Kivy might need. The current\n    capabilities tested are:\n\n        - GLCAP_BGRA: Test the support of BGRA texture format\n        - GLCAP_NPOT: Test the support of Non Power of Two texture\n        - GLCAP_S3TC: Test the support of S3TC texture (DXT1, DXT3, DXT5)\n        - GLCAP_DXT1: Test the support of DXT texture (subset of S3TC)\n        - GLCAP_ETC1: Test the support of ETC1 texture\n\n    '
    pass

def gl_has_extension():
    "Check if an OpenGL extension is available. If the name starts with `GL_`,\n    it will be stripped for the test and converted to lowercase.\n\n        >>> gl_has_extension('NV_get_tex_image')\n        False\n        >>> gl_has_extension('OES_texture_npot')\n        True\n\n    "
    pass

def gl_has_texture_conversion():
    'Return 1 if the texture can be converted to a native format.\n    '
    pass

def gl_has_texture_format():
    "Return whether a texture format is supported by your system, natively or\n    by conversion. For example, if your card doesn't support 'bgra', we are able\n    to convert to 'rgba' but only in software mode.\n    "
    pass

def gl_has_texture_native_format():
    "Return 1 if the texture format is handled natively.\n\n    >>> gl_has_texture_format('azdmok')\n    0\n    >>> gl_has_texture_format('rgba')\n    1\n    >>> gl_has_texture_format('s3tc_dxt1')\n    [INFO   ] [GL          ] S3TC texture support is available\n    [INFO   ] [GL          ] DXT1 texture support is available\n    1\n\n    "
    pass

def gl_register_get_size():
    'Register an association between an OpenGL Const used in glGet* to a number\n    of elements.\n\n    By example, the GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX is a special pname that\n    will return the integer 1 (nvidia only).\n\n        >>> GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX = 0x9047\n        >>> gl_register_get_size(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX, 1)\n        >>> glGetIntegerv(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX)[0]\n        524288\n\n    '
    pass

platform = 'linux'
