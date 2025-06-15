import streamlit as st                    # UI Web
import matplotlib.pyplot as plt          # Grafik

def run_queue_model():
    st.title("Model Antrian M/M/1")       # Judul halaman

    # Input dari user
    lambd = st.number_input("Tingkat kedatangan rata-rata (λ)", value=5.0)  # Lambda: pelanggan/jam
    mu = st.number_input("Tingkat pelayanan rata-rata (μ)", value=8.0)      # Mu: pelayanan/jam

    if lambd >= mu:
        st.error("λ harus lebih kecil dari μ agar sistem stabil.")          # Validasi sistem stabil
        return

    # Hitung metrik antrian
    rho = lambd / mu                            # Utilisasi server
    L = rho / (1 - rho)                         # Jumlah rata-rata dalam sistem
    Lq = rho ** 2 / (1 - rho)                   # Jumlah rata-rata dalam antrian
    W = 1 / (mu - lambd)                        # Waktu rata-rata dalam sistem
    Wq = lambd / (mu * (mu - lambd))            # Waktu rata-rata dalam antrian

    # Tampilkan hasil
    st.markdown(f"**Tingkat Utilisasi (ρ)**: {rho:.2f}")
    st.markdown(f"**Rata-rata jumlah dalam sistem (L)**: {L:.2f}")
    st.markdown(f"**Rata-rata jumlah dalam antrian (Lq)**: {Lq:.2f}")
    st.markdown(f"**Rata-rata waktu dalam sistem (W)**: {W:.2f} satuan waktu")
    st.markdown(f"**Rata-rata waktu dalam antrian (Wq)**: {Wq:.2f} satuan waktu")

    # Tampilkan grafik bar
    plt.bar(["L", "Lq"], [L, Lq], color=["blue", "orange"])
    plt.title("Jumlah rata-rata dalam sistem dan antrian")
    st.pyplot(plt)
