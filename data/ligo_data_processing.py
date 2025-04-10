import h5py
import pandas as pd

def process_gw_event(h5_file_path):
    """
    Converte dados .hdf5 do LIGO para .csv.
    """
    with h5py.File(h5_file_path, 'r') as f:
        strain = f['strain/Strain'][()]
        time = f['strain/Strain'].attrs['Xstart']
        delta_t = f['strain/Strain'].attrs['Xspacing']
        
    df = pd.DataFrame({'time': time + np.arange(len(strain)) * delta_t, 'strain': strain})
    df.to_csv('data/processed_event.csv', index=False)
    return df
