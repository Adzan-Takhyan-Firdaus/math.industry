import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_exponential_model():
    st.title("Model Eksponensial (Decay/Growth)")

    # Input nilai awal dan laju pertumbuhan/peluruhan
    A = st.number_input("Nilai awal (A)", value=100.0)
    r = st.number_input("Laju pertumbuhan (+) / peluruhan (-) (r)", value=-0.05)
    target = st.number_input("Nilai target (berapa sisa dari A, misalnya 80%)", value=80.0)

    t = np.linspace(0, 50, 200)
    y = A * np.exp(r * t)

    # Tampilkan grafik
    plt.plot(t, y, label='Q(t) = A * e^(rt)')
    plt.axhline(y=target, color='red', linestyle='--', label=f'Target: {target}')
    plt.xlabel("Waktu")
    plt.ylabel("Nilai")
    plt.title("Model Eksponensial")
    plt.legend()
    st.pyplot(plt)

    # Perhitungan waktu t kapan mencapai nilai target
    if (A > 0) and (0 < target < A) and r != 0:
        try:
            t_target = -np.log(target / A) / r
            st.success(f"Nilai akan turun menjadi {target} setelah sekitar {t_target:.2f} waktu satuan.")
        except:
            st.error("Gagal menghitung waktu, pastikan input valid.")
    else:
        st.warning("Nilai target harus lebih kecil dari A dan r ≠ 0")
