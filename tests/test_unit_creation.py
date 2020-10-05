from yunit import Unit
from yunit.prefixes import milli


def test_from_prefix():
    volt = Unit.define("V")
    mV = Unit.from_prefix(milli, volt)

    assert mV.name == "mV"
    assert mV.data_unit == volt
    assert mV.scale == 1e-3


def test_new():
    second = Unit.define("s")
    minute = Unit.define("min", data_unit=second, data_scale=60)
    assert minute.data_unit == second
    assert minute.scale == 60