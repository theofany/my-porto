import mysql.connector as mysql

db = mysql.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = db.cursor()
db.database = "MAHASISWA"

# 1. Membuat database dengan nama mahasiswa
# sql = "CREATE DATABASE MAHASISWA"

# 2. Membuat table datamhs pada db MAHASISWA
# sql = '''create table datamhs(
#        id int not null auto_increment,
#          nama varchar(100) not null,
#          NIM varchar(20) not null,
#          prodi text not null,
#          Jurusan text not null,
#          alamat text not null,
#          kota_asal text not null,
#          primary key (ID)
# );
# '''
# cursor.execute(sql)
# db.commit()

#3. CRUD Tabel
  #INSERT
# sql ='''INSERT INTO datamhs(nama,NIM,prodi,Jurusan,alamat,kota_asal) values
# ('THEO','205150707111030','Teknologi Informasi', 'Sistem Informasi', 'Plaosan', 'Malang'),
# ('AHMAD','205150707111020','Sistem Informasi', 'Sistem Informasi', 'SUHAT', 'TANGERANG'),
# ('SHELLA','2051507071110100','Teknologi Informasi', 'Sistem Informasi', 'SULFAT', 'SURABAYA'),
# ('JOHAN','205150701111030','Teknik Informatika', 'Teknik Informatika', 'Araya', 'Malang'),
# ('ROMPIS','205150701111020','Teknik Komputer', 'Teknik Informatika', 'Merjosari', 'Bogor')
# '''
# cursor.execute(sql)
# db.commit()

  #UPDATE
# sql = '''UPDATE datamhs SET alamat ="Polehan" where id=4'''
# cursor.execute(sql)
# db.commit()
  #DELETE
# sql ='''DELETE FROM datamhs WHERE id=6'''
# cursor.execute(sql)
# db.commit()

# 4. Melihat isi tabel
sql = "select nama,prodi from datamhs"
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
  print(row)


# cursor.execute("SHOW TABLES")
# data = cursor.fetchall()
# print(data)
