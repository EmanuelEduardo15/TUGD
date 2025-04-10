import numpy as np
from sympy import symbols, simplify

def compute_einstein_tensor(metric, coordinates):
    """
    Computes the Einstein tensor Gμν for a given metric.
    - Uses EinsteinPy for symbolic calculations.
    """
    from einsteinpy.symbolic import EinsteinTensor, MetricTensor
    g = MetricTensor(metric, coordinates)
    return EinsteinTensor.from_metric(g)
