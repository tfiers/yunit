from .core_objects import Unit, Quantity, Array, define_unit


try:
    import matplotlib
except ModuleNotFoundError:
    pass  # A matplotlib installation is not required.
else:
    # But if it is installed, allow it to plot unitlib Arrays.
    from .support import matplotlib_support
