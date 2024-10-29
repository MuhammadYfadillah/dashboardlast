import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



# Load dataframes
rata_rata_shunyi_pm25 = pd.read_csv('rata_rata_shunyi_pm25.csv', index_col='month')
rata_rata_shunyi_pm10 = pd.read_csv('rata_rata_shunyi_pm10.csv', index_col='month')
rata_rata_tiantan_pm25 = pd.read_csv('rata_rata_tiantan_pm25.csv', index_col='month')
rata_rata_tiantan_pm10 = pd.read_csv('rata_rata_tiantan_pm10.csv', index_col='month')
suhu_shunyi = pd.read_csv('suhu_shunyi.csv', index_col='month')
suhu_tiantan = pd.read_csv('suhu_tiantan.csv', index_col='month')
curah_hujan_shunyi = pd.read_csv('curah_hujan_shunyi.csv', index_col='month')
curah_hujan_tiantan = pd.read_csv('curah_hujan_tiantan.csv', index_col='month')

# Fungsi untuk membuat visualisasi
def plot_data(df1, df2, label1, label2, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(df1.index, df1.values, label=label1, marker='o', color='blue')
    plt.plot(df2.index, df2.values, label=label2, marker='o', color='orange')
    plt.title(f'Perbandingan Rata-rata {label1} dan {label2} (2014)')
    plt.xlabel('Bulan')
    plt.ylabel(ylabel)
    plt.xticks(df1.index)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

# Streamlit app
st.title('Tren Kualitas Udara dikota Shunyi dan Tiantan')

st.write('Berikut merupakan visualisasi tren kualitas udara yang terjadi di kota Shunyi dan Tiantan pada periode tahun 2014.')

# Filter tombol
filter_option = st.selectbox('Pilih parameter kualitas udara', ['PM2.5', 'PM10', 'Suhu', 'Curah Hujan'])

# Menampilkan visualisasi berdasarkan filter
if filter_option == 'PM2.5':
    plot_data(rata_rata_shunyi_pm25, rata_rata_tiantan_pm25, 'PM2.5 Shunyi', 'PM2.5 Tiantan', 'Konsentrasi PM2.5 (µg/m³)')
elif filter_option == 'PM10':
    plot_data(rata_rata_shunyi_pm10, rata_rata_tiantan_pm10, 'PM10 Shunyi', 'PM10 Tiantan', 'Konsentrasi PM10 (µg/m³)')
elif filter_option == 'Suhu':
    plot_data(suhu_shunyi, suhu_tiantan, 'Suhu Shunyi', 'Suhu Tiantan', 'Suhu (°C)')
elif filter_option == 'Curah Hujan':
    plot_data(curah_hujan_shunyi, curah_hujan_tiantan, 'Curah Hujan Shunyi', 'Curah Hujan Tiantan', 'Intensitas Curah Hujan (mm)')

st.write('Kualitas Udara: Line Chart menunjukkan bahwa konsentrasi PM2.5 dan PM10 tertinggi di kedua kota terjadi pada bulan kedua tahun 2014. Pola ini menunjukkan potensi faktor pemicu polusi udara yang serupa di kedua kota pada periode tersebut.')

st.write('Suhu: Line Chart menunjukkan bahwa tren suhu di Shunyi dan Tiantan memiliki pola yang serupa selama tahun 2014. suhu di kedua kota mengalami periode terendah pada bulan januari, februari, dan desember. kemudian periode suhu tertinggi pada bulan juli. Hal ini menunjukkan bahwa faktor-faktor meteorologi yang memengaruhi suhu mungkin serupa di kedua kota.')

st.write('Curah Hujan: Line Chart menunjukkan bahwa tren curah hujan di Shunyi dan Tiantan berbeda selama tahun 2014. Meskipun perbedaannya tidak signifikan, tetapi Ini menunjukkan bahwa faktor-faktor meteorologi yang memengaruhi curah hujan mungkin berbeda di kedua kota.')