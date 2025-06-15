import streamlit as st                    # Untuk UI web
import numpy as np                       # Untuk perhitungan matematis
import matplotlib.pyplot as plt          # Untuk grafik

def run_exponential_model():
    st.title("Model Eksponensial (Decay/Growth)")     # Judul halaman

    # Input nilai awal dan laju
    A = st.number_input("Nilai awal (A)", value=100.0)                   # Nilai awal
    r = st.number_input("Laju pertumbuhan (positif) atau peluruhan (negatif) (r)", value=-0.1)  # Laju

    t = np.linspace(0, 50, 200)        # Rentang waktu 0–50
    y = A * np.exp(r * t)              # Rumus pertumbuhan/peluruhan eksponensial

    st.line_chart({"Waktu": t, "Nilai": y})  # Tampilkan grafik cepat Streamlit
    plt.plot(t, y)                           # Buat grafik dengan matplotlib
    plt.title("Model Eksponensial")         # Judul grafik
    plt.xlabel("Waktu")                     # Label X
    plt.ylabel("Nilai")                     # Label Y
    st.pyplot(plt)                          # Tampilkan grafik
