import builtins as _mod_builtins

class LayoutLine(_mod_builtins.object):
    " Formally describes a line of text. A line of text is composed of many\n    :class:`LayoutWord` instances, each with it's own text, size and options.\n\n    A :class:`LayoutLine` instance does not always imply that the words\n    contained in the line ended with a newline. That is only the case if\n    :attr:`is_last_line` is True. For example a single real line of text can\n    be split across multiple :class:`LayoutLine` instances if the whole line\n    doesn't fit in the constrained width.\n\n    :Parameters:\n        `x`: int\n            the location in a texture from where the left side of this line is\n            began drawn.\n        `y`: int\n            the location in a texture from where the bottom of this line is\n            drawn.\n        `w`: int\n            the width of the line. This is the sum of the individual widths\n            of its :class:`LayoutWord` instances. Does not include any padding.\n        `h`: int\n            the height of the line. This is the maximum of the individual\n            heights of its :class:`LayoutWord` instances multiplied by the\n            `line_height` of these instance. So this is larger then the word\n            height.\n        `is_last_line`: bool\n            whether this line was the last line in a paragraph. When True, it\n            implies that the line was followed by a newline. Newlines should\n            not be included in the text of words, but is implicit by setting\n            this to True.\n        `line_wrap`: bool\n            whether this line is continued from a previous line which didn't\n            fit into a constrained width and was therefore split across\n            multiple :class:`LayoutLine` instances. `line_wrap` can be True\n            or False independently of `is_last_line`.\n        `words`: python list\n            a list that contains only :class:`LayoutWord` instances describing\n            the text of the line.\n\n    "
    __class__ = LayoutLine
    def __init__(self, *args, **kwargs):
        " Formally describes a line of text. A line of text is composed of many\n    :class:`LayoutWord` instances, each with it's own text, size and options.\n\n    A :class:`LayoutLine` instance does not always imply that the words\n    contained in the line ended with a newline. That is only the case if\n    :attr:`is_last_line` is True. For example a single real line of text can\n    be split across multiple :class:`LayoutLine` instances if the whole line\n    doesn't fit in the constrained width.\n\n    :Parameters:\n        `x`: int\n            the location in a texture from where the left side of this line is\n            began drawn.\n        `y`: int\n            the location in a texture from where the bottom of this line is\n            drawn.\n        `w`: int\n            the width of the line. This is the sum of the individual widths\n            of its :class:`LayoutWord` instances. Does not include any padding.\n        `h`: int\n            the height of the line. This is the maximum of the individual\n            heights of its :class:`LayoutWord` instances multiplied by the\n            `line_height` of these instance. So this is larger then the word\n            height.\n        `is_last_line`: bool\n            whether this line was the last line in a paragraph. When True, it\n            implies that the line was followed by a newline. Newlines should\n            not be included in the text of words, but is implicit by setting\n            this to True.\n        `line_wrap`: bool\n            whether this line is continued from a previous line which didn't\n            fit into a constrained width and was therefore split across\n            multiple :class:`LayoutLine` instances. `line_wrap` can be True\n            or False independently of `is_last_line`.\n        `words`: python list\n            a list that contains only :class:`LayoutWord` instances describing\n            the text of the line.\n\n    "
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
    def h(self):
        pass
    
    @property
    def is_last_line(self):
        pass
    
    @property
    def line_wrap(self):
        pass
    
    @property
    def w(self):
        pass
    
    @property
    def words(self):
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    

class LayoutWord(_mod_builtins.object):
    'Formally describes a word contained in a line. The name word simply\n    means a chunk of text and can be used to describe any text.\n\n    A word has some width, height and is rendered according to options saved\n    in :attr:`options`. See :class:`LayoutLine` for its usage.\n\n    :Parameters:\n        `options`: dict\n            the label options dictionary for this word.\n        `lw`: int\n            the width of the text in pixels.\n        `lh`: int\n            the height of the text in pixels.\n        `text`: string\n            the text of the word.\n    '
    __class__ = LayoutWord
    def __init__(self, *args, **kwargs):
        'Formally describes a word contained in a line. The name word simply\n    means a chunk of text and can be used to describe any text.\n\n    A word has some width, height and is rendered according to options saved\n    in :attr:`options`. See :class:`LayoutLine` for its usage.\n\n    :Parameters:\n        `options`: dict\n            the label options dictionary for this word.\n        `lw`: int\n            the width of the text in pixels.\n        `lh`: int\n            the height of the text in pixels.\n        `text`: string\n            the text of the word.\n    '
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
    def lh(self):
        pass
    
    @property
    def lw(self):
        pass
    
    @property
    def options(self):
        pass
    
    @property
    def text(self):
        pass
    

__all__ = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\nText layout\n============\n\nAn internal module for laying out text according to options and constraints.\nThis is not part of the API and may change at any time.\n'
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/kivy/core/text/text_layout.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'kivy.core.text.text_layout'
__package__ = 'kivy.core.text'
__test__ = _mod_builtins.dict()
def layout_text():
    " Lays out text into a series of :class:`LayoutWord` and\n    :class:`LayoutLine` instances according to the options specified.\n\n    The function is designed to be called many times, each time new text is\n    appended to the last line (or first line if appending upwards), unless a\n    newline is present in the text. Each text appended is described by it's own\n    options which can change between successive calls. If the text is\n    constrained, we stop as soon as the constraint is reached.\n\n    :Parameters:\n        `text`: string or bytes\n            the text to be broken down into lines. If lines is not empty,\n            the text is added to the last line (or first line if `append_down`\n            is False) until a newline is reached which creates a new line in\n            `lines`. See :class:`LayoutLine`.\n        `lines`: list\n            a list of :class:`LayoutLine` instances, each describing a line of\n            the text. Calls to :func:`layout_text` append or create\n            new :class:`LayoutLine` instances in `lines`.\n        `size`: 2-tuple of ints\n            the size of the laid out text so far. Upon first call it should\n            probably be (0, 0), afterwards it should be the (w, h) returned\n            by this function in a previous call. When size reaches the\n            constraining size, `text_size`, we stop adding lines and return\n            True for the clipped parameter. size includes the x and y padding.\n        `text_size`: 2-tuple of ints or None.\n            the size constraint on the laid out text. If either element is\n            None, the text is not constrained in that dimension. For example,\n            (None, 200) will constrain the height, including padding to 200,\n            while the width is unconstrained. The first line, and the first\n            character of a line is always returned, even if it exceeds the\n            constraint. The value be changed between different calls.\n        `options`: dict\n            the label options of this `text`. The options are saved with each\n            word allowing different words to have different options from\n            successive calls.\n\n            Note, `options` must include a `space_width` key with a value\n            indicating the width of a space for that set of options.\n        `get_extents`: callable\n            a function called with a string, which returns a tuple containing\n            the width, height of the string.\n        `append_down`: bool\n            Whether successive calls to the function appends lines before or\n            after the existing lines. If True, they are appended to the last\n            line and below it. If False, it's appended at the first line and\n            above. For example, if False, everything after the last\n            newline in `text` is appended to the first line in lines.\n            Everything before the last newline is inserted at the start of\n            lines in same order as text; that is we do not invert the line\n            order.\n\n            This allows laying out from top to bottom until the constrained is\n            reached, or from bottom to top until the constrained is reached.\n        `complete`: bool\n            whether this text complete lines. It use is that normally is\n            strip in `options` is True, all leading and trailing spaces\n            are removed from each line except from the last line (or first\n            line if `append_down` is False) which only removes leading spaces.\n            That's because further text can still be appended to the last line\n            so we cannot strip them. If `complete` is True, it indicates no\n            further text is coming and all lines will be stripped.\n\n            The function can also be called with `text` set to the empty string\n            and `complete` set to True in order for the last (first) line to\n            be stripped.\n\n    :returns:\n        3-tuple, (w, h, clipped).\n        w and h is the width and height of the text in lines so far and\n        includes padding. This can be larger than `text_size`, e.g. if not even\n        a single fitted, the first line would still be returned.\n        `clipped` is True if not all the text has been added to lines because\n        w, h reached the constrained size.\n\n    Following is a simple example with no padding and no stripping::\n\n        >>> from kivy.core.text import Label\n        >>> from kivy.core.text.text_layout import layout_text\n\n        >>> l = Label()\n        >>> lines = []\n        >>> # layout text with width constraint by 50, but no height constraint\n        >>> w, h, clipped = layout_text('heres some text\\nah, another line',\n        ... lines, (0, 0), (50, None), l.options, l.get_cached_extents(), True,\n        ... False)\n        >>> w, h, clipped\n        (46, 90, False)\n        # now add text from bottom up, and constrain width only be 100\n        >>> w, h, clipped = layout_text('\\nyay, more text\\n', lines, (w, h),\n        ... (100, None), l.options, l.get_cached_extents(), False, True)\n        >>> w, h, clipped\n        (77, 120, 0)\n        >>> for line in lines:\n        ...     print('line w: {}, line h: {}'.format(line.w, line.h))\n        ...     for word in line.words:\n        ...         print('w: {}, h: {}, text: {}'.format(word.lw, word.lh,\n        ...         [word.text]))\n        line w: 0, line h: 15\n        line w: 77, line h: 15\n        w: 77, h: 15, text: ['yay, more text']\n        line w: 31, line h: 15\n        w: 31, h: 15, text: ['heres']\n        line w: 34, line h: 15\n        w: 34, h: 15, text: [' some']\n        line w: 24, line h: 15\n        w: 24, h: 15, text: [' text']\n        line w: 17, line h: 15\n        w: 17, h: 15, text: ['ah,']\n        line w: 46, line h: 15\n        w: 46, h: 15, text: [' another']\n        line w: 23, line h: 15\n        w: 23, h: 15, text: [' line']\n    "
    pass

