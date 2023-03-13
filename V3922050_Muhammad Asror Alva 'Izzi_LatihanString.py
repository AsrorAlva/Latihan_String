#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Meminta pengguna memasukkan nama lengkap
nama_lengkap = input("Masukkan nama lengkap Anda: ")

# Menghitung jumlah kata dalam nama lengkap
jumlah_nama = len(nama_lengkap.split())

# Menghitung jumlah huruf vokal dan konsonan
jumlah_vokal = 0
jumlah_konsonan = 0

# Daftar huruf vokal
vokal = ["a", "e", "i", "o", "u"]

# Menghitung jumlah huruf vokal dan konsonan
for huruf in nama_lengkap.lower():
    if huruf in vokal:
        jumlah_vokal += 1
    elif huruf.isalpha():
        jumlah_konsonan += 1

# Mencetak hasil
print("Jumlah nama lengkap: ", jumlah_nama)
print("Jumlah huruf vokal dalam nama: ", jumlah_vokal)
print("Jumlah huruf konsonan dalam nama: ", jumlah_konsonan)


# In[ ]:




