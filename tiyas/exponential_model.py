import streamlit as st                    # Streamlit untuk tampilan web
import numpy as np                       # Untuk perhitungan matematis
import matplotlib.pyplot as plt          # Untuk grafik visual

def run_exponential_model():
    st.title("Model Eksponensial (Pertumbuhan / Peluruhan)")

    # Input dari user
    A = st.number_input("Nilai awal (A)", value=100.0)  # Nilai awal
    r = st.number_input("Laju pertumbuhan (+) / peluruhan (-) (r)", value=-0.1)  # Laju r

    t = np.linspace(0, 50, 200)            # Waktu dari 0 sampai 50
    y = A * np.exp(r * t)                  # Rumus eksponensial: y = A * e^(rt)

    # Tampilkan jenis model
    if r > 0:
        st.info("📈 Ini adalah model **Pertumbuhan Eksponensial**.")
    elif r < 0:
        st.info("📉 Ini adalah model **Peluruhan Eksponensial**.")
    else:
        st.warning("📊 Nilai r = 0, grafik akan datar (konstan).")

    # Tampilkan nilai-nilai penting
    st.markdown("### Hasil Perhitungan:")
    st.write(f"Nilai saat t = 10: **{A * np.exp(r * 10):.2f}**")
    st.write(f"Nilai saat t = 25: **{A * np.exp(r * 25):.2f}**")
    st.write(f"Nilai saat t = 50: **{A * np.exp(r * 50):.2f}**")

    # Tampilkan grafik
    plt.plot(t, y)
    plt.xlabel("Waktu (t)")
    plt.ylabel("Nilai (y)")
    plt.title("Model Eksponensial y = A * e^(rt)")
    st.pyplot(plt)
