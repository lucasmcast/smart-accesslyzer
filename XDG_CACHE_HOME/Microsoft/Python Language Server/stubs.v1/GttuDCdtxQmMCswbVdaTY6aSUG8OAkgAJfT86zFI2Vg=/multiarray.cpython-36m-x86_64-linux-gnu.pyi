import builtins as _mod_builtins

ALLOW_THREADS = 1
BUFSIZE = 8192
CLIP = 0
DATETIMEUNITS = _mod_builtins.PyCapsule()
ITEM_HASOBJECT = 1
ITEM_IS_POINTER = 4
LIST_PICKLE = 2
MAXDIMS = 32
MAY_SHARE_BOUNDS = 0
MAY_SHARE_EXACT = -1
NEEDS_INIT = 8
NEEDS_PYAPI = 16
RAISE = 2
USE_GETITEM = 32
USE_SETITEM = 64
WRAP = 1
_ARRAY_API = _mod_builtins.PyCapsule()
__doc__ = None
__file__ = '/home/lucas/anaconda3/envs/curso_dlib/lib/python3.6/site-packages/numpy/core/multiarray.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'numpy.core.multiarray'
__package__ = 'numpy.core'
__version__ = '3.1'
def _fastCopyAndTranspose(a):
    '_fastCopyAndTranspose(a)'
    pass

_flagdict = _mod_builtins.dict()
def _get_ndarray_c_version():
    '_get_ndarray_c_version()\n\n    Return the compile time NDARRAY_VERSION number.'
    pass

def _insert():
    'Insert vals sequentially into equivalent 1-d positions indicated by mask.'
    pass

def _reconstruct(subtype, shape, dtype):
    '_reconstruct(subtype, shape, dtype)\n\n    Construct an empty array. Used by Pickles.'
    pass

def _vec_string():
    pass

def add_docstring(obj, docstring):
    'add_docstring(obj, docstring)\n\n    Add a docstring to a built-in obj if possible.\n    If the obj already has a docstring raise a RuntimeError\n    If this routine does not know how to add a docstring to the object\n    raise a TypeError'
    pass

def arange(start=None, stop=None, step=None, dtype=None):
    'arange([start,] stop[, step,], dtype=None)\n\n    Return evenly spaced values within a given interval.\n\n    Values are generated within the half-open interval ``[start, stop)``\n    (in other words, the interval including `start` but excluding `stop`).\n    For integer arguments the function is equivalent to the Python built-in\n    `range <http://docs.python.org/lib/built-in-funcs.html>`_ function,\n    but returns an ndarray rather than a list.\n\n    When using a non-integer step, such as 0.1, the results will often not\n    be consistent.  It is better to use ``linspace`` for these cases.\n\n    Parameters\n    ----------\n    start : number, optional\n        Start of interval.  The interval includes this value.  The default\n        start value is 0.\n    stop : number\n        End of interval.  The interval does not include this value, except\n        in some cases where `step` is not an integer and floating point\n        round-off affects the length of `out`.\n    step : number, optional\n        Spacing between values.  For any output `out`, this is the distance\n        between two adjacent values, ``out[i+1] - out[i]``.  The default\n        step size is 1.  If `step` is specified as a position argument,\n        `start` must also be given.\n    dtype : dtype\n        The type of the output array.  If `dtype` is not given, infer the data\n        type from the other input arguments.\n\n    Returns\n    -------\n    arange : ndarray\n        Array of evenly spaced values.\n\n        For floating point arguments, the length of the result is\n        ``ceil((stop - start)/step)``.  Because of floating point overflow,\n        this rule may result in the last element of `out` being greater\n        than `stop`.\n\n    See Also\n    --------\n    linspace : Evenly spaced numbers with careful handling of endpoints.\n    ogrid: Arrays of evenly spaced numbers in N-dimensions.\n    mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.\n\n    Examples\n    --------\n    >>> np.arange(3)\n    array([0, 1, 2])\n    >>> np.arange(3.0)\n    array([ 0.,  1.,  2.])\n    >>> np.arange(3,7)\n    array([3, 4, 5, 6])\n    >>> np.arange(3,7,2)\n    array([3, 5])'
    pass

def array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0):
    "array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)\n\n    Create an array.\n\n    Parameters\n    ----------\n    object : array_like\n        An array, any object exposing the array interface, an object whose\n        __array__ method returns an array, or any (nested) sequence.\n    dtype : data-type, optional\n        The desired data-type for the array.  If not given, then the type will\n        be determined as the minimum type required to hold the objects in the\n        sequence.  This argument can only be used to 'upcast' the array.  For\n        downcasting, use the .astype(t) method.\n    copy : bool, optional\n        If true (default), then the object is copied.  Otherwise, a copy will\n        only be made if __array__ returns a copy, if obj is a nested sequence,\n        or if a copy is needed to satisfy any of the other requirements\n        (`dtype`, `order`, etc.).\n    order : {'K', 'A', 'C', 'F'}, optional\n        Specify the memory layout of the array. If object is not an array, the\n        newly created array will be in C order (row major) unless 'F' is\n        specified, in which case it will be in Fortran order (column major).\n        If object is an array the following holds.\n\n        ===== ========= ===================================================\n        order  no copy                     copy=True\n        ===== ========= ===================================================\n        'K'   unchanged F & C order preserved, otherwise most similar order\n        'A'   unchanged F order if input is F and not C, otherwise C order\n        'C'   C order   C order\n        'F'   F order   F order\n        ===== ========= ===================================================\n\n        When ``copy=False`` and a copy is made for other reasons, the result is\n        the same as if ``copy=True``, with some exceptions for `A`, see the\n        Notes section. The default order is 'K'.\n    subok : bool, optional\n        If True, then sub-classes will be passed-through, otherwise\n        the returned array will be forced to be a base-class array (default).\n    ndmin : int, optional\n        Specifies the minimum number of dimensions that the resulting\n        array should have.  Ones will be pre-pended to the shape as\n        needed to meet this requirement.\n\n    Returns\n    -------\n    out : ndarray\n        An array object satisfying the specified requirements.\n\n    See Also\n    --------\n    empty_like : Return an empty array with shape and type of input.\n    ones_like : Return an array of ones with shape and type of input.\n    zeros_like : Return an array of zeros with shape and type of input.\n    full_like : Return a new array with shape of input filled with value.\n    empty : Return a new uninitialized array.\n    ones : Return a new array setting values to one.\n    zeros : Return a new array setting values to zero.\n    full : Return a new array of given shape filled with value.\n\n\n    Notes\n    -----\n    When order is 'A' and `object` is an array in neither 'C' nor 'F' order,\n    and a copy is forced by a change in dtype, then the order of the result is\n    not necessarily 'C' as expected. This is likely a bug.\n\n    Examples\n    --------\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n\n    Upcasting:\n\n    >>> np.array([1, 2, 3.0])\n    array([ 1.,  2.,  3.])\n\n    More than one dimension:\n\n    >>> np.array([[1, 2], [3, 4]])\n    array([[1, 2],\n           [3, 4]])\n\n    Minimum dimensions 2:\n\n    >>> np.array([1, 2, 3], ndmin=2)\n    array([[1, 2, 3]])\n\n    Type provided:\n\n    >>> np.array([1, 2, 3], dtype=complex)\n    array([ 1.+0.j,  2.+0.j,  3.+0.j])\n\n    Data-type consisting of more than one element:\n\n    >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])\n    >>> x['a']\n    array([1, 3])\n\n    Creating an array from sub-classes:\n\n    >>> np.array(np.mat('1 2; 3 4'))\n    array([[1, 2],\n           [3, 4]])\n\n    >>> np.array(np.mat('1 2; 3 4'), subok=True)\n    matrix([[1, 2],\n            [3, 4]])"
    pass

def bincount(x, weights=None, minlength=0):
    'bincount(x, weights=None, minlength=0)\n\n    Count number of occurrences of each value in array of non-negative ints.\n\n    The number of bins (of size 1) is one larger than the largest value in\n    `x`. If `minlength` is specified, there will be at least this number\n    of bins in the output array (though it will be longer if necessary,\n    depending on the contents of `x`).\n    Each bin gives the number of occurrences of its index value in `x`.\n    If `weights` is specified the input array is weighted by it, i.e. if a\n    value ``n`` is found at position ``i``, ``out[n] += weight[i]`` instead\n    of ``out[n] += 1``.\n\n    Parameters\n    ----------\n    x : array_like, 1 dimension, nonnegative ints\n        Input array.\n    weights : array_like, optional\n        Weights, array of the same shape as `x`.\n    minlength : int, optional\n        A minimum number of bins for the output array.\n\n        .. versionadded:: 1.6.0\n\n    Returns\n    -------\n    out : ndarray of ints\n        The result of binning the input array.\n        The length of `out` is equal to ``np.amax(x)+1``.\n\n    Raises\n    ------\n    ValueError\n        If the input is not 1-dimensional, or contains elements with negative\n        values, or if `minlength` is negative.\n    TypeError\n        If the type of the input is float or complex.\n\n    See Also\n    --------\n    histogram, digitize, unique\n\n    Examples\n    --------\n    >>> np.bincount(np.arange(5))\n    array([1, 1, 1, 1, 1])\n    >>> np.bincount(np.array([0, 1, 1, 3, 2, 1, 7]))\n    array([1, 3, 1, 1, 0, 0, 0, 1])\n\n    >>> x = np.array([0, 1, 1, 3, 2, 1, 7, 23])\n    >>> np.bincount(x).size == np.amax(x)+1\n    True\n\n    The input array needs to be of integer dtype, otherwise a\n    TypeError is raised:\n\n    >>> np.bincount(np.arange(5, dtype=float))\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    TypeError: array cannot be safely cast to required type\n\n    A possible use of ``bincount`` is to perform sums over\n    variable-size chunks of an array, using the ``weights`` keyword.\n\n    >>> w = np.array([0.3, 0.5, 0.2, 0.7, 1., -0.6]) # weights\n    >>> x = np.array([0, 1, 1, 2, 2, 2])\n    >>> np.bincount(x,  weights=w)\n    array([ 0.3,  0.7,  1.1])'
    pass

class broadcast(_mod_builtins.object):
    'Produce an object that mimics broadcasting.\n\n    Parameters\n    ----------\n    in1, in2, ... : array_like\n        Input parameters.\n\n    Returns\n    -------\n    b : broadcast object\n        Broadcast the input parameters against one another, and\n        return an object that encapsulates the result.\n        Amongst others, it has ``shape`` and ``nd`` properties, and\n        may be used as an iterator.\n\n    See Also\n    --------\n    broadcast_arrays\n    broadcast_to\n\n    Examples\n    --------\n    Manually adding two vectors, using broadcasting:\n\n    >>> x = np.array([[1], [2], [3]])\n    >>> y = np.array([4, 5, 6])\n    >>> b = np.broadcast(x, y)\n\n    >>> out = np.empty(b.shape)\n    >>> out.flat = [u+v for (u,v) in b]\n    >>> out\n    array([[ 5.,  6.,  7.],\n           [ 6.,  7.,  8.],\n           [ 7.,  8.,  9.]])\n\n    Compare against built-in broadcasting:\n\n    >>> x + y\n    array([[5, 6, 7],\n           [6, 7, 8],\n           [7, 8, 9]])'
    __class__ = broadcast
    def __init__(self, *args, **kwargs):
        'Produce an object that mimics broadcasting.\n\n    Parameters\n    ----------\n    in1, in2, ... : array_like\n        Input parameters.\n\n    Returns\n    -------\n    b : broadcast object\n        Broadcast the input parameters against one another, and\n        return an object that encapsulates the result.\n        Amongst others, it has ``shape`` and ``nd`` properties, and\n        may be used as an iterator.\n\n    See Also\n    --------\n    broadcast_arrays\n    broadcast_to\n\n    Examples\n    --------\n    Manually adding two vectors, using broadcasting:\n\n    >>> x = np.array([[1], [2], [3]])\n    >>> y = np.array([4, 5, 6])\n    >>> b = np.broadcast(x, y)\n\n    >>> out = np.empty(b.shape)\n    >>> out.flat = [u+v for (u,v) in b]\n    >>> out\n    array([[ 5.,  6.,  7.],\n           [ 6.,  7.,  8.],\n           [ 7.,  8.,  9.]])\n\n    Compare against built-in broadcasting:\n\n    >>> x + y\n    array([[5, 6, 7],\n           [6, 7, 8],\n           [7, 8, 9]])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return broadcast()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def index(self):
        'current index in broadcasted result\n\n    Examples\n    --------\n    >>> x = np.array([[1], [2], [3]])\n    >>> y = np.array([4, 5, 6])\n    >>> b = np.broadcast(x, y)\n    >>> b.index\n    0\n    >>> b.next(), b.next(), b.next()\n    ((1, 4), (1, 5), (1, 6))\n    >>> b.index\n    3'
        pass
    
    @property
    def iters(self):
        'tuple of iterators along ``self``\'s "components."\n\n    Returns a tuple of `numpy.flatiter` objects, one for each "component"\n    of ``self``.\n\n    See Also\n    --------\n    numpy.flatiter\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> row, col = b.iters\n    >>> row.next(), col.next()\n    (1, 4)'
        pass
    
    @property
    def nd(self):
        'Number of dimensions of broadcasted result. For code intended for NumPy\n    1.12.0 and later the more consistent `ndim` is preferred.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> b.nd\n    2'
        pass
    
    @property
    def ndim(self):
        'Number of dimensions of broadcasted result. Alias for `nd`.\n\n    .. versionadded:: 1.12.0\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> b.ndim\n    2'
        pass
    
    @property
    def numiter(self):
        'Number of iterators possessed by the broadcasted result.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> b.numiter\n    2'
        pass
    
    def reset(self):
        "reset()\n\n    Reset the broadcasted result's iterator(s).\n\n    Parameters\n    ----------\n    None\n\n    Returns\n    -------\n    None\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]]\n    >>> b = np.broadcast(x, y)\n    >>> b.index\n    0\n    >>> b.next(), b.next(), b.next()\n    ((1, 4), (2, 4), (3, 4))\n    >>> b.index\n    3\n    >>> b.reset()\n    >>> b.index\n    0"
        pass
    
    @property
    def shape(self):
        'Shape of broadcasted result.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> b.shape\n    (3, 3)'
        pass
    
    @property
    def size(self):
        'Total size of broadcasted result.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> y = np.array([[4], [5], [6]])\n    >>> b = np.broadcast(x, y)\n    >>> b.size\n    9'
        pass
    

def busday_count(begindates, enddates, weekmask='1111100', holidays=[], busdaycal=None, out=None):
    'busday_count(begindates, enddates, weekmask=\'1111100\', holidays=[], busdaycal=None, out=None)\n\n    Counts the number of valid days between `begindates` and\n    `enddates`, not including the day of `enddates`.\n\n    If ``enddates`` specifies a date value that is earlier than the\n    corresponding ``begindates`` date value, the count will be negative.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    begindates : array_like of datetime64[D]\n        The array of the first dates for counting.\n    enddates : array_like of datetime64[D]\n        The array of the end dates for counting, which are excluded\n        from the count themselves.\n    weekmask : str or array_like of bool, optional\n        A seven-element array indicating which of Monday through Sunday are\n        valid days. May be specified as a length-seven list or array, like\n        [1,1,1,1,1,0,0]; a length-seven string, like \'1111100\'; or a string\n        like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for\n        weekdays, optionally separated by white space. Valid abbreviations\n        are: Mon Tue Wed Thu Fri Sat Sun\n    holidays : array_like of datetime64[D], optional\n        An array of dates to consider as invalid dates.  They may be\n        specified in any order, and NaT (not-a-time) dates are ignored.\n        This list is saved in a normalized form that is suited for\n        fast calculations of valid days.\n    busdaycal : busdaycalendar, optional\n        A `busdaycalendar` object which specifies the valid days. If this\n        parameter is provided, neither weekmask nor holidays may be\n        provided.\n    out : array of int, optional\n        If provided, this array is filled with the result.\n\n    Returns\n    -------\n    out : array of int\n        An array with a shape from broadcasting ``begindates`` and ``enddates``\n        together, containing the number of valid days between\n        the begin and end dates.\n\n    See Also\n    --------\n    busdaycalendar: An object that specifies a custom set of valid days.\n    is_busday : Returns a boolean array indicating valid days.\n    busday_offset : Applies an offset counted in valid days.\n\n    Examples\n    --------\n    >>> # Number of weekdays in January 2011\n    ... np.busday_count(\'2011-01\', \'2011-02\')\n    21\n    >>> # Number of weekdays in 2011\n    ...  np.busday_count(\'2011\', \'2012\')\n    260\n    >>> # Number of Saturdays in 2011\n    ... np.busday_count(\'2011\', \'2012\', weekmask=\'Sat\')\n    53'
    pass

def busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None):
    'busday_offset(dates, offsets, roll=\'raise\', weekmask=\'1111100\', holidays=None, busdaycal=None, out=None)\n\n    First adjusts the date to fall on a valid day according to\n    the ``roll`` rule, then applies offsets to the given dates\n    counted in valid days.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    dates : array_like of datetime64[D]\n        The array of dates to process.\n    offsets : array_like of int\n        The array of offsets, which is broadcast with ``dates``.\n    roll : {\'raise\', \'nat\', \'forward\', \'following\', \'backward\', \'preceding\', \'modifiedfollowing\', \'modifiedpreceding\'}, optional\n        How to treat dates that do not fall on a valid day. The default\n        is \'raise\'.\n\n          * \'raise\' means to raise an exception for an invalid day.\n          * \'nat\' means to return a NaT (not-a-time) for an invalid day.\n          * \'forward\' and \'following\' mean to take the first valid day\n            later in time.\n          * \'backward\' and \'preceding\' mean to take the first valid day\n            earlier in time.\n          * \'modifiedfollowing\' means to take the first valid day\n            later in time unless it is across a Month boundary, in which\n            case to take the first valid day earlier in time.\n          * \'modifiedpreceding\' means to take the first valid day\n            earlier in time unless it is across a Month boundary, in which\n            case to take the first valid day later in time.\n    weekmask : str or array_like of bool, optional\n        A seven-element array indicating which of Monday through Sunday are\n        valid days. May be specified as a length-seven list or array, like\n        [1,1,1,1,1,0,0]; a length-seven string, like \'1111100\'; or a string\n        like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for\n        weekdays, optionally separated by white space. Valid abbreviations\n        are: Mon Tue Wed Thu Fri Sat Sun\n    holidays : array_like of datetime64[D], optional\n        An array of dates to consider as invalid dates.  They may be\n        specified in any order, and NaT (not-a-time) dates are ignored.\n        This list is saved in a normalized form that is suited for\n        fast calculations of valid days.\n    busdaycal : busdaycalendar, optional\n        A `busdaycalendar` object which specifies the valid days. If this\n        parameter is provided, neither weekmask nor holidays may be\n        provided.\n    out : array of datetime64[D], optional\n        If provided, this array is filled with the result.\n\n    Returns\n    -------\n    out : array of datetime64[D]\n        An array with a shape from broadcasting ``dates`` and ``offsets``\n        together, containing the dates with offsets applied.\n\n    See Also\n    --------\n    busdaycalendar: An object that specifies a custom set of valid days.\n    is_busday : Returns a boolean array indicating valid days.\n    busday_count : Counts how many valid days are in a half-open date range.\n\n    Examples\n    --------\n    >>> # First business day in October 2011 (not accounting for holidays)\n    ... np.busday_offset(\'2011-10\', 0, roll=\'forward\')\n    numpy.datetime64(\'2011-10-03\',\'D\')\n    >>> # Last business day in February 2012 (not accounting for holidays)\n    ... np.busday_offset(\'2012-03\', -1, roll=\'forward\')\n    numpy.datetime64(\'2012-02-29\',\'D\')\n    >>> # Third Wednesday in January 2011\n    ... np.busday_offset(\'2011-01\', 2, roll=\'forward\', weekmask=\'Wed\')\n    numpy.datetime64(\'2011-01-19\',\'D\')\n    >>> # 2012 Mother\'s Day in Canada and the U.S.\n    ... np.busday_offset(\'2012-05\', 1, roll=\'forward\', weekmask=\'Sun\')\n    numpy.datetime64(\'2012-05-13\',\'D\')\n\n    >>> # First business day on or after a date\n    ... np.busday_offset(\'2011-03-20\', 0, roll=\'forward\')\n    numpy.datetime64(\'2011-03-21\',\'D\')\n    >>> np.busday_offset(\'2011-03-22\', 0, roll=\'forward\')\n    numpy.datetime64(\'2011-03-22\',\'D\')\n    >>> # First business day after a date\n    ... np.busday_offset(\'2011-03-20\', 1, roll=\'backward\')\n    numpy.datetime64(\'2011-03-21\',\'D\')\n    >>> np.busday_offset(\'2011-03-22\', 1, roll=\'backward\')\n    numpy.datetime64(\'2011-03-23\',\'D\')'
    pass

class busdaycalendar(_mod_builtins.object):
    'busdaycalendar(weekmask=\'1111100\', holidays=None)\n\n    A business day calendar object that efficiently stores information\n    defining valid days for the busday family of functions.\n\n    The default valid days are Monday through Friday ("business days").\n    A busdaycalendar object can be specified with any set of weekly\n    valid days, plus an optional "holiday" dates that always will be invalid.\n\n    Once a busdaycalendar object is created, the weekmask and holidays\n    cannot be modified.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    weekmask : str or array_like of bool, optional\n        A seven-element array indicating which of Monday through Sunday are\n        valid days. May be specified as a length-seven list or array, like\n        [1,1,1,1,1,0,0]; a length-seven string, like \'1111100\'; or a string\n        like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for\n        weekdays, optionally separated by white space. Valid abbreviations\n        are: Mon Tue Wed Thu Fri Sat Sun\n    holidays : array_like of datetime64[D], optional\n        An array of dates to consider as invalid dates, no matter which\n        weekday they fall upon.  Holiday dates may be specified in any\n        order, and NaT (not-a-time) dates are ignored.  This list is\n        saved in a normalized form that is suited for fast calculations\n        of valid days.\n\n    Returns\n    -------\n    out : busdaycalendar\n        A business day calendar object containing the specified\n        weekmask and holidays values.\n\n    See Also\n    --------\n    is_busday : Returns a boolean array indicating valid days.\n    busday_offset : Applies an offset counted in valid days.\n    busday_count : Counts how many valid days are in a half-open date range.\n\n    Attributes\n    ----------\n    Note: once a busdaycalendar object is created, you cannot modify the\n    weekmask or holidays.  The attributes return copies of internal data.\n    weekmask : (copy) seven-element array of bool\n    holidays : (copy) sorted array of datetime64[D]\n\n    Examples\n    --------\n    >>> # Some important days in July\n    ... bdd = np.busdaycalendar(\n    ...             holidays=[\'2011-07-01\', \'2011-07-04\', \'2011-07-17\'])\n    >>> # Default is Monday to Friday weekdays\n    ... bdd.weekmask\n    array([ True,  True,  True,  True,  True, False, False], dtype=\'bool\')\n    >>> # Any holidays already on the weekend are removed\n    ... bdd.holidays\n    array([\'2011-07-01\', \'2011-07-04\'], dtype=\'datetime64[D]\')'
    __class__ = busdaycalendar
    def __init__(self, weekmask='1111100', holidays=None):
        'busdaycalendar(weekmask=\'1111100\', holidays=None)\n\n    A business day calendar object that efficiently stores information\n    defining valid days for the busday family of functions.\n\n    The default valid days are Monday through Friday ("business days").\n    A busdaycalendar object can be specified with any set of weekly\n    valid days, plus an optional "holiday" dates that always will be invalid.\n\n    Once a busdaycalendar object is created, the weekmask and holidays\n    cannot be modified.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    weekmask : str or array_like of bool, optional\n        A seven-element array indicating which of Monday through Sunday are\n        valid days. May be specified as a length-seven list or array, like\n        [1,1,1,1,1,0,0]; a length-seven string, like \'1111100\'; or a string\n        like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for\n        weekdays, optionally separated by white space. Valid abbreviations\n        are: Mon Tue Wed Thu Fri Sat Sun\n    holidays : array_like of datetime64[D], optional\n        An array of dates to consider as invalid dates, no matter which\n        weekday they fall upon.  Holiday dates may be specified in any\n        order, and NaT (not-a-time) dates are ignored.  This list is\n        saved in a normalized form that is suited for fast calculations\n        of valid days.\n\n    Returns\n    -------\n    out : busdaycalendar\n        A business day calendar object containing the specified\n        weekmask and holidays values.\n\n    See Also\n    --------\n    is_busday : Returns a boolean array indicating valid days.\n    busday_offset : Applies an offset counted in valid days.\n    busday_count : Counts how many valid days are in a half-open date range.\n\n    Attributes\n    ----------\n    Note: once a busdaycalendar object is created, you cannot modify the\n    weekmask or holidays.  The attributes return copies of internal data.\n    weekmask : (copy) seven-element array of bool\n    holidays : (copy) sorted array of datetime64[D]\n\n    Examples\n    --------\n    >>> # Some important days in July\n    ... bdd = np.busdaycalendar(\n    ...             holidays=[\'2011-07-01\', \'2011-07-04\', \'2011-07-17\'])\n    >>> # Default is Monday to Friday weekdays\n    ... bdd.weekmask\n    array([ True,  True,  True,  True,  True, False, False], dtype=\'bool\')\n    >>> # Any holidays already on the weekend are removed\n    ... bdd.holidays\n    array([\'2011-07-01\', \'2011-07-04\'], dtype=\'datetime64[D]\')'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def holidays(self):
        'A copy of the holiday array indicating additional invalid days.'
        pass
    
    @property
    def weekmask(self):
        'A copy of the seven-element boolean mask indicating valid days.'
        pass
    

def c_einsum():
    pass

def can_cast(from_, to, casting='safe'):
    "can_cast(from_, to, casting='safe')\n\n    Returns True if cast between data types can occur according to the\n    casting rule.  If from is a scalar or array scalar, also returns\n    True if the scalar value can be cast without overflow or truncation\n    to an integer.\n\n    Parameters\n    ----------\n    from_ : dtype, dtype specifier, scalar, or array\n        Data type, scalar, or array to cast from.\n    to : dtype or dtype specifier\n        Data type to cast to.\n    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional\n        Controls what kind of data casting may occur.\n\n          * 'no' means the data types should not be cast at all.\n          * 'equiv' means only byte-order changes are allowed.\n          * 'safe' means only casts which can preserve values are allowed.\n          * 'same_kind' means only safe casts or casts within a kind,\n            like float64 to float32, are allowed.\n          * 'unsafe' means any data conversions may be done.\n\n    Returns\n    -------\n    out : bool\n        True if cast can occur according to the casting rule.\n\n    Notes\n    -----\n    Starting in NumPy 1.9, can_cast function now returns False in 'safe'\n    casting mode for integer/float dtype and string dtype if the string dtype\n    length is not long enough to store the max integer/float value converted\n    to a string. Previously can_cast in 'safe' mode returned True for\n    integer/float dtype and a string dtype of any length.\n\n    See also\n    --------\n    dtype, result_type\n\n    Examples\n    --------\n    Basic examples\n\n    >>> np.can_cast(np.int32, np.int64)\n    True\n    >>> np.can_cast(np.float64, complex)\n    True\n    >>> np.can_cast(complex, float)\n    False\n\n    >>> np.can_cast('i8', 'f8')\n    True\n    >>> np.can_cast('i8', 'f4')\n    False\n    >>> np.can_cast('i4', 'S4')\n    False\n\n    Casting scalars\n\n    >>> np.can_cast(100, 'i1')\n    True\n    >>> np.can_cast(150, 'i1')\n    False\n    >>> np.can_cast(150, 'u1')\n    True\n\n    >>> np.can_cast(3.5e100, np.float32)\n    False\n    >>> np.can_cast(1000.0, np.float32)\n    True\n\n    Array scalar checks the value, array does not\n\n    >>> np.can_cast(np.array(1000.0), np.float32)\n    True\n    >>> np.can_cast(np.array([1000.0]), np.float32)\n    False\n\n    Using the casting rules\n\n    >>> np.can_cast('i8', 'i8', 'no')\n    True\n    >>> np.can_cast('<i8', '>i8', 'no')\n    False\n\n    >>> np.can_cast('<i8', '>i8', 'equiv')\n    True\n    >>> np.can_cast('<i4', '>i8', 'equiv')\n    False\n\n    >>> np.can_cast('<i4', '>i8', 'safe')\n    True\n    >>> np.can_cast('<i8', '>i4', 'safe')\n    False\n\n    >>> np.can_cast('<i8', '>i4', 'same_kind')\n    True\n    >>> np.can_cast('<i8', '>u4', 'same_kind')\n    False\n\n    >>> np.can_cast('<i8', '>u4', 'unsafe')\n    True"
    pass

def compare_chararrays():
    pass

def concatenate():
    'concatenate((a1, a2, ...), axis=0, out=None)\n\n    Join a sequence of arrays along an existing axis.\n\n    Parameters\n    ----------\n    a1, a2, ... : sequence of array_like\n        The arrays must have the same shape, except in the dimension\n        corresponding to `axis` (the first, by default).\n    axis : int, optional\n        The axis along which the arrays will be joined.  If axis is None,\n        arrays are flattened before use.  Default is 0.\n    out : ndarray, optional\n        If provided, the destination to place the result. The shape must be\n        correct, matching that of what concatenate would have returned if no\n        out argument were specified.\n\n    Returns\n    -------\n    res : ndarray\n        The concatenated array.\n\n    See Also\n    --------\n    ma.concatenate : Concatenate function that preserves input masks.\n    array_split : Split an array into multiple sub-arrays of equal or\n                  near-equal size.\n    split : Split array into a list of multiple sub-arrays of equal size.\n    hsplit : Split array into multiple sub-arrays horizontally (column wise)\n    vsplit : Split array into multiple sub-arrays vertically (row wise)\n    dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).\n    stack : Stack a sequence of arrays along a new axis.\n    hstack : Stack arrays in sequence horizontally (column wise)\n    vstack : Stack arrays in sequence vertically (row wise)\n    dstack : Stack arrays in sequence depth wise (along third dimension)\n\n    Notes\n    -----\n    When one or more of the arrays to be concatenated is a MaskedArray,\n    this function will return a MaskedArray object instead of an ndarray,\n    but the input masks are *not* preserved. In cases where a MaskedArray\n    is expected as input, use the ma.concatenate function from the masked\n    array module instead.\n\n    Examples\n    --------\n    >>> a = np.array([[1, 2], [3, 4]])\n    >>> b = np.array([[5, 6]])\n    >>> np.concatenate((a, b), axis=0)\n    array([[1, 2],\n           [3, 4],\n           [5, 6]])\n    >>> np.concatenate((a, b.T), axis=1)\n    array([[1, 2, 5],\n           [3, 4, 6]])\n    >>> np.concatenate((a, b), axis=None)\n    array([1, 2, 3, 4, 5, 6])\n\n    This function will not preserve masking of MaskedArray inputs.\n\n    >>> a = np.ma.arange(3)\n    >>> a[1] = np.ma.masked\n    >>> b = np.arange(2, 5)\n    >>> a\n    masked_array(data = [0 -- 2],\n                 mask = [False  True False],\n           fill_value = 999999)\n    >>> b\n    array([2, 3, 4])\n    >>> np.concatenate([a, b])\n    masked_array(data = [0 1 2 2 3 4],\n                 mask = False,\n           fill_value = 999999)\n    >>> np.ma.concatenate([a, b])\n    masked_array(data = [0 -- 2 2 3 4],\n                 mask = [False  True False False False False],\n           fill_value = 999999)'
    pass

def copyto(dst, src, casting='same_kind', where=True):
    "copyto(dst, src, casting='same_kind', where=True)\n\n    Copies values from one array to another, broadcasting as necessary.\n\n    Raises a TypeError if the `casting` rule is violated, and if\n    `where` is provided, it selects which elements to copy.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    dst : ndarray\n        The array into which values are copied.\n    src : array_like\n        The array from which values are copied.\n    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional\n        Controls what kind of data casting may occur when copying.\n\n          * 'no' means the data types should not be cast at all.\n          * 'equiv' means only byte-order changes are allowed.\n          * 'safe' means only casts which can preserve values are allowed.\n          * 'same_kind' means only safe casts or casts within a kind,\n            like float64 to float32, are allowed.\n          * 'unsafe' means any data conversions may be done.\n    where : array_like of bool, optional\n        A boolean array which is broadcasted to match the dimensions\n        of `dst`, and selects elements to copy from `src` to `dst`\n        wherever it contains the value True."
    pass

def correlate():
    'cross_correlate(a,v, mode=0)'
    pass

def correlate2():
    pass

def count_nonzero():
    pass

def datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind'):
    "datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')\n\n    Convert an array of datetimes into an array of strings.\n\n    Parameters\n    ----------\n    arr : array_like of datetime64\n        The array of UTC timestamps to format.\n    unit : str\n        One of None, 'auto', or a :ref:`datetime unit <arrays.dtypes.dateunits>`.\n    timezone : {'naive', 'UTC', 'local'} or tzinfo\n        Timezone information to use when displaying the datetime. If 'UTC', end\n        with a Z to indicate UTC time. If 'local', convert to the local timezone\n        first, and suffix with a +-#### timezone offset. If a tzinfo object,\n        then do as with 'local', but use the specified timezone.\n    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}\n        Casting to allow when changing between datetime units.\n\n    Returns\n    -------\n    str_arr : ndarray\n        An array of strings the same shape as `arr`.\n\n    Examples\n    --------\n    >>> d = np.arange('2002-10-27T04:30', 4*60, 60, dtype='M8[m]')\n    >>> d\n    array(['2002-10-27T04:30', '2002-10-27T05:30', '2002-10-27T06:30',\n           '2002-10-27T07:30'], dtype='datetime64[m]')\n\n    Setting the timezone to UTC shows the same information, but with a Z suffix\n\n    >>> np.datetime_as_string(d, timezone='UTC')\n    array(['2002-10-27T04:30Z', '2002-10-27T05:30Z', '2002-10-27T06:30Z',\n           '2002-10-27T07:30Z'], dtype='<U35')\n\n    Note that we picked datetimes that cross a DST boundary. Passing in a\n    ``pytz`` timezone object will print the appropriate offset\n\n    >>> np.datetime_as_string(d, timezone=pytz.timezone('US/Eastern'))\n    array(['2002-10-27T00:30-0400', '2002-10-27T01:30-0400',\n           '2002-10-27T01:30-0500', '2002-10-27T02:30-0500'], dtype='<U39')\n\n    Passing in a unit will change the precision\n\n    >>> np.datetime_as_string(d, unit='h')\n    array(['2002-10-27T04', '2002-10-27T05', '2002-10-27T06', '2002-10-27T07'],\n          dtype='<U32')\n    >>> np.datetime_as_string(d, unit='s')\n    array(['2002-10-27T04:30:00', '2002-10-27T05:30:00', '2002-10-27T06:30:00',\n           '2002-10-27T07:30:00'], dtype='<U38')\n\n    'casting' can be used to specify whether precision can be changed\n\n    >>> np.datetime_as_string(d, unit='h', casting='safe')\n    TypeError: Cannot create a datetime string as units 'h' from a NumPy\n    datetime with units 'm' according to the rule 'safe'"
    pass

def datetime_data(dtype):
    "datetime_data(dtype, /)\n\n    Get information about the step size of a date or time type.\n\n    The returned tuple can be passed as the second argument of `datetime64` and\n    `timedelta64`.\n\n    Parameters\n    ----------\n    dtype : dtype\n        The dtype object, which must be a `datetime64` or `timedelta64` type.\n\n    Returns\n    -------\n    unit : str\n        The :ref:`datetime unit <arrays.dtypes.dateunits>` on which this dtype\n        is based.\n    count : int\n        The number of base units in a step.\n\n    Examples\n    --------\n    >>> dt_25s = np.dtype('timedelta64[25s]')\n    >>> np.datetime_data(dt_25s)\n    ('s', 25)\n    >>> np.array(10, dt_25s).astype('timedelta64[s]')\n    array(250, dtype='timedelta64[s]')\n\n    The result can be used to construct a datetime that uses the same units\n    as a timedelta::\n\n    >>> np.datetime64('2010', np.datetime_data(dt_25s))\n    numpy.datetime64('2010-01-01T00:00:00','25s')"
    pass

def digitize(x, bins, right=False):
    'digitize(x, bins, right=False)\n\n    Return the indices of the bins to which each value in input array belongs.\n\n    =========  =============  ============================\n    `right`    order of bins  returned index `i` satisfies\n    =========  =============  ============================\n    ``False``  increasing     ``bins[i-1] <= x < bins[i]``\n    ``True``   increasing     ``bins[i-1] < x <= bins[i]``\n    ``False``  decreasing     ``bins[i-1] > x >= bins[i]``\n    ``True``   decreasing     ``bins[i-1] >= x > bins[i]``\n    =========  =============  ============================\n\n    If values in `x` are beyond the bounds of `bins`, 0 or ``len(bins)`` is\n    returned as appropriate.\n\n    Parameters\n    ----------\n    x : array_like\n        Input array to be binned. Prior to NumPy 1.10.0, this array had to\n        be 1-dimensional, but can now have any shape.\n    bins : array_like\n        Array of bins. It has to be 1-dimensional and monotonic.\n    right : bool, optional\n        Indicating whether the intervals include the right or the left bin\n        edge. Default behavior is (right==False) indicating that the interval\n        does not include the right edge. The left bin end is open in this\n        case, i.e., bins[i-1] <= x < bins[i] is the default behavior for\n        monotonically increasing bins.\n\n    Returns\n    -------\n    indices : ndarray of ints\n        Output array of indices, of same shape as `x`.\n\n    Raises\n    ------\n    ValueError\n        If `bins` is not monotonic.\n    TypeError\n        If the type of the input is complex.\n\n    See Also\n    --------\n    bincount, histogram, unique, searchsorted\n\n    Notes\n    -----\n    If values in `x` are such that they fall outside the bin range,\n    attempting to index `bins` with the indices that `digitize` returns\n    will result in an IndexError.\n\n    .. versionadded:: 1.10.0\n\n    `np.digitize` is  implemented in terms of `np.searchsorted`. This means\n    that a binary search is used to bin the values, which scales much better\n    for larger number of bins than the previous linear search. It also removes\n    the requirement for the input array to be 1-dimensional.\n\n    For monotonically _increasing_ `bins`, the following are equivalent::\n\n        np.digitize(x, bins, right=True)\n        np.searchsorted(bins, x, side=\'left\')\n\n    Note that as the order of the arguments are reversed, the side must be too.\n    The `searchsorted` call is marginally faster, as it does not do any\n    monotonicity checks. Perhaps more importantly, it supports all dtypes.\n\n    Examples\n    --------\n    >>> x = np.array([0.2, 6.4, 3.0, 1.6])\n    >>> bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])\n    >>> inds = np.digitize(x, bins)\n    >>> inds\n    array([1, 4, 3, 2])\n    >>> for n in range(x.size):\n    ...   print(bins[inds[n]-1], "<=", x[n], "<", bins[inds[n]])\n    ...\n    0.0 <= 0.2 < 1.0\n    4.0 <= 6.4 < 10.0\n    2.5 <= 3.0 < 4.0\n    1.0 <= 1.6 < 2.5\n\n    >>> x = np.array([1.2, 10.0, 12.4, 15.5, 20.])\n    >>> bins = np.array([0, 5, 10, 15, 20])\n    >>> np.digitize(x,bins,right=True)\n    array([1, 2, 3, 4, 4])\n    >>> np.digitize(x,bins,right=False)\n    array([1, 3, 3, 4, 5])'
    pass

def dot(a, b, out=None):
    "dot(a, b, out=None)\n\n    Dot product of two arrays. Specifically,\n\n    - If both `a` and `b` are 1-D arrays, it is inner product of vectors\n      (without complex conjugation).\n\n    - If both `a` and `b` are 2-D arrays, it is matrix multiplication,\n      but using :func:`matmul` or ``a @ b`` is preferred.\n\n    - If either `a` or `b` is 0-D (scalar), it is equivalent to :func:`multiply`\n      and using ``numpy.multiply(a, b)`` or ``a * b`` is preferred.\n\n    - If `a` is an N-D array and `b` is a 1-D array, it is a sum product over\n      the last axis of `a` and `b`.\n\n    - If `a` is an N-D array and `b` is an M-D array (where ``M>=2``), it is a\n      sum product over the last axis of `a` and the second-to-last axis of `b`::\n\n        dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])\n\n    Parameters\n    ----------\n    a : array_like\n        First argument.\n    b : array_like\n        Second argument.\n    out : ndarray, optional\n        Output argument. This must have the exact kind that would be returned\n        if it was not used. In particular, it must have the right type, must be\n        C-contiguous, and its dtype must be the dtype that would be returned\n        for `dot(a,b)`. This is a performance feature. Therefore, if these\n        conditions are not met, an exception is raised, instead of attempting\n        to be flexible.\n\n    Returns\n    -------\n    output : ndarray\n        Returns the dot product of `a` and `b`.  If `a` and `b` are both\n        scalars or both 1-D arrays then a scalar is returned; otherwise\n        an array is returned.\n        If `out` is given, then it is returned.\n\n    Raises\n    ------\n    ValueError\n        If the last dimension of `a` is not the same size as\n        the second-to-last dimension of `b`.\n\n    See Also\n    --------\n    vdot : Complex-conjugating dot product.\n    tensordot : Sum products over arbitrary axes.\n    einsum : Einstein summation convention.\n    matmul : '@' operator as method with out parameter.\n\n    Examples\n    --------\n    >>> np.dot(3, 4)\n    12\n\n    Neither argument is complex-conjugated:\n\n    >>> np.dot([2j, 3j], [2j, 3j])\n    (-13+0j)\n\n    For 2-D arrays it is the matrix product:\n\n    >>> a = [[1, 0], [0, 1]]\n    >>> b = [[4, 1], [2, 2]]\n    >>> np.dot(a, b)\n    array([[4, 1],\n           [2, 2]])\n\n    >>> a = np.arange(3*4*5*6).reshape((3,4,5,6))\n    >>> b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))\n    >>> np.dot(a, b)[2,3,2,1,2,2]\n    499128\n    >>> sum(a[2,3,2,:] * b[1,2,:,2])\n    499128"
    pass

def dragon4_positional():
    pass

def dragon4_scientific():
    pass

class dtype(_mod_builtins.object):
    'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = dtype
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, obj, align=False, copy=False):
        'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.n'
        return dtype()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return self*value.'
        return dtype()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def alignment(self):
        'The required alignment (bytes) of this data-type according to the compiler.\n\n    More information is available in the C-API section of the manual.'
        pass
    
    @property
    def base(self):
        pass
    
    @property
    def byteorder(self):
        "A character indicating the byte-order of this data-type object.\n\n    One of:\n\n    ===  ==============\n    '='  native\n    '<'  little-endian\n    '>'  big-endian\n    '|'  not applicable\n    ===  ==============\n\n    All built-in data-type objects have byteorder either '=' or '|'.\n\n    Examples\n    --------\n\n    >>> dt = np.dtype('i2')\n    >>> dt.byteorder\n    '='\n    >>> # endian is not relevant for 8 bit numbers\n    >>> np.dtype('i1').byteorder\n    '|'\n    >>> # or ASCII strings\n    >>> np.dtype('S2').byteorder\n    '|'\n    >>> # Even if specific code is given, and it is native\n    >>> # '=' is the byteorder\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> dt = np.dtype(native_code + 'i2')\n    >>> dt.byteorder\n    '='\n    >>> # Swapped code shows up as itself\n    >>> dt = np.dtype(swapped_code + 'i2')\n    >>> dt.byteorder == swapped_code\n    True"
        pass
    
    @property
    def char(self):
        'A unique character code for each of the 21 different built-in types.'
        pass
    
    @property
    def descr(self):
        "PEP3118 interface description of the data-type.\n\n    The format is that required by the 'descr' key in the\n    PEP3118 `__array_interface__` attribute.\n\n    Warning: This attribute exists specifically for PEP3118 compliance, and\n    is not a datatype description compatible with `np.dtype`."
        pass
    
    @property
    def fields(self):
        "Dictionary of named fields defined for this data type, or ``None``.\n\n    The dictionary is indexed by keys that are the names of the fields.\n    Each entry in the dictionary is a tuple fully describing the field::\n\n      (dtype, offset[, title])\n\n    If present, the optional title can be any object (if it is a string\n    or unicode then it will also be a key in the fields dictionary,\n    otherwise it's meta-data). Notice also that the first two elements\n    of the tuple can be passed directly as arguments to the ``ndarray.getfield``\n    and ``ndarray.setfield`` methods.\n\n    See Also\n    --------\n    ndarray.getfield, ndarray.setfield\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> print(dt.fields)\n    {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}"
        pass
    
    @property
    def flags(self):
        'Bit-flags describing how this data type is to be interpreted.\n\n    Bit-masks are in `numpy.core.multiarray` as the constants\n    `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,\n    `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation\n    of these flags is in C-API documentation; they are largely useful\n    for user-defined data-types.'
        pass
    
    @property
    def hasobject(self):
        "Boolean indicating whether this dtype contains any reference-counted\n    objects in any fields or sub-dtypes.\n\n    Recall that what is actually in the ndarray memory representing\n    the Python object is the memory address of that object (a pointer).\n    Special handling may be required, and this attribute is useful for\n    distinguishing data types that may contain arbitrary Python objects\n    and data-types that won't."
        pass
    
    @property
    def isalignedstruct(self):
        'Boolean indicating whether the dtype is a struct which maintains\n    field alignment. This flag is sticky, so when combining multiple\n    structs together, it is preserved and produces new dtypes which\n    are also aligned.'
        pass
    
    @property
    def isbuiltin(self):
        "Integer indicating how this dtype relates to the built-in dtypes.\n\n    Read-only.\n\n    =  ========================================================================\n    0  if this is a structured array type, with fields\n    1  if this is a dtype compiled into numpy (such as ints, floats etc)\n    2  if the dtype is for a user-defined numpy type\n       A user-defined type uses the numpy C-API machinery to extend\n       numpy to handle a new array type. See\n       :ref:`user.user-defined-data-types` in the NumPy manual.\n    =  ========================================================================\n\n    Examples\n    --------\n    >>> dt = np.dtype('i2')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype('f8')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype([('field1', 'f8')])\n    >>> dt.isbuiltin\n    0"
        pass
    
    @property
    def isnative(self):
        'Boolean indicating whether the byte order of this dtype is native\n    to the platform.'
        pass
    
    @property
    def itemsize(self):
        'The element size of this data-type object.\n\n    For 18 of the 21 types this number is fixed by the data-type.\n    For the flexible data-types, this number can be anything.'
        pass
    
    @property
    def kind(self):
        "A character code (one of 'biufcmMOSUV') identifying the general kind of data.\n\n    =  ======================\n    b  boolean\n    i  signed integer\n    u  unsigned integer\n    f  floating-point\n    c  complex floating-point\n    m  timedelta\n    M  datetime\n    O  object\n    S  (byte-)string\n    U  Unicode\n    V  void\n    =  ======================"
        pass
    
    @property
    def metadata(self):
        pass
    
    @property
    def name(self):
        'A bit-width name for this data-type.\n\n    Un-sized flexible data-type objects do not have this attribute.'
        pass
    
    @property
    def names(self):
        "Ordered list of field names, or ``None`` if there are no fields.\n\n    The names are ordered according to increasing byte offset. This can be\n    used, for example, to walk through all of the named fields in offset order.\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> dt.names\n    ('name', 'grades')"
        pass
    
    @property
    def ndim(self):
        'Number of dimensions of the sub-array if this data type describes a\n    sub-array, and ``0`` otherwise.\n\n    .. versionadded:: 1.13.0'
        pass
    
    def newbyteorder(self, new_order='S'):
        "newbyteorder(new_order='S')\n\n    Return a new dtype with a different byte order.\n\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Parameters\n    ----------\n    new_order : string, optional\n        Byte order to force; a value from the byte order specifications\n        below.  The default value ('S') results in swapping the current\n        byte order.  `new_order` codes can be any of:\n\n        * 'S' - swap dtype from current to opposite endian\n        * {'<', 'L'} - little endian\n        * {'>', 'B'} - big endian\n        * {'=', 'N'} - native order\n        * {'|', 'I'} - ignore (no change to byte order)\n\n        The code does a case-insensitive check on the first letter of\n        `new_order` for these alternatives.  For example, any of '>'\n        or 'B' or 'b' or 'brian' are valid to specify big-endian.\n\n    Returns\n    -------\n    new_dtype : dtype\n        New dtype object with the given change to the byte order.\n\n    Notes\n    -----\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Examples\n    --------\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> native_dt = np.dtype(native_code+'i2')\n    >>> swapped_dt = np.dtype(swapped_code+'i2')\n    >>> native_dt.newbyteorder('S') == swapped_dt\n    True\n    >>> native_dt.newbyteorder() == swapped_dt\n    True\n    >>> native_dt == swapped_dt.newbyteorder('S')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('=')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('N')\n    True\n    >>> native_dt == native_dt.newbyteorder('|')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('<')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('L')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('>')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('B')\n    True"
        pass
    
    @property
    def num(self):
        'A unique number for each of the 21 different built-in types.\n\n    These are roughly ordered from least-to-most precision.'
        pass
    
    @property
    def shape(self):
        'Shape tuple of the sub-array if this data type describes a sub-array,\n    and ``()`` otherwise.'
        pass
    
    @property
    def str(self):
        'The array-protocol typestring of this data-type object.'
        pass
    
    @property
    def subdtype(self):
        'Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and\n    None otherwise.\n\n    The *shape* is the fixed shape of the sub-array described by this\n    data type, and *item_dtype* the data type of the array.\n\n    If a field whose dtype object has this attribute is retrieved,\n    then the extra dimensions implied by *shape* are tacked on to\n    the end of the retrieved array.'
        pass
    
    @property
    def type(self):
        'The type object used to instantiate a scalar of this data-type.'
        pass
    

def empty(shape, dtype=float, order='C'):
    "empty(shape, dtype=float, order='C')\n\n    Return a new array of given shape and type, without initializing entries.\n\n    Parameters\n    ----------\n    shape : int or tuple of int\n        Shape of the empty array, e.g., ``(2, 3)`` or ``2``.\n    dtype : data-type, optional\n        Desired output data-type for the array, e.g, `numpy.int8`. Default is\n        `numpy.float64`.\n    order : {'C', 'F'}, optional, default: 'C'\n        Whether to store multi-dimensional data in row-major\n        (C-style) or column-major (Fortran-style) order in\n        memory.\n\n    Returns\n    -------\n    out : ndarray\n        Array of uninitialized (arbitrary) data of the given shape, dtype, and\n        order.  Object arrays will be initialized to None.\n\n    See Also\n    --------\n    empty_like : Return an empty array with shape and type of input.\n    ones : Return a new array setting values to one.\n    zeros : Return a new array setting values to zero.\n    full : Return a new array of given shape filled with value.\n\n\n    Notes\n    -----\n    `empty`, unlike `zeros`, does not set the array values to zero,\n    and may therefore be marginally faster.  On the other hand, it requires\n    the user to manually set all the values in the array, and should be\n    used with caution.\n\n    Examples\n    --------\n    >>> np.empty([2, 2])\n    array([[ -9.74499359e+001,   6.69583040e-309],\n           [  2.13182611e-314,   3.06959433e-309]])         #random\n\n    >>> np.empty([2, 2], dtype=int)\n    array([[-1073741821, -1067949133],\n           [  496041986,    19249760]])                     #random"
    pass

def empty_like(prototype, dtype=None, order='K', subok=True):
    "empty_like(prototype, dtype=None, order='K', subok=True)\n\n    Return a new array with the same shape and type as a given array.\n\n    Parameters\n    ----------\n    prototype : array_like\n        The shape and data-type of `prototype` define these same attributes\n        of the returned array.\n    dtype : data-type, optional\n        Overrides the data type of the result.\n\n        .. versionadded:: 1.6.0\n    order : {'C', 'F', 'A', or 'K'}, optional\n        Overrides the memory layout of the result. 'C' means C-order,\n        'F' means F-order, 'A' means 'F' if ``prototype`` is Fortran\n        contiguous, 'C' otherwise. 'K' means match the layout of ``prototype``\n        as closely as possible.\n\n        .. versionadded:: 1.6.0\n    subok : bool, optional.\n        If True, then the newly created array will use the sub-class\n        type of 'a', otherwise it will be a base-class array. Defaults\n        to True.\n\n    Returns\n    -------\n    out : ndarray\n        Array of uninitialized (arbitrary) data with the same\n        shape and type as `prototype`.\n\n    See Also\n    --------\n    ones_like : Return an array of ones with shape and type of input.\n    zeros_like : Return an array of zeros with shape and type of input.\n    full_like : Return a new array with shape of input filled with value.\n    empty : Return a new uninitialized array.\n\n    Notes\n    -----\n    This function does *not* initialize the returned array; to do that use\n    `zeros_like` or `ones_like` instead.  It may be marginally faster than\n    the functions that do set the array values.\n\n    Examples\n    --------\n    >>> a = ([1,2,3], [4,5,6])                         # a is array-like\n    >>> np.empty_like(a)\n    array([[-1073741821, -1073741821,           3],    #random\n           [          0,           0, -1073741821]])\n    >>> a = np.array([[1., 2., 3.],[4.,5.,6.]])\n    >>> np.empty_like(a)\n    array([[ -2.00000715e+000,   1.48219694e-323,  -2.00000572e+000],#random\n           [  4.38791518e-305,  -2.00000715e+000,   4.17269252e-309]])"
    pass

error = _mod_builtins.Exception
class flagsobj(_mod_builtins.object):
    __class__ = flagsobj
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def aligned(self):
        pass
    
    @property
    def behaved(self):
        pass
    
    @property
    def c_contiguous(self):
        pass
    
    @property
    def carray(self):
        pass
    
    @property
    def contiguous(self):
        pass
    
    @property
    def f_contiguous(self):
        pass
    
    @property
    def farray(self):
        pass
    
    @property
    def fnc(self):
        pass
    
    @property
    def forc(self):
        pass
    
    @property
    def fortran(self):
        pass
    
    @property
    def num(self):
        pass
    
    @property
    def owndata(self):
        pass
    
    @property
    def updateifcopy(self):
        pass
    
    @property
    def writeable(self):
        pass
    
    @property
    def writebackifcopy(self):
        pass
    

class flatiter(_mod_builtins.object):
    "Flat iterator object to iterate over arrays.\n\n    A `flatiter` iterator is returned by ``x.flat`` for any array `x`.\n    It allows iterating over the array as if it were a 1-D array,\n    either in a for-loop or by calling its `next` method.\n\n    Iteration is done in row-major, C-style order (the last\n    index varying the fastest). The iterator can also be indexed using\n    basic slicing or advanced indexing.\n\n    See Also\n    --------\n    ndarray.flat : Return a flat iterator over an array.\n    ndarray.flatten : Returns a flattened copy of an array.\n\n    Notes\n    -----\n    A `flatiter` iterator can not be constructed directly from Python code\n    by calling the `flatiter` constructor.\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> fl = x.flat\n    >>> type(fl)\n    <type 'numpy.flatiter'>\n    >>> for item in fl:\n    ...     print(item)\n    ...\n    0\n    1\n    2\n    3\n    4\n    5\n\n    >>> fl[2:4]\n    array([2, 3])"
    def __array__(self, type=None):
        '__array__(type=None) Get array from iterator'
        pass
    
    __class__ = flatiter
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        "Flat iterator object to iterate over arrays.\n\n    A `flatiter` iterator is returned by ``x.flat`` for any array `x`.\n    It allows iterating over the array as if it were a 1-D array,\n    either in a for-loop or by calling its `next` method.\n\n    Iteration is done in row-major, C-style order (the last\n    index varying the fastest). The iterator can also be indexed using\n    basic slicing or advanced indexing.\n\n    See Also\n    --------\n    ndarray.flat : Return a flat iterator over an array.\n    ndarray.flatten : Returns a flattened copy of an array.\n\n    Notes\n    -----\n    A `flatiter` iterator can not be constructed directly from Python code\n    by calling the `flatiter` constructor.\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> fl = x.flat\n    >>> type(fl)\n    <type 'numpy.flatiter'>\n    >>> for item in fl:\n    ...     print(item)\n    ...\n    0\n    1\n    2\n    3\n    4\n    5\n\n    >>> fl[2:4]\n    array([2, 3])"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return flatiter()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def base(self):
        'A reference to the array that is iterated over.\n\n    Examples\n    --------\n    >>> x = np.arange(5)\n    >>> fl = x.flat\n    >>> fl.base is x\n    True'
        pass
    
    @property
    def coords(self):
        'An N-dimensional tuple of current coordinates.\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> fl = x.flat\n    >>> fl.coords\n    (0, 0)\n    >>> fl.next()\n    0\n    >>> fl.coords\n    (0, 1)'
        pass
    
    def copy(self):
        'copy()\n\n    Get a copy of the iterator as a 1-D array.\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> x\n    array([[0, 1, 2],\n           [3, 4, 5]])\n    >>> fl = x.flat\n    >>> fl.copy()\n    array([0, 1, 2, 3, 4, 5])'
        pass
    
    @property
    def index(self):
        'Current flat index into the array.\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> fl = x.flat\n    >>> fl.index\n    0\n    >>> fl.next()\n    0\n    >>> fl.index\n    1'
        pass
    

def format_longfloat():
    pass

def frombuffer(buffer, dtype=float, count=-1, offset=0):
    "frombuffer(buffer, dtype=float, count=-1, offset=0)\n\n    Interpret a buffer as a 1-dimensional array.\n\n    Parameters\n    ----------\n    buffer : buffer_like\n        An object that exposes the buffer interface.\n    dtype : data-type, optional\n        Data-type of the returned array; default: float.\n    count : int, optional\n        Number of items to read. ``-1`` means all data in the buffer.\n    offset : int, optional\n        Start reading the buffer from this offset (in bytes); default: 0.\n\n    Notes\n    -----\n    If the buffer has data that is not in machine byte-order, this should\n    be specified as part of the data-type, e.g.::\n\n      >>> dt = np.dtype(int)\n      >>> dt = dt.newbyteorder('>')\n      >>> np.frombuffer(buf, dtype=dt)\n\n    The data of the resulting array will not be byteswapped, but will be\n    interpreted correctly.\n\n    Examples\n    --------\n    >>> s = 'hello world'\n    >>> np.frombuffer(s, dtype='S1', count=5, offset=6)\n    array(['w', 'o', 'r', 'l', 'd'],\n          dtype='|S1')\n\n    >>> np.frombuffer(b'\\x01\\x02', dtype=np.uint8)\n    array([1, 2], dtype=uint8)\n    >>> np.frombuffer(b'\\x01\\x02\\x03\\x04\\x05', dtype=np.uint8, count=3)\n    array([1, 2, 3], dtype=uint8)"
    pass

def fromfile(file, dtype=float, count=-1, sep=''):
    'fromfile(file, dtype=float, count=-1, sep=\'\')\n\n    Construct an array from data in a text or binary file.\n\n    A highly efficient way of reading binary data with a known data-type,\n    as well as parsing simply formatted text files.  Data written using the\n    `tofile` method can be read using this function.\n\n    Parameters\n    ----------\n    file : file or str\n        Open file object or filename.\n    dtype : data-type\n        Data type of the returned array.\n        For binary files, it is used to determine the size and byte-order\n        of the items in the file.\n    count : int\n        Number of items to read. ``-1`` means all items (i.e., the complete\n        file).\n    sep : str\n        Separator between items if file is a text file.\n        Empty ("") separator means the file should be treated as binary.\n        Spaces (" ") in the separator match zero or more whitespace characters.\n        A separator consisting only of spaces must match at least one\n        whitespace.\n\n    See also\n    --------\n    load, save\n    ndarray.tofile\n    loadtxt : More flexible way of loading data from a text file.\n\n    Notes\n    -----\n    Do not rely on the combination of `tofile` and `fromfile` for\n    data storage, as the binary files generated are are not platform\n    independent.  In particular, no byte-order or data-type information is\n    saved.  Data can be stored in the platform independent ``.npy`` format\n    using `save` and `load` instead.\n\n    Examples\n    --------\n    Construct an ndarray:\n\n    >>> dt = np.dtype([(\'time\', [(\'min\', int), (\'sec\', int)]),\n    ...                (\'temp\', float)])\n    >>> x = np.zeros((1,), dtype=dt)\n    >>> x[\'time\'][\'min\'] = 10; x[\'temp\'] = 98.25\n    >>> x\n    array([((10, 0), 98.25)],\n          dtype=[(\'time\', [(\'min\', \'<i4\'), (\'sec\', \'<i4\')]), (\'temp\', \'<f8\')])\n\n    Save the raw data to disk:\n\n    >>> import os\n    >>> fname = os.tmpnam()\n    >>> x.tofile(fname)\n\n    Read the raw data from disk:\n\n    >>> np.fromfile(fname, dtype=dt)\n    array([((10, 0), 98.25)],\n          dtype=[(\'time\', [(\'min\', \'<i4\'), (\'sec\', \'<i4\')]), (\'temp\', \'<f8\')])\n\n    The recommended way to store and load data:\n\n    >>> np.save(fname, x)\n    >>> np.load(fname + \'.npy\')\n    array([((10, 0), 98.25)],\n          dtype=[(\'time\', [(\'min\', \'<i4\'), (\'sec\', \'<i4\')]), (\'temp\', \'<f8\')])'
    pass

def fromiter(iterable, dtype, count=-1):
    'fromiter(iterable, dtype, count=-1)\n\n    Create a new 1-dimensional array from an iterable object.\n\n    Parameters\n    ----------\n    iterable : iterable object\n        An iterable object providing data for the array.\n    dtype : data-type\n        The data-type of the returned array.\n    count : int, optional\n        The number of items to read from *iterable*.  The default is -1,\n        which means all data is read.\n\n    Returns\n    -------\n    out : ndarray\n        The output array.\n\n    Notes\n    -----\n    Specify `count` to improve performance.  It allows ``fromiter`` to\n    pre-allocate the output array, instead of resizing it on demand.\n\n    Examples\n    --------\n    >>> iterable = (x*x for x in range(5))\n    >>> np.fromiter(iterable, float)\n    array([  0.,   1.,   4.,   9.,  16.])'
    pass

def fromstring(string, dtype=float, count=-1, sep=''):
    "fromstring(string, dtype=float, count=-1, sep='')\n\n    A new 1-D array initialized from text data in a string.\n\n    Parameters\n    ----------\n    string : str\n        A string containing the data.\n    dtype : data-type, optional\n        The data type of the array; default: float.  For binary input data,\n        the data must be in exactly this format.\n    count : int, optional\n        Read this number of `dtype` elements from the data.  If this is\n        negative (the default), the count will be determined from the\n        length of the data.\n    sep : str, optional\n        The string separating numbers in the data; extra whitespace between\n        elements is also ignored.\n\n        .. deprecated:: 1.14\n            If this argument is not provided, `fromstring` falls back on the\n            behaviour of `frombuffer` after encoding unicode string inputs as\n            either utf-8 (python 3), or the default encoding (python 2).\n\n    Returns\n    -------\n    arr : ndarray\n        The constructed array.\n\n    Raises\n    ------\n    ValueError\n        If the string is not the correct size to satisfy the requested\n        `dtype` and `count`.\n\n    See Also\n    --------\n    frombuffer, fromfile, fromiter\n\n    Examples\n    --------\n    >>> np.fromstring('1 2', dtype=int, sep=' ')\n    array([1, 2])\n    >>> np.fromstring('1, 2', dtype=int, sep=',')\n    array([1, 2])"
    pass

def inner(a, b):
    'inner(a, b)\n\n    Inner product of two arrays.\n\n    Ordinary inner product of vectors for 1-D arrays (without complex\n    conjugation), in higher dimensions a sum product over the last axes.\n\n    Parameters\n    ----------\n    a, b : array_like\n        If `a` and `b` are nonscalar, their last dimensions must match.\n\n    Returns\n    -------\n    out : ndarray\n        `out.shape = a.shape[:-1] + b.shape[:-1]`\n\n    Raises\n    ------\n    ValueError\n        If the last dimension of `a` and `b` has different size.\n\n    See Also\n    --------\n    tensordot : Sum products over arbitrary axes.\n    dot : Generalised matrix product, using second last dimension of `b`.\n    einsum : Einstein summation convention.\n\n    Notes\n    -----\n    For vectors (1-D arrays) it computes the ordinary inner-product::\n\n        np.inner(a, b) = sum(a[:]*b[:])\n\n    More generally, if `ndim(a) = r > 0` and `ndim(b) = s > 0`::\n\n        np.inner(a, b) = np.tensordot(a, b, axes=(-1,-1))\n\n    or explicitly::\n\n        np.inner(a, b)[i0,...,ir-1,j0,...,js-1]\n             = sum(a[i0,...,ir-1,:]*b[j0,...,js-1,:])\n\n    In addition `a` or `b` may be scalars, in which case::\n\n       np.inner(a,b) = a*b\n\n    Examples\n    --------\n    Ordinary inner product for vectors:\n\n    >>> a = np.array([1,2,3])\n    >>> b = np.array([0,1,0])\n    >>> np.inner(a, b)\n    2\n\n    A multidimensional example:\n\n    >>> a = np.arange(24).reshape((2,3,4))\n    >>> b = np.arange(4)\n    >>> np.inner(a, b)\n    array([[ 14,  38,  62],\n           [ 86, 110, 134]])\n\n    An example where `b` is a scalar:\n\n    >>> np.inner(np.eye(2), 7)\n    array([[ 7.,  0.],\n           [ 0.,  7.]])'
    pass

def int_asbuffer():
    pass

def interp():
    pass

def interp_complex():
    pass

def is_busday(dates, weekmask='1111100', holidays=None, busdaycal=None, out=None):
    'is_busday(dates, weekmask=\'1111100\', holidays=None, busdaycal=None, out=None)\n\n    Calculates which of the given dates are valid days, and which are not.\n\n    .. versionadded:: 1.7.0\n\n    Parameters\n    ----------\n    dates : array_like of datetime64[D]\n        The array of dates to process.\n    weekmask : str or array_like of bool, optional\n        A seven-element array indicating which of Monday through Sunday are\n        valid days. May be specified as a length-seven list or array, like\n        [1,1,1,1,1,0,0]; a length-seven string, like \'1111100\'; or a string\n        like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for\n        weekdays, optionally separated by white space. Valid abbreviations\n        are: Mon Tue Wed Thu Fri Sat Sun\n    holidays : array_like of datetime64[D], optional\n        An array of dates to consider as invalid dates.  They may be\n        specified in any order, and NaT (not-a-time) dates are ignored.\n        This list is saved in a normalized form that is suited for\n        fast calculations of valid days.\n    busdaycal : busdaycalendar, optional\n        A `busdaycalendar` object which specifies the valid days. If this\n        parameter is provided, neither weekmask nor holidays may be\n        provided.\n    out : array of bool, optional\n        If provided, this array is filled with the result.\n\n    Returns\n    -------\n    out : array of bool\n        An array with the same shape as ``dates``, containing True for\n        each valid day, and False for each invalid day.\n\n    See Also\n    --------\n    busdaycalendar: An object that specifies a custom set of valid days.\n    busday_offset : Applies an offset counted in valid days.\n    busday_count : Counts how many valid days are in a half-open date range.\n\n    Examples\n    --------\n    >>> # The weekdays are Friday, Saturday, and Monday\n    ... np.is_busday([\'2011-07-01\', \'2011-07-02\', \'2011-07-18\'],\n    ...                 holidays=[\'2011-07-01\', \'2011-07-04\', \'2011-07-17\'])\n    array([False, False,  True], dtype=\'bool\')'
    pass

def lexsort(keys, axis=-1):
    'lexsort(keys, axis=-1)\n\n    Perform an indirect stable sort using a sequence of keys.\n\n    Given multiple sorting keys, which can be interpreted as columns in a\n    spreadsheet, lexsort returns an array of integer indices that describes\n    the sort order by multiple columns. The last key in the sequence is used\n    for the primary sort order, the second-to-last key for the secondary sort\n    order, and so on. The keys argument must be a sequence of objects that\n    can be converted to arrays of the same shape. If a 2D array is provided\n    for the keys argument, it\'s rows are interpreted as the sorting keys and\n    sorting is according to the last row, second last row etc.\n\n    Parameters\n    ----------\n    keys : (k, N) array or tuple containing k (N,)-shaped sequences\n        The `k` different "columns" to be sorted.  The last column (or row if\n        `keys` is a 2D array) is the primary sort key.\n    axis : int, optional\n        Axis to be indirectly sorted.  By default, sort over the last axis.\n\n    Returns\n    -------\n    indices : (N,) ndarray of ints\n        Array of indices that sort the keys along the specified axis.\n\n    See Also\n    --------\n    argsort : Indirect sort.\n    ndarray.sort : In-place sort.\n    sort : Return a sorted copy of an array.\n\n    Examples\n    --------\n    Sort names: first by surname, then by name.\n\n    >>> surnames =    (\'Hertz\',    \'Galilei\', \'Hertz\')\n    >>> first_names = (\'Heinrich\', \'Galileo\', \'Gustav\')\n    >>> ind = np.lexsort((first_names, surnames))\n    >>> ind\n    array([1, 2, 0])\n\n    >>> [surnames[i] + ", " + first_names[i] for i in ind]\n    [\'Galilei, Galileo\', \'Hertz, Gustav\', \'Hertz, Heinrich\']\n\n    Sort two columns of numbers:\n\n    >>> a = [1,5,1,4,3,4,4] # First column\n    >>> b = [9,4,0,4,0,2,1] # Second column\n    >>> ind = np.lexsort((b,a)) # Sort by a, then by b\n    >>> print(ind)\n    [2 0 4 6 5 3 1]\n\n    >>> [(a[i],b[i]) for i in ind]\n    [(1, 0), (1, 9), (3, 0), (4, 1), (4, 2), (4, 4), (5, 4)]\n\n    Note that sorting is first according to the elements of ``a``.\n    Secondary sorting is according to the elements of ``b``.\n\n    A normal ``argsort`` would have yielded:\n\n    >>> [(a[i],b[i]) for i in np.argsort(a)]\n    [(1, 9), (1, 0), (3, 0), (4, 4), (4, 2), (4, 1), (5, 4)]\n\n    Structured arrays are sorted lexically by ``argsort``:\n\n    >>> x = np.array([(1,9), (5,4), (1,0), (4,4), (3,0), (4,2), (4,1)],\n    ...              dtype=np.dtype([(\'x\', int), (\'y\', int)]))\n\n    >>> np.argsort(x) # or np.argsort(x, order=(\'x\', \'y\'))\n    array([2, 0, 4, 6, 5, 3, 1])'
    pass

def matmul(a, b, out=None):
    "matmul(a, b, out=None)\n\n    Matrix product of two arrays.\n\n    The behavior depends on the arguments in the following way.\n\n    - If both arguments are 2-D they are multiplied like conventional\n      matrices.\n    - If either argument is N-D, N > 2, it is treated as a stack of\n      matrices residing in the last two indexes and broadcast accordingly.\n    - If the first argument is 1-D, it is promoted to a matrix by\n      prepending a 1 to its dimensions. After matrix multiplication\n      the prepended 1 is removed.\n    - If the second argument is 1-D, it is promoted to a matrix by\n      appending a 1 to its dimensions. After matrix multiplication\n      the appended 1 is removed.\n\n    Multiplication by a scalar is not allowed, use ``*`` instead. Note that\n    multiplying a stack of matrices with a vector will result in a stack of\n    vectors, but matmul will not recognize it as such.\n\n    ``matmul`` differs from ``dot`` in two important ways.\n\n    - Multiplication by scalars is not allowed.\n    - Stacks of matrices are broadcast together as if the matrices\n      were elements.\n\n    .. warning::\n       This function is preliminary and included in NumPy 1.10.0 for testing\n       and documentation. Its semantics will not change, but the number and\n       order of the optional arguments will.\n\n    .. versionadded:: 1.10.0\n\n    Parameters\n    ----------\n    a : array_like\n        First argument.\n    b : array_like\n        Second argument.\n    out : ndarray, optional\n        Output argument. This must have the exact kind that would be returned\n        if it was not used. In particular, it must have the right type, must be\n        C-contiguous, and its dtype must be the dtype that would be returned\n        for `dot(a,b)`. This is a performance feature. Therefore, if these\n        conditions are not met, an exception is raised, instead of attempting\n        to be flexible.\n\n    Returns\n    -------\n    output : ndarray\n        Returns the dot product of `a` and `b`.  If `a` and `b` are both\n        1-D arrays then a scalar is returned; otherwise an array is\n        returned.  If `out` is given, then it is returned.\n\n    Raises\n    ------\n    ValueError\n        If the last dimension of `a` is not the same size as\n        the second-to-last dimension of `b`.\n\n        If scalar value is passed.\n\n    See Also\n    --------\n    vdot : Complex-conjugating dot product.\n    tensordot : Sum products over arbitrary axes.\n    einsum : Einstein summation convention.\n    dot : alternative matrix product with different broadcasting rules.\n\n    Notes\n    -----\n    The matmul function implements the semantics of the `@` operator introduced\n    in Python 3.5 following PEP465.\n\n    Examples\n    --------\n    For 2-D arrays it is the matrix product:\n\n    >>> a = [[1, 0], [0, 1]]\n    >>> b = [[4, 1], [2, 2]]\n    >>> np.matmul(a, b)\n    array([[4, 1],\n           [2, 2]])\n\n    For 2-D mixed with 1-D, the result is the usual.\n\n    >>> a = [[1, 0], [0, 1]]\n    >>> b = [1, 2]\n    >>> np.matmul(a, b)\n    array([1, 2])\n    >>> np.matmul(b, a)\n    array([1, 2])\n\n\n    Broadcasting is conventional for stacks of arrays\n\n    >>> a = np.arange(2*2*4).reshape((2,2,4))\n    >>> b = np.arange(2*2*4).reshape((2,4,2))\n    >>> np.matmul(a,b).shape\n    (2, 2, 2)\n    >>> np.matmul(a,b)[0,1,1]\n    98\n    >>> sum(a[0,1,:] * b[0,:,1])\n    98\n\n    Vector, vector returns the scalar inner product, but neither argument\n    is complex-conjugated:\n\n    >>> np.matmul([2j, 3j], [2j, 3j])\n    (-13+0j)\n\n    Scalar multiplication raises an error.\n\n    >>> np.matmul([1,2], 3)\n    Traceback (most recent call last):\n    ...\n    ValueError: Scalar operands are not allowed, use '*' instead"
    pass

def may_share_memory(a, b, max_work=None):
    'may_share_memory(a, b, max_work=None)\n\n    Determine if two arrays might share memory\n\n    A return of True does not necessarily mean that the two arrays\n    share any element.  It just means that they *might*.\n\n    Only the memory bounds of a and b are checked by default.\n\n    Parameters\n    ----------\n    a, b : ndarray\n        Input arrays\n    max_work : int, optional\n        Effort to spend on solving the overlap problem.  See\n        `shares_memory` for details.  Default for ``may_share_memory``\n        is to do a bounds check.\n\n    Returns\n    -------\n    out : bool\n\n    See Also\n    --------\n    shares_memory\n\n    Examples\n    --------\n    >>> np.may_share_memory(np.array([1,2]), np.array([5,8,9]))\n    False\n    >>> x = np.zeros([3, 4])\n    >>> np.may_share_memory(x[:,0], x[:,1])\n    True'
    pass

def min_scalar_type(a):
    "min_scalar_type(a)\n\n    For scalar ``a``, returns the data type with the smallest size\n    and smallest scalar kind which can hold its value.  For non-scalar\n    array ``a``, returns the vector's dtype unmodified.\n\n    Floating point values are not demoted to integers,\n    and complex values are not demoted to floats.\n\n    Parameters\n    ----------\n    a : scalar or array_like\n        The value whose minimal data type is to be found.\n\n    Returns\n    -------\n    out : dtype\n        The minimal data type.\n\n    Notes\n    -----\n    .. versionadded:: 1.6.0\n\n    See Also\n    --------\n    result_type, promote_types, dtype, can_cast\n\n    Examples\n    --------\n    >>> np.min_scalar_type(10)\n    dtype('uint8')\n\n    >>> np.min_scalar_type(-260)\n    dtype('int16')\n\n    >>> np.min_scalar_type(3.1)\n    dtype('float16')\n\n    >>> np.min_scalar_type(1e50)\n    dtype('float64')\n\n    >>> np.min_scalar_type(np.arange(4,dtype='f8'))\n    dtype('float64')"
    pass

class ndarray(_mod_builtins.object):
    'ndarray(shape, dtype=float, buffer=None, offset=0,\n            strides=None, order=None)\n\n    An array object represents a multidimensional, homogeneous array\n    of fixed-size items.  An associated data-type object describes the\n    format of each element in the array (its byte-order, how many bytes it\n    occupies in memory, whether it is an integer, a floating point number,\n    or something else, etc.)\n\n    Arrays should be constructed using `array`, `zeros` or `empty` (refer\n    to the See Also section below).  The parameters given here refer to\n    a low-level method (`ndarray(...)`) for instantiating an array.\n\n    For more information, refer to the `numpy` module and examine the\n    methods and attributes of an array.\n\n    Parameters\n    ----------\n    (for the __new__ method; see Notes below)\n\n    shape : tuple of ints\n        Shape of created array.\n    dtype : data-type, optional\n        Any object that can be interpreted as a numpy data type.\n    buffer : object exposing buffer interface, optional\n        Used to fill the array with data.\n    offset : int, optional\n        Offset of array data in buffer.\n    strides : tuple of ints, optional\n        Strides of data in memory.\n    order : {\'C\', \'F\'}, optional\n        Row-major (C-style) or column-major (Fortran-style) order.\n\n    Attributes\n    ----------\n    T : ndarray\n        Transpose of the array.\n    data : buffer\n        The array\'s elements, in memory.\n    dtype : dtype object\n        Describes the format of the elements in the array.\n    flags : dict\n        Dictionary containing information related to memory use, e.g.,\n        \'C_CONTIGUOUS\', \'OWNDATA\', \'WRITEABLE\', etc.\n    flat : numpy.flatiter object\n        Flattened version of the array as an iterator.  The iterator\n        allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for\n        assignment examples; TODO).\n    imag : ndarray\n        Imaginary part of the array.\n    real : ndarray\n        Real part of the array.\n    size : int\n        Number of elements in the array.\n    itemsize : int\n        The memory use of each array element in bytes.\n    nbytes : int\n        The total number of bytes required to store the array data,\n        i.e., ``itemsize * size``.\n    ndim : int\n        The array\'s number of dimensions.\n    shape : tuple of ints\n        Shape of the array.\n    strides : tuple of ints\n        The step-size required to move from one element to the next in\n        memory. For example, a contiguous ``(3, 4)`` array of type\n        ``int16`` in C-order has strides ``(8, 2)``.  This implies that\n        to move from element to element in memory requires jumps of 2 bytes.\n        To move from row-to-row, one needs to jump 8 bytes at a time\n        (``2 * 4``).\n    ctypes : ctypes object\n        Class containing properties of the array needed for interaction\n        with ctypes.\n    base : ndarray\n        If the array is a view into another array, that array is its `base`\n        (unless that array is also a view).  The `base` array is where the\n        array data is actually stored.\n\n    See Also\n    --------\n    array : Construct an array.\n    zeros : Create an array, each element of which is zero.\n    empty : Create an array, but leave its allocated memory unchanged (i.e.,\n            it contains "garbage").\n    dtype : Create a data-type.\n\n    Notes\n    -----\n    There are two modes of creating an array using ``__new__``:\n\n    1. If `buffer` is None, then only `shape`, `dtype`, and `order`\n       are used.\n    2. If `buffer` is an object exposing the buffer interface, then\n       all keywords are interpreted.\n\n    No ``__init__`` method is needed because the array is fully initialized\n    after the ``__new__`` method.\n\n    Examples\n    --------\n    These examples illustrate the low-level `ndarray` constructor.  Refer\n    to the `See Also` section above for easier ways of constructing an\n    ndarray.\n\n    First mode, `buffer` is None:\n\n    >>> np.ndarray(shape=(2,2), dtype=float, order=\'F\')\n    array([[ -1.13698227e+002,   4.25087011e-303],\n           [  2.88528414e-306,   3.27025015e-309]])         #random\n\n    Second mode:\n\n    >>> np.ndarray((2,), buffer=np.array([1,2,3]),\n    ...            offset=np.int_().itemsize,\n    ...            dtype=int) # offset = 1*itemsize, i.e. skip first element\n    array([2, 3])'
    @property
    def T(self):
        'Same as self.transpose(), except that self is returned if\n    self.ndim < 2.\n\n    Examples\n    --------\n    >>> x = np.array([[1.,2.],[3.,4.]])\n    >>> x\n    array([[ 1.,  2.],\n           [ 3.,  4.]])\n    >>> x.T\n    array([[ 1.,  3.],\n           [ 2.,  4.]])\n    >>> x = np.array([1.,2.,3.,4.])\n    >>> x\n    array([ 1.,  2.,  3.,  4.])\n    >>> x.T\n    array([ 1.,  2.,  3.,  4.])'
        pass
    
    def __abs__(self):
        'abs(self)'
        return ndarray()
    
    def __add__(self, value):
        'Return self+value.'
        return ndarray()
    
    def __and__(self, value):
        'Return self&value.'
        return ndarray()
    
    def __array__(self):
        'a.__array__(|dtype) -> reference if type unchanged, copy otherwise.\n\n    Returns either a new reference to self if dtype is not given or a new array\n    of provided data type if dtype is different from the current dtype of the\n    array.'
        pass
    
    @property
    def __array_finalize__(self):
        'None.'
        pass
    
    @property
    def __array_interface__(self):
        'Array protocol: Python side.'
        pass
    
    def __array_prepare__(self):
        'a.__array_prepare__(obj) -> Object of same type as ndarray object obj.'
        pass
    
    @property
    def __array_priority__(self):
        'Array priority.'
        pass
    
    @property
    def __array_struct__(self):
        'Array protocol: C-struct side.'
        pass
    
    def __array_ufunc__(self):
        pass
    
    def __array_wrap__(self):
        'a.__array_wrap__(obj) -> Object of same type as ndarray object a.'
        pass
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = ndarray
    def __complex__(self):
        pass
    
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __copy__(self):
        "a.__copy__()\n\n    Used if :func:`copy.copy` is called on an array. Returns a copy of the array.\n\n    Equivalent to ``a.copy(order='K')``."
        pass
    
    def __deepcopy__(self):
        'a.__deepcopy__(memo, /) -> Deep copy of array.\n\n    Used if :func:`copy.deepcopy` is called on an array.'
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __divmod__(self, value):
        'Return divmod(self, value).'
        return (0, 0)
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __format__(self, format_spec):
        return ''
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __iand__(self, value):
        'Return self&=value.'
        return None
    
    def __ifloordiv__(self, value):
        'Return self//=value.'
        pass
    
    def __ilshift__(self, value):
        'Return self<<=value.'
        pass
    
    def __imatmul__(self, value):
        'Return self@=value.'
        pass
    
    def __imod__(self, value):
        'Return self%=value.'
        pass
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        return 0
    
    def __init__(self, *args, **kwargs):
        'ndarray(shape, dtype=float, buffer=None, offset=0,\n            strides=None, order=None)\n\n    An array object represents a multidimensional, homogeneous array\n    of fixed-size items.  An associated data-type object describes the\n    format of each element in the array (its byte-order, how many bytes it\n    occupies in memory, whether it is an integer, a floating point number,\n    or something else, etc.)\n\n    Arrays should be constructed using `array`, `zeros` or `empty` (refer\n    to the See Also section below).  The parameters given here refer to\n    a low-level method (`ndarray(...)`) for instantiating an array.\n\n    For more information, refer to the `numpy` module and examine the\n    methods and attributes of an array.\n\n    Parameters\n    ----------\n    (for the __new__ method; see Notes below)\n\n    shape : tuple of ints\n        Shape of created array.\n    dtype : data-type, optional\n        Any object that can be interpreted as a numpy data type.\n    buffer : object exposing buffer interface, optional\n        Used to fill the array with data.\n    offset : int, optional\n        Offset of array data in buffer.\n    strides : tuple of ints, optional\n        Strides of data in memory.\n    order : {\'C\', \'F\'}, optional\n        Row-major (C-style) or column-major (Fortran-style) order.\n\n    Attributes\n    ----------\n    T : ndarray\n        Transpose of the array.\n    data : buffer\n        The array\'s elements, in memory.\n    dtype : dtype object\n        Describes the format of the elements in the array.\n    flags : dict\n        Dictionary containing information related to memory use, e.g.,\n        \'C_CONTIGUOUS\', \'OWNDATA\', \'WRITEABLE\', etc.\n    flat : numpy.flatiter object\n        Flattened version of the array as an iterator.  The iterator\n        allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for\n        assignment examples; TODO).\n    imag : ndarray\n        Imaginary part of the array.\n    real : ndarray\n        Real part of the array.\n    size : int\n        Number of elements in the array.\n    itemsize : int\n        The memory use of each array element in bytes.\n    nbytes : int\n        The total number of bytes required to store the array data,\n        i.e., ``itemsize * size``.\n    ndim : int\n        The array\'s number of dimensions.\n    shape : tuple of ints\n        Shape of the array.\n    strides : tuple of ints\n        The step-size required to move from one element to the next in\n        memory. For example, a contiguous ``(3, 4)`` array of type\n        ``int16`` in C-order has strides ``(8, 2)``.  This implies that\n        to move from element to element in memory requires jumps of 2 bytes.\n        To move from row-to-row, one needs to jump 8 bytes at a time\n        (``2 * 4``).\n    ctypes : ctypes object\n        Class containing properties of the array needed for interaction\n        with ctypes.\n    base : ndarray\n        If the array is a view into another array, that array is its `base`\n        (unless that array is also a view).  The `base` array is where the\n        array data is actually stored.\n\n    See Also\n    --------\n    array : Construct an array.\n    zeros : Create an array, each element of which is zero.\n    empty : Create an array, but leave its allocated memory unchanged (i.e.,\n            it contains "garbage").\n    dtype : Create a data-type.\n\n    Notes\n    -----\n    There are two modes of creating an array using ``__new__``:\n\n    1. If `buffer` is None, then only `shape`, `dtype`, and `order`\n       are used.\n    2. If `buffer` is an object exposing the buffer interface, then\n       all keywords are interpreted.\n\n    No ``__init__`` method is needed because the array is fully initialized\n    after the ``__new__`` method.\n\n    Examples\n    --------\n    These examples illustrate the low-level `ndarray` constructor.  Refer\n    to the `See Also` section above for easier ways of constructing an\n    ndarray.\n\n    First mode, `buffer` is None:\n\n    >>> np.ndarray(shape=(2,2), dtype=float, order=\'F\')\n    array([[ -1.13698227e+002,   4.25087011e-303],\n           [  2.88528414e-306,   3.27025015e-309]])         #random\n\n    Second mode:\n\n    >>> np.ndarray((2,), buffer=np.array([1,2,3]),\n    ...            offset=np.int_().itemsize,\n    ...            dtype=int) # offset = 1*itemsize, i.e. skip first element\n    array([2, 3])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __invert__(self):
        '~self'
        return ndarray()
    
    def __ior__(self, value):
        'Return self|=value.'
        return None
    
    def __ipow__(self, value):
        'Return self**=value.'
        pass
    
    def __irshift__(self, value):
        'Return self>>=value.'
        pass
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return ndarray()
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __ixor__(self, value):
        'Return self^=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lshift__(self, value):
        'Return self<<value.'
        return ndarray()
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __matmul__(self, value):
        'Return self@value.'
        pass
    
    def __mod__(self, value):
        'Return self%value.'
        return ndarray()
    
    def __mul__(self, value):
        'Return self*value.'
        return ndarray()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return ndarray()
    
    def __or__(self, value):
        'Return self|value.'
        return ndarray()
    
    def __pos__(self):
        '+self'
        return ndarray()
    
    def __pow__(self, value, mod):
        'Return pow(self, value, mod).'
        return ndarray()
    
    def __radd__(self, value):
        'Return value+self.'
        return ndarray()
    
    def __rand__(self, value):
        'Return value&self.'
        return ndarray()
    
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        return (0, 0)
    
    def __reduce__(self):
        'a.__reduce__()\n\n    For pickling.'
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return ndarray()
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return ndarray()
    
    def __rmatmul__(self, value):
        'Return value@self.'
        pass
    
    def __rmod__(self, value):
        'Return value%self.'
        return ndarray()
    
    def __rmul__(self, value):
        'Return value*self.'
        return ndarray()
    
    def __ror__(self, value):
        'Return value|self.'
        return ndarray()
    
    def __rpow__(self, value, mod):
        'Return pow(value, self, mod).'
        return ndarray()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return ndarray()
    
    def __rshift__(self, value):
        'Return self>>value.'
        return ndarray()
    
    def __rsub__(self, value):
        'Return value-self.'
        return ndarray()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return ndarray()
    
    def __rxor__(self, value):
        'Return value^self.'
        return ndarray()
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        "a.__setstate__(state, /)\n\n    For unpickling.\n\n    The `state` argument must be a sequence that contains the following\n    elements:\n\n    Parameters\n    ----------\n    version : int\n        optional pickle version. If omitted defaults to 0.\n    shape : tuple\n    dtype : data-type\n    isFortran : bool\n    rawdata : string or list\n        a binary string with the data (or a list if 'a' is an object array)"
        return None
    
    def __sizeof__(self):
        return 0
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return ndarray()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def __xor__(self, value):
        'Return self^value.'
        return ndarray()
    
    def all(self):
        'a.all(axis=None, out=None, keepdims=False)\n\n    Returns True if all elements evaluate to True.\n\n    Refer to `numpy.all` for full documentation.\n\n    See Also\n    --------\n    numpy.all : equivalent function'
        pass
    
    def any(self):
        'a.any(axis=None, out=None, keepdims=False)\n\n    Returns True if any of the elements of `a` evaluate to True.\n\n    Refer to `numpy.any` for full documentation.\n\n    See Also\n    --------\n    numpy.any : equivalent function'
        pass
    
    def argmax(self):
        'a.argmax(axis=None, out=None)\n\n    Return indices of the maximum values along the given axis.\n\n    Refer to `numpy.argmax` for full documentation.\n\n    See Also\n    --------\n    numpy.argmax : equivalent function'
        pass
    
    def argmin(self):
        'a.argmin(axis=None, out=None)\n\n    Return indices of the minimum values along the given axis of `a`.\n\n    Refer to `numpy.argmin` for detailed documentation.\n\n    See Also\n    --------\n    numpy.argmin : equivalent function'
        pass
    
    def argpartition(self):
        "a.argpartition(kth, axis=-1, kind='introselect', order=None)\n\n    Returns the indices that would partition this array.\n\n    Refer to `numpy.argpartition` for full documentation.\n\n    .. versionadded:: 1.8.0\n\n    See Also\n    --------\n    numpy.argpartition : equivalent function"
        pass
    
    def argsort(self):
        "a.argsort(axis=-1, kind='quicksort', order=None)\n\n    Returns the indices that would sort this array.\n\n    Refer to `numpy.argsort` for full documentation.\n\n    See Also\n    --------\n    numpy.argsort : equivalent function"
        pass
    
    def astype(self):
        "a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)\n\n    Copy of the array, cast to a specified type.\n\n    Parameters\n    ----------\n    dtype : str or dtype\n        Typecode or data-type to which the array is cast.\n    order : {'C', 'F', 'A', 'K'}, optional\n        Controls the memory layout order of the result.\n        'C' means C order, 'F' means Fortran order, 'A'\n        means 'F' order if all the arrays are Fortran contiguous,\n        'C' order otherwise, and 'K' means as close to the\n        order the array elements appear in memory as possible.\n        Default is 'K'.\n    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional\n        Controls what kind of data casting may occur. Defaults to 'unsafe'\n        for backwards compatibility.\n\n          * 'no' means the data types should not be cast at all.\n          * 'equiv' means only byte-order changes are allowed.\n          * 'safe' means only casts which can preserve values are allowed.\n          * 'same_kind' means only safe casts or casts within a kind,\n            like float64 to float32, are allowed.\n          * 'unsafe' means any data conversions may be done.\n    subok : bool, optional\n        If True, then sub-classes will be passed-through (default), otherwise\n        the returned array will be forced to be a base-class array.\n    copy : bool, optional\n        By default, astype always returns a newly allocated array. If this\n        is set to false, and the `dtype`, `order`, and `subok`\n        requirements are satisfied, the input array is returned instead\n        of a copy.\n\n    Returns\n    -------\n    arr_t : ndarray\n        Unless `copy` is False and the other conditions for returning the input\n        array are satisfied (see description for `copy` input parameter), `arr_t`\n        is a new array of the same shape as the input array, with dtype, order\n        given by `dtype`, `order`.\n\n    Notes\n    -----\n    Starting in NumPy 1.9, astype method now returns an error if the string\n    dtype to cast to is not long enough in 'safe' casting mode to hold the max\n    value of integer/float array that is being casted. Previously the casting\n    was allowed even if the result was truncated.\n\n    Raises\n    ------\n    ComplexWarning\n        When casting from complex to float or int. To avoid this,\n        one should use ``a.real.astype(t)``.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 2.5])\n    >>> x\n    array([ 1. ,  2. ,  2.5])\n\n    >>> x.astype(int)\n    array([1, 2, 2])"
        pass
    
    @property
    def base(self):
        'Base object if memory is from some other object.\n\n    Examples\n    --------\n    The base of an array that owns its memory is None:\n\n    >>> x = np.array([1,2,3,4])\n    >>> x.base is None\n    True\n\n    Slicing creates a view, whose memory is shared with x:\n\n    >>> y = x[2:]\n    >>> y.base is x\n    True'
        pass
    
    def byteswap(self):
        "a.byteswap(inplace=False)\n\n    Swap the bytes of the array elements\n\n    Toggle between low-endian and big-endian data representation by\n    returning a byteswapped array, optionally swapped in-place.\n\n    Parameters\n    ----------\n    inplace : bool, optional\n        If ``True``, swap bytes in-place, default is ``False``.\n\n    Returns\n    -------\n    out : ndarray\n        The byteswapped array. If `inplace` is ``True``, this is\n        a view to self.\n\n    Examples\n    --------\n    >>> A = np.array([1, 256, 8755], dtype=np.int16)\n    >>> map(hex, A)\n    ['0x1', '0x100', '0x2233']\n    >>> A.byteswap(inplace=True)\n    array([  256,     1, 13090], dtype=int16)\n    >>> map(hex, A)\n    ['0x100', '0x1', '0x3322']\n\n    Arrays of strings are not swapped\n\n    >>> A = np.array(['ceg', 'fac'])\n    >>> A.byteswap()\n    array(['ceg', 'fac'],\n          dtype='|S3')"
        pass
    
    def choose(self):
        "a.choose(choices, out=None, mode='raise')\n\n    Use an index array to construct a new array from a set of choices.\n\n    Refer to `numpy.choose` for full documentation.\n\n    See Also\n    --------\n    numpy.choose : equivalent function"
        pass
    
    def clip(self):
        'a.clip(min=None, max=None, out=None)\n\n    Return an array whose values are limited to ``[min, max]``.\n    One of max or min must be given.\n\n    Refer to `numpy.clip` for full documentation.\n\n    See Also\n    --------\n    numpy.clip : equivalent function'
        pass
    
    def compress(self):
        'a.compress(condition, axis=None, out=None)\n\n    Return selected slices of this array along given axis.\n\n    Refer to `numpy.compress` for full documentation.\n\n    See Also\n    --------\n    numpy.compress : equivalent function'
        pass
    
    def conj(self):
        'a.conj()\n\n    Complex-conjugate all elements.\n\n    Refer to `numpy.conjugate` for full documentation.\n\n    See Also\n    --------\n    numpy.conjugate : equivalent function'
        pass
    
    def conjugate(self):
        'a.conjugate()\n\n    Return the complex conjugate, element-wise.\n\n    Refer to `numpy.conjugate` for full documentation.\n\n    See Also\n    --------\n    numpy.conjugate : equivalent function'
        pass
    
    def copy(self):
        "a.copy(order='C')\n\n    Return a copy of the array.\n\n    Parameters\n    ----------\n    order : {'C', 'F', 'A', 'K'}, optional\n        Controls the memory layout of the copy. 'C' means C-order,\n        'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,\n        'C' otherwise. 'K' means match the layout of `a` as closely\n        as possible. (Note that this function and :func:`numpy.copy` are very\n        similar, but have different default values for their order=\n        arguments.)\n\n    See also\n    --------\n    numpy.copy\n    numpy.copyto\n\n    Examples\n    --------\n    >>> x = np.array([[1,2,3],[4,5,6]], order='F')\n\n    >>> y = x.copy()\n\n    >>> x.fill(0)\n\n    >>> x\n    array([[0, 0, 0],\n           [0, 0, 0]])\n\n    >>> y\n    array([[1, 2, 3],\n           [4, 5, 6]])\n\n    >>> y.flags['C_CONTIGUOUS']\n    True"
        pass
    
    @property
    def ctypes(self):
        'An object to simplify the interaction of the array with the ctypes\n    module.\n\n    This attribute creates an object that makes it easier to use arrays\n    when calling shared libraries with the ctypes module. The returned\n    object has, among others, data, shape, and strides attributes (see\n    Notes below) which themselves return ctypes objects that can be used\n    as arguments to a shared library.\n\n    Parameters\n    ----------\n    None\n\n    Returns\n    -------\n    c : Python object\n        Possessing attributes data, shape, strides, etc.\n\n    See Also\n    --------\n    numpy.ctypeslib\n\n    Notes\n    -----\n    Below are the public attributes of this object which were documented\n    in "Guide to NumPy" (we have omitted undocumented public attributes,\n    as well as documented private attributes):\n\n    * data: A pointer to the memory area of the array as a Python integer.\n      This memory area may contain data that is not aligned, or not in correct\n      byte-order. The memory area may not even be writeable. The array\n      flags and data-type of this array should be respected when passing this\n      attribute to arbitrary C-code to avoid trouble that can include Python\n      crashing. User Beware! The value of this attribute is exactly the same\n      as self._array_interface_[\'data\'][0].\n\n    * shape (c_intp*self.ndim): A ctypes array of length self.ndim where\n      the basetype is the C-integer corresponding to dtype(\'p\') on this\n      platform. This base-type could be c_int, c_long, or c_longlong\n      depending on the platform. The c_intp type is defined accordingly in\n      numpy.ctypeslib. The ctypes array contains the shape of the underlying\n      array.\n\n    * strides (c_intp*self.ndim): A ctypes array of length self.ndim where\n      the basetype is the same as for the shape attribute. This ctypes array\n      contains the strides information from the underlying array. This strides\n      information is important for showing how many bytes must be jumped to\n      get to the next element in the array.\n\n    * data_as(obj): Return the data pointer cast to a particular c-types object.\n      For example, calling self._as_parameter_ is equivalent to\n      self.data_as(ctypes.c_void_p). Perhaps you want to use the data as a\n      pointer to a ctypes array of floating-point data:\n      self.data_as(ctypes.POINTER(ctypes.c_double)).\n\n    * shape_as(obj): Return the shape tuple as an array of some other c-types\n      type. For example: self.shape_as(ctypes.c_short).\n\n    * strides_as(obj): Return the strides tuple as an array of some other\n      c-types type. For example: self.strides_as(ctypes.c_longlong).\n\n    Be careful using the ctypes attribute - especially on temporary\n    arrays or arrays constructed on the fly. For example, calling\n    ``(a+b).ctypes.data_as(ctypes.c_void_p)`` returns a pointer to memory\n    that is invalid because the array created as (a+b) is deallocated\n    before the next Python statement. You can avoid this problem using\n    either ``c=a+b`` or ``ct=(a+b).ctypes``. In the latter case, ct will\n    hold a reference to the array until ct is deleted or re-assigned.\n\n    If the ctypes module is not available, then the ctypes attribute\n    of array objects still returns something useful, but ctypes objects\n    are not returned and errors may be raised instead. In particular,\n    the object will still have the as parameter attribute which will\n    return an integer equal to the data attribute.\n\n    Examples\n    --------\n    >>> import ctypes\n    >>> x\n    array([[0, 1],\n           [2, 3]])\n    >>> x.ctypes.data\n    30439712\n    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long))\n    <ctypes.LP_c_long object at 0x01F01300>\n    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long)).contents\n    c_long(0)\n    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_longlong)).contents\n    c_longlong(4294967296L)\n    >>> x.ctypes.shape\n    <numpy.core._internal.c_long_Array_2 object at 0x01FFD580>\n    >>> x.ctypes.shape_as(ctypes.c_long)\n    <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>\n    >>> x.ctypes.strides\n    <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>\n    >>> x.ctypes.strides_as(ctypes.c_longlong)\n    <numpy.core._internal.c_longlong_Array_2 object at 0x01F01300>'
        pass
    
    def cumprod(self):
        'a.cumprod(axis=None, dtype=None, out=None)\n\n    Return the cumulative product of the elements along the given axis.\n\n    Refer to `numpy.cumprod` for full documentation.\n\n    See Also\n    --------\n    numpy.cumprod : equivalent function'
        pass
    
    def cumsum(self):
        'a.cumsum(axis=None, dtype=None, out=None)\n\n    Return the cumulative sum of the elements along the given axis.\n\n    Refer to `numpy.cumsum` for full documentation.\n\n    See Also\n    --------\n    numpy.cumsum : equivalent function'
        pass
    
    @property
    def data(self):
        "Python buffer object pointing to the start of the array's data."
        pass
    
    def diagonal(self):
        'a.diagonal(offset=0, axis1=0, axis2=1)\n\n    Return specified diagonals. In NumPy 1.9 the returned array is a\n    read-only view instead of a copy as in previous NumPy versions.  In\n    a future version the read-only restriction will be removed.\n\n    Refer to :func:`numpy.diagonal` for full documentation.\n\n    See Also\n    --------\n    numpy.diagonal : equivalent function'
        pass
    
    def dot(self):
        'a.dot(b, out=None)\n\n    Dot product of two arrays.\n\n    Refer to `numpy.dot` for full documentation.\n\n    See Also\n    --------\n    numpy.dot : equivalent function\n\n    Examples\n    --------\n    >>> a = np.eye(2)\n    >>> b = np.ones((2, 2)) * 2\n    >>> a.dot(b)\n    array([[ 2.,  2.],\n           [ 2.,  2.]])\n\n    This array method can be conveniently chained:\n\n    >>> a.dot(b).dot(b)\n    array([[ 8.,  8.],\n           [ 8.,  8.]])'
        pass
    
    @property
    def dtype(self):
        "Data-type of the array's elements.\n\n    Parameters\n    ----------\n    None\n\n    Returns\n    -------\n    d : numpy dtype object\n\n    See Also\n    --------\n    numpy.dtype\n\n    Examples\n    --------\n    >>> x\n    array([[0, 1],\n           [2, 3]])\n    >>> x.dtype\n    dtype('int32')\n    >>> type(x.dtype)\n    <type 'numpy.dtype'>"
        pass
    
    def dump(self):
        'a.dump(file)\n\n    Dump a pickle of the array to the specified file.\n    The array can be read back with pickle.load or numpy.load.\n\n    Parameters\n    ----------\n    file : str\n        A string naming the dump file.'
        pass
    
    def dumps(self):
        'a.dumps()\n\n    Returns the pickle of the array as a string.\n    pickle.loads or numpy.loads will convert the string back to an array.\n\n    Parameters\n    ----------\n    None'
        pass
    
    def fill(self):
        'a.fill(value)\n\n    Fill the array with a scalar value.\n\n    Parameters\n    ----------\n    value : scalar\n        All elements of `a` will be assigned this value.\n\n    Examples\n    --------\n    >>> a = np.array([1, 2])\n    >>> a.fill(0)\n    >>> a\n    array([0, 0])\n    >>> a = np.empty(2)\n    >>> a.fill(1)\n    >>> a\n    array([ 1.,  1.])'
        pass
    
    @property
    def flags(self):
        "Information about the memory layout of the array.\n\n    Attributes\n    ----------\n    C_CONTIGUOUS (C)\n        The data is in a single, C-style contiguous segment.\n    F_CONTIGUOUS (F)\n        The data is in a single, Fortran-style contiguous segment.\n    OWNDATA (O)\n        The array owns the memory it uses or borrows it from another object.\n    WRITEABLE (W)\n        The data area can be written to.  Setting this to False locks\n        the data, making it read-only.  A view (slice, etc.) inherits WRITEABLE\n        from its base array at creation time, but a view of a writeable\n        array may be subsequently locked while the base array remains writeable.\n        (The opposite is not true, in that a view of a locked array may not\n        be made writeable.  However, currently, locking a base object does not\n        lock any views that already reference it, so under that circumstance it\n        is possible to alter the contents of a locked array via a previously\n        created writeable view onto it.)  Attempting to change a non-writeable\n        array raises a RuntimeError exception.\n    ALIGNED (A)\n        The data and all elements are aligned appropriately for the hardware.\n    WRITEBACKIFCOPY (X)\n        This array is a copy of some other array. The C-API function\n        PyArray_ResolveWritebackIfCopy must be called before deallocating\n        to the base array will be updated with the contents of this array.\n    UPDATEIFCOPY (U)\n        (Deprecated, use WRITEBACKIFCOPY) This array is a copy of some other array.\n        When this array is\n        deallocated, the base array will be updated with the contents of\n        this array.\n    FNC\n        F_CONTIGUOUS and not C_CONTIGUOUS.\n    FORC\n        F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).\n    BEHAVED (B)\n        ALIGNED and WRITEABLE.\n    CARRAY (CA)\n        BEHAVED and C_CONTIGUOUS.\n    FARRAY (FA)\n        BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.\n\n    Notes\n    -----\n    The `flags` object can be accessed dictionary-like (as in ``a.flags['WRITEABLE']``),\n    or by using lowercased attribute names (as in ``a.flags.writeable``). Short flag\n    names are only supported in dictionary access.\n\n    Only the WRITEBACKIFCOPY, UPDATEIFCOPY, WRITEABLE, and ALIGNED flags can be\n    changed by the user, via direct assignment to the attribute or dictionary\n    entry, or by calling `ndarray.setflags`.\n\n    The array flags cannot be set arbitrarily:\n\n    - UPDATEIFCOPY can only be set ``False``.\n    - WRITEBACKIFCOPY can only be set ``False``.\n    - ALIGNED can only be set ``True`` if the data is truly aligned.\n    - WRITEABLE can only be set ``True`` if the array owns its own memory\n      or the ultimate owner of the memory exposes a writeable buffer\n      interface or is a string.\n\n    Arrays can be both C-style and Fortran-style contiguous simultaneously.\n    This is clear for 1-dimensional arrays, but can also be true for higher\n    dimensional arrays.\n\n    Even for contiguous arrays a stride for a given dimension\n    ``arr.strides[dim]`` may be *arbitrary* if ``arr.shape[dim] == 1``\n    or the array has no elements.\n    It does *not* generally hold that ``self.strides[-1] == self.itemsize``\n    for C-style contiguous arrays or ``self.strides[0] == self.itemsize`` for\n    Fortran-style contiguous arrays is true."
        pass
    
    @property
    def flat(self):
        "A 1-D iterator over the array.\n\n    This is a `numpy.flatiter` instance, which acts similarly to, but is not\n    a subclass of, Python's built-in iterator object.\n\n    See Also\n    --------\n    flatten : Return a copy of the array collapsed into one dimension.\n\n    flatiter\n\n    Examples\n    --------\n    >>> x = np.arange(1, 7).reshape(2, 3)\n    >>> x\n    array([[1, 2, 3],\n           [4, 5, 6]])\n    >>> x.flat[3]\n    4\n    >>> x.T\n    array([[1, 4],\n           [2, 5],\n           [3, 6]])\n    >>> x.T.flat[3]\n    5\n    >>> type(x.flat)\n    <type 'numpy.flatiter'>\n\n    An assignment example:\n\n    >>> x.flat = 3; x\n    array([[3, 3, 3],\n           [3, 3, 3]])\n    >>> x.flat[[1,4]] = 1; x\n    array([[3, 1, 3],\n           [3, 1, 3]])"
        pass
    
    def flatten(self):
        "a.flatten(order='C')\n\n    Return a copy of the array collapsed into one dimension.\n\n    Parameters\n    ----------\n    order : {'C', 'F', 'A', 'K'}, optional\n        'C' means to flatten in row-major (C-style) order.\n        'F' means to flatten in column-major (Fortran-\n        style) order. 'A' means to flatten in column-major\n        order if `a` is Fortran *contiguous* in memory,\n        row-major order otherwise. 'K' means to flatten\n        `a` in the order the elements occur in memory.\n        The default is 'C'.\n\n    Returns\n    -------\n    y : ndarray\n        A copy of the input array, flattened to one dimension.\n\n    See Also\n    --------\n    ravel : Return a flattened array.\n    flat : A 1-D flat iterator over the array.\n\n    Examples\n    --------\n    >>> a = np.array([[1,2], [3,4]])\n    >>> a.flatten()\n    array([1, 2, 3, 4])\n    >>> a.flatten('F')\n    array([1, 3, 2, 4])"
        pass
    
    def getfield(self):
        'a.getfield(dtype, offset=0)\n\n    Returns a field of the given array as a certain type.\n\n    A field is a view of the array data with a given data-type. The values in\n    the view are determined by the given type and the offset into the current\n    array in bytes. The offset needs to be such that the view dtype fits in the\n    array dtype; for example an array of dtype complex128 has 16-byte elements.\n    If taking a view with a 32-bit integer (4 bytes), the offset needs to be\n    between 0 and 12 bytes.\n\n    Parameters\n    ----------\n    dtype : str or dtype\n        The data type of the view. The dtype size of the view can not be larger\n        than that of the array itself.\n    offset : int\n        Number of bytes to skip before beginning the element view.\n\n    Examples\n    --------\n    >>> x = np.diag([1.+1.j]*2)\n    >>> x[1, 1] = 2 + 4.j\n    >>> x\n    array([[ 1.+1.j,  0.+0.j],\n           [ 0.+0.j,  2.+4.j]])\n    >>> x.getfield(np.float64)\n    array([[ 1.,  0.],\n           [ 0.,  2.]])\n\n    By choosing an offset of 8 bytes we can select the complex part of the\n    array for our view:\n\n    >>> x.getfield(np.float64, offset=8)\n    array([[ 1.,  0.],\n       [ 0.,  4.]])'
        pass
    
    @property
    def imag(self):
        "The imaginary part of the array.\n\n    Examples\n    --------\n    >>> x = np.sqrt([1+0j, 0+1j])\n    >>> x.imag\n    array([ 0.        ,  0.70710678])\n    >>> x.imag.dtype\n    dtype('float64')"
        pass
    
    def item(self):
        "a.item(*args)\n\n    Copy an element of an array to a standard Python scalar and return it.\n\n    Parameters\n    ----------\n    \\*args : Arguments (variable number and type)\n\n        * none: in this case, the method only works for arrays\n          with one element (`a.size == 1`), which element is\n          copied into a standard Python scalar object and returned.\n\n        * int_type: this argument is interpreted as a flat index into\n          the array, specifying which element to copy and return.\n\n        * tuple of int_types: functions as does a single int_type argument,\n          except that the argument is interpreted as an nd-index into the\n          array.\n\n    Returns\n    -------\n    z : Standard Python scalar object\n        A copy of the specified element of the array as a suitable\n        Python scalar\n\n    Notes\n    -----\n    When the data type of `a` is longdouble or clongdouble, item() returns\n    a scalar array object because there is no available Python scalar that\n    would not lose information. Void arrays return a buffer object for item(),\n    unless fields are defined, in which case a tuple is returned.\n\n    `item` is very similar to a[args], except, instead of an array scalar,\n    a standard Python scalar is returned. This can be useful for speeding up\n    access to elements of the array and doing arithmetic on elements of the\n    array using Python's optimized math.\n\n    Examples\n    --------\n    >>> x = np.random.randint(9, size=(3, 3))\n    >>> x\n    array([[3, 1, 7],\n           [2, 8, 3],\n           [8, 5, 3]])\n    >>> x.item(3)\n    2\n    >>> x.item(7)\n    5\n    >>> x.item((0, 1))\n    1\n    >>> x.item((2, 2))\n    3"
        pass
    
    def itemset(self):
        "a.itemset(*args)\n\n    Insert scalar into an array (scalar is cast to array's dtype, if possible)\n\n    There must be at least 1 argument, and define the last argument\n    as *item*.  Then, ``a.itemset(*args)`` is equivalent to but faster\n    than ``a[args] = item``.  The item should be a scalar value and `args`\n    must select a single item in the array `a`.\n\n    Parameters\n    ----------\n    \\*args : Arguments\n        If one argument: a scalar, only used in case `a` is of size 1.\n        If two arguments: the last argument is the value to be set\n        and must be a scalar, the first argument specifies a single array\n        element location. It is either an int or a tuple.\n\n    Notes\n    -----\n    Compared to indexing syntax, `itemset` provides some speed increase\n    for placing a scalar into a particular location in an `ndarray`,\n    if you must do this.  However, generally this is discouraged:\n    among other problems, it complicates the appearance of the code.\n    Also, when using `itemset` (and `item`) inside a loop, be sure\n    to assign the methods to a local variable to avoid the attribute\n    look-up at each loop iteration.\n\n    Examples\n    --------\n    >>> x = np.random.randint(9, size=(3, 3))\n    >>> x\n    array([[3, 1, 7],\n           [2, 8, 3],\n           [8, 5, 3]])\n    >>> x.itemset(4, 0)\n    >>> x.itemset((2, 2), 9)\n    >>> x\n    array([[3, 1, 7],\n           [2, 0, 3],\n           [8, 5, 9]])"
        pass
    
    @property
    def itemsize(self):
        'Length of one array element in bytes.\n\n    Examples\n    --------\n    >>> x = np.array([1,2,3], dtype=np.float64)\n    >>> x.itemsize\n    8\n    >>> x = np.array([1,2,3], dtype=np.complex128)\n    >>> x.itemsize\n    16'
        pass
    
    def max(self):
        'a.max(axis=None, out=None, keepdims=False)\n\n    Return the maximum along a given axis.\n\n    Refer to `numpy.amax` for full documentation.\n\n    See Also\n    --------\n    numpy.amax : equivalent function'
        pass
    
    def mean(self):
        'a.mean(axis=None, dtype=None, out=None, keepdims=False)\n\n    Returns the average of the array elements along given axis.\n\n    Refer to `numpy.mean` for full documentation.\n\n    See Also\n    --------\n    numpy.mean : equivalent function'
        pass
    
    def min(self):
        'a.min(axis=None, out=None, keepdims=False)\n\n    Return the minimum along a given axis.\n\n    Refer to `numpy.amin` for full documentation.\n\n    See Also\n    --------\n    numpy.amin : equivalent function'
        pass
    
    @property
    def nbytes(self):
        'Total bytes consumed by the elements of the array.\n\n    Notes\n    -----\n    Does not include memory consumed by non-element attributes of the\n    array object.\n\n    Examples\n    --------\n    >>> x = np.zeros((3,5,2), dtype=np.complex128)\n    >>> x.nbytes\n    480\n    >>> np.prod(x.shape) * x.itemsize\n    480'
        pass
    
    @property
    def ndim(self):
        'Number of array dimensions.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3])\n    >>> x.ndim\n    1\n    >>> y = np.zeros((2, 3, 4))\n    >>> y.ndim\n    3'
        pass
    
    def newbyteorder(self):
        "arr.newbyteorder(new_order='S')\n\n    Return the array with the same data viewed with a different byte order.\n\n    Equivalent to::\n\n        arr.view(arr.dtype.newbytorder(new_order))\n\n    Changes are also made in all fields and sub-arrays of the array data\n    type.\n\n\n\n    Parameters\n    ----------\n    new_order : string, optional\n        Byte order to force; a value from the byte order specifications\n        below. `new_order` codes can be any of:\n\n        * 'S' - swap dtype from current to opposite endian\n        * {'<', 'L'} - little endian\n        * {'>', 'B'} - big endian\n        * {'=', 'N'} - native order\n        * {'|', 'I'} - ignore (no change to byte order)\n\n        The default value ('S') results in swapping the current\n        byte order. The code does a case-insensitive check on the first\n        letter of `new_order` for the alternatives above.  For example,\n        any of 'B' or 'b' or 'biggish' are valid to specify big-endian.\n\n\n    Returns\n    -------\n    new_arr : array\n        New array object with the dtype reflecting given change to the\n        byte order."
        pass
    
    def nonzero(self):
        'a.nonzero()\n\n    Return the indices of the elements that are non-zero.\n\n    Refer to `numpy.nonzero` for full documentation.\n\n    See Also\n    --------\n    numpy.nonzero : equivalent function'
        pass
    
    def partition(self):
        "a.partition(kth, axis=-1, kind='introselect', order=None)\n\n    Rearranges the elements in the array in such a way that the value of the\n    element in kth position is in the position it would be in a sorted array.\n    All elements smaller than the kth element are moved before this element and\n    all equal or greater are moved behind it. The ordering of the elements in\n    the two partitions is undefined.\n\n    .. versionadded:: 1.8.0\n\n    Parameters\n    ----------\n    kth : int or sequence of ints\n        Element index to partition by. The kth element value will be in its\n        final sorted position and all smaller elements will be moved before it\n        and all equal or greater elements behind it.\n        The order of all elements in the partitions is undefined.\n        If provided with a sequence of kth it will partition all elements\n        indexed by kth of them into their sorted position at once.\n    axis : int, optional\n        Axis along which to sort. Default is -1, which means sort along the\n        last axis.\n    kind : {'introselect'}, optional\n        Selection algorithm. Default is 'introselect'.\n    order : str or list of str, optional\n        When `a` is an array with fields defined, this argument specifies\n        which fields to compare first, second, etc. A single field can\n        be specified as a string, and not all fields need to be specified,\n        but unspecified fields will still be used, in the order in which\n        they come up in the dtype, to break ties.\n\n    See Also\n    --------\n    numpy.partition : Return a parititioned copy of an array.\n    argpartition : Indirect partition.\n    sort : Full sort.\n\n    Notes\n    -----\n    See ``np.partition`` for notes on the different algorithms.\n\n    Examples\n    --------\n    >>> a = np.array([3, 4, 2, 1])\n    >>> a.partition(3)\n    >>> a\n    array([2, 1, 3, 4])\n\n    >>> a.partition((1, 3))\n    array([1, 2, 3, 4])"
        pass
    
    def prod(self):
        'a.prod(axis=None, dtype=None, out=None, keepdims=False)\n\n    Return the product of the array elements over the given axis\n\n    Refer to `numpy.prod` for full documentation.\n\n    See Also\n    --------\n    numpy.prod : equivalent function'
        pass
    
    def ptp(self):
        'a.ptp(axis=None, out=None, keepdims=False)\n\n    Peak to peak (maximum - minimum) value along a given axis.\n\n    Refer to `numpy.ptp` for full documentation.\n\n    See Also\n    --------\n    numpy.ptp : equivalent function'
        pass
    
    def put(self):
        "a.put(indices, values, mode='raise')\n\n    Set ``a.flat[n] = values[n]`` for all `n` in indices.\n\n    Refer to `numpy.put` for full documentation.\n\n    See Also\n    --------\n    numpy.put : equivalent function"
        pass
    
    def ravel(self):
        'a.ravel([order])\n\n    Return a flattened array.\n\n    Refer to `numpy.ravel` for full documentation.\n\n    See Also\n    --------\n    numpy.ravel : equivalent function\n\n    ndarray.flat : a flat iterator on the array.'
        pass
    
    @property
    def real(self):
        "The real part of the array.\n\n    Examples\n    --------\n    >>> x = np.sqrt([1+0j, 0+1j])\n    >>> x.real\n    array([ 1.        ,  0.70710678])\n    >>> x.real.dtype\n    dtype('float64')\n\n    See Also\n    --------\n    numpy.real : equivalent function"
        pass
    
    def repeat(self):
        'a.repeat(repeats, axis=None)\n\n    Repeat elements of an array.\n\n    Refer to `numpy.repeat` for full documentation.\n\n    See Also\n    --------\n    numpy.repeat : equivalent function'
        pass
    
    def reshape(self):
        "a.reshape(shape, order='C')\n\n    Returns an array containing the same data with a new shape.\n\n    Refer to `numpy.reshape` for full documentation.\n\n    See Also\n    --------\n    numpy.reshape : equivalent function\n\n    Notes\n    -----\n    Unlike the free function `numpy.reshape`, this method on `ndarray` allows\n    the elements of the shape parameter to be passed in as separate arguments.\n    For example, ``a.reshape(10, 11)`` is equivalent to\n    ``a.reshape((10, 11))``."
        pass
    
    def resize(self):
        "a.resize(new_shape, refcheck=True)\n\n    Change shape and size of array in-place.\n\n    Parameters\n    ----------\n    new_shape : tuple of ints, or `n` ints\n        Shape of resized array.\n    refcheck : bool, optional\n        If False, reference count will not be checked. Default is True.\n\n    Returns\n    -------\n    None\n\n    Raises\n    ------\n    ValueError\n        If `a` does not own its own data or references or views to it exist,\n        and the data memory must be changed.\n        PyPy only: will always raise if the data memory must be changed, since\n        there is no reliable way to determine if references or views to it\n        exist.\n\n    SystemError\n        If the `order` keyword argument is specified. This behaviour is a\n        bug in NumPy.\n\n    See Also\n    --------\n    resize : Return a new array with the specified shape.\n\n    Notes\n    -----\n    This reallocates space for the data area if necessary.\n\n    Only contiguous arrays (data elements consecutive in memory) can be\n    resized.\n\n    The purpose of the reference count check is to make sure you\n    do not use this array as a buffer for another Python object and then\n    reallocate the memory. However, reference counts can increase in\n    other ways so if you are sure that you have not shared the memory\n    for this array with another Python object, then you may safely set\n    `refcheck` to False.\n\n    Examples\n    --------\n    Shrinking an array: array is flattened (in the order that the data are\n    stored in memory), resized, and reshaped:\n\n    >>> a = np.array([[0, 1], [2, 3]], order='C')\n    >>> a.resize((2, 1))\n    >>> a\n    array([[0],\n           [1]])\n\n    >>> a = np.array([[0, 1], [2, 3]], order='F')\n    >>> a.resize((2, 1))\n    >>> a\n    array([[0],\n           [2]])\n\n    Enlarging an array: as above, but missing entries are filled with zeros:\n\n    >>> b = np.array([[0, 1], [2, 3]])\n    >>> b.resize(2, 3) # new_shape parameter doesn't have to be a tuple\n    >>> b\n    array([[0, 1, 2],\n           [3, 0, 0]])\n\n    Referencing an array prevents resizing...\n\n    >>> c = a\n    >>> a.resize((1, 1))\n    Traceback (most recent call last):\n    ...\n    ValueError: cannot resize an array that has been referenced ...\n\n    Unless `refcheck` is False:\n\n    >>> a.resize((1, 1), refcheck=False)\n    >>> a\n    array([[0]])\n    >>> c\n    array([[0]])"
        pass
    
    def round(self):
        'a.round(decimals=0, out=None)\n\n    Return `a` with each element rounded to the given number of decimals.\n\n    Refer to `numpy.around` for full documentation.\n\n    See Also\n    --------\n    numpy.around : equivalent function'
        pass
    
    def searchsorted(self):
        "a.searchsorted(v, side='left', sorter=None)\n\n    Find indices where elements of v should be inserted in a to maintain order.\n\n    For full documentation, see `numpy.searchsorted`\n\n    See Also\n    --------\n    numpy.searchsorted : equivalent function"
        pass
    
    def setfield(self):
        "a.setfield(val, dtype, offset=0)\n\n    Put a value into a specified place in a field defined by a data-type.\n\n    Place `val` into `a`'s field defined by `dtype` and beginning `offset`\n    bytes into the field.\n\n    Parameters\n    ----------\n    val : object\n        Value to be placed in field.\n    dtype : dtype object\n        Data-type of the field in which to place `val`.\n    offset : int, optional\n        The number of bytes into the field at which to place `val`.\n\n    Returns\n    -------\n    None\n\n    See Also\n    --------\n    getfield\n\n    Examples\n    --------\n    >>> x = np.eye(3)\n    >>> x.getfield(np.float64)\n    array([[ 1.,  0.,  0.],\n           [ 0.,  1.,  0.],\n           [ 0.,  0.,  1.]])\n    >>> x.setfield(3, np.int32)\n    >>> x.getfield(np.int32)\n    array([[3, 3, 3],\n           [3, 3, 3],\n           [3, 3, 3]])\n    >>> x\n    array([[  1.00000000e+000,   1.48219694e-323,   1.48219694e-323],\n           [  1.48219694e-323,   1.00000000e+000,   1.48219694e-323],\n           [  1.48219694e-323,   1.48219694e-323,   1.00000000e+000]])\n    >>> x.setfield(np.eye(3), np.int32)\n    >>> x\n    array([[ 1.,  0.,  0.],\n           [ 0.,  1.,  0.],\n           [ 0.,  0.,  1.]])"
        pass
    
    def setflags(self):
        'a.setflags(write=None, align=None, uic=None)\n\n    Set array flags WRITEABLE, ALIGNED, (WRITEBACKIFCOPY and UPDATEIFCOPY),\n    respectively.\n\n    These Boolean-valued flags affect how numpy interprets the memory\n    area used by `a` (see Notes below). The ALIGNED flag can only\n    be set to True if the data is actually aligned according to the type.\n    The WRITEBACKIFCOPY and (deprecated) UPDATEIFCOPY flags can never be set\n    to True. The flag WRITEABLE can only be set to True if the array owns its\n    own memory, or the ultimate owner of the memory exposes a writeable buffer\n    interface, or is a string. (The exception for string is made so that\n    unpickling can be done without copying memory.)\n\n    Parameters\n    ----------\n    write : bool, optional\n        Describes whether or not `a` can be written to.\n    align : bool, optional\n        Describes whether or not `a` is aligned properly for its type.\n    uic : bool, optional\n        Describes whether or not `a` is a copy of another "base" array.\n\n    Notes\n    -----\n    Array flags provide information about how the memory area used\n    for the array is to be interpreted. There are 7 Boolean flags\n    in use, only four of which can be changed by the user:\n    WRITEBACKIFCOPY, UPDATEIFCOPY, WRITEABLE, and ALIGNED.\n\n    WRITEABLE (W) the data area can be written to;\n\n    ALIGNED (A) the data and strides are aligned appropriately for the hardware\n    (as determined by the compiler);\n\n    UPDATEIFCOPY (U) (deprecated), replaced by WRITEBACKIFCOPY;\n\n    WRITEBACKIFCOPY (X) this array is a copy of some other array (referenced\n    by .base). When the C-API function PyArray_ResolveWritebackIfCopy is\n    called, the base array will be updated with the contents of this array.\n\n    All flags can be accessed using the single (upper case) letter as well\n    as the full name.\n\n    Examples\n    --------\n    >>> y\n    array([[3, 1, 7],\n           [2, 0, 0],\n           [8, 5, 9]])\n    >>> y.flags\n      C_CONTIGUOUS : True\n      F_CONTIGUOUS : False\n      OWNDATA : True\n      WRITEABLE : True\n      ALIGNED : True\n      WRITEBACKIFCOPY : False\n      UPDATEIFCOPY : False\n    >>> y.setflags(write=0, align=0)\n    >>> y.flags\n      C_CONTIGUOUS : True\n      F_CONTIGUOUS : False\n      OWNDATA : True\n      WRITEABLE : False\n      ALIGNED : False\n      WRITEBACKIFCOPY : False\n      UPDATEIFCOPY : False\n    >>> y.setflags(uic=1)\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    ValueError: cannot set WRITEBACKIFCOPY flag to True'
        pass
    
    @property
    def shape(self):
        'Tuple of array dimensions.\n\n    The shape property is usually used to get the current shape of an array,\n    but may also be used to reshape the array in-place by assigning a tuple of\n    array dimensions to it.  As with `numpy.reshape`, one of the new shape\n    dimensions can be -1, in which case its value is inferred from the size of\n    the array and the remaining dimensions. Reshaping an array in-place will\n    fail if a copy is required.\n\n    Examples\n    --------\n    >>> x = np.array([1, 2, 3, 4])\n    >>> x.shape\n    (4,)\n    >>> y = np.zeros((2, 3, 4))\n    >>> y.shape\n    (2, 3, 4)\n    >>> y.shape = (3, 8)\n    >>> y\n    array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],\n           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],\n           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])\n    >>> y.shape = (3, 6)\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    ValueError: total size of new array must be unchanged\n    >>> np.zeros((4,2))[::2].shape = (-1,)\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    AttributeError: incompatible shape for a non-contiguous array\n\n    See Also\n    --------\n    numpy.reshape : similar function\n    ndarray.reshape : similar method'
        pass
    
    @property
    def size(self):
        "Number of elements in the array.\n\n    Equal to ``np.prod(a.shape)``, i.e., the product of the array's\n    dimensions.\n\n    Notes\n    -----\n    `a.size` returns a standard arbitrary precision Python integer. This \n    may not be the case with other methods of obtaining the same value\n    (like the suggested ``np.prod(a.shape)``, which returns an instance\n    of ``np.int_``), and may be relevant if the value is used further in\n    calculations that may overflow a fixed size integer type.\n\n    Examples\n    --------\n    >>> x = np.zeros((3, 5, 2), dtype=np.complex128)\n    >>> x.size\n    30\n    >>> np.prod(x.shape)\n    30"
        pass
    
    def sort(self):
        "a.sort(axis=-1, kind='quicksort', order=None)\n\n    Sort an array, in-place.\n\n    Parameters\n    ----------\n    axis : int, optional\n        Axis along which to sort. Default is -1, which means sort along the\n        last axis.\n    kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional\n        Sorting algorithm. Default is 'quicksort'.\n    order : str or list of str, optional\n        When `a` is an array with fields defined, this argument specifies\n        which fields to compare first, second, etc.  A single field can\n        be specified as a string, and not all fields need be specified,\n        but unspecified fields will still be used, in the order in which\n        they come up in the dtype, to break ties.\n\n    See Also\n    --------\n    numpy.sort : Return a sorted copy of an array.\n    argsort : Indirect sort.\n    lexsort : Indirect stable sort on multiple keys.\n    searchsorted : Find elements in sorted array.\n    partition: Partial sort.\n\n    Notes\n    -----\n    See ``sort`` for notes on the different sorting algorithms.\n\n    Examples\n    --------\n    >>> a = np.array([[1,4], [3,1]])\n    >>> a.sort(axis=1)\n    >>> a\n    array([[1, 4],\n           [1, 3]])\n    >>> a.sort(axis=0)\n    >>> a\n    array([[1, 3],\n           [1, 4]])\n\n    Use the `order` keyword to specify a field to use when sorting a\n    structured array:\n\n    >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])\n    >>> a.sort(order='y')\n    >>> a\n    array([('c', 1), ('a', 2)],\n          dtype=[('x', '|S1'), ('y', '<i4')])"
        pass
    
    def squeeze(self):
        'a.squeeze(axis=None)\n\n    Remove single-dimensional entries from the shape of `a`.\n\n    Refer to `numpy.squeeze` for full documentation.\n\n    See Also\n    --------\n    numpy.squeeze : equivalent function'
        pass
    
    def std(self):
        'a.std(axis=None, dtype=None, out=None, ddof=0, keepdims=False)\n\n    Returns the standard deviation of the array elements along given axis.\n\n    Refer to `numpy.std` for full documentation.\n\n    See Also\n    --------\n    numpy.std : equivalent function'
        pass
    
    @property
    def strides(self):
        'Tuple of bytes to step in each dimension when traversing an array.\n\n    The byte offset of element ``(i[0], i[1], ..., i[n])`` in an array `a`\n    is::\n\n        offset = sum(np.array(i) * a.strides)\n\n    A more detailed explanation of strides can be found in the\n    "ndarray.rst" file in the NumPy reference guide.\n\n    Notes\n    -----\n    Imagine an array of 32-bit integers (each 4 bytes)::\n\n      x = np.array([[0, 1, 2, 3, 4],\n                    [5, 6, 7, 8, 9]], dtype=np.int32)\n\n    This array is stored in memory as 40 bytes, one after the other\n    (known as a contiguous block of memory).  The strides of an array tell\n    us how many bytes we have to skip in memory to move to the next position\n    along a certain axis.  For example, we have to skip 4 bytes (1 value) to\n    move to the next column, but 20 bytes (5 values) to get to the same\n    position in the next row.  As such, the strides for the array `x` will be\n    ``(20, 4)``.\n\n    See Also\n    --------\n    numpy.lib.stride_tricks.as_strided\n\n    Examples\n    --------\n    >>> y = np.reshape(np.arange(2*3*4), (2,3,4))\n    >>> y\n    array([[[ 0,  1,  2,  3],\n            [ 4,  5,  6,  7],\n            [ 8,  9, 10, 11]],\n           [[12, 13, 14, 15],\n            [16, 17, 18, 19],\n            [20, 21, 22, 23]]])\n    >>> y.strides\n    (48, 16, 4)\n    >>> y[1,1,1]\n    17\n    >>> offset=sum(y.strides * np.array((1,1,1)))\n    >>> offset/y.itemsize\n    17\n\n    >>> x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)\n    >>> x.strides\n    (32, 4, 224, 1344)\n    >>> i = np.array([3,5,2,2])\n    >>> offset = sum(i * x.strides)\n    >>> x[3,5,2,2]\n    813\n    >>> offset / x.itemsize\n    813'
        pass
    
    def sum(self):
        'a.sum(axis=None, dtype=None, out=None, keepdims=False)\n\n    Return the sum of the array elements over the given axis.\n\n    Refer to `numpy.sum` for full documentation.\n\n    See Also\n    --------\n    numpy.sum : equivalent function'
        pass
    
    def swapaxes(self):
        'a.swapaxes(axis1, axis2)\n\n    Return a view of the array with `axis1` and `axis2` interchanged.\n\n    Refer to `numpy.swapaxes` for full documentation.\n\n    See Also\n    --------\n    numpy.swapaxes : equivalent function'
        pass
    
    def take(self):
        "a.take(indices, axis=None, out=None, mode='raise')\n\n    Return an array formed from the elements of `a` at the given indices.\n\n    Refer to `numpy.take` for full documentation.\n\n    See Also\n    --------\n    numpy.take : equivalent function"
        pass
    
    def tobytes(self):
        "a.tobytes(order='C')\n\n    Construct Python bytes containing the raw data bytes in the array.\n\n    Constructs Python bytes showing a copy of the raw contents of\n    data memory. The bytes object can be produced in either 'C' or 'Fortran',\n    or 'Any' order (the default is 'C'-order). 'Any' order means C-order\n    unless the F_CONTIGUOUS flag in the array is set, in which case it\n    means 'Fortran' order.\n\n    .. versionadded:: 1.9.0\n\n    Parameters\n    ----------\n    order : {'C', 'F', None}, optional\n        Order of the data for multidimensional arrays:\n        C, Fortran, or the same as for the original array.\n\n    Returns\n    -------\n    s : bytes\n        Python bytes exhibiting a copy of `a`'s raw data.\n\n    Examples\n    --------\n    >>> x = np.array([[0, 1], [2, 3]])\n    >>> x.tobytes()\n    b'\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x03\\x00\\x00\\x00'\n    >>> x.tobytes('C') == x.tobytes()\n    True\n    >>> x.tobytes('F')\n    b'\\x00\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x03\\x00\\x00\\x00'"
        pass
    
    def tofile(self):
        'a.tofile(fid, sep="", format="%s")\n\n    Write array to a file as text or binary (default).\n\n    Data is always written in \'C\' order, independent of the order of `a`.\n    The data produced by this method can be recovered using the function\n    fromfile().\n\n    Parameters\n    ----------\n    fid : file or str\n        An open file object, or a string containing a filename.\n    sep : str\n        Separator between array items for text output.\n        If "" (empty), a binary file is written, equivalent to\n        ``file.write(a.tobytes())``.\n    format : str\n        Format string for text file output.\n        Each entry in the array is formatted to text by first converting\n        it to the closest Python type, and then using "format" % item.\n\n    Notes\n    -----\n    This is a convenience function for quick storage of array data.\n    Information on endianness and precision is lost, so this method is not a\n    good choice for files intended to archive data or transport data between\n    machines with different endianness. Some of these problems can be overcome\n    by outputting the data as text files, at the expense of speed and file\n    size.\n    \n    When fid is a file object, array contents are directly written to the\n    file, bypassing the file object\'s ``write`` method. As a result, tofile\n    cannot be used with files objects supporting compression (e.g., GzipFile)\n    or file-like objects that do not support ``fileno()`` (e.g., BytesIO).'
        pass
    
    def tolist(self):
        'a.tolist()\n\n    Return the array as a (possibly nested) list.\n\n    Return a copy of the array data as a (nested) Python list.\n    Data items are converted to the nearest compatible Python type.\n\n    Parameters\n    ----------\n    none\n\n    Returns\n    -------\n    y : list\n        The possibly nested list of array elements.\n\n    Notes\n    -----\n    The array may be recreated, ``a = np.array(a.tolist())``.\n\n    Examples\n    --------\n    >>> a = np.array([1, 2])\n    >>> a.tolist()\n    [1, 2]\n    >>> a = np.array([[1, 2], [3, 4]])\n    >>> list(a)\n    [array([1, 2]), array([3, 4])]\n    >>> a.tolist()\n    [[1, 2], [3, 4]]'
        pass
    
    def tostring(self):
        "a.tostring(order='C')\n\n    Construct Python bytes containing the raw data bytes in the array.\n\n    Constructs Python bytes showing a copy of the raw contents of\n    data memory. The bytes object can be produced in either 'C' or 'Fortran',\n    or 'Any' order (the default is 'C'-order). 'Any' order means C-order\n    unless the F_CONTIGUOUS flag in the array is set, in which case it\n    means 'Fortran' order.\n\n    This function is a compatibility alias for tobytes. Despite its name it returns bytes not strings.\n\n    Parameters\n    ----------\n    order : {'C', 'F', None}, optional\n        Order of the data for multidimensional arrays:\n        C, Fortran, or the same as for the original array.\n\n    Returns\n    -------\n    s : bytes\n        Python bytes exhibiting a copy of `a`'s raw data.\n\n    Examples\n    --------\n    >>> x = np.array([[0, 1], [2, 3]])\n    >>> x.tobytes()\n    b'\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x03\\x00\\x00\\x00'\n    >>> x.tobytes('C') == x.tobytes()\n    True\n    >>> x.tobytes('F')\n    b'\\x00\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x03\\x00\\x00\\x00'"
        pass
    
    def trace(self):
        'a.trace(offset=0, axis1=0, axis2=1, dtype=None, out=None)\n\n    Return the sum along diagonals of the array.\n\n    Refer to `numpy.trace` for full documentation.\n\n    See Also\n    --------\n    numpy.trace : equivalent function'
        pass
    
    def transpose(self):
        'a.transpose(*axes)\n\n    Returns a view of the array with axes transposed.\n\n    For a 1-D array, this has no effect. (To change between column and\n    row vectors, first cast the 1-D array into a matrix object.)\n    For a 2-D array, this is the usual matrix transpose.\n    For an n-D array, if axes are given, their order indicates how the\n    axes are permuted (see Examples). If axes are not provided and\n    ``a.shape = (i[0], i[1], ... i[n-2], i[n-1])``, then\n    ``a.transpose().shape = (i[n-1], i[n-2], ... i[1], i[0])``.\n\n    Parameters\n    ----------\n    axes : None, tuple of ints, or `n` ints\n\n     * None or no argument: reverses the order of the axes.\n\n     * tuple of ints: `i` in the `j`-th place in the tuple means `a`\'s\n       `i`-th axis becomes `a.transpose()`\'s `j`-th axis.\n\n     * `n` ints: same as an n-tuple of the same ints (this form is\n       intended simply as a "convenience" alternative to the tuple form)\n\n    Returns\n    -------\n    out : ndarray\n        View of `a`, with axes suitably permuted.\n\n    See Also\n    --------\n    ndarray.T : Array property returning the array transposed.\n\n    Examples\n    --------\n    >>> a = np.array([[1, 2], [3, 4]])\n    >>> a\n    array([[1, 2],\n           [3, 4]])\n    >>> a.transpose()\n    array([[1, 3],\n           [2, 4]])\n    >>> a.transpose((1, 0))\n    array([[1, 3],\n           [2, 4]])\n    >>> a.transpose(1, 0)\n    array([[1, 3],\n           [2, 4]])'
        pass
    
    def var(self):
        'a.var(axis=None, dtype=None, out=None, ddof=0, keepdims=False)\n\n    Returns the variance of the array elements, along given axis.\n\n    Refer to `numpy.var` for full documentation.\n\n    See Also\n    --------\n    numpy.var : equivalent function'
        pass
    
    def view(self):
        'a.view(dtype=None, type=None)\n\n    New view of array with the same data.\n\n    Parameters\n    ----------\n    dtype : data-type or ndarray sub-class, optional\n        Data-type descriptor of the returned view, e.g., float32 or int16. The\n        default, None, results in the view having the same data-type as `a`.\n        This argument can also be specified as an ndarray sub-class, which\n        then specifies the type of the returned object (this is equivalent to\n        setting the ``type`` parameter).\n    type : Python type, optional\n        Type of the returned view, e.g., ndarray or matrix.  Again, the\n        default None results in type preservation.\n\n    Notes\n    -----\n    ``a.view()`` is used two different ways:\n\n    ``a.view(some_dtype)`` or ``a.view(dtype=some_dtype)`` constructs a view\n    of the array\'s memory with a different data-type.  This can cause a\n    reinterpretation of the bytes of memory.\n\n    ``a.view(ndarray_subclass)`` or ``a.view(type=ndarray_subclass)`` just\n    returns an instance of `ndarray_subclass` that looks at the same array\n    (same shape, dtype, etc.)  This does not cause a reinterpretation of the\n    memory.\n\n    For ``a.view(some_dtype)``, if ``some_dtype`` has a different number of\n    bytes per entry than the previous dtype (for example, converting a\n    regular array to a structured array), then the behavior of the view\n    cannot be predicted just from the superficial appearance of ``a`` (shown\n    by ``print(a)``). It also depends on exactly how ``a`` is stored in\n    memory. Therefore if ``a`` is C-ordered versus fortran-ordered, versus\n    defined as a slice or transpose, etc., the view may give different\n    results.\n\n\n    Examples\n    --------\n    >>> x = np.array([(1, 2)], dtype=[(\'a\', np.int8), (\'b\', np.int8)])\n\n    Viewing array data using a different type and dtype:\n\n    >>> y = x.view(dtype=np.int16, type=np.matrix)\n    >>> y\n    matrix([[513]], dtype=int16)\n    >>> print(type(y))\n    <class \'numpy.matrixlib.defmatrix.matrix\'>\n\n    Creating a view on a structured array so it can be used in calculations\n\n    >>> x = np.array([(1, 2),(3,4)], dtype=[(\'a\', np.int8), (\'b\', np.int8)])\n    >>> xv = x.view(dtype=np.int8).reshape(-1,2)\n    >>> xv\n    array([[1, 2],\n           [3, 4]], dtype=int8)\n    >>> xv.mean(0)\n    array([ 2.,  3.])\n\n    Making changes to the view changes the underlying array\n\n    >>> xv[0,1] = 20\n    >>> print(x)\n    [(1, 20) (3, 4)]\n\n    Using a view to convert an array to a recarray:\n\n    >>> z = x.view(np.recarray)\n    >>> z.a\n    array([1], dtype=int8)\n\n    Views share data:\n\n    >>> x[0] = (9, 10)\n    >>> z[0]\n    (9, 10)\n\n    Views that change the dtype size (bytes per entry) should normally be\n    avoided on arrays defined by slices, transposes, fortran-ordering, etc.:\n\n    >>> x = np.array([[1,2,3],[4,5,6]], dtype=np.int16)\n    >>> y = x[:, 0:2]\n    >>> y\n    array([[1, 2],\n           [4, 5]], dtype=int16)\n    >>> y.view(dtype=[(\'width\', np.int16), (\'length\', np.int16)])\n    Traceback (most recent call last):\n      File "<stdin>", line 1, in <module>\n    ValueError: new type not compatible with array.\n    >>> z = y.copy()\n    >>> z.view(dtype=[(\'width\', np.int16), (\'length\', np.int16)])\n    array([[(1, 2)],\n           [(4, 5)]], dtype=[(\'width\', \'<i2\'), (\'length\', \'<i2\')])'
        pass
    

class nditer(_mod_builtins.object):
    'Efficient multi-dimensional iterator object to iterate over arrays.\n    To get started using this object, see the\n    :ref:`introductory guide to array iteration <arrays.nditer>`.\n\n    Parameters\n    ----------\n    op : ndarray or sequence of array_like\n        The array(s) to iterate over.\n    flags : sequence of str, optional\n        Flags to control the behavior of the iterator.\n\n          * "buffered" enables buffering when required.\n          * "c_index" causes a C-order index to be tracked.\n          * "f_index" causes a Fortran-order index to be tracked.\n          * "multi_index" causes a multi-index, or a tuple of indices\n            with one per iteration dimension, to be tracked.\n          * "common_dtype" causes all the operands to be converted to\n            a common data type, with copying or buffering as necessary.\n          * "copy_if_overlap" causes the iterator to determine if read\n            operands have overlap with write operands, and make temporary\n            copies as necessary to avoid overlap. False positives (needless\n            copying) are possible in some cases.\n          * "delay_bufalloc" delays allocation of the buffers until\n            a reset() call is made. Allows "allocate" operands to\n            be initialized before their values are copied into the buffers.\n          * "external_loop" causes the `values` given to be\n            one-dimensional arrays with multiple values instead of\n            zero-dimensional arrays.\n          * "grow_inner" allows the `value` array sizes to be made\n            larger than the buffer size when both "buffered" and\n            "external_loop" is used.\n          * "ranged" allows the iterator to be restricted to a sub-range\n            of the iterindex values.\n          * "refs_ok" enables iteration of reference types, such as\n            object arrays.\n          * "reduce_ok" enables iteration of "readwrite" operands\n            which are broadcasted, also known as reduction operands.\n          * "zerosize_ok" allows `itersize` to be zero.\n    op_flags : list of list of str, optional\n        This is a list of flags for each operand. At minimum, one of\n        "readonly", "readwrite", or "writeonly" must be specified.\n\n          * "readonly" indicates the operand will only be read from.\n          * "readwrite" indicates the operand will be read from and written to.\n          * "writeonly" indicates the operand will only be written to.\n          * "no_broadcast" prevents the operand from being broadcasted.\n          * "contig" forces the operand data to be contiguous.\n          * "aligned" forces the operand data to be aligned.\n          * "nbo" forces the operand data to be in native byte order.\n          * "copy" allows a temporary read-only copy if required.\n          * "updateifcopy" allows a temporary read-write copy if required.\n          * "allocate" causes the array to be allocated if it is None\n            in the `op` parameter.\n          * "no_subtype" prevents an "allocate" operand from using a subtype.\n          * "arraymask" indicates that this operand is the mask to use\n            for selecting elements when writing to operands with the\n            \'writemasked\' flag set. The iterator does not enforce this,\n            but when writing from a buffer back to the array, it only\n            copies those elements indicated by this mask.\n          * \'writemasked\' indicates that only elements where the chosen\n            \'arraymask\' operand is True will be written to.\n          * "overlap_assume_elementwise" can be used to mark operands that are\n            accessed only in the iterator order, to allow less conservative\n            copying when "copy_if_overlap" is present.\n    op_dtypes : dtype or tuple of dtype(s), optional\n        The required data type(s) of the operands. If copying or buffering\n        is enabled, the data will be converted to/from their original types.\n    order : {\'C\', \'F\', \'A\', \'K\'}, optional\n        Controls the iteration order. \'C\' means C order, \'F\' means\n        Fortran order, \'A\' means \'F\' order if all the arrays are Fortran\n        contiguous, \'C\' order otherwise, and \'K\' means as close to the\n        order the array elements appear in memory as possible. This also\n        affects the element memory order of "allocate" operands, as they\n        are allocated to be compatible with iteration order.\n        Default is \'K\'.\n    casting : {\'no\', \'equiv\', \'safe\', \'same_kind\', \'unsafe\'}, optional\n        Controls what kind of data casting may occur when making a copy\n        or buffering.  Setting this to \'unsafe\' is not recommended,\n        as it can adversely affect accumulations.\n\n          * \'no\' means the data types should not be cast at all.\n          * \'equiv\' means only byte-order changes are allowed.\n          * \'safe\' means only casts which can preserve values are allowed.\n          * \'same_kind\' means only safe casts or casts within a kind,\n            like float64 to float32, are allowed.\n          * \'unsafe\' means any data conversions may be done.\n    op_axes : list of list of ints, optional\n        If provided, is a list of ints or None for each operands.\n        The list of axes for an operand is a mapping from the dimensions\n        of the iterator to the dimensions of the operand. A value of\n        -1 can be placed for entries, causing that dimension to be\n        treated as "newaxis".\n    itershape : tuple of ints, optional\n        The desired shape of the iterator. This allows "allocate" operands\n        with a dimension mapped by op_axes not corresponding to a dimension\n        of a different operand to get a value not equal to 1 for that\n        dimension.\n    buffersize : int, optional\n        When buffering is enabled, controls the size of the temporary\n        buffers. Set to 0 for the default value.\n\n    Attributes\n    ----------\n    dtypes : tuple of dtype(s)\n        The data types of the values provided in `value`. This may be\n        different from the operand data types if buffering is enabled.\n        Valid only before the iterator is closed.\n    finished : bool\n        Whether the iteration over the operands is finished or not.\n    has_delayed_bufalloc : bool\n        If True, the iterator was created with the "delay_bufalloc" flag,\n        and no reset() function was called on it yet.\n    has_index : bool\n        If True, the iterator was created with either the "c_index" or\n        the "f_index" flag, and the property `index` can be used to\n        retrieve it.\n    has_multi_index : bool\n        If True, the iterator was created with the "multi_index" flag,\n        and the property `multi_index` can be used to retrieve it.\n    index\n        When the "c_index" or "f_index" flag was used, this property\n        provides access to the index. Raises a ValueError if accessed\n        and `has_index` is False.\n    iterationneedsapi : bool\n        Whether iteration requires access to the Python API, for example\n        if one of the operands is an object array.\n    iterindex : int\n        An index which matches the order of iteration.\n    itersize : int\n        Size of the iterator.\n    itviews\n        Structured view(s) of `operands` in memory, matching the reordered\n        and optimized iterator access pattern. Valid only before the iterator\n        is closed.\n    multi_index\n        When the "multi_index" flag was used, this property\n        provides access to the index. Raises a ValueError if accessed\n        accessed and `has_multi_index` is False.\n    ndim : int\n        The iterator\'s dimension.\n    nop : int\n        The number of iterator operands.\n    operands : tuple of operand(s)\n        The array(s) to be iterated over. Valid only before the iterator is\n        closed.\n    shape : tuple of ints\n        Shape tuple, the shape of the iterator.\n    value\n        Value of `operands` at current iteration. Normally, this is a\n        tuple of array scalars, but if the flag "external_loop" is used,\n        it is a tuple of one dimensional arrays.\n\n    Notes\n    -----\n    `nditer` supersedes `flatiter`.  The iterator implementation behind\n    `nditer` is also exposed by the NumPy C API.\n\n    The Python exposure supplies two iteration interfaces, one which follows\n    the Python iterator protocol, and another which mirrors the C-style\n    do-while pattern.  The native Python approach is better in most cases, but\n    if you need the iterator\'s coordinates or index, use the C-style pattern.\n\n    Examples\n    --------\n    Here is how we might write an ``iter_add`` function, using the\n    Python iterator protocol::\n\n        def iter_add_py(x, y, out=None):\n            addop = np.add\n            it = np.nditer([x, y, out], [],\n                        [[\'readonly\'], [\'readonly\'], [\'writeonly\',\'allocate\']])\n            with it:\n                for (a, b, c) in it:\n                    addop(a, b, out=c)\n            return it.operands[2]\n\n    Here is the same function, but following the C-style pattern::\n\n        def iter_add(x, y, out=None):\n            addop = np.add\n\n            it = np.nditer([x, y, out], [],\n                        [[\'readonly\'], [\'readonly\'], [\'writeonly\',\'allocate\']])\n            with it:\n                while not it.finished:\n                    addop(it[0], it[1], out=it[2])\n                    it.iternext()\n\n                return it.operands[2]\n\n    Here is an example outer product function::\n\n        def outer_it(x, y, out=None):\n            mulop = np.multiply\n\n            it = np.nditer([x, y, out], [\'external_loop\'],\n                    [[\'readonly\'], [\'readonly\'], [\'writeonly\', \'allocate\']],\n                    op_axes=[list(range(x.ndim)) + [-1] * y.ndim,\n                             [-1] * x.ndim + list(range(y.ndim)),\n                             None])\n            with it:\n                for (a, b, c) in it:\n                    mulop(a, b, out=c)\n                return it.operands[2]\n\n        >>> a = np.arange(2)+1\n        >>> b = np.arange(3)+1\n        >>> outer_it(a,b)\n        array([[1, 2, 3],\n               [2, 4, 6]])\n\n    Here is an example function which operates like a "lambda" ufunc::\n\n        def luf(lamdaexpr, *args, **kwargs):\n            "luf(lambdaexpr, op1, ..., opn, out=None, order=\'K\', casting=\'safe\', buffersize=0)"\n            nargs = len(args)\n            op = (kwargs.get(\'out\',None),) + args\n            it = np.nditer(op, [\'buffered\',\'external_loop\'],\n                    [[\'writeonly\',\'allocate\',\'no_broadcast\']] +\n                                    [[\'readonly\',\'nbo\',\'aligned\']]*nargs,\n                    order=kwargs.get(\'order\',\'K\'),\n                    casting=kwargs.get(\'casting\',\'safe\'),\n                    buffersize=kwargs.get(\'buffersize\',0))\n            while not it.finished:\n                it[0] = lamdaexpr(*it[1:])\n                it.iternext()\n                return it.operands[0]\n\n        >>> a = np.arange(5)\n        >>> b = np.ones(5)\n        >>> luf(lambda i,j:i*i + j/2, a, b)\n        array([  0.5,   1.5,   4.5,   9.5,  16.5])\n\n    If operand flags `"writeonly"` or `"readwrite"` are used the operands may\n    be views into the original data with the `WRITEBACKIFCOPY` flag. In this case\n    nditer must be used as a context manager or the nditer.close\n    method must be called before using the result. The temporary\n    data will be written back to the original data when the `__exit__`\n    function is called but not before:\n\n        >>> a = np.arange(6, dtype=\'i4\')[::-2]\n        >>> with nditer(a, [],\n        ...        [[\'writeonly\', \'updateifcopy\']],\n        ...        casting=\'unsafe\',\n        ...        op_dtypes=[np.dtype(\'f4\')]) as i:\n        ...    x = i.operands[0]\n        ...    x[:] = [-1, -2, -3]\n        ...    # a still unchanged here\n        >>> a, x\n        array([-1, -2, -3]), array([-1, -2, -3])\n\n    It is important to note that once the iterator is exited, dangling\n    references (like `x` in the example) may or may not share data with\n    the original data `a`. If writeback semantics were active, i.e. if\n    `x.base.flags.writebackifcopy` is `True`, then exiting the iterator\n    will sever the connection between `x` and `a`, writing to `x` will\n    no longer write to `a`. If writeback semantics are not active, then\n    `x.data` will still point at some part of `a.data`, and writing to\n    one will affect the other.'
    __class__ = nditer
    def __copy__(self):
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'Efficient multi-dimensional iterator object to iterate over arrays.\n    To get started using this object, see the\n    :ref:`introductory guide to array iteration <arrays.nditer>`.\n\n    Parameters\n    ----------\n    op : ndarray or sequence of array_like\n        The array(s) to iterate over.\n    flags : sequence of str, optional\n        Flags to control the behavior of the iterator.\n\n          * "buffered" enables buffering when required.\n          * "c_index" causes a C-order index to be tracked.\n          * "f_index" causes a Fortran-order index to be tracked.\n          * "multi_index" causes a multi-index, or a tuple of indices\n            with one per iteration dimension, to be tracked.\n          * "common_dtype" causes all the operands to be converted to\n            a common data type, with copying or buffering as necessary.\n          * "copy_if_overlap" causes the iterator to determine if read\n            operands have overlap with write operands, and make temporary\n            copies as necessary to avoid overlap. False positives (needless\n            copying) are possible in some cases.\n          * "delay_bufalloc" delays allocation of the buffers until\n            a reset() call is made. Allows "allocate" operands to\n            be initialized before their values are copied into the buffers.\n          * "external_loop" causes the `values` given to be\n            one-dimensional arrays with multiple values instead of\n            zero-dimensional arrays.\n          * "grow_inner" allows the `value` array sizes to be made\n            larger than the buffer size when both "buffered" and\n            "external_loop" is used.\n          * "ranged" allows the iterator to be restricted to a sub-range\n            of the iterindex values.\n          * "refs_ok" enables iteration of reference types, such as\n            object arrays.\n          * "reduce_ok" enables iteration of "readwrite" operands\n            which are broadcasted, also known as reduction operands.\n          * "zerosize_ok" allows `itersize` to be zero.\n    op_flags : list of list of str, optional\n        This is a list of flags for each operand. At minimum, one of\n        "readonly", "readwrite", or "writeonly" must be specified.\n\n          * "readonly" indicates the operand will only be read from.\n          * "readwrite" indicates the operand will be read from and written to.\n          * "writeonly" indicates the operand will only be written to.\n          * "no_broadcast" prevents the operand from being broadcasted.\n          * "contig" forces the operand data to be contiguous.\n          * "aligned" forces the operand data to be aligned.\n          * "nbo" forces the operand data to be in native byte order.\n          * "copy" allows a temporary read-only copy if required.\n          * "updateifcopy" allows a temporary read-write copy if required.\n          * "allocate" causes the array to be allocated if it is None\n            in the `op` parameter.\n          * "no_subtype" prevents an "allocate" operand from using a subtype.\n          * "arraymask" indicates that this operand is the mask to use\n            for selecting elements when writing to operands with the\n            \'writemasked\' flag set. The iterator does not enforce this,\n            but when writing from a buffer back to the array, it only\n            copies those elements indicated by this mask.\n          * \'writemasked\' indicates that only elements where the chosen\n            \'arraymask\' operand is True will be written to.\n          * "overlap_assume_elementwise" can be used to mark operands that are\n            accessed only in the iterator order, to allow less conservative\n            copying when "copy_if_overlap" is present.\n    op_dtypes : dtype or tuple of dtype(s), optional\n        The required data type(s) of the operands. If copying or buffering\n        is enabled, the data will be converted to/from their original types.\n    order : {\'C\', \'F\', \'A\', \'K\'}, optional\n        Controls the iteration order. \'C\' means C order, \'F\' means\n        Fortran order, \'A\' means \'F\' order if all the arrays are Fortran\n        contiguous, \'C\' order otherwise, and \'K\' means as close to the\n        order the array elements appear in memory as possible. This also\n        affects the element memory order of "allocate" operands, as they\n        are allocated to be compatible with iteration order.\n        Default is \'K\'.\n    casting : {\'no\', \'equiv\', \'safe\', \'same_kind\', \'unsafe\'}, optional\n        Controls what kind of data casting may occur when making a copy\n        or buffering.  Setting this to \'unsafe\' is not recommended,\n        as it can adversely affect accumulations.\n\n          * \'no\' means the data types should not be cast at all.\n          * \'equiv\' means only byte-order changes are allowed.\n          * \'safe\' means only casts which can preserve values are allowed.\n          * \'same_kind\' means only safe casts or casts within a kind,\n            like float64 to float32, are allowed.\n          * \'unsafe\' means any data conversions may be done.\n    op_axes : list of list of ints, optional\n        If provided, is a list of ints or None for each operands.\n        The list of axes for an operand is a mapping from the dimensions\n        of the iterator to the dimensions of the operand. A value of\n        -1 can be placed for entries, causing that dimension to be\n        treated as "newaxis".\n    itershape : tuple of ints, optional\n        The desired shape of the iterator. This allows "allocate" operands\n        with a dimension mapped by op_axes not corresponding to a dimension\n        of a different operand to get a value not equal to 1 for that\n        dimension.\n    buffersize : int, optional\n        When buffering is enabled, controls the size of the temporary\n        buffers. Set to 0 for the default value.\n\n    Attributes\n    ----------\n    dtypes : tuple of dtype(s)\n        The data types of the values provided in `value`. This may be\n        different from the operand data types if buffering is enabled.\n        Valid only before the iterator is closed.\n    finished : bool\n        Whether the iteration over the operands is finished or not.\n    has_delayed_bufalloc : bool\n        If True, the iterator was created with the "delay_bufalloc" flag,\n        and no reset() function was called on it yet.\n    has_index : bool\n        If True, the iterator was created with either the "c_index" or\n        the "f_index" flag, and the property `index` can be used to\n        retrieve it.\n    has_multi_index : bool\n        If True, the iterator was created with the "multi_index" flag,\n        and the property `multi_index` can be used to retrieve it.\n    index\n        When the "c_index" or "f_index" flag was used, this property\n        provides access to the index. Raises a ValueError if accessed\n        and `has_index` is False.\n    iterationneedsapi : bool\n        Whether iteration requires access to the Python API, for example\n        if one of the operands is an object array.\n    iterindex : int\n        An index which matches the order of iteration.\n    itersize : int\n        Size of the iterator.\n    itviews\n        Structured view(s) of `operands` in memory, matching the reordered\n        and optimized iterator access pattern. Valid only before the iterator\n        is closed.\n    multi_index\n        When the "multi_index" flag was used, this property\n        provides access to the index. Raises a ValueError if accessed\n        accessed and `has_multi_index` is False.\n    ndim : int\n        The iterator\'s dimension.\n    nop : int\n        The number of iterator operands.\n    operands : tuple of operand(s)\n        The array(s) to be iterated over. Valid only before the iterator is\n        closed.\n    shape : tuple of ints\n        Shape tuple, the shape of the iterator.\n    value\n        Value of `operands` at current iteration. Normally, this is a\n        tuple of array scalars, but if the flag "external_loop" is used,\n        it is a tuple of one dimensional arrays.\n\n    Notes\n    -----\n    `nditer` supersedes `flatiter`.  The iterator implementation behind\n    `nditer` is also exposed by the NumPy C API.\n\n    The Python exposure supplies two iteration interfaces, one which follows\n    the Python iterator protocol, and another which mirrors the C-style\n    do-while pattern.  The native Python approach is better in most cases, but\n    if you need the iterator\'s coordinates or index, use the C-style pattern.\n\n    Examples\n    --------\n    Here is how we might write an ``iter_add`` function, using the\n    Python iterator protocol::\n\n        def iter_add_py(x, y, out=None):\n            addop = np.add\n            it = np.nditer([x, y, out], [],\n                        [[\'readonly\'], [\'readonly\'], [\'writeonly\',\'allocate\']])\n            with it:\n                for (a, b, c) in it:\n                    addop(a, b, out=c)\n            return it.operands[2]\n\n    Here is the same function, but following the C-style pattern::\n\n        def iter_add(x, y, out=None):\n            addop = np.add\n\n            it = np.nditer([x, y, out], [],\n                        [[\'readonly\'], [\'readonly\'], [\'writeonly\',\'allocate\']])\n            with it:\n                while not it.finished:\n                    addop(it[0], it[1], out=it[2])\n                    it.iternext()\n\n                return it.operands[2]\n\n    Here is an example outer product function::\n\n        def outer_it(x, y, out=None):\n            mulop = np.multiply\n\n            it = np.nditer([x, y, out], [\'external_loop\'],\n                    [[\'readonly\'], [\'readonly\'], [\'writeonly\', \'allocate\']],\n                    op_axes=[list(range(x.ndim)) + [-1] * y.ndim,\n                             [-1] * x.ndim + list(range(y.ndim)),\n                             None])\n            with it:\n                for (a, b, c) in it:\n                    mulop(a, b, out=c)\n                return it.operands[2]\n\n        >>> a = np.arange(2)+1\n        >>> b = np.arange(3)+1\n        >>> outer_it(a,b)\n        array([[1, 2, 3],\n               [2, 4, 6]])\n\n    Here is an example function which operates like a "lambda" ufunc::\n\n        def luf(lamdaexpr, *args, **kwargs):\n            "luf(lambdaexpr, op1, ..., opn, out=None, order=\'K\', casting=\'safe\', buffersize=0)"\n            nargs = len(args)\n            op = (kwargs.get(\'out\',None),) + args\n            it = np.nditer(op, [\'buffered\',\'external_loop\'],\n                    [[\'writeonly\',\'allocate\',\'no_broadcast\']] +\n                                    [[\'readonly\',\'nbo\',\'aligned\']]*nargs,\n                    order=kwargs.get(\'order\',\'K\'),\n                    casting=kwargs.get(\'casting\',\'safe\'),\n                    buffersize=kwargs.get(\'buffersize\',0))\n            while not it.finished:\n                it[0] = lamdaexpr(*it[1:])\n                it.iternext()\n                return it.operands[0]\n\n        >>> a = np.arange(5)\n        >>> b = np.ones(5)\n        >>> luf(lambda i,j:i*i + j/2, a, b)\n        array([  0.5,   1.5,   4.5,   9.5,  16.5])\n\n    If operand flags `"writeonly"` or `"readwrite"` are used the operands may\n    be views into the original data with the `WRITEBACKIFCOPY` flag. In this case\n    nditer must be used as a context manager or the nditer.close\n    method must be called before using the result. The temporary\n    data will be written back to the original data when the `__exit__`\n    function is called but not before:\n\n        >>> a = np.arange(6, dtype=\'i4\')[::-2]\n        >>> with nditer(a, [],\n        ...        [[\'writeonly\', \'updateifcopy\']],\n        ...        casting=\'unsafe\',\n        ...        op_dtypes=[np.dtype(\'f4\')]) as i:\n        ...    x = i.operands[0]\n        ...    x[:] = [-1, -2, -3]\n        ...    # a still unchanged here\n        >>> a, x\n        array([-1, -2, -3]), array([-1, -2, -3])\n\n    It is important to note that once the iterator is exited, dangling\n    references (like `x` in the example) may or may not share data with\n    the original data `a`. If writeback semantics were active, i.e. if\n    `x.base.flags.writebackifcopy` is `True`, then exiting the iterator\n    will sever the connection between `x` and `a`, writing to `x` will\n    no longer write to `a`. If writeback semantics are not active, then\n    `x.data` will still point at some part of `a.data`, and writing to\n    one will affect the other.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return nditer()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close()\n\n    Resolve all writeback semantics in writeable operands.\n\n    See Also\n    --------\n\n    :ref:`nditer-context-manager`'
        pass
    
    def copy(self):
        'copy()\n\n    Get a copy of the iterator in its current state.\n\n    Examples\n    --------\n    >>> x = np.arange(10)\n    >>> y = x + 1\n    >>> it = np.nditer([x, y])\n    >>> it.next()\n    (array(0), array(1))\n    >>> it2 = it.copy()\n    >>> it2.next()\n    (array(1), array(2))'
        pass
    
    def debug_print(self):
        'debug_print()\n\n    Print the current state of the `nditer` instance and debug info to stdout.'
        pass
    
    @property
    def dtypes(self):
        pass
    
    def enable_external_loop(self):
        'enable_external_loop()\n\n    When the "external_loop" was not used during construction, but\n    is desired, this modifies the iterator to behave as if the flag\n    was specified.'
        pass
    
    @property
    def finished(self):
        pass
    
    @property
    def has_delayed_bufalloc(self):
        pass
    
    @property
    def has_index(self):
        pass
    
    @property
    def has_multi_index(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def iterationneedsapi(self):
        pass
    
    @property
    def iterindex(self):
        pass
    
    def iternext(self):
        'iternext()\n\n    Check whether iterations are left, and perform a single internal iteration\n    without returning the result.  Used in the C-style pattern do-while\n    pattern.  For an example, see `nditer`.\n\n    Returns\n    -------\n    iternext : bool\n        Whether or not there are iterations left.'
        pass
    
    @property
    def iterrange(self):
        pass
    
    @property
    def itersize(self):
        pass
    
    @property
    def itviews(self):
        pass
    
    @property
    def multi_index(self):
        pass
    
    @property
    def ndim(self):
        pass
    
    @property
    def nop(self):
        pass
    
    @property
    def operands(self):
        'operands[`Slice`]\n\n    The array(s) to be iterated over. Valid only before the iterator is closed.'
        pass
    
    def remove_axis(self, i):
        'remove_axis(i)\n\n    Removes axis `i` from the iterator. Requires that the flag "multi_index"\n    be enabled.'
        pass
    
    def remove_multi_index(self):
        'remove_multi_index()\n\n    When the "multi_index" flag was specified, this removes it, allowing\n    the internal iteration structure to be optimized further.'
        pass
    
    def reset(self):
        'reset()\n\n    Reset the iterator to its initial state.'
        pass
    
    @property
    def shape(self):
        pass
    
    @property
    def value(self):
        pass
    

def nested_iters():
    'Create nditers for use in nested loops\n\n    Create a tuple of `nditer` objects which iterate in nested loops over\n    different axes of the op argument. The first iterator is used in the\n    outermost loop, the last in the innermost loop. Advancing one will change\n    the subsequent iterators to point at its new element.\n\n    Parameters\n    ----------\n    op : ndarray or sequence of array_like\n        The array(s) to iterate over.\n\n    axes : list of list of int\n        Each item is used as an "op_axes" argument to an nditer\n\n    flags, op_flags, op_dtypes, order, casting, buffersize (optional)\n        See `nditer` parameters of the same name\n\n    Returns\n    -------\n    iters : tuple of nditer\n        An nditer for each item in `axes`, outermost first\n\n    See Also\n    --------\n    nditer\n\n    Examples\n    --------\n\n    Basic usage. Note how y is the "flattened" version of\n    [a[:, 0, :], a[:, 1, 0], a[:, 2, :]] since we specified\n    the first iter\'s axes as [1]\n\n    >>> a = np.arange(12).reshape(2, 3, 2)\n    >>> i, j = np.nested_iters(a, [[1], [0, 2]], flags=["multi_index"])\n    >>> for x in i:\n    ...      print(i.multi_index)\n    ...      for y in j:\n    ...          print(\'\', j.multi_index, y)\n\n    (0,)\n     (0, 0) 0\n     (0, 1) 1\n     (1, 0) 6\n     (1, 1) 7\n    (1,)\n     (0, 0) 2\n     (0, 1) 3\n     (1, 0) 8\n     (1, 1) 9\n    (2,)\n     (0, 0) 4\n     (0, 1) 5\n     (1, 0) 10\n     (1, 1) 11'
    pass

def normalize_axis_index(axis, ndim, msg_prefix=None):
    "normalize_axis_index(axis, ndim, msg_prefix=None)\n\n    Normalizes an axis index, `axis`, such that is a valid positive index into\n    the shape of array with `ndim` dimensions. Raises an AxisError with an\n    appropriate message if this is not possible.\n\n    Used internally by all axis-checking logic.\n\n    .. versionadded:: 1.13.0\n\n    Parameters\n    ----------\n    axis : int\n        The un-normalized index of the axis. Can be negative\n    ndim : int\n        The number of dimensions of the array that `axis` should be normalized\n        against\n    msg_prefix : str\n        A prefix to put before the message, typically the name of the argument\n\n    Returns\n    -------\n    normalized_axis : int\n        The normalized axis index, such that `0 <= normalized_axis < ndim`\n\n    Raises\n    ------\n    AxisError\n        If the axis index is invalid, when `-ndim <= axis < ndim` is false.\n\n    Examples\n    --------\n    >>> normalize_axis_index(0, ndim=3)\n    0\n    >>> normalize_axis_index(1, ndim=3)\n    1\n    >>> normalize_axis_index(-1, ndim=3)\n    2\n\n    >>> normalize_axis_index(3, ndim=3)\n    Traceback (most recent call last):\n    ...\n    AxisError: axis 3 is out of bounds for array of dimension 3\n    >>> normalize_axis_index(-4, ndim=3, msg_prefix='axes_arg')\n    Traceback (most recent call last):\n    ...\n    AxisError: axes_arg: axis -4 is out of bounds for array of dimension 3"
    pass

def packbits(myarray, axis=None):
    'packbits(myarray, axis=None)\n\n    Packs the elements of a binary-valued array into bits in a uint8 array.\n\n    The result is padded to full bytes by inserting zero bits at the end.\n\n    Parameters\n    ----------\n    myarray : array_like\n        An array of integers or booleans whose elements should be packed to\n        bits.\n    axis : int, optional\n        The dimension over which bit-packing is done.\n        ``None`` implies packing the flattened array.\n\n    Returns\n    -------\n    packed : ndarray\n        Array of type uint8 whose elements represent bits corresponding to the\n        logical (0 or nonzero) value of the input elements. The shape of\n        `packed` has the same number of dimensions as the input (unless `axis`\n        is None, in which case the output is 1-D).\n\n    See Also\n    --------\n    unpackbits: Unpacks elements of a uint8 array into a binary-valued output\n                array.\n\n    Examples\n    --------\n    >>> a = np.array([[[1,0,1],\n    ...                [0,1,0]],\n    ...               [[1,1,0],\n    ...                [0,0,1]]])\n    >>> b = np.packbits(a, axis=-1)\n    >>> b\n    array([[[160],[64]],[[192],[32]]], dtype=uint8)\n\n    Note that in binary 160 = 1010 0000, 64 = 0100 0000, 192 = 1100 0000,\n    and 32 = 0010 0000.'
    pass

def promote_types(type1, type2):
    "promote_types(type1, type2)\n\n    Returns the data type with the smallest size and smallest scalar\n    kind to which both ``type1`` and ``type2`` may be safely cast.\n    The returned data type is always in native byte order.\n\n    This function is symmetric, but rarely associative.\n\n    Parameters\n    ----------\n    type1 : dtype or dtype specifier\n        First data type.\n    type2 : dtype or dtype specifier\n        Second data type.\n\n    Returns\n    -------\n    out : dtype\n        The promoted data type.\n\n    Notes\n    -----\n    .. versionadded:: 1.6.0\n\n    Starting in NumPy 1.9, promote_types function now returns a valid string\n    length when given an integer or float dtype as one argument and a string\n    dtype as another argument. Previously it always returned the input string\n    dtype, even if it wasn't long enough to store the max integer/float value\n    converted to a string.\n\n    See Also\n    --------\n    result_type, dtype, can_cast\n\n    Examples\n    --------\n    >>> np.promote_types('f4', 'f8')\n    dtype('float64')\n\n    >>> np.promote_types('i8', 'f4')\n    dtype('float64')\n\n    >>> np.promote_types('>i8', '<c8')\n    dtype('complex128')\n\n    >>> np.promote_types('i4', 'S8')\n    dtype('S11')\n\n    An example of a non-associative case:\n\n    >>> p = np.promote_types\n    >>> p('S', p('i1', 'u1'))\n    dtype('S6')\n    >>> p(p('S', 'i1'), 'u1')\n    dtype('S4')"
    pass

def putmask(a, mask, values):
    'putmask(a, mask, values)\n\n    Changes elements of an array based on conditional and input values.\n\n    Sets ``a.flat[n] = values[n]`` for each n where ``mask.flat[n]==True``.\n\n    If `values` is not the same size as `a` and `mask` then it will repeat.\n    This gives behavior different from ``a[mask] = values``.\n\n    Parameters\n    ----------\n    a : array_like\n        Target array.\n    mask : array_like\n        Boolean mask array. It has to be the same shape as `a`.\n    values : array_like\n        Values to put into `a` where `mask` is True. If `values` is smaller\n        than `a` it will be repeated.\n\n    See Also\n    --------\n    place, put, take, copyto\n\n    Examples\n    --------\n    >>> x = np.arange(6).reshape(2, 3)\n    >>> np.putmask(x, x>2, x**2)\n    >>> x\n    array([[ 0,  1,  2],\n           [ 9, 16, 25]])\n\n    If `values` is smaller than `a` it is repeated:\n\n    >>> x = np.arange(5)\n    >>> np.putmask(x, x>1, [-33, -44])\n    >>> x\n    array([  0,   1, -33, -44, -33])'
    pass

def ravel_multi_index(multi_index, dims, mode='raise', order='C'):
    "ravel_multi_index(multi_index, dims, mode='raise', order='C')\n\n    Converts a tuple of index arrays into an array of flat\n    indices, applying boundary modes to the multi-index.\n\n    Parameters\n    ----------\n    multi_index : tuple of array_like\n        A tuple of integer arrays, one array for each dimension.\n    dims : tuple of ints\n        The shape of array into which the indices from ``multi_index`` apply.\n    mode : {'raise', 'wrap', 'clip'}, optional\n        Specifies how out-of-bounds indices are handled.  Can specify\n        either one mode or a tuple of modes, one mode per index.\n\n        * 'raise' -- raise an error (default)\n        * 'wrap' -- wrap around\n        * 'clip' -- clip to the range\n\n        In 'clip' mode, a negative index which would normally\n        wrap will clip to 0 instead.\n    order : {'C', 'F'}, optional\n        Determines whether the multi-index should be viewed as\n        indexing in row-major (C-style) or column-major\n        (Fortran-style) order.\n\n    Returns\n    -------\n    raveled_indices : ndarray\n        An array of indices into the flattened version of an array\n        of dimensions ``dims``.\n\n    See Also\n    --------\n    unravel_index\n\n    Notes\n    -----\n    .. versionadded:: 1.6.0\n\n    Examples\n    --------\n    >>> arr = np.array([[3,6,6],[4,5,1]])\n    >>> np.ravel_multi_index(arr, (7,6))\n    array([22, 41, 37])\n    >>> np.ravel_multi_index(arr, (7,6), order='F')\n    array([31, 41, 13])\n    >>> np.ravel_multi_index(arr, (4,6), mode='clip')\n    array([22, 23, 19])\n    >>> np.ravel_multi_index(arr, (4,4), mode=('clip','wrap'))\n    array([12, 13, 13])\n\n    >>> np.ravel_multi_index((3,1,4,1), (6,7,8,9))\n    1621"
    pass

def result_type(*arrays_and_dtypes):
    "result_type(*arrays_and_dtypes)\n\n    Returns the type that results from applying the NumPy\n    type promotion rules to the arguments.\n\n    Type promotion in NumPy works similarly to the rules in languages\n    like C++, with some slight differences.  When both scalars and\n    arrays are used, the array's type takes precedence and the actual value\n    of the scalar is taken into account.\n\n    For example, calculating 3*a, where a is an array of 32-bit floats,\n    intuitively should result in a 32-bit float output.  If the 3 is a\n    32-bit integer, the NumPy rules indicate it can't convert losslessly\n    into a 32-bit float, so a 64-bit float should be the result type.\n    By examining the value of the constant, '3', we see that it fits in\n    an 8-bit integer, which can be cast losslessly into the 32-bit float.\n\n    Parameters\n    ----------\n    arrays_and_dtypes : list of arrays and dtypes\n        The operands of some operation whose result type is needed.\n\n    Returns\n    -------\n    out : dtype\n        The result type.\n\n    See also\n    --------\n    dtype, promote_types, min_scalar_type, can_cast\n\n    Notes\n    -----\n    .. versionadded:: 1.6.0\n\n    The specific algorithm used is as follows.\n\n    Categories are determined by first checking which of boolean,\n    integer (int/uint), or floating point (float/complex) the maximum\n    kind of all the arrays and the scalars are.\n\n    If there are only scalars or the maximum category of the scalars\n    is higher than the maximum category of the arrays,\n    the data types are combined with :func:`promote_types`\n    to produce the return value.\n\n    Otherwise, `min_scalar_type` is called on each array, and\n    the resulting data types are all combined with :func:`promote_types`\n    to produce the return value.\n\n    The set of int values is not a subset of the uint values for types\n    with the same number of bits, something not reflected in\n    :func:`min_scalar_type`, but handled as a special case in `result_type`.\n\n    Examples\n    --------\n    >>> np.result_type(3, np.arange(7, dtype='i1'))\n    dtype('int8')\n\n    >>> np.result_type('i4', 'c8')\n    dtype('complex128')\n\n    >>> np.result_type(3.0, -2)\n    dtype('float64')"
    pass

def scalar(dtype, obj):
    'scalar(dtype, obj)\n\n    Return a new scalar array of the given type initialized with obj.\n\n    This function is meant mainly for pickle support. `dtype` must be a\n    valid data-type descriptor. If `dtype` corresponds to an object\n    descriptor, then `obj` can be any object, otherwise `obj` must be a\n    string. If `obj` is not given, it will be interpreted as None for object\n    type and as zeros for all other types.'
    pass

def set_datetimeparse_function():
    pass

def set_legacy_print_mode():
    pass

def set_numeric_ops():
    'set_numeric_ops(op1=func1, op2=func2, ...)\n\n    Set numerical operators for array objects.\n\n    Parameters\n    ----------\n    op1, op2, ... : callable\n        Each ``op = func`` pair describes an operator to be replaced.\n        For example, ``add = lambda x, y: np.add(x, y) % 5`` would replace\n        addition by modulus 5 addition.\n\n    Returns\n    -------\n    saved_ops : list of callables\n        A list of all operators, stored before making replacements.\n\n    Notes\n    -----\n    .. WARNING::\n       Use with care!  Incorrect usage may lead to memory errors.\n\n    A function replacing an operator cannot make use of that operator.\n    For example, when replacing add, you may not use ``+``.  Instead,\n    directly call ufuncs.\n\n    Examples\n    --------\n    >>> def add_mod5(x, y):\n    ...     return np.add(x, y) % 5\n    ...\n    >>> old_funcs = np.set_numeric_ops(add=add_mod5)\n\n    >>> x = np.arange(12).reshape((3, 4))\n    >>> x + x\n    array([[0, 2, 4, 1],\n           [3, 0, 2, 4],\n           [1, 3, 0, 2]])\n\n    >>> ignore = np.set_numeric_ops(**old_funcs) # restore operators'
    pass

def set_string_function(f, repr=1):
    'set_string_function(f, repr=1)\n\n    Internal method to set a function to be used when pretty printing arrays.'
    pass

def set_typeDict(dict):
    'set_typeDict(dict)\n\n    Set the internal dictionary that can look up an array type using a\n    registered code.'
    pass

def shares_memory(a, b, max_work=None):
    'shares_memory(a, b, max_work=None)\n\n    Determine if two arrays share memory\n\n    Parameters\n    ----------\n    a, b : ndarray\n        Input arrays\n    max_work : int, optional\n        Effort to spend on solving the overlap problem (maximum number\n        of candidate solutions to consider). The following special\n        values are recognized:\n\n        max_work=MAY_SHARE_EXACT  (default)\n            The problem is solved exactly. In this case, the function returns\n            True only if there is an element shared between the arrays.\n        max_work=MAY_SHARE_BOUNDS\n            Only the memory bounds of a and b are checked.\n\n    Raises\n    ------\n    numpy.TooHardError\n        Exceeded max_work.\n\n    Returns\n    -------\n    out : bool\n\n    See Also\n    --------\n    may_share_memory\n\n    Examples\n    --------\n    >>> np.may_share_memory(np.array([1,2]), np.array([5,8,9]))\n    False'
    pass

def test_interrupt():
    pass

tracemalloc_domain = 389047
typeinfo = _mod_builtins.dict()
class typeinforanged(_mod_builtins.tuple):
    'Information about a scalar numpy type with a range'
    __class__ = typeinforanged
    def __init__(self, *args, **kwargs):
        'Information about a scalar numpy type with a range'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def alignment(self):
        'The alignment of the type in bytes'
        pass
    
    @property
    def bits(self):
        'The number of bits in the type'
        pass
    
    @property
    def char(self):
        'The character used to represent the type'
        pass
    
    @property
    def max(self):
        'The maximum value of this type'
        pass
    
    @property
    def min(self):
        'The minimum value of this type'
        pass
    
    n_fields = 7
    n_sequence_fields = 7
    n_unnamed_fields = 0
    @property
    def num(self):
        'The numeric id assigned to the type'
        pass
    
    @property
    def type(self):
        'The python type object this info is about'
        pass
    

def unpackbits(myarray, axis=None):
    'unpackbits(myarray, axis=None)\n\n    Unpacks elements of a uint8 array into a binary-valued output array.\n\n    Each element of `myarray` represents a bit-field that should be unpacked\n    into a binary-valued output array. The shape of the output array is either\n    1-D (if `axis` is None) or the same shape as the input array with unpacking\n    done along the axis specified.\n\n    Parameters\n    ----------\n    myarray : ndarray, uint8 type\n       Input array.\n    axis : int, optional\n        The dimension over which bit-unpacking is done.\n        ``None`` implies unpacking the flattened array.\n\n    Returns\n    -------\n    unpacked : ndarray, uint8 type\n       The elements are binary-valued (0 or 1).\n\n    See Also\n    --------\n    packbits : Packs the elements of a binary-valued array into bits in a uint8\n               array.\n\n    Examples\n    --------\n    >>> a = np.array([[2], [7], [23]], dtype=np.uint8)\n    >>> a\n    array([[ 2],\n           [ 7],\n           [23]], dtype=uint8)\n    >>> b = np.unpackbits(a, axis=1)\n    >>> b\n    array([[0, 0, 0, 0, 0, 0, 1, 0],\n           [0, 0, 0, 0, 0, 1, 1, 1],\n           [0, 0, 0, 1, 0, 1, 1, 1]], dtype=uint8)'
    pass

def unravel_index(indices, dims, order='C'):
    "unravel_index(indices, dims, order='C')\n\n    Converts a flat index or array of flat indices into a tuple\n    of coordinate arrays.\n\n    Parameters\n    ----------\n    indices : array_like\n        An integer array whose elements are indices into the flattened\n        version of an array of dimensions ``dims``. Before version 1.6.0,\n        this function accepted just one index value.\n    dims : tuple of ints\n        The shape of the array to use for unraveling ``indices``.\n    order : {'C', 'F'}, optional\n        Determines whether the indices should be viewed as indexing in\n        row-major (C-style) or column-major (Fortran-style) order.\n\n        .. versionadded:: 1.6.0\n\n    Returns\n    -------\n    unraveled_coords : tuple of ndarray\n        Each array in the tuple has the same shape as the ``indices``\n        array.\n\n    See Also\n    --------\n    ravel_multi_index\n\n    Examples\n    --------\n    >>> np.unravel_index([22, 41, 37], (7,6))\n    (array([3, 6, 6]), array([4, 5, 1]))\n    >>> np.unravel_index([31, 41, 13], (7,6), order='F')\n    (array([3, 6, 6]), array([4, 5, 1]))\n\n    >>> np.unravel_index(1621, (6,7,8,9))\n    (3, 1, 4, 1)"
    pass

def vdot(a, b):
    'vdot(a, b)\n\n    Return the dot product of two vectors.\n\n    The vdot(`a`, `b`) function handles complex numbers differently than\n    dot(`a`, `b`).  If the first argument is complex the complex conjugate\n    of the first argument is used for the calculation of the dot product.\n\n    Note that `vdot` handles multidimensional arrays differently than `dot`:\n    it does *not* perform a matrix product, but flattens input arguments\n    to 1-D vectors first. Consequently, it should only be used for vectors.\n\n    Parameters\n    ----------\n    a : array_like\n        If `a` is complex the complex conjugate is taken before calculation\n        of the dot product.\n    b : array_like\n        Second argument to the dot product.\n\n    Returns\n    -------\n    output : ndarray\n        Dot product of `a` and `b`.  Can be an int, float, or\n        complex depending on the types of `a` and `b`.\n\n    See Also\n    --------\n    dot : Return the dot product without using the complex conjugate of the\n          first argument.\n\n    Examples\n    --------\n    >>> a = np.array([1+2j,3+4j])\n    >>> b = np.array([5+6j,7+8j])\n    >>> np.vdot(a, b)\n    (70-8j)\n    >>> np.vdot(b, a)\n    (70+8j)\n\n    Note that higher-dimensional arrays are flattened!\n\n    >>> a = np.array([[1, 4], [5, 6]])\n    >>> b = np.array([[4, 1], [2, 2]])\n    >>> np.vdot(a, b)\n    30\n    >>> np.vdot(b, a)\n    30\n    >>> 1*4 + 4*1 + 5*2 + 6*2\n    30'
    pass

def where(condition, x=None, y=None):
    'where(condition, [x, y])\n\n    Return elements, either from `x` or `y`, depending on `condition`.\n\n    If only `condition` is given, return ``condition.nonzero()``.\n\n    Parameters\n    ----------\n    condition : array_like, bool\n        When True, yield `x`, otherwise yield `y`.\n    x, y : array_like, optional\n        Values from which to choose. `x`, `y` and `condition` need to be\n        broadcastable to some shape.\n\n    Returns\n    -------\n    out : ndarray or tuple of ndarrays\n        If both `x` and `y` are specified, the output array contains\n        elements of `x` where `condition` is True, and elements from\n        `y` elsewhere.\n\n        If only `condition` is given, return the tuple\n        ``condition.nonzero()``, the indices where `condition` is True.\n\n    See Also\n    --------\n    nonzero, choose\n\n    Notes\n    -----\n    If `x` and `y` are given and input arrays are 1-D, `where` is\n    equivalent to::\n\n        [xv if c else yv for (c,xv,yv) in zip(condition,x,y)]\n\n    Examples\n    --------\n    >>> np.where([[True, False], [True, True]],\n    ...          [[1, 2], [3, 4]],\n    ...          [[9, 8], [7, 6]])\n    array([[1, 8],\n           [3, 4]])\n\n    >>> np.where([[0, 1], [1, 0]])\n    (array([0, 1]), array([1, 0]))\n\n    >>> x = np.arange(9.).reshape(3, 3)\n    >>> np.where( x > 5 )\n    (array([2, 2, 2]), array([0, 1, 2]))\n    >>> x[np.where( x > 3.0 )]               # Note: result is 1D.\n    array([ 4.,  5.,  6.,  7.,  8.])\n    >>> np.where(x < 5, x, -1)               # Note: broadcasting.\n    array([[ 0.,  1.,  2.],\n           [ 3.,  4., -1.],\n           [-1., -1., -1.]])\n\n    Find the indices of elements of `x` that are in `goodvalues`.\n\n    >>> goodvalues = [3, 4, 7]\n    >>> ix = np.isin(x, goodvalues)\n    >>> ix\n    array([[False, False, False],\n           [ True,  True, False],\n           [False,  True, False]])\n    >>> np.where(ix)\n    (array([1, 1, 2]), array([0, 1, 1]))'
    pass

def zeros(shape, dtype=float, order='C'):
    "zeros(shape, dtype=float, order='C')\n\n    Return a new array of given shape and type, filled with zeros.\n\n    Parameters\n    ----------\n    shape : int or tuple of ints\n        Shape of the new array, e.g., ``(2, 3)`` or ``2``.\n    dtype : data-type, optional\n        The desired data-type for the array, e.g., `numpy.int8`.  Default is\n        `numpy.float64`.\n    order : {'C', 'F'}, optional, default: 'C'\n        Whether to store multi-dimensional data in row-major\n        (C-style) or column-major (Fortran-style) order in\n        memory.\n\n    Returns\n    -------\n    out : ndarray\n        Array of zeros with the given shape, dtype, and order.\n\n    See Also\n    --------\n    zeros_like : Return an array of zeros with shape and type of input.\n    empty : Return a new uninitialized array.\n    ones : Return a new array setting values to one.\n    full : Return a new array of given shape filled with value.\n\n    Examples\n    --------\n    >>> np.zeros(5)\n    array([ 0.,  0.,  0.,  0.,  0.])\n\n    >>> np.zeros((5,), dtype=int)\n    array([0, 0, 0, 0, 0])\n\n    >>> np.zeros((2, 1))\n    array([[ 0.],\n           [ 0.]])\n\n    >>> s = (2,2)\n    >>> np.zeros(s)\n    array([[ 0.,  0.],\n           [ 0.,  0.]])\n\n    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype\n    array([(0, 0), (0, 0)],\n          dtype=[('x', '<i4'), ('y', '<i4')])"
    pass

