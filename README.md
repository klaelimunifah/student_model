# Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan



## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Permasalahan bisnis yang dihadapi adalah tingginya nilai Dropout rate Jaya Jaya Institut Nilai Dropout Rate ini menunjukkan banyaknya mahasiswa yang dropout 
dibanding mahasiswa yang lulus atau terdaftar di institusi tersebut. Banyaknya siswa yang dropout dapat menurunkan akreditasi dan penilaian institusi karna 
dinilai tidak dapat memberikan pengajaran dengan baik. Akreditasi dan penilaian institusi yang buruk akan berpengaruh pada lulusan kampus, sumber dana yang diperoleh, dan 
banyaknya jumlah pendaftar di tahun ajaran berikutnya.

Untuk mengetahui hal-hal yang menyebabkan dropout rate, kita perlu mencari tahu terlebih dahulu faktor faktor yang menyebabkan tingginya dropout rate. 
Faktor faktor ini bisa dari beban perkuliahan, masalah finansial, asal mahasiswa, dan background keluarga mahasiswa.

### Cakupan Proyek

- Membersihkan dan mengolah data awal
- Menganalisis faktor-faktor yang menyebabkan tingginya Dropout Rate dengan ekploratory data numerical dan categorical
- Membuat business dashboard dari faktor-faktor tersebut
- Membuat solusi machine learning untuk memprediksi status mahasiswa berdasarkan nilai dari faktor-faktor yang dimasukan
- Melakukan simulasi terhadap action item yang dapat dilakukan institusi

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv] (https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv) 

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.11
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_students_performance
cd proyek_students_performance
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run app.py
```

## Business Dashboard

Business dashboard proyek ini dibuat menggunakan Google Looker Studio dengan menambah fitur filter berdasarkan status mahasiswa, application order, 
application mode dan previous qualification. Pada dashboard ditampilkan jumlah mahasiswa, jumlah mahasiswa graduate, dropout dan enrolled, dropout rate, 
rata-rata umur mahasiswa ketika masuk, rata-rata nilai admission grade, jumlah mahasiswa berdasarkan status tuition fees, scholarship holder, debtor, gender, 
course yang diambil dan nilai selama berkuliah. Terdapat juga scatter plot dengan sumbu x rata-rata unit kurikulum yang disetujui, 
sumbu y rata-rata unit kurikulum yang didaftarkan, dibedakan berdasarkan status, serta berat bubble berdasarkan rata rata unit kurikulum yang perlu dievaluasi.
Pada pojok atas terdapat tombol yang mengarahkan ke github repository tempat proyek ini disimpan, serta link menuju dashboard streamlit 
untuk mengakses dashboard prediksi berdasarkan model machine learning yang sudah dibuat. Dashboard terdiri dari 2 halaman yaitu dashboard main yang merupakan data asli dan dashboard simulation adalah dashboard dari data hasil prediksi ketika dilakukan action item memberikan beasiswa pada peraih nilai di atas 15.

Model machine learning yang dibuat menerapkan teknik XGBClassifier dengan mencapai 0,9765 atau 97,65% dengan score micro OVR(One Vs Rest) 
dan macro OVR ROC AUC bernilai 1 atau 100%. Score micro OVR(One Vs Rest) dan macro OVR ROC AUC menunjukkan kemampuan model dalam memisahkan 1 kelas dari seluruh kelas lain. 
Sedangkan pada data validation score accuracy hanya 0,7681 atau 76,81% dengan score micro OVR(One Vs Rest) dan macro OVR ROC AUC berturut-turut bernilai 0,91 
atau 91%% dan 0,88 atau 88%. Dapat dilihat bahwa accuracy score training dan validation memiliki perbedaan yang cukup besar. 
Akan tetapi, ketika melihat score micro OVR(One Vs Rest) dan macro OVR ROC AUC dari validation, nilai tersebut sudah bisa diterima untuk 
menggolongkan model dapat memisahkan class dengan baik.

Link Looker Studio: https://lookerstudio.google.com/reporting/70ad2a18-1feb-48c3-95d5-3fc087d075a5

Link Streamlit: https://studentmodel-klm.streamlit.app/

## Conclusion

Berdasarkan bussiness dashboard ini dapat dilihat bahwaJumlah keseluruhan mahasiswa adalah 4424 orang dengan jumlah graduate 2209, jumlah enrolled 794 dan dropout 1421 serta dropout_rate 32.12%
- Tagihan pembayaran yang belum terupdate paling banyak dari mahasiswa dropout
- Sebagian besar mahasiswa dropout tidak memiliki beasiswa. Sebagian besar yang memiliki beasiswa berhasil lulus
- Jumlah mahasiswa yang lulus dari masing-masing jurusan jumlahnya lebih banyak dibanding yang dropout kecuali pada jurusan technology dan engineering, basic education
- Kebanyakan mahasiswa yang dropout tidak memiliki tagihan hutang. Akan tetapi, sebagian besar yang memiliki tagihan hutang mengalami dropout.
- Sebaran gender mahasiswa dropout hampir sama, pada masing-masing kategori status mahasiswa, jumlah terbesarnya adalah laki-laki.
- Berdasarkan curricular_units_grade, kebanyakan mahasiswa yang dropout memiliki nilai di bawah 5 dan antara 10-15
- Curricular_units_enrolled dan Curricular_units_approve besarnya berbanding lurus
- Rata-rata umur mahasiswa di angka 23,7

### Rekomendasi Action Items 

Untuk mengurangi tingkat dropout rate hal hal yang mungkin dapat dilakukan institusi adalah sebagai berikut
- Memberi beasiswa pada peraih grade 75% ke atas. Dengan menerapkan action item ini model berhasil memprediksi jumlah mahasiswa graduate naik sebesar 4.66%, jumlah mahasiswa dropout berkurang sebesar 9.57% dan jumlah mahasiswa enrolled naik sebesar 4.16%. Selain itu dropout rate turun menjadi 29.05%.
- Mengadakan tutor agar mahasiswa bisa menaikan nilai perkuliahan.
