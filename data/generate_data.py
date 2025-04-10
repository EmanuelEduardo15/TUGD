import pandas as pd

def generate_ligo_data():
    data = {
        "event": ["GW150914", "GW170817", "GW190521", "GW200115"],
        "delta_t": [0.2, 0.15, 0.1, 0.25],  # Em segundos
        "energy": [1.2e52, 8.3e51, 2.1e53, 5.7e51],  # Em joules
        "frequency": [150, 2000, 80, 500],  # Em Hz
        "distance": [410, 40, 1500, 300]  # Em Mpc
    }
    df = pd.DataFrame(data)
    df.to_csv("data/ligo_events.csv", index=False)
    return df

if __name__ == "__main__":
    generate_ligo_data()
