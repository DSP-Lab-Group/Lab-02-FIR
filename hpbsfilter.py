import numpy as np
import firdesign
from firfilter import FirFilter

if __name__ == '__main__':
    file_path = 'ECG_1000Hz.dat'
    sample_rate = 1000
    w_1 = 49
    w_2 = 51
    data = np.loadtxt(file_path)
    n = len(data)
    # Create bands-top filter
    band_stop_h = firdesign.band_stop_design(sample_rate, [w_1, w_2])
    band_stop_filter = FirFilter(band_stop_h)
    # Create high-pass filter
    high_pass_h = firdesign.high_pass_design(sample_rate)
    high_pass_filter = FirFilter(high_pass_h)
    # Remove the 50Hz interference using the band-stop filter
    band_stop_output = np.zeros(n)
    for i in range(n):
        band_stop_output[i] = band_stop_filter.dofilter(data[i])
    # Process the baseline wander using the high-pass filter
    high_pass_output = np.zeros(n)
    for i in range(n):
        high_pass_output[i] = high_pass_filter.dofilter(band_stop_output[i])
