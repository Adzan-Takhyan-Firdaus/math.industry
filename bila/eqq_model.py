import streamlit as st                    # Streamlit untuk interface web
import numpy as np                       # Numpy untuk perhitungan matematis
import matplotlib.pyplot as plt          # Matplotlib untuk membuat grafik

def run_eqq_model():
    st.title("Model Persediaan (EOQ)")   # Judul halaman EOQ

    # Input variabel dari user
    D = st.number_input("Permintaan tahunan (D)", value=1000.0)        # Permintaan tahunan
    S = st.number_input("Biaya pemesanan per order (S)", value=50.0)   # Biaya pesan per order
    H = st.number_input("Biaya penyimpanan per unit per tahun (H)", value=5.0)  # Biaya simpan per unit

    # Hitung EOQ jika input valid
    if D > 0 and S > 0 and H > 0:
        EOQ = np.sqrt((2 * D * S) / H)  # Rumus EOQ: √(2DS / H)
        st.success(f"EOQ (Economic Order Quantity) = {EOQ:.2f} unit")  # Tampilkan hasil EOQ

        # Hitung dan tampilkan grafik total cost
        Q = np.linspace(1, 2 * EOQ, 100)               # Range jumlah order
        TC = (D / Q) * S + (Q / 2) * H                 # Total cost untuk tiap Q

        plt.figure()                                   # Buat figure baru
        plt.plot(Q, TC, label="Total Cost")            # Plot kurva biaya total
        plt.axvline(EOQ, color='r', linestyle='--', label="EOQ")  # Garis EOQ
        plt.xlabel("Kuantitas Pesanan (Q)")            # Label sumbu X
        plt.ylabel("Total Biaya")                      # Label sumbu Y
        plt.title("Grafik Total Biaya terhadap EOQ")   # Judul grafik
        plt.legend()                                   # Tampilkan legenda
        st.pyplot(plt)                                 # Tampilkan grafik di Streamlit
