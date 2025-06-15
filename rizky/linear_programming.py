import streamlit as st                    # Import library Streamlit untuk antarmuka web
import numpy as np                       # Import numpy untuk operasi numerik (array, dll)
from scipy.optimize import linprog       # Import fungsi linprog untuk optimasi linear
import matplotlib.pyplot as plt          # Import matplotlib untuk plotting grafik

def run_linear_programming():
    st.title("Optimasi Produksi (Linear Programming)")  # Judul halaman Streamlit

    # Input fungsi objektif Z = c1*x + c2*y
    st.markdown("### Masukkan Fungsi Objektif")
    c1 = st.number_input("Koefisien x (misal: 40)", value=40.0)  # Input koefisien x
    c2 = st.number_input("Koefisien y (misal: 30)", value=30.0)  # Input koefisien y

    # Input kendala pertama: a1_1*x + a1_2*y <= b1
    st.markdown("### Masukkan Kendala 1 (misal: 2x + 1y ≤ 100)")
    a1_1 = st.number_input("Koefisien x (kendala 1)", value=2.0)     # Input x untuk kendala 1
    a1_2 = st.number_input("Koefisien y (kendala 1)", value=1.0)     # Input y untuk kendala 1
    b1 = st.number_input("Nilai batas kanan (kendala 1)", value=100.0)  # Batas kanan kendala 1

    # Input kendala kedua: a2_1*x + a2_2*y <= b2
    st.markdown("### Masukkan Kendala 2 (misal: 1x + 1y ≤ 80)")
    a2_1 = st.number_input("Koefisien x (kendala 2)", value=1.0)     # Input x untuk kendala 2
    a2_2 = st.number_input("Koefisien y (kendala 2)", value=1.0)     # Input y untuk kendala 2
    b2 = st.number_input("Nilai batas kanan (kendala 2)", value=80.0)  # Batas kanan kendala 2

    # Fungsi objektif untuk linprog (pakai tanda minus karena linprog default = minimisasi)
    c = [-c1, -c2]                              # Ubah ke negatif untuk maksimisasi
    A = [[a1_1, a1_2], [a2_1, a2_2]]            # Matriks koefisien kendala
    b = [b1, b2]                                # Vektor batas kendala
    bounds = [(0, None), (0, None)]             # Batasan variabel x, y ≥ 0

    # Jalankan optimasi menggunakan linprog dari scipy
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')  # Proses optimasi

    if res.success:  # Jika solusi berhasil ditemukan
        # Tampilkan solusi ke layar
        st.success(f"Solusi optimal: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}")  # Output nilai x dan y
        st.info(f"Nilai maksimum Z = {-res.fun:.2f}")  # Output nilai Z (ingat awalnya dibalik minus)

        # Visualisasi wilayah feasible dan solusi optimal
        x_vals = np.linspace(0, max(b1, b2), 200)                # Bikin nilai x dari 0 ke maksimum
        y1 = (b1 - a1_1 * x_vals) / a1_2                         # Rumus garis kendala 1
        y2 = (b2 - a2_1 * x_vals) / a2_2                         # Rumus garis kendala 2

        plt.figure(figsize=(8, 6))                               # Ukuran grafik
        plt.plot(x_vals, y1, label=f"{a1_1}x + {a1_2}y ≤ {b1}")  # Plot garis kendala 1
        plt.plot(x_vals, y2, label=f"{a2_1}x + {a2_2}y ≤ {b2}")  # Plot garis kendala 2
        plt.fill_between(x_vals, np.minimum(y1, y2), color='skyblue', alpha=0.3)  # Wilayah feasible
        plt.plot(res.x[0], res.x[1], 'ro', label='Solusi Optimal')  # Titik solusi optimal
        plt.xlabel('x')                                          # Label sumbu x
        plt.ylabel('y')                                          # Label sumbu y
        plt.title('Wilayah Feasible dan Solusi Optimal')         # Judul grafik
        plt.legend()                                             # Tampilkan legenda
        st.pyplot(plt)                                           # Tampilkan grafik di Streamlit
    else:
        st.error("Tidak ditemukan solusi optimal.")              # Jika gagal menemukan solusi
