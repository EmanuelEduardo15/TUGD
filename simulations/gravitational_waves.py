import numpy as np
from scipy.integrate import solve_ivp
from core.field_equations import compute_einstein_tensor

def simulate_wave(initial_conditions, alpha=1.2e-44, steps=1000):
    """
    Solves the TUGD wave equation: ∂²Cμν/∂t² = α∇²Cμν.
    """
    def wave_eq(t, y):
        C_mu_nu, dC_dt = y[:4], y[4:]
        d2C_dt2 = alpha * np.gradient(np.gradient(C_mu_nu))
        return np.concatenate((dC_dt, d2C_dt2))
    
    sol = solve_ivp(wave_eq, [0, steps], initial_conditions, method='RK45')
    return sol
