import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Proyek Akhir Dicoding')
st.header('Visualisasi Data')

data_day = pd.read_csv("data_day.csv")
data_hour = pd.read_csv("data_hour.csv")

# Pertanyaan 1: Bagaimana perbandingan distribusi penyewa kasual dibandingkan dengan penyewa terdaftar pada tahun 2011 dan 2012?
data_day['TanggalWaktu'] = pd.to_datetime(data_day['TanggalWaktu'])
data_2011 = data_day[data_day['TanggalWaktu'].dt.year == 2011]
total_casual_2011 = data_2011['Kasual'].sum()
total_registered_2011 = data_2011['Terdaftar'].sum()
labels = ['Penyewa Kasual', 'Penyewa Terdaftar']
sizes_2011 = [total_casual_2011, total_registered_2011]
data_2012 = data_day[data_day['TanggalWaktu'].dt.year == 2012]
total_casual_2012 = data_2012['Kasual'].sum()
total_registered_2012 = data_2012['Terdaftar'].sum()
sizes_2012 = [total_casual_2012, total_registered_2012]
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
# Pie chart untuk tahun 2011
axs[0].pie(sizes_2011, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'], explode=(0.1, 0))
axs[0].set_title('Distribusi Penyewa Kasual dan Terdaftar pada Tahun 2011')
# Pie chart untuk tahun 2012
axs[1].pie(sizes_2012, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'], explode=(0.1, 0))
axs[1].set_title('Distribusi Penyewa Kasual dan Terdaftar pada Tahun 2012')
st.pyplot(plt)


# Pertanyaan 2: Apakah hari libur mempengaruhi jumlah penggunaan sepeda kasual dibandingkan dengan hari kerja dalam periode tahun 2011 dan 2012?
data_day['TanggalWaktu'] = pd.to_datetime(data_day['TanggalWaktu'])
tahun_data_2011 = data_day[data_day['TanggalWaktu'].dt.year == 2011]
libur_vs_kerja_2011 = tahun_data_2011.groupby('Libur')['Kasual'].mean()
tahun_data_2012 = data_day[data_day['TanggalWaktu'].dt.year == 2012]
libur_vs_kerja_2012 = tahun_data_2012.groupby('Libur')['Kasual'].mean()
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
# Plot untuk tahun 2011
libur_vs_kerja_2011.plot(kind='bar', ax=ax[0], color='lightblue')
ax[0].set_title('Pengguna Kasual di Hari Libur vs Hari Kerja (2011)')
ax[0].set_ylabel('Rata-rata Jumlah Pengguna')
ax[0].set_xlabel('Libur (1: Ya, 0: Tidak)')
ax[0].set_xticks([0, 1])
ax[0].set_xticklabels(['Tidak', 'Ya'], rotation=0)
# Plot untuk tahun 2012
libur_vs_kerja_2012.plot(kind='bar', ax=ax[1], color='lightgreen')
ax[1].set_title('Pengguna Kasual di Hari Libur vs Hari Kerja (2012)')
ax[1].set_ylabel('Rata-rata Jumlah Pengguna')
ax[1].set_xlabel('Libur (1: Ya, 0: Tidak)')
ax[1].set_xticks([0, 1])
ax[1].set_xticklabels(['Tidak', 'Ya'], rotation=0)
plt.tight_layout()
st.pyplot(plt)


# Pertanyaan 3: Di musim apa jumlah penyewa sepeda paling banyak dalam periode tahun 2011 dan 2012?
data_day['TanggalWaktu'] = pd.to_datetime(data_day['TanggalWaktu'])
data_2011_2012 = data_day[data_day['TanggalWaktu'].dt.year.isin([2011, 2012])]
season_rentals = data_2011_2012.groupby([data_2011_2012['TanggalWaktu'].dt.year, 'Musim'])['Jumlah'].sum().reset_index()
season_rentals.columns = ['Tahun', 'Musim', 'Jumlah']
plt.figure(figsize=(10, 6))
sns.barplot(x='Musim', y='Jumlah', hue='Tahun', data=season_rentals, palette='Set2')
plt.title('Total Bike Rentals per Season for 2011 and 2012', fontsize=16)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Total Rentals', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)


# Pertanyaan 4: Jam berapa yang paling sering digunakan oleh penyewa kasual dan terdaftar untuk menyewa sepeda pada tahun 2011 dan 2012?
data_hour['TanggalWaktu'] = pd.to_datetime(data_hour['TanggalWaktu'])
data_hour_2011 = data_hour[data_hour['TanggalWaktu'].dt.year == 2011]
data_hour_2012 = data_hour[data_hour['TanggalWaktu'].dt.year == 2012]
data_agg_hour_2011 = data_hour_2011.groupby('Jam').agg({'Kasual': 'sum', 'Terdaftar': 'sum'}).reset_index()
data_agg_hour_2012 = data_hour_2012.groupby('Jam').agg({'Kasual': 'sum', 'Terdaftar': 'sum'}).reset_index()
# Membuat visualisasi untuk tahun 2011
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_agg_hour_2011, x='Jam', y='Kasual', marker='o', color='blue', label='Penyewa Kasual 2011')
sns.lineplot(data=data_agg_hour_2011, x='Jam', y='Terdaftar', marker='o', color='orange', label='Penyewa Terdaftar 2011')
plt.title('Jumlah Penyewa Kasual dan Terdaftar Berdasarkan Jam (2011)')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewa Sepeda (cnt)')
plt.xticks(range(0, 24))
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
st.pyplot(plt)
# Membuat visualisasi untuk tahun 2012
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_agg_hour_2012, x='Jam', y='Kasual', marker='o', color='green', label='Penyewa Kasual 2012')
sns.lineplot(data=data_agg_hour_2012, x='Jam', y='Terdaftar', marker='o', color='red', label='Penyewa Terdaftar 2012')
plt.title('Jumlah Penyewa Kasual dan Terdaftar Berdasarkan Jam (2012)')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewa Sepeda (cnt)')
plt.xticks(range(0, 24))
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
st.pyplot(plt)