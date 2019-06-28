import builtins as _mod_builtins
import logging as _mod_logging

GL_ACTIVE_ATTRIBUTES = 35721
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722
GL_ACTIVE_TEXTURE = 34016
GL_ACTIVE_UNIFORMS = 35718
GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719
GL_ALIASED_LINE_WIDTH_RANGE = 33902
GL_ALIASED_POINT_SIZE_RANGE = 33901
GL_ALPHA = 6406
GL_ALPHA_BITS = 3413
GL_ALWAYS = 519
GL_ARRAY_BUFFER = 34962
GL_ARRAY_BUFFER_BINDING = 34964
GL_ATTACHED_SHADERS = 35717
GL_BACK = 1029
GL_BLEND = 3042
GL_BLEND_COLOR = 32773
GL_BLEND_DST_ALPHA = 32970
GL_BLEND_DST_RGB = 32968
GL_BLEND_EQUATION = 32777
GL_BLEND_EQUATION_ALPHA = 34877
GL_BLEND_EQUATION_RGB = 32777
GL_BLEND_SRC_ALPHA = 32971
GL_BLEND_SRC_RGB = 32969
GL_BLUE_BITS = 3412
GL_BOOL = 35670
GL_BOOL_VEC2 = 35671
GL_BOOL_VEC3 = 35672
GL_BOOL_VEC4 = 35673
GL_BUFFER_SIZE = 34660
GL_BUFFER_USAGE = 34661
GL_BYTE = 5120
GL_CCW = 2305
GL_CLAMP_TO_EDGE = 33071
GL_COLOR_ATTACHMENT0 = 36064
GL_COLOR_BUFFER_BIT = 16384
GL_COLOR_CLEAR_VALUE = 3106
GL_COLOR_WRITEMASK = 3107
GL_COMPILE_STATUS = 35713
GL_COMPRESSED_TEXTURE_FORMATS = 34467
GL_CULL_FACE = 2884
GL_CULL_FACE_MODE = 2885
GL_CURRENT_PROGRAM = 35725
GL_CURRENT_VERTEX_ATTRIB = 34342
GL_CW = 2304
GL_DECR = 7683
GL_DECR_WRAP = 34056
GL_DELETE_STATUS = 35712
GL_DEPTH_ATTACHMENT = 36096
GL_DEPTH_BITS = 3414
GL_DEPTH_BUFFER_BIT = 256
GL_DEPTH_CLEAR_VALUE = 2931
GL_DEPTH_COMPONENT = 6402
GL_DEPTH_COMPONENT16 = 33189
GL_DEPTH_FUNC = 2932
GL_DEPTH_RANGE = 2928
GL_DEPTH_TEST = 2929
GL_DEPTH_WRITEMASK = 2930
GL_DITHER = 3024
GL_DONT_CARE = 4352
GL_DST_ALPHA = 772
GL_DST_COLOR = 774
GL_DYNAMIC_DRAW = 35048
GL_ELEMENT_ARRAY_BUFFER = 34963
GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965
GL_EQUAL = 514
GL_EXTENSIONS = 7939
GL_FALSE = 0
GL_FASTEST = 4353
GL_FLOAT = 5126
GL_FLOAT_MAT2 = 35674
GL_FLOAT_MAT3 = 35675
GL_FLOAT_MAT4 = 35676
GL_FLOAT_VEC2 = 35664
GL_FLOAT_VEC3 = 35665
GL_FLOAT_VEC4 = 35666
GL_FRAGMENT_SHADER = 35632
GL_FRAMEBUFFER = 36160
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050
GL_FRAMEBUFFER_BINDING = 36006
GL_FRAMEBUFFER_COMPLETE = 36053
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 36057
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055
GL_FRAMEBUFFER_UNSUPPORTED = 36061
GL_FRONT = 1028
GL_FRONT_AND_BACK = 1032
GL_FRONT_FACE = 2886
GL_FUNC_ADD = 32774
GL_FUNC_REVERSE_SUBTRACT = 32779
GL_FUNC_SUBTRACT = 32778
GL_GENERATE_MIPMAP_HINT = 33170
GL_GEQUAL = 518
GL_GREATER = 516
GL_GREEN_BITS = 3411
GL_INCR = 7682
GL_INCR_WRAP = 34055
GL_INFO_LOG_LENGTH = 35716
GL_INT = 5124
GL_INT_VEC2 = 35667
GL_INT_VEC3 = 35668
GL_INT_VEC4 = 35669
GL_INVALID_ENUM = 1280
GL_INVALID_FRAMEBUFFER_OPERATION = 1286
GL_INVALID_OPERATION = 1282
GL_INVALID_VALUE = 1281
GL_INVERT = 5386
GL_KEEP = 7680
GL_LEQUAL = 515
GL_LESS = 513
GL_LINEAR = 9729
GL_LINEAR_MIPMAP_LINEAR = 9987
GL_LINEAR_MIPMAP_NEAREST = 9985
GL_LINES = 1
GL_LINE_LOOP = 2
GL_LINE_STRIP = 3
GL_LINE_WIDTH = 2849
GL_LINK_STATUS = 35714
GL_LUMINANCE = 6409
GL_LUMINANCE_ALPHA = 6410
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076
GL_MAX_RENDERBUFFER_SIZE = 34024
GL_MAX_TEXTURE_IMAGE_UNITS = 34930
GL_MAX_TEXTURE_SIZE = 3379
GL_MAX_VERTEX_ATTRIBS = 34921
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660
GL_MAX_VIEWPORT_DIMS = 3386
GL_MIRRORED_REPEAT = 33648
GL_NEAREST = 9728
GL_NEAREST_MIPMAP_LINEAR = 9986
GL_NEAREST_MIPMAP_NEAREST = 9984
GL_NEVER = 512
GL_NICEST = 4354
GL_NONE = 0
GL_NOTEQUAL = 517
GL_NO_ERROR = 0
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466
GL_ONE = 1
GL_ONE_MINUS_DST_ALPHA = 773
GL_ONE_MINUS_DST_COLOR = 775
GL_ONE_MINUS_SRC_ALPHA = 771
GL_ONE_MINUS_SRC_COLOR = 769
GL_OUT_OF_MEMORY = 1285
GL_PACK_ALIGNMENT = 3333
GL_POINTS = 0
GL_POLYGON_OFFSET_FACTOR = 32824
GL_POLYGON_OFFSET_FILL = 32823
GL_POLYGON_OFFSET_UNITS = 10752
GL_RED_BITS = 3410
GL_RENDERBUFFER = 36161
GL_RENDERBUFFER_ALPHA_SIZE = 36179
GL_RENDERBUFFER_BINDING = 36007
GL_RENDERBUFFER_BLUE_SIZE = 36178
GL_RENDERBUFFER_DEPTH_SIZE = 36180
GL_RENDERBUFFER_GREEN_SIZE = 36177
GL_RENDERBUFFER_HEIGHT = 36163
GL_RENDERBUFFER_INTERNAL_FORMAT = 36164
GL_RENDERBUFFER_RED_SIZE = 36176
GL_RENDERBUFFER_STENCIL_SIZE = 36181
GL_RENDERBUFFER_WIDTH = 36162
GL_RENDERER = 7937
GL_REPEAT = 10497
GL_REPLACE = 7681
GL_RGB = 6407
GL_RGB565 = 36194
GL_RGB5_A1 = 32855
GL_RGBA = 6408
GL_RGBA4 = 32854
GL_SAMPLER_2D = 35678
GL_SAMPLER_CUBE = 35680
GL_SAMPLES = 32937
GL_SAMPLE_ALPHA_TO_COVERAGE = 32926
GL_SAMPLE_BUFFERS = 32936
GL_SAMPLE_COVERAGE = 32928
GL_SAMPLE_COVERAGE_INVERT = 32939
GL_SAMPLE_COVERAGE_VALUE = 32938
GL_SCISSOR_BOX = 3088
GL_SCISSOR_TEST = 3089
GL_SHADER_BINARY_FORMATS = 36344
GL_SHADER_SOURCE_LENGTH = 35720
GL_SHADER_TYPE = 35663
GL_SHADING_LANGUAGE_VERSION = 35724
GL_SHORT = 5122
GL_SRC_ALPHA = 770
GL_SRC_ALPHA_SATURATE = 776
GL_SRC_COLOR = 768
GL_STATIC_DRAW = 35044
GL_STENCIL_ATTACHMENT = 36128
GL_STENCIL_BACK_FAIL = 34817
GL_STENCIL_BACK_FUNC = 34816
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818
GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819
GL_STENCIL_BACK_REF = 36003
GL_STENCIL_BACK_VALUE_MASK = 36004
GL_STENCIL_BACK_WRITEMASK = 36005
GL_STENCIL_BITS = 3415
GL_STENCIL_BUFFER_BIT = 1024
GL_STENCIL_CLEAR_VALUE = 2961
GL_STENCIL_FAIL = 2964
GL_STENCIL_FUNC = 2962
GL_STENCIL_INDEX8 = 36168
GL_STENCIL_PASS_DEPTH_FAIL = 2965
GL_STENCIL_PASS_DEPTH_PASS = 2966
GL_STENCIL_REF = 2967
GL_STENCIL_TEST = 2960
GL_STENCIL_VALUE_MASK = 2963
GL_STENCIL_WRITEMASK = 2968
GL_STREAM_DRAW = 35040
GL_SUBPIXEL_BITS = 3408
GL_TEXTURE = 5890
GL_TEXTURE0 = 33984
GL_TEXTURE1 = 33985
GL_TEXTURE10 = 33994
GL_TEXTURE11 = 33995
GL_TEXTURE12 = 33996
GL_TEXTURE13 = 33997
GL_TEXTURE14 = 33998
GL_TEXTURE15 = 33999
GL_TEXTURE16 = 34000
GL_TEXTURE17 = 34001
GL_TEXTURE18 = 34002
GL_TEXTURE19 = 34003
GL_TEXTURE2 = 33986
GL_TEXTURE20 = 34004
GL_TEXTURE21 = 34005
GL_TEXTURE22 = 34006
GL_TEXTURE23 = 34007
GL_TEXTURE24 = 34008
GL_TEXTURE25 = 34009
GL_TEXTURE26 = 34010
GL_TEXTURE27 = 34011
GL_TEXTURE28 = 34012
GL_TEXTURE29 = 34013
GL_TEXTURE3 = 33987
GL_TEXTURE30 = 34014
GL_TEXTURE31 = 34015
GL_TEXTURE4 = 33988
GL_TEXTURE5 = 33989
GL_TEXTURE6 = 33990
GL_TEXTURE7 = 33991
GL_TEXTURE8 = 33992
GL_TEXTURE9 = 33993
GL_TEXTURE_2D = 3553
GL_TEXTURE_BINDING_2D = 32873
GL_TEXTURE_BINDING_CUBE_MAP = 34068
GL_TEXTURE_CUBE_MAP = 34067
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073
GL_TEXTURE_MAG_FILTER = 10240
GL_TEXTURE_MIN_FILTER = 10241
GL_TEXTURE_WRAP_S = 10242
GL_TEXTURE_WRAP_T = 10243
GL_TRIANGLES = 4
GL_TRIANGLE_FAN = 6
GL_TRIANGLE_STRIP = 5
GL_TRUE = 1
GL_UNPACK_ALIGNMENT = 3317
GL_UNSIGNED_BYTE = 5121
GL_UNSIGNED_INT = 5125
GL_UNSIGNED_SHORT = 5123
GL_UNSIGNED_SHORT_4_4_4_4 = 32819
GL_UNSIGNED_SHORT_5_5_5_1 = 32820
GL_UNSIGNED_SHORT_5_6_5 = 33635
GL_VALIDATE_STATUS = 35715
GL_VENDOR = 7936
GL_VERSION = 7938
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373
GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340
GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341
GL_VERTEX_SHADER = 35633
GL_VIEWPORT = 2978
GL_ZERO = 0
Logger = _mod_logging.Logger()
_GL_GET_SIZE = _mod_builtins.dict()
__builtins__ = {}
__doc__ = '\nOpenGL\n======\n\nThis module is a Python wrapper for OpenGL commands.\n\n.. warning::\n\n    Not every OpenGL command has been wrapped and because we are using the C\n    binding for higher performance, and you should rather stick to the Kivy\n    Graphics API. By using OpenGL commands directly, you might change\n    the OpenGL context and introduce inconsistency between the Kivy state and\n    the OpenGL state.\n\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/graphics/opengl.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.graphics.opengl'
__package__ = 'kivy.graphics'
__test__ = _mod_builtins.dict()
def glActiveTexture():
    'See: `glActiveTexture() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glActiveTexture.xml>`_\n    '
    pass

def glAttachShader():
    'See: `glAttachShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glAttachShader.xml>`_\n    '
    pass

def glBindAttribLocation():
    'See: `glBindAttribLocation() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindAttribLocation.xml>`_\n    '
    pass

def glBindBuffer():
    'See: `glBindBuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindBuffer.xml>`_\n    '
    pass

def glBindFramebuffer():
    'See: `glBindFramebuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindFramebuffer.xml>`_\n    '
    pass

def glBindRenderbuffer():
    'See: `glBindRenderbuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindRenderbuffer.xml>`_\n    '
    pass

def glBindTexture():
    'See: `glBindTexture() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindTexture.xml>`_\n    '
    pass

def glBlendColor():
    'See: `glBlendColor() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendColor.xml>`_\n    '
    pass

def glBlendEquation():
    'See: `glBlendEquation() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendEquation.xml>`_\n    '
    pass

def glBlendEquationSeparate():
    'See: `glBlendEquationSeparate() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendEquationSeparate.xml>`_\n    '
    pass

def glBlendFunc():
    'See: `glBlendFunc() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendFunc.xml>`_\n    '
    pass

def glBlendFuncSeparate():
    'See: `glBlendFuncSeparate() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendFuncSeparate.xml>`_\n    '
    pass

def glBufferData():
    'See: `glBufferData() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBufferData.xml>`_\n    '
    pass

def glBufferSubData():
    'See: `glBufferSubData() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBufferSubData.xml>`_\n    '
    pass

def glCheckFramebufferStatus():
    'See: `glCheckFramebufferStatus() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCheckFramebufferStatus.xml>`_\n    '
    pass

def glClear():
    'See: `glClear() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClear.xml>`_\n    '
    pass

def glClearColor():
    'See: `glClearColor() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClearColor.xml>`_\n    '
    pass

def glClearStencil():
    'See: `glClearStencil() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClearStencil.xml>`_\n    '
    pass

def glColorMask():
    'See: `glColorMask() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glColorMask.xml>`_\n    '
    pass

def glCompileShader():
    'See: `glCompileShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompileShader.xml>`_\n    '
    pass

def glCompressedTexImage2D():
    'See: `glCompressedTexImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompressedTexImage2D.xml>`_\n    '
    pass

def glCompressedTexSubImage2D():
    'See: `glCompressedTexSubImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompressedTexSubImage2D.xml>`_\n    '
    pass

def glCopyTexImage2D():
    'See: `glCopyTexImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCopyTexImage2D.xml>`_\n    '
    pass

def glCopyTexSubImage2D():
    'See: `glCopyTexSubImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCopyTexSubImage2D.xml>`_\n    '
    pass

def glCreateProgram():
    'See: `glCreateProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCreateProgram.xml>`_\n    '
    pass

def glCreateShader():
    'See: `glCreateShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCreateShader.xml>`_\n    '
    pass

def glCullFace():
    'See: `glCullFace() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCullFace.xml>`_\n    '
    pass

def glDeleteBuffers():
    'See: `glDeleteBuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteBuffers.xml>`_\n    '
    pass

def glDeleteFramebuffers():
    'See: `glDeleteFramebuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteFramebuffers.xml>`_\n    '
    pass

def glDeleteProgram():
    'See: `glDeleteProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteProgram.xml>`_\n    '
    pass

def glDeleteRenderbuffers():
    'See: `glDeleteRenderbuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteRenderbuffers.xml>`_\n    '
    pass

def glDeleteShader():
    'See: `glDeleteShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteShader.xml>`_\n    '
    pass

def glDeleteTextures():
    'See: `glDeleteTextures() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteTextures.xml>`_\n    '
    pass

def glDepthFunc():
    'See: `glDepthFunc() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDepthFunc.xml>`_\n    '
    pass

def glDepthMask():
    'See: `glDepthMask() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDepthMask.xml>`_\n    '
    pass

def glDetachShader():
    'See: `glDetachShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDetachShader.xml>`_\n    '
    pass

def glDisable():
    'See: `glDisable() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDisable.xml>`_\n    '
    pass

def glDisableVertexAttribArray():
    'See: `glDisableVertexAttribArray() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDisableVertexAttribArray.xml>`_\n    '
    pass

def glDrawArrays():
    'See: `glDrawArrays() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDrawArrays.xml>`_\n    '
    pass

def glDrawElements():
    'See: `glDrawElements() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDrawElements.xml>`_\n    '
    pass

def glEnable():
    'See: `glEnable() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glEnable.xml>`_\n    '
    pass

def glEnableVertexAttribArray():
    'See: `glEnableVertexAttribArray() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glEnableVertexAttribArray.xml>`_\n    '
    pass

def glFinish():
    'See: `glFinish() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFinish.xml>`_\n    '
    pass

def glFlush():
    'See: `glFlush() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFlush.xml>`_\n    '
    pass

def glFramebufferRenderbuffer():
    'See: `glFramebufferRenderbuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFramebufferRenderbuffer.xml>`_\n    '
    pass

def glFramebufferTexture2D():
    'See: `glFramebufferTexture2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFramebufferTexture2D.xml>`_\n    '
    pass

def glFrontFace():
    'See: `glFrontFace() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFrontFace.xml>`_\n    '
    pass

def glGenBuffers():
    'See: `glGenBuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenBuffers.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGenFramebuffers():
    'See: `glGenFramebuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenFramebuffers.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGenRenderbuffers():
    'See: `glGenRenderbuffers() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenRenderbuffers.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGenTextures():
    'See: `glGenTextures() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenTextures.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGenerateMipmap():
    'See: `glGenerateMipmap() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenerateMipmap.xml>`_\n    '
    pass

def glGetActiveAttrib():
    'See: `glGetActiveAttrib() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetActiveAttrib.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetActiveUniform():
    'See: `glGetActiveUniform() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetActiveUniform.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetAttachedShaders():
    'See: `glGetAttachedShaders() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetAttachedShaders.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetAttribLocation():
    'See: `glGetAttribLocation() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetAttribLocation.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetBooleanv():
    'See: `glGetBooleanv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetBooleanv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetBufferParameteriv():
    'See: `glGetBufferParameteriv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetBufferParameteriv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetError():
    'See: `glGetError() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetError.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetFloatv():
    'See: `glGetFloatv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetFloatv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetFramebufferAttachmentParameteriv():
    'See: `glGetFramebufferAttachmentParameteriv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetFramebufferAttachmentParameteriv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetIntegerv():
    'See: `glGetIntegerv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetIntegerv.xml>`_\n\n    Unlike the C specification, the value(s) will be the result of the call\n    '
    pass

def glGetProgramInfoLog():
    'See: `glGetProgramInfoLog() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetProgramInfoLog.xml>`_\n\n    Unlike the C specification, the source code will be returned as a string.\n    '
    pass

def glGetProgramiv():
    'See: `glGetProgramiv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetProgramiv.xml>`_\n\n    Unlike the C specification, the value(s) will be the result of the call\n    '
    pass

def glGetRenderbufferParameteriv():
    'See: `glGetRenderbufferParameteriv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetRenderbufferParameteriv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetShaderInfoLog():
    'See: `glGetShaderInfoLog() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderInfoLog.xml>`_\n\n    Unlike the C specification, the source code will be returned as a string.\n    '
    pass

def glGetShaderPrecisionFormat():
    'See: `glGetShaderPrecisionFormat() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderPrecisionFormat.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glGetShaderSource():
    'See: `glGetShaderSource() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderSource.xml>`_\n\n    Unlike the C specification, the source code will be returned as a string.\n    '
    pass

def glGetShaderiv():
    'See: `glGetShaderiv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderiv.xml>`_\n\n    Unlike the C specification, the value will be the result of call.\n    '
    pass

def glGetString():
    'See: `glGetString() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetString.xml>`_\n\n    Unlike the C specification, the value will be returned as a string.\n    '
    pass

def glGetTexParameterfv():
    'See: `glGetTexParameterfv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetTexParameterfv.xml>`_\n    '
    pass

def glGetTexParameteriv():
    'See: `glGetTexParameteriv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetTexParameteriv.xml>`_\n    '
    pass

def glGetUniformLocation():
    'See: `glGetUniformLocation() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformLocation.xml>`_\n    '
    pass

def glGetUniformfv():
    'See: `glGetUniformfv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformfv.xml>`_\n    '
    pass

def glGetUniformiv():
    'See: `glGetUniformiv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformiv.xml>`_\n    '
    pass

def glGetVertexAttribPointerv():
    'See: `glGetVertexAttribPointerv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribPointerv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glGetVertexAttribfv():
    'See: `glGetVertexAttribfv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribfv.xml>`_\n    '
    pass

def glGetVertexAttribiv():
    'See: `glGetVertexAttribiv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribiv.xml>`_\n    '
    pass

def glHint():
    'See: `glHint() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glHint.xml>`_\n    '
    pass

def glIsBuffer():
    'See: `glIsBuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsBuffer.xml>`_\n    '
    pass

def glIsEnabled():
    'See: `glIsEnabled() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsEnabled.xml>`_\n    '
    pass

def glIsFramebuffer():
    'See: `glIsFramebuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsFramebuffer.xml>`_\n    '
    pass

def glIsProgram():
    'See: `glIsProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsProgram.xml>`_\n    '
    pass

def glIsRenderbuffer():
    'See: `glIsRenderbuffer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsRenderbuffer.xml>`_\n    '
    pass

def glIsShader():
    'See: `glIsShader() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsShader.xml>`_\n    '
    pass

def glIsTexture():
    'See: `glIsTexture() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsTexture.xml>`_\n    '
    pass

def glLineWidth():
    'See: `glLineWidth() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glLineWidth.xml>`_\n    '
    pass

def glLinkProgram():
    'See: `glLinkProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glLinkProgram.xml>`_\n    '
    pass

def glPixelStorei():
    'See: `glPixelStorei() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPixelStorei.xml>`_\n    '
    pass

def glPolygonOffset():
    'See: `glPolygonOffset() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPolygonOffset.xml>`_\n    '
    pass

def glReadPixels():
    'See: `glReadPixels() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glReadPixels.xml>`_\n\n    We support only GL_RGB/GL_RGBA as a format and GL_UNSIGNED_BYTE as a\n    type.\n    '
    pass

def glReleaseShaderCompiler():
    'See: `glReleaseShaderCompiler() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glReleaseShaderCompiler.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glRenderbufferStorage():
    'See: `glRenderbufferStorage() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glRenderbufferStorage.xml>`_\n    '
    pass

def glSampleCoverage():
    'See: `glSampleCoverage() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glSampleCoverage.xml>`_\n    '
    pass

def glScissor():
    'See: `glScissor() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glScissor.xml>`_\n    '
    pass

def glShaderBinary():
    'See: `glShaderBinary() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glShaderBinary.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glShaderSource():
    'See: `glShaderSource() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glShaderSource.xml>`_\n    '
    pass

def glStencilFunc():
    'See: `glStencilFunc() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilFunc.xml>`_\n    '
    pass

def glStencilFuncSeparate():
    'See: `glStencilFuncSeparate() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilFuncSeparate.xml>`_\n    '
    pass

def glStencilMask():
    'See: `glStencilMask() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilMask.xml>`_\n    '
    pass

def glStencilMaskSeparate():
    'See: `glStencilMaskSeparate() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilMaskSeparate.xml>`_\n    '
    pass

def glStencilOp():
    'See: `glStencilOp() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilOp.xml>`_\n    '
    pass

def glStencilOpSeparate():
    'See: `glStencilOpSeparate() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilOpSeparate.xml>`_\n    '
    pass

def glTexImage2D():
    'See: `glTexImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexImage2D.xml>`_\n    '
    pass

def glTexParameterf():
    'See: `glTexParameterf() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameterf.xml>`_\n    '
    pass

def glTexParameterfv():
    'See: `glTexParameterfv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameterfv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glTexParameteri():
    'See: `glTexParameteri() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameteri.xml>`_\n    '
    pass

def glTexParameteriv():
    'See: `glTexParameteriv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameteriv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glTexSubImage2D():
    'See: `glTexSubImage2D() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexSubImage2D.xml>`_\n    '
    pass

def glUniform1f():
    'See: `glUniform1f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1f.xml>`_\n    '
    pass

def glUniform1fv():
    'See: `glUniform1fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform1i():
    'See: `glUniform1i() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1i.xml>`_\n    '
    pass

def glUniform1iv():
    'See: `glUniform1iv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1iv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform2f():
    'See: `glUniform2f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2f.xml>`_\n    '
    pass

def glUniform2fv():
    'See: `glUniform2fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform2i():
    'See: `glUniform2i() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2i.xml>`_\n    '
    pass

def glUniform2iv():
    'See: `glUniform2iv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2iv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform3f():
    'See: `glUniform3f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3f.xml>`_\n    '
    pass

def glUniform3fv():
    'See: `glUniform3fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform3i():
    'See: `glUniform3i() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3i.xml>`_\n    '
    pass

def glUniform3iv():
    'See: `glUniform3iv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3iv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform4f():
    'See: `glUniform4f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4f.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform4fv():
    'See: `glUniform4fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniform4i():
    'See: `glUniform4i() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4i.xml>`_\n    '
    pass

def glUniform4iv():
    'See: `glUniform4iv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4iv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniformMatrix2fv():
    'See: `glUniformMatrix2fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix2fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniformMatrix3fv():
    'See: `glUniformMatrix3fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix3fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glUniformMatrix4fv():
    'See: `glUniformMatrix4fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix4fv.xml>`_\n    '
    pass

def glUseProgram():
    'See: `glUseProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUseProgram.xml>`_\n    '
    pass

def glValidateProgram():
    'See: `glValidateProgram() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glValidateProgram.xml>`_\n    '
    pass

def glVertexAttrib1f():
    'See: `glVertexAttrib1f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib1f.xml>`_\n    '
    pass

def glVertexAttrib1fv():
    'See: `glVertexAttrib1fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib1fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glVertexAttrib2f():
    'See: `glVertexAttrib2f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib2f.xml>`_\n    '
    pass

def glVertexAttrib2fv():
    'See: `glVertexAttrib2fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib2fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glVertexAttrib3f():
    'See: `glVertexAttrib3f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib3f.xml>`_\n    '
    pass

def glVertexAttrib3fv():
    'See: `glVertexAttrib3fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib3fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glVertexAttrib4f():
    'See: `glVertexAttrib4f() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib4f.xml>`_\n    '
    pass

def glVertexAttrib4fv():
    'See: `glVertexAttrib4fv() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib4fv.xml>`_\n\n    .. warning:: Not implemented yet.\n    '
    pass

def glVertexAttribPointer():
    'See: `glVertexAttribPointer() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttribPointer.xml>`_\n\n    '
    pass

def glViewport():
    'See: `glViewport() on Kronos website\n    <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glViewport.xml>`_\n    '
    pass

def gl_init_symbols():
    pass

