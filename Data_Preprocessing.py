# Memuat Data
# Import library yang diperlukan, seperti Pandas
import pandas as pd

# Muat dataset dari file CSV kedalam DataFrame
df = pd.read_csv('C:/Users/Axioo/Documents/movie_sample_dataset.csv')

# Memeriksa Data
# Menampilkan beberapa baris pertama dari dataset untuk memahami struktur data
print(df.head())

# Periksa informasi umum tentang dataset, termasuk tipe data dan nilai missing value
import numpy as np
# Ganti "NaN" dengan " "
df['director_name'] = df['director_name'].replace(['Nan', 'Null'], '', regex=True)

# Periksa jumlah missing value di setiap kolom
print(df.isnull().sum())

# Membersihkan Data
# Hapus baris yang memiliki missing value (NaN) di kolom penting seperti gross dan budget
# Hapus baris missing value (NaN) pada kolom "gross"
df_cleaned1 = df.dropna(subset=["gross"], axis=0, inplace=True)
# Reset index setelah menghapus baris NaN
df.reset_index(drop=True, inplace=True)

# Hapus baris missing value (NaN) pada kolom "budget"
df_cleaned2 = df.dropna(subset=["budget"], axis=0, inplace=True)
# Reset index setelah menghapus baris NaN
df.reset_index(drop=True, inplace=True)

# Atasi nilai yang inkonsistensi atau kesalahan penulisan di kolom
# seperti perbedaan antara "Color" dan "color" serta "USA" dan "usa"
# Atasi perbedaan antara "Color" dan "color" atau inkonsistensi serupa pada kolom
# Misalnya, ubah nilai dalam kolom "color" menjadi huruf non-kapital semua
if 'color' in df.columns:
    df['color'] = df['color'].str.lower()  # Ubah semua nilai di kolom "color" menjadi huruf kecil
print(df.head())

# Ubah nilai dalam kolom "usa" menjadi huruf kapital yakni "USA"
if 'country' in df.columns:
    df['country'] = df['country'].str.upper()  # Ubah semua nilai di kolom "usa" menjadi "USA"
print(df.head())

# Ubah atau hapus nilai-nilai yang tidak standar
# seperti nilai negatif atau "NaN"

# Ubah nilai negatif pada kolom 'duration' dan 'imdb_score'
# Ganti nilai negatif dengan NaN
df['duration'] = df['duration'].apply(lambda x: x if x >= 0 else np.nan)
df['imdb_score'] = df['imdb_score'].apply(lambda x: x if x >= 0 else np.nan)

# Ganti dengan frekuensi pada kolom 'color', 'director name', dan 'genres', duration', dan 'imdb_score'
for column in ['color', 'director_name', 'genres', 'duration', 'imdb_score']:
    # Tentukan nilai mode
    mode_value = df[column].mode()[0]
    # Ganti nilai NaN dengan nilai mode
    df[column].fillna(mode_value, inplace=True)
    mode_value = df['director_name'].mode()[0]  # Dapatkan nilai mode
    df['director_name'].replace('', mode_value, inplace=True)  # Ganti string kosong dengan mode

# Transformasi Data
# Ubah tipe data kolom menjadi tipe data yang sesuai (misalnya, konversi genres dari onject ke string).
# agar dapat melakukan pemisahan genre yang tergabung dalam satu kolom menjadi beberapa kolom
print(df.dtypes)
df['genres'] = df['genres'].astype(str)
print(df['genres'])


# Tidak ada yang diubah karena tipe data sudah sesuai
# Variabel numerik (int atau float) dan variabel kategorik (string atau object)

# Normalisasi Teks untuk Memastikan Konsistensi
# (misalnya mengubah teks menjadi huruf kecil)
# Lakukan normalisasi teks untuk kolom 'color', 'director_name', 'genres', 'movie_title',
# 'language', 'country', dan 'actors'
columns_to_normalize = ['color', 'director_name', 'genres', 'movie_title', 'language', 'country', 'actors']

for column in columns_to_normalize:
    df[column] = df[column].str.lower()  # Ubah teks menjadi huruf non-kapital
    df[column] = df[column].str.strip()  # Hapus spasi di awal dan akhir teks

#5. Penyimpanan Data
df.to_csv('C:/Users/Axioo/Documents/movie_dataset_cleaned.csv', index=False)