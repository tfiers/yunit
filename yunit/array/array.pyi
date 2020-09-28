# Type hints for `array.py`.
#
# Main reason for this file (instead of just giving all type-hints in `array.py` itself)
# is to add type-hints on top of the `NDArrayOperatorsMixin` dunder methods (i.e.
# `__mul__` and `__imul__` etc).

from typing import Union as Either

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

from ..type_aliases import ArrayLike
from ..unit import DataUnit, Unit

class UnitError(Exception): ...

class Array(NDArrayOperatorsMixin):
    data: np.ndarray
    data_unit: DataUnit
    display_unit: Unit
    def __init__(
        self,
        data: ArrayLike,
        display_unit: Unit,
        data_are_given_in_display_units: bool = False,
    ): ...
    data_in_display_units: np.ndarray
    dd: np.ndarray
    def __array_ufunc__(self, *args, **kwargs) -> Either[Array, ArrayLike]: ...
    def __add__(self, other) -> Array: ...
    def __sub__(self, other) -> Array: ...
    def __mul__(self, other) -> Array: ...
    def __truediv__(self, other) -> Array: ...
    def __radd__(self, other) -> Array: ...
    def __rsub__(self, other) -> Array: ...
    def __rmul__(self, other) -> Array: ...
    def __rtruediv__(self, other) -> Array: ...
    _DIY_help_text: str
