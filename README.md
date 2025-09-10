# ANSWER

- Cara implemntasi checklist step-by-step, saya tidak hanya mengikuti tutorial. Namun saya juga berusaha untuk memahami apa yang terjadi dan bagaimana cara kerjanya.

- Client request -> Django project -> urls.py -> views.py -> models.py (optional) -> HTML templates -> response ke client

### PENJELASAN

1. **urls.py** : Menentukan rute mana yang perlu dijalankan berdasarkan request dari client.
2. **views.py** : Berdasarkan rute yang dipilih, jalankan fungsi yang sesuai dengan rute.
3. **models.py** : Ini bersifat opsional. Jika data sudah ada dalam views.py, maka tidak perlu mengambil data dari models.py. Namun, jika data berhubungan dengan models.py (nama barang, dsb), maka harus melewati models.py.
4. **HTML templates** : Di render berdasarkan data yang sudah diberikan menjadi webpage.
5. **Response** :  Hasil yang sudah di render, dikirim kembali dalam bentuk webpage untuk di display ke client dalam browsernya.

- settings.py memiliki peran sebagai konfigurasi utama dalam proyek Django yang berisi hal-hal sensitif seperti private key, lalu juga berisi pengaturan untuk database, aplikasi yang digunakan, hosts yang diizinkan, dan sebagainya.

- migrasi database bekerja dengan menerapkan/mengaplikasikan apa yang sudah dibuat dari command makemigrations. Pertama, makemigrations membuat kode migrasi untuk models.py terbaru tanpa menjalankan/menerapkan kode tersebut ke project (masih dalam bentuk python). Sehingga, kita butuh melakukan command migration untuk mengeksekusi kode tersebut sehingga kode tersebut akan diubah ke dalam bentuk SQL dan diterapkan ke dalam project

- Framework Django, menggunakan bahasa python, yaitu bahasa yang paling mudah untuk dipahami oleh manusia dan juga berisi banyak fitur-fitur yang sudah disediakan. Lalu, framework Django memiliki struktur yang jelas dan mudah dipahami, sehingga cocok sebagai permulaan dalam pembelajaran pengembangan perangkat lunak

- Tidak ada