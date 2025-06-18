# 🌟 SignalSense
## Live Demo 🚀
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://signalsense.streamlit.app)
## Project Overview

SignalSense is a Python desktop/web application that allows users to simulate various real-world signals, introduce noise to mimic interference, and then effectively clean these signals using digital filters. The application provides intuitive visualizations (time-domain and frequency-domain plots) to demonstrate the signal's state at each stage (raw, noisy, and filtered).

This project showcases core concepts in digital signal processing (DSP) and interactive application development.

## ✨ Features

* **Signal Generation:** Create clean sine waves with adjustable frequency, amplitude, and duration.
* **Noise Injection:** Add white noise to signals to simulate real-world interference.
* **Digital Filtering:** Apply a Butterworth low-pass filter to clean noisy signals, with configurable cutoff frequency and filter order.
* **Interactive Visualization:**
    * Real-time plots displaying the clean, noisy, and filtered signals in the time domain.
    * Frequency spectrum (FFT) plots for all three signal states, highlighting frequency content.
* **User-Friendly Interface:** Built with Streamlit for an interactive web-based experience with adjustable parameters via sliders.

## 🚀 How to Run

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need the following Python libraries:

* `numpy`
* `scipy`
* `matplotlib`
* `streamlit`

You can install them using pip:

```bash
pip install numpy scipy matplotlib streamlit
# Done by Albin Cleatus
