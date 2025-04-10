import pandas as pd
from scipy.optimize import curve_fit

def fit_alpha(data_path='data/events.csv'):
    """
    Fits α using LIGO's Δt vs energy data.
    """
    data = pd.read_csv(data_path)
    def model(t, alpha):
        return alpha * np.sqrt(data['energy'])
    
    params, _ = curve_fit(model, data['delta_t'], data['delta_t'])
    return params[0]
