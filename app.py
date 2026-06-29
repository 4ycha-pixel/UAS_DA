import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Forecasting Penjualan Retail",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/combo-chart--v1.png",
        width=80
    )

    st.title("Forecasting Retail")

    st.markdown("---")

    st.subheader("📚 Informasi")

    st.write("""
### Mata Kuliah
- Data Mining

### Metode
- Exponential Smoothing
- ARIMA (1,0,0)

### Dataset
Customer Shopping Dataset
""")

    st.markdown("---")

    st.success("🏆 Model Terbaik : ARIMA (1,0,0)")

# =====================================================
# MEMBACA DATASET
# =====================================================

df = pd.read_csv("customer_shopping_data.csv")

df["invoice_date"] = pd.to_datetime(
    df["invoice_date"],
    dayfirst=True
)

# Membuat kolom sales
df["sales"] = df["quantity"] * df["price"]

# Agregasi penjualan bulanan
monthly_sales = (
    df.groupby(
        pd.Grouper(
            key="invoice_date",
            freq="ME"
        )
    )["sales"]
    .sum()
    .reset_index()
)

# =====================================================
# HAPUS BULAN TERAKHIR (BELUM LENGKAP)
# =====================================================

monthly_sales = monthly_sales.iloc[:-1]

# =====================================================
# HEADER
# =====================================================

st.title("📈 Forecasting Penjualan Retail")

st.markdown("## UAS Data Mining")

st.write("""
Dashboard ini menampilkan hasil forecasting penjualan retail
menggunakan metode **Exponential Smoothing** dan
**ARIMA (1,0,0)**.

Model terbaik dipilih berdasarkan nilai
**MAE**, **RMSE**, dan **MAPE**.
""")
# =====================================================
# RINGKASAN DATASET
# =====================================================

st.markdown("---")

st.subheader("📊 Ringkasan Dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Jumlah Transaksi",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Jumlah Bulan",
        len(monthly_sales)
    )

with col3:
    st.metric(
        "Model Terbaik",
        "ARIMA (1,0,0)"
    )

st.info(
    f"""
📅 **Periode Dataset**

{monthly_sales['invoice_date'].min().strftime('%B %Y')}
hingga
{monthly_sales['invoice_date'].max().strftime('%B %Y')}
"""
)

# =====================================================
# GRAFIK PENJUALAN
# =====================================================

st.markdown("---")

st.subheader("📈 Grafik Penjualan Bulanan")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(
    monthly_sales["invoice_date"],
    monthly_sales["sales"],
    marker="o",
    linewidth=3,
    color="#1f77b4"
)

ax.set_title("Monthly Retail Sales")

ax.set_xlabel("Periode")

ax.set_ylabel("Total Penjualan")

ax.grid(alpha=0.3)

plt.xticks(rotation=45)

st.pyplot(fig)

# =====================================================
# HASIL EVALUASI
# =====================================================

st.markdown("---")

st.subheader("📋 Hasil Evaluasi Model")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "MAE",
        "202.829,23"
    )

with c2:
    st.metric(
        "RMSE",
        "244.902,24"
    )

with c3:
    st.metric(
        "MAPE",
        "2,19%"
    )

st.success(
    """
🏆 **Model terbaik adalah ARIMA (1,0,0)**

Model dipilih karena memiliki nilai MAPE paling kecil
dibandingkan Exponential Smoothing.
"""
)
# =====================================================
# FORECAST PENJUALAN
# =====================================================

st.markdown("---")

st.subheader("🔮 Forecast Penjualan")

st.write("""
Tekan tombol di bawah untuk menampilkan hasil prediksi
penjualan menggunakan model terbaik **ARIMA (1,0,0)**.
""")

if st.button("🚀 Prediksi Bulan Berikutnya", use_container_width=True):

    st.success("✅ Prediksi berhasil dilakukan menggunakan model ARIMA (1,0,0).")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Periode Prediksi",
            "Maret 2023"
        )

    with col2:

        st.metric(
            "Prediksi Penjualan",
            "Rp 9.371.164,99"
        )

    st.info("""
Model ARIMA menghasilkan nilai MAPE sebesar **2,19%** sehingga
dipilih sebagai model terbaik untuk melakukan forecasting.
""")

    st.balloons()

# =====================================================
# DATA BULANAN
# =====================================================

st.markdown("---")

st.subheader("📑 Data Penjualan Bulanan")

st.dataframe(
    monthly_sales,
    use_container_width=True,
    hide_index=True
)

# =====================================================
# KESIMPULAN
# =====================================================

st.markdown("---")

st.subheader("📝 Kesimpulan")

st.write("""
Berdasarkan hasil evaluasi model forecasting, metode
**ARIMA (1,0,0)** memberikan performa terbaik dibandingkan
Exponential Smoothing.

Model ARIMA memperoleh:

- MAE = **202.829,23**
- RMSE = **244.902,24**
- MAPE = **2,19%**

Sehingga model tersebut dipilih untuk melakukan prediksi
penjualan retail pada periode berikutnya.
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption("""
Developed by **Aisyah**

Ujian Akhir Semester - Data Mining

Institut Bisnis dan Teknologi Indonesia
""")