from abc import ABC, abstractproperty, abstractmethod
from numbers import Number

import numpy as np

from .quantity import Quantity


class Unit(Quantity, ABC):
    """
    A physical unit. For example, "farad", "μm²", or "mV/nS".

    Units can be:
     - raised to a power (`meter**2`);
     - composed with other units (`newton * meter`);
     - applied to numeric data (`8 * farad`, `[3,5] * mV`);

    This abstract base class (`ABC`) defines the interface and functionality common to
    all `Unit` subclasses:
        - `DataUnit`
        - `UnitAtom`
        - `DataUnitAtom`
        - `PoweredUnitAtom`
        - `PoweredDataUnitAtom`
        - `CompoundUnit`
        - `CompoundDataUnit`.
    """

    #
    #
    # ---------------
    # Core properties

    @abstractproperty
    def name(self) -> str:
        """
        How this unit is displayed textually (eg. in print statements or in axis labels
        of data plots). Examples: "min", "mV".
        """
        ...  # For subclasses to implement.

    @abstractproperty
    def scale(self) -> Number:
        """
        Factor with which numeric data annotated with this unit is multiplied before
        being stored in memory.

        For example, if this `unit` is "mV" (with a `data_unit` of "volt") and its
        `scale` is 1E-3, the numeric data underlying the expression `8 * mV` will
        be stored as `0.008` in memory.
        """
        ...  # For subclasses to implement.

    @abstractproperty
    def data_unit(self) -> "DataUnit":
        """
        A scalar multiple or submultiple of this `unit`.

        Numeric data annotated with this `unit` is stored in `data_unit`s in memory.
        See `scale`.

        One `unit` equals "`scale`" of its `data_unit`s.
        E.g. 1 minute = 60 seconds.
        """
        ...  # For subclasses to implement.

    #
    #
    # --------------------------------
    # Behave as a proper Python object

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.__class__.__name__} "{self.name}">'

    def __format__(self, format_spec: str = "") -> str:
        return str(self)

    #
    #
    # ---------
    # Internals

    @abstractmethod
    def __hash__(self) -> int:
        """ Used for unit (in)equality checks. """
        ...  # For subclasses to implement.

    @abstractmethod
    def _raised_to(self, power: int) -> "Unit":
        ...  # For subclasses to implement.

    #
    #
    # -------------------------------------------
    # Substitutability with `Quantity` base class

    @property
    def data(self):
        return np.array(self.scale)

    @property
    def display_unit(self):
        return self

    _DIY_help_text = (
        "If you're working with unitlib Arrays or Quantities, you can get their "
        "bare numeric values (plain NumPy arrays or Python scalars) "
        "via `array.data` or `quantity.value`, and work with them manually."
    )


class DataUnit(Unit, ABC):
    """
    A `Unit` in which numeric data is stored in memory.

    See the `Unit.data_unit` property.
    """

    @property
    def data_unit(self):
        return self

    @property
    def scale(self):
        return 1


class IncompatibleUnitsError(Exception):
    """
    Raised when an operation with incompatible units is attempted
    (eg `8 volt + 2 newton`).
    """
