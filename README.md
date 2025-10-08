## Tugas 2

- Cara implemntasi checklist step-by-step, saya tidak hanya mengikuti tutorial. Namun saya juga berusaha untuk memahami apa yang terjadi dan bagaimana cara kerjanya.

---

- Client request -> Django project -> urls.py -> views.py -> models.py (optional) -> HTML templates -> response ke client

### PENJELASAN
1. urls.py : Menentukan rute mana yang perlu dijalankan berdasarkan request dari client.
2. views.py : Berdasarkan rute yang dipilih, jalankan fungsi yang sesuai dengan rute.
3. models.py : Ini bersifat opsional. Jika data sudah ada dalam views.py, maka tidak perlu mengambil data dari models.py. Namun, jika data berhubungan dengan models.py (nama barang, dsb), maka harus melewati models.py.
4. HTML templates : Di render berdasarkan data yang sudah diberikan menjadi webpage.
5. Response : Hasil yang sudah di render, dikirim kembali dalam bentuk webpage untuk di display ke client dalam browsernya.

---

- settings.py memiliki peran sebagai konfigurasi utama dalam proyek Django yang berisi hal-hal sensitif seperti private key, lalu juga berisi pengaturan untuk database, aplikasi yang digunakan, hosts yang diizinkan, dan sebagainya.

---

- Migrasi database bekerja dengan menerapkan/mengaplikasikan apa yang sudah dibuat dari command makemigrations. Pertama, makemigrations membuat kode migrasi untuk models.py terbaru tanpa menjalankan/menerapkan kode tersebut ke project (masih dalam bentuk python). Sehingga, kita butuh melakukan command migration untuk mengeksekusi kode tersebut sehingga kode tersebut akan diubah ke dalam bentuk SQL dan diterapkan ke dalam project.

---

- Framework Django, menggunakan bahasa python, yaitu bahasa yang paling mudah untuk dipahami oleh manusia dan juga berisi banyak fitur-fitur yang sudah disediakan. Lalu, framework Django memiliki struktur yang jelas dan mudah dipahami, sehingga cocok sebagai permulaan dalam pembelajaran pengembangan perangkat lunak

---

- Good job!

## Tugas 3

- Data delivery digunakan dalam platform karena platform sekarang ini biasanya berinteraksi dengan banyak user, sistem, dan perangkat secara real-time atau near-real-time

---

- JSON, karena JSON mudah dibaca dan juga lebih ringkas dan ringan.

---

- Fungsi is_valid() diperlukan untuk memeriksa dan memverifikasi data yang diberikan, apakah sudah memenuhi syarat sesuai dengan setting-setting pada field yang diberikan.

---

- Karena csrf_token dibutuhkan untuk melindungi form dari request palsu yang datang dari situs luar. Tanpa csrf_token, platform rentan diserang oleh CSRF dari website lain, yang bisa menyebabkan aksi tidak sah atas nama user. Django secara default menolak POST tanpa token, sehingga ini merupakan lapisan keamanan yang penting.

---

- Cara implementasi checklist step-by-step, saya tidak hanya mengikuti tutorial. Namun saya juga berusaha untuk memahami apa yang terjadi dan bagaimana cara kerjanya dari internet ataupun AI tools.

---

- Tidak ada

--- 

### POSTMAN
![alt text](images/json.png)
![alt text](images/json_id.png)
![alt text](images/xml.png)
![alt text](images/xml_id.png)

## TUGAS 4

Form bawaan Django yang digunakan untuk login user/pengguna. Form ini terletak di modul django.contrib.auth.forms. Fungsi utamanya adalah untuk memvalidasi username dan password yang dimasukkan user/pengguna saat login, lalu mengecek apakah kombinasi username dan password tersebut benar, serta melihat apakah akun pengguna tersebut aktif atau tidak.

### KELEBIHAN
1. Tidak perlu membuat login dari nol.
2. Validasi dilakukan secara otomatis, memeriksa apakah username dan password cocok, dan memastikan akun aktif.
3. Sudah terintegrasi dengan sistem auth Django, bisa langsung dipakai dengan login(), logout(), dan sebagainya.
4. Sudah menangani hal-hal yang bersifat dasar pada keamanan, contohnya brute force protection dan sebagainya.

### KEKURANGAN
1. Tidak fleksibel untuk memodifikasi tampilannya, harus di override untuk styling khusus.
2. hanya terbatas pada username dan password, selain itu harus membaut form kustomm.
3. Tidak bisa menangani autentikasi multi-step.
4. Pesan error bawaan bersifat terlalu umum, jika ingin diganti harus dikustomisasi.

---

Autentikasi adalah proses memvalidasi identitas pengguna, otorisasi adalah proses menentukan hak apa yang dimiliki oleh pengguna.

Django menyediakan modul django.contrib.auth untuk autentikasi:
- User model: django.contrib.auth.models.User menyimpan username, password, dan sebagainya.
- Form login: AuthenticationForm untuk memvalidasi username & password

Django menyediakan permissions dan group untuk otorisasi:
1. Permissions: Setiap model bisa memiliki permission default (add, change, delete, view).
2. Groups: Kumpulan permissions yang bisa diberikan ke beberapa user sekaligus.
3. Decorator dan mixins: 
    - @login_required: Perlu login untuk mengakses.
    - @permission_required('...'): Cek permission secara spesifik.
    - dan sebagainya.

---

### Cookies
Data kecil yang disimpan di browser pengguna. Dikirim ke server setiap request (HTTP Headers). Salah satu contoh penggunaannya adalah menyimpan preferensi pengguna, token login, dan sebagainya.

Kelebihan:
1. Persisten, bisa bertahan walau browser sudah ditutup.
2. Tidak perlu storage server, semua data berada di client.
3. Mudah diakses, bisa dibaca langsung dari document.cookie atau server-side.

Kekurangan:
1. Ukurannya terbatas.
2. Kurang aman, jika tidak dienkripsi maka mudah dimanipulasi oleh user dan bisa juga dicuri lewat XSS jika HttpOnly tidak digunakan.
3. Dikirim setiap request, sehingga bisa menambah bandwith jika terlalu besar.

### Session
Data state disimpan di server dan browser hanya menyimpan session ID (biasanya di cookie). Digunakan untuk login, menyimpan informasi sementara pengguna, dan sebagainya.

Kelebihan:
1. Lebih aman, data ada di server dan user hanya punya ID.
2. Menyimpan data lebih besar, sehingga bisa menyimpan lebih banyak object.
3. Kontrol penuh server, server bisa invalidate session kapanpun, sehingga logout otomatis.

Kekurangan:
1. Membebani server, karena server harus menyimpan state untuk setiap user.
2. Tidak persisten secara default, sehingga akan hilang jika browser ditutup, kecuali jika ada konfigurasi khusus.
3. Perlu mekanisme scaling, terutama untuk aplikasi besar, session server harus shared antara beberapa server

---

Penggunaan cookies tidak sepenuhnya aman secara default dalam pengembangan web. Ada beberapa resiko potensial yang harus diperhatikan:
1. Manipulasi data oleh user, cookie terletak di browser user sehingga user bisa memanipulasi.
2. Pencurian cookie, menggunakan XSS dan jika cookies berisi token login, maka penyerang bisa menyalahgunakan hal tersebut.
3. CSRF (Cross-Site Request Forgery), cookies dikirim otomatis ke server setiap request, tanpa proteksi CSRF, maka penyerang bisa memanfaatkan cookie user untuk melakukan hal yang tidak diinginkan.
4. Pengiriman cookie melalui koneksi tidak aman, cookie yang dikirim lewat HTTP biasa bisa dicuri lewat sniffing jaringan.

Cara Django menangani keamanan cookie:
1. Session cookies aman, django menyimpan session data di server, dan browser hanya menyimpan session ID.
2. HttpOnly cookie, Django menandai cookie session sebagai HttpOnly secara default, sehingga mengurangi kemungkinan penyerangan lewat XSS.
3. Secure cookie, jika site menggunakan HTTPS, Django bisa menandai cookie sebagai Secure. Karena dikirim lewat koneksi Https, sehingga bisa mengurangi adanya kemungkinan sniffing.
4. CSRF Protection, Django memiliki CSRF token yang dipakai untuk mencegah request palsu walau cookies dikirim secara otomatis.
5. Signing dan enkripsi, Cookies seperti signed_cookies dapat digunakan untuk mencegah manipulasi data.

---

Saya mengimplementasi checklist step-by-step dengan tidak hanya mengikuti tutorial, Namun saya juga berusaha untuk memahami apa yang terjadi dan bagaimana cara kerjanya dari internet ataupun memanfaatkan AI tools.

## TUGAS 5

Urutan prioritas pengambilan CSS selector:
1. !important
2. Inline style (langsung di atribut elemen)
3. Selector berdasarkan ID
4. Selector berdasarkan Class, Pseudo-class, dan Attribute
5. Selector berdasarkan Tag / Elemen / Pseudo-element
6. Jika sama, lihat urutan penulisan (yang terakhir menang)


---

Responsive design penting karena pengguna dapat mengakses web dari berbagai perangkat, seperti laptop, tablet, smartphone, bahkan layar besar seperti TV. Kalau desain tidak responsif, tampilan bisa berantakan, sulit dibaca,dan membuat pengalaman pengguna (UX) menjadi buruk.

Contoh aplikasi yang sudah menerapkan responsive design:
1. Shopee
2. Tokopedia
3. dan sebagainya.

Contoh aplikasi yang belum menerapkan responsive design:
1. Situs forum lama yang sudah tidak aktif, karena ada kemungkinan website dibuat saat keahlian untuk membuat responsive design masih minim.

---

Margin:
- Area luar elemen.
- Memberikan jarak antar elemen.
- Tidak terlihat (transparan).

```css
div {
  margin: 20px; /* jarak luar 20px dari elemen lain */
}
```
Border:
- Garis yang membungkus elemen (antara margin dan padding).
- Bisa diberi warna, ketebalan, dan gaya.

```css
div {
  border: 2px solid black; /* garis hitam 2px solid */
}
```

Padding:
- Area dalam elemen.
- Memberi jarak antara content (teks/gambar) dengan border.
- Membuat isi elemen terlihat tidak padat.

```css
div {
  padding: 15px; /* jarak isi dengan border */
}
```

---

Flexbox adalah sistem layout 1 dimensi(satu arah, baris atau kolom).

Konsep utamanya:
- Container → elemen yang diberi display: flex;
- Items → elemen di dalamnya otomatis jadi fleksibel.
- Arah (main axis & cross axis) → bisa horizontal (row) atau vertikal (column).

Kegunaannya:
- Navbar yang rapi.
- Centering konten secara mudah (horizontal & vertikal).
- Mengatur button, card, atau list item yang fleksibel.

Grid layout adalah sistem layout 2 dimensi (baris dan kolom).

Konsep utamanya:
- Container → elemen dengan display: grid;
- Grid Lines → garis pembagi baris dan kolom.
- Grid Track → baris/kolom tunggal.
- Grid Area → area gabungan dari beberapa cell.

Kegunaannya:
- Layout halaman penuh (header, sidebar, main, footer).
- Galeri gambar multi-kolom.
- Dashboard dengan banyak panel.

--- 

Saya mengimplementasi checklist step-by-step dengan tidak hanya mengikuti tutorial, Namun saya juga berusaha untuk memahami apa yang terjadi dan bagaimana cara kerjanya dari internet ataupun memanfaatkan AI tools. Saya juga mencari warna dan design terbaik yang cocok bagi saya sebagai warna untuk websitenya.

## TUGAS 6

Synchronous request

- permintaan yang dijalankan secara berurutan, artinya program akan menunggu hingga permintaan selesai sebelum melanjutkan ke kode berikutnya, sehingga bisa membuat aplikasi terblokir sementara menunggu respons.
Asynchronous request

- permintaan yang dijalankan tanpa menunggu respons, sehingga program bisa melanjutkan eksekusi kode lain sementara permintaan diproses, membuat aplikasi lebih responsif meski alurnya lebih kompleks.

---

Cara AJAX bekerja di Django (alur request-response):
1. Client side (Browser/JS) -> Kirim request AJAX ke server (GET/POST).
2. Server side (Django view) -> Proses request, ambil data, dan buat JsonResponse.
3. Server mengirim respons.
4. Client Side (Browser/JS) -> menerima respons JSON dengan memperbarui tampilan tanpa reload halaman.

---

Keuntungan menggunakan AJAX dibandingkan render biasa di Django:
1. Tanpa reload halaman
- AJAX memungkinkan data diperbarui atau dikirim ke server tanpa memuat ulang seluruh halaman, sehingga UX lebih lancar.
2. Responsif dan cepat
- Hanya data yang diperlukan yang dikirim dan diterima, bukan seluruh halaman HTML, sehingga waktu loading lebih singkat.
3. Interaksi Dinamis
- Memudahkan membuat fitur interaktif seperti live search, form validasi real-time, atau update konten otomatis.
4. Hemat Bandwidth
- Karena hanya data yang dikirim, penggunaan bandwidth lebih efisien dibanding render ulang seluruh halaman HTML.
5. User Experience lebih baik
- User tidak terganggu dengan reload halaman yang penuh, sehingga membuat website terasa lebih modern dan responsif.

---

Cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django:
1. Gunakan HTTPS.
2. Gunakan CSRF Token.
3. Validasi input di server.
4. Gunakan password hashing, dsb.

---

AJAX mempengaruhi User Experience pada website dengan:
1. Tanpa reload halaman
2. Responsif dan cepat
3. Interaksi Dinamis
4. Hemat Bandwidth
5. User Experience lebih baik








