import numpy as np
from numpy import allclose as numeric_equals

from yunit import Array, Quantity, Unit
from yunit.prefixes import milli, nano
from yunit.unit import PoweredUnit

volt = Unit("V")
mV = Unit.from_prefix(milli, volt)
nV = Unit.from_prefix(nano, volt)

second = Unit("s")
ms = Unit.from_prefix(milli, second)
minute = Unit("min", data_unit=second, data_scale=60)

siemens = Unit("S")
nS = Unit.from_prefix(nano, siemens)


def test_array_times_unit():
    amumu = 3 * mV * mV
    assert numeric_equals(amumu.data, 3e-6)


def test_array_div_unit():
    amudu = 3 * nS / mV
    assert numeric_equals(amudu.data, 3e-6)


def test_1_over_vs_x_over():
    recip = 1 / ms
    assert isinstance(recip, (Unit, PoweredUnit))
    assert recip.data_unit == 1 / second
    assert numeric_equals(recip.data_scale, 1000)

    recip2 = 2 / ms
    assert isinstance(recip2, Quantity)
    assert recip2.data_unit == 1 / second
    assert numeric_equals(recip2.data, 2000)


def test_power():
    smup = 8 * (mV ** 2)
    assert numeric_equals(smup.data, 8e-6)
    assert smup.data_unit == volt ** 2 == volt * volt


def test_quantity():
    time = 2 * minute
    assert time.value_unit == time.display_unit == minute
    assert time.data_unit == second
    assert time.value == time.data_in_display_units.item() == 2
    assert time.data.item() == 120


def test_array():
    amu = [3, 1, 5] * nV
    assert isinstance(amu, Array) and not isinstance(amu, Quantity)


def test_quantity_mul():
    smu = 3 * mV
    assert isinstance(smu, Quantity)
    # assert 2 * smu == smu + smu  # todo: implement ufunc `equal`


def test_remove_units():
    assert 1 * ms / ms == 1


def test_ndarray():
    lmu = np.ones(2) * mV
    assert lmu.display_unit == mV
    assert numeric_equals(lmu.data, [1e-3, 1e-3])
    assert numeric_equals(lmu.data_in_display_units, [1, 1])
    assert str(lmu) == "[1 1] mV"
