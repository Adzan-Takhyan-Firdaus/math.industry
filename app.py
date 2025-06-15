import streamlit as st
from rizky.linear_programming import run_linear_programming
from bila.eqq_model import run_eqq_model
from wulan.queue_model import run_queue_model
from tiyas.exponential_model import run_exponential_model

st.set_page_config(page_title="Aplikasi Matematika Industri", layout="wide")


st.sidebar.title("Aplikasi Matematika pada Lingkungan Industri")
st.sidebar.write("Pilih salah satu model dari menu di bawah ini. Masukkan input yang diminta, lalu lihat hasil dan grafik.")

menu = st.sidebar.radio("Pilih Model", ["Optimasi Produksi (Linear Programming)",
                                        "Model Persediaan (EOQ)",
                                        "Model Antrian (M/M/1)",
                                        "Model Eksponensial"])

st.sidebar.title("Kelompok 2 Matematika Terapan")
st.sidebar.markdown("""
- Adzan Takhyan Firdaus
- Wulan Melinda Sari
- Muhamad Rizky
- Nabila Rahmadani
- Tiyas Sulis Setyawati
""")

if menu == "Optimasi Produksi (Linear Programming)":
    run_linear_programming()
elif menu == "Model Persediaan (EOQ)":
    run_eqq_model()
elif menu == "Model Antrian (M/M/1)":
    run_queue_model()
elif menu == "Model Eksponensial":
    run_exponential_model()
