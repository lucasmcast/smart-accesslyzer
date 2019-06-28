import builtins as _mod_builtins
import collections.abc as _mod_collections_abc
import logging as _mod_logging
import os as _mod_os

Logger = _mod_logging.Logger()
__builtins__ = {}
__doc__ = "\nCGL: standard C interface for OpenGL\n====================================\n\nKivy uses OpenGL and therefore requires a backend that provides it.\nThe backend used is controlled through the ``USE_OPENGL_MOCK`` and ``USE_SDL2``\ncompile-time variables and through the ``KIVY_GL_BACKEND`` runtime\nenvironmental variable.\n\nCurrently, OpenGL is used through direct linking (gl/glew), sdl2,\nor by mocking it. Setting ``USE_OPENGL_MOCK`` disables gl/glew.\nSimilarly, setting ``USE_SDL2`` to ``0`` will disable sdl2. Mocking\nis always available.\n\nAt runtime the following backends are available and can be set using\n``KIVY_GL_BACKEND``:\n\n* ``gl`` -- Available on unix (the default backend). Unavailable when\n  ``USE_OPENGL_MOCK=0``. Requires gl be installed.\n* ``glew`` -- Available on Windows (the default backend). Unavailable when\n  ``USE_OPENGL_MOCK=0``. Requires glew be installed.\n* ``sdl2`` -- Available on Windows/unix (the default when gl/glew is disabled).\n  Unavailable when ``USE_SDL2=0``. Requires ``kivy.deps.sdl2`` be installed.\n* ``angle_sdl2`` -- Available on Windows with Python 3.5+.\n  Unavailable when ``USE_SDL2=0``. Requires ``kivy.deps.sdl2`` and\n  ``kivy.deps.angle`` be installed.\n* ``mock`` -- Always available. Doesn't actually do anything.\n\n\nAdditionally, the following environmental runtime variables control the graphics\nsystem:\n\n* ``KIVY_GL_DEBUG`` -- Logs al gl calls when ``1``.\n* ``KIVY_GRAPHICS`` -- Forces OpenGL ES2 when it is ``gles``. OpenGL ES2 is always\n  used on the android, ios, rpi, and mali OSs.\n"
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/cgl.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.cgl'
__package__ = 'kivy.graphics'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def cgl_get_backend_name():
    pass

environ = _mod_os._Environ()
platform = 'linux'
