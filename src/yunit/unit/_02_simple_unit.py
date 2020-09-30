from ._03_powered_unit import PoweredDataUnit, PoweredUnit


class SimpleUnit(PoweredUnit):
    """
    Eg "newton" or "mV"; as contrasted with "mV²" (a `PoweredUnit`) or "newton * meter²"
    (a `CompoundUnit`).
    """

    def __new__(
        cls,
        name: str,
        data_unit: "SimpleDataUnit",
        data_scale: float,
    ):
        simple_unit = object.__new__(cls)
        #   `cls` can be `SimpleUnit` or `SimpleDataUnit`.
        # We are a special case of a `PoweredUnit`:
        simple_unit.power = 1
        simple_unit.ground_unit = simple_unit
        # The below three attributes cannot be set directly (e.g. using
        # `simple_unit.name = name`); this would yield an `AttributeError`. This is
        # because these attributes are *properties* in the parent class. Properties can
        # only be overriden by new properties. Hence the annoying verbosity of dummy
        # variables and trivial property getters.
        # (And no, using `simple_unit.name = property(..)`
        #  or `simple_unit.__dict__["name"] = ..` also doesn't work :) ).
        simple_unit._name = name
        simple_unit._data_unit = data_unit
        simple_unit._data_scale = data_scale
        return simple_unit

    @property
    def name(self):
        return self._name

    @property
    def data_unit(self):
        return self._data_unit

    @property
    def data_scale(self):
        return self._data_scale

    def __hash__(self):
        return hash((self.name, self.data_unit, self.data_scale))

    def _raised_to(self, power):
        return PoweredUnit(self, power)


class SimpleDataUnit(PoweredDataUnit, SimpleUnit):
    def __new__(cls, name: str):
        return SimpleUnit.__new__(cls, name, ..., ...)

    def __hash__(self):
        return hash(self.name)

    def _raised_to(self, power):
        return PoweredDataUnit(self, power)


dimensionless = SimpleDataUnit("1")
