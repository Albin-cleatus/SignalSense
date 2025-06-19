import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# --- Signal Processing Functions ---
def generate_signal(frequency, amplitude, duration, sample_rate):
    """Generates a clean sine wave."""
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return time, amplitude * np.sin(2 * np.pi * frequency * time)

def add_noise(signal_input, noise_level):
    """Adds white Gaussian noise to a signal."""
    noise = noise_level * np.random.randn(len(signal_input))
    return signal_input + noise

def apply_lowpass_filter(signal_input, cutoff_freq, sample_rate, order=4):
    """Applies a Butterworth low-pass filter to the signal."""
    nyquist = 0.5 * sample_rate
    if cutoff_freq >= nyquist:
        raise ValueError("Cutoff frequency must be below Nyquist frequency.")
    normal_cutoff = cutoff_freq / nyquist
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, signal_input)

def compute_fft(signal_input, sample_rate):
    """Computes FFT and returns frequency and magnitude arrays."""
    N = len(signal_input)
    T = 1.0 / sample_rate
    yf = np.fft.fft(signal_input)
    xf = np.fft.fftfreq(N, T)[:N // 2]
    return xf, 2.0 / N * np.abs(yf[0:N // 2])

# --- Streamlit App ---
st.set_page_config(layout="wide", page_title="SignalSense: Signal Simulation & Filtering")
st.title("\U0001F31F SignalSense: Signal Simulation & Filtering")
st.markdown("Simulate, add noise, filter, and visualize signals in real-time!")

# Footer credit

# --- Sidebar Controls ---
st.sidebar.header("Signal Parameters")
signal_freq = st.sidebar.slider("Signal Frequency (Hz)", 1, 50, 5)
signal_amp = st.sidebar.slider("Signal Amplitude", 0.1, 5.0, 1.0, 0.1)
duration = st.sidebar.slider("Duration (seconds)", 0.5, 5.0, 2.0, 0.5)
sample_rate = st.sidebar.slider("Sample Rate (Hz)", 100, 5000, 1000, 100)

st.sidebar.header("Noise Parameters")
noise_level = st.sidebar.slider("Noise Level", 0.0, 2.0, 0.5, 0.1)

st.sidebar.header("Filter Parameters")
cutoff_freq = st.sidebar.slider("Filter Cutoff Frequency (Hz)", 1, 100, 10)
filter_order = st.sidebar.slider("Filter Order", 1, 10, 4)

# --- Generate & Visualise ---
if st.sidebar.button("Generate & Process Signal"):
    try:
        st.info("Generating and processing signal...")

        time_vec, clean = generate_signal(signal_freq, signal_amp, duration, sample_rate)
        noisy = add_noise(clean, noise_level)
        filtered = apply_lowpass_filter(noisy, cutoff_freq, sample_rate, filter_order)

        xf_clean, yf_clean = compute_fft(clean, sample_rate)
        xf_noisy, yf_noisy = compute_fft(noisy, sample_rate)
        xf_filtered, yf_filtered = compute_fft(filtered, sample_rate)

        fig, axs = plt.subplots(3, 2, figsize=(16, 12))

        axs[0, 0].plot(time_vec, clean, label='Clean', color='blue')
        axs[0, 0].set(title='Clean Signal (Time Domain)', xlabel='Time [s]', ylabel='Amplitude', xlim=(0, duration))
        axs[0, 0].legend(); axs[0, 0].grid(True)

        axs[0, 1].plot(xf_clean, yf_clean, color='blue')
        axs[0, 1].set(title='Clean Signal (FFT)', xlabel='Frequency [Hz]', ylabel='Magnitude', xlim=(0, 2 * signal_freq + 5), ylim=(0, signal_amp * 1.2))
        axs[0, 1].grid(True)

        axs[1, 0].plot(time_vec, noisy, label='Noisy', color='red', alpha=0.7)
        axs[1, 0].set(title='Noisy Signal (Time Domain)', xlabel='Time [s]', ylabel='Amplitude', xlim=(0, duration))
        axs[1, 0].legend(); axs[1, 0].grid(True)

        axs[1, 1].plot(xf_noisy, yf_noisy, color='red', alpha=0.7)
        axs[1, 1].set(title='Noisy Signal (FFT)', xlabel='Frequency [Hz]', ylabel='Magnitude', xlim=(0, 2 * signal_freq + 5))
        axs[1, 1].grid(True)

        axs[2, 0].plot(time_vec, filtered, label='Filtered', color='green')
        axs[2, 0].set(title='Filtered Signal (Time Domain)', xlabel='Time [s]', ylabel='Amplitude', xlim=(0, duration))
        axs[2, 0].legend(); axs[2, 0].grid(True)

        axs[2, 1].plot(xf_filtered, yf_filtered, color='green')
        axs[2, 1].set(title='Filtered Signal (FFT)', xlabel='Frequency [Hz]', ylabel='Magnitude', xlim=(0, 2 * signal_freq + 5), ylim=(0, signal_amp * 1.2))
        axs[2, 1].grid(True)

        plt.tight_layout()
        st.pyplot(fig)

    except ValueError as ve:
        st.error(f"❌ Error: {ve}")
else:
    st.write("Use the sidebar to adjust parameters, then click the button to generate and filter your signal.")

# Written by Albin Cleatus
