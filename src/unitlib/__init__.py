from .core_objects import Unit, Quantity, Array, define_unit
from .support.function_wrapper import add_unit_support

# Do not import `auto_axis_labelling.py` by default, to spare the heavy matplotlib
# import when it is not needed.
def enable_auto_axis_labelling():
    """
    After calling this, when plotting unitlib `Array`s with matplotlib, their axes will
    automatically be labelled with their `display_unit` and `name` (if specified).
    """
    from .support import auto_axis_labelling
