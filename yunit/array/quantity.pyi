# Type hints for `quantity.py`.
# See also `array.pyi`.

from .array import Array
from ..type_aliases import Scalar
from ..unit import DataUnit, Unit

class Quantity(Array):
    def __init__(
        self,
        value: Scalar,
        display_unit: Unit,
        value_is_given_in_display_units: bool = True,
    ): ...
    value: Scalar
    value_in_display_units: Scalar
    vd: Scalar
    value_unit: DataUnit
    # A `Quantity + Quantity` remains a `Quantity`, but a `Quantity + Array` becomes an
    # `Array`. That's why for the below operations we only specify that a `Quantity` is
    # returned when `other` is also a `Quantity`.
    def __add__(self, other: Quantity) -> Quantity: ...
    def __sub__(self, other: Quantity) -> Quantity: ...
    def __mul__(self, other: Quantity) -> Quantity: ...
    def __truediv__(self, other: Quantity) -> Quantity: ...
    def __radd__(self, other: Quantity) -> Quantity: ...
    def __rsub__(self, other: Quantity) -> Quantity: ...
    def __rmul__(self, other: Quantity) -> Quantity: ...
    def __rtruediv__(self, other: Quantity) -> Quantity: ...