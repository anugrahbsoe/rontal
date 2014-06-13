Status
======

Belum release


Rontal
======

Aplikasi Manajemen Penulisan Tugas Akhir. Fungsi utama aplikasi ini adalah membantu mahasiswa dan dosen dalam proses penulisan Tugas Akhir/Skripsi.


Fitur Utama
======

Fitur utama yang akan ditambahkan ke dalam Rontal:
* Manajemen dokumen, arsip, dan URL bookmark yang digunakan dalam penulisan Landasan Teori dan Daftar Pustaka.
* Draft dokumen Tugas Akhir/Skripsi.
* Bimbingan jarak jauh (online).


Spesifikasi
======

Rontal dibangun menggunakan: 
* Python 2.7
* Django 1.4.13 LTS
* ElementaryOS Luna, Ubuntu 12.04 LTS atau Debian 7 (wheezy)


Instalasi
======

* Cek versi python Anda lewat terminal:

        $ python -V

pastikan versi python anda 2.7 

* Install virtualenv 

        $ sudo apt-get install python-pip python-virtualenv python-dev
        
* Jika Anda ingin menggunakan MySQL, install library yang diperlukan

        $ sudo apt-get install mysql-client mysql-server libmysqlclient-dev

* Setup folder untuk development
  
        $ mkdir ~/projects
        $ cd ~/projects
        $ virtualenv rontal
        $ cd rontal

* Masuk ke virtualenv

        $ source bin/activate

Jika Anda berhasil masuk ke virtualenv, tampilan diterminal akan seperti ini:

        (rontal)user@host:~/projects/rontal$

Untuk selanjutnya, operasi di lingkungan virtual env akan ditulis sebagai berikut:

        (rontal)$

* Update package python di virtualenv

        (rontal)$ easy_install -U distribute

* Jika ingin menambahkan dukungan MySQL
 
        (rontal)$ pip install MySQL-python

* Download Django 1.4.13 LTS di https://www.djangoproject.com/download/1.4.13/tarball/ lalu extract di folder ~/project/rontal/tmp. Atau lewat terminal

        (rontal)$ mkdir ~/projects/rontal/tmp 
        (rontal)$ cd ~/projects/rontal/tmp
        (rontal)$ wget https://www.djangoproject.com/download/1.4.13/tarball/
        (rontal)$ ls

* Entah kenapa, di komputer saya, wget salah menyimpan file Django-1.4.13.tar.gz manjadi index.html. Tidak masalah, cukup rename dan extract.

        (rontal)$ mv index.html Django-1.4.13.tar.gz 
        (rontal)$ tar -zxvf Django-1.4.13.tar.gz
        (rontal)$ cd Django-1.4.13
        (rontal)$ python setup.py install

* Setelah proses instalasi selesai, silahkan meng-clone project rontal

        (rontal)$ cd ~/projects/rontal/
        (rontal)$ git clone https://github.com/aanlinuxer/rontal.git
        (rontal)$ cd ~/projects/rontal/rontal/rontal

* Jika ingin men-setting ke database selain SQLITE3

        (rontal)$ mv default-setting.py setting.py

* Jika inging menggukanan database SQLITE3

        (rontal)$ mv example-settings.py setting.py

Edit file setting.py sesuai dengan kebutuhan.

* Setup database
        
        (rontal)$ cd ~/projects/rontal/rontal
        (rontal)$ ./manage.py syncdb

* Test Rontal

        (rontal)$ ./manage.py runserver
        
* Buka http://127.0.0.1:8000/admin  dari browser


Tambahan
======

Untuk pemula yang tertarik dengan Django, bisa mendownload dokumentasinya : https://docs.djangoproject.com/m/docs/django-docs-1.4-en.zip  extract lalu buka file index.html yang ada di dalamnya.
