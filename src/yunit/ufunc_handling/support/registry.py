from typing import Dict, Iterable, Union, Callable

import numpy as np

from yunit.core_objects import YunitObject
from .ufunc_args import UfuncArgs

UfuncOutput = Union[YunitObject, np.ndarray, bool]
UfuncHandler = Callable[[UfuncArgs], UfuncOutput]


ufunc_handlers: Dict[np.ufunc, UfuncHandler] = {}


def implements(ufuncs: Iterable[np.ufunc]):
    """ Decorator to register a function as handling specific NumPy ufuncs. """

    # Called at `implements(..)`-time.

    def decorator(ufunc_handler: UfuncHandler):
        # Called at `def ufunc_handler(..`-time.

        for ufunc in ufuncs:
            ufunc_handlers[ufunc] = ufunc_handler

        return ufunc_handler

    return decorator