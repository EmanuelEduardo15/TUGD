import numpy as np

def quantum_fluctuations(shape, amplitude=1e-30):
    """
    Generates Gaussian quantum fluctuations Qμν.
    - Toy model for validation.
    """
    return amplitude * np.random.randn(*shape)
