import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_eqq_model():
    st.title("Model Persediaan (EOQ)")
    D = st.number_input("Permintaan tahunan (D)", value=1000.0)
    S = st.number_input("Biaya pemesanan per order (S)", value=50.0)
    H = st.number_input("Biaya penyimpanan per unit per tahun (H)", value=5.0)

    if D > 0 and S > 0 and H > 0:
        EOQ = np.sqrt((2 * D * S) / H)
        st.success(f"EOQ (Economic Order Quantity) = {EOQ:.2f} unit")

        Q = np.linspace(1, 2 * EOQ, 100)
        TC = (D / Q) * S + (Q / 2) * H

        plt.figure()
        plt.plot(Q, TC, label="Total Cost")
        plt.axvline(EOQ, color='r', linestyle='--', label="EOQ")
        plt.xlabel("Kuantitas Pesanan (Q)")
        plt.ylabel("Total Biaya")
        plt.title("Grafik Total Biaya terhadap EOQ")
        plt.legend()
        st.pyplot(plt)