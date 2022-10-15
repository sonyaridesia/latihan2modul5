#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:35:17 2022

@author: sonyaridesia
"""

umur = "0"
total = 0
while (umur != ""):
    umur = input("\nmasukkan umur: ")
    if umur != '':
        umur_angka = int(umur)
        if umur_angka <= 2:
            print("Gratis")
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12:
            print("Harga $14.00")
            price = 14
        elif umur_angka >= 65:
            print("Harga $18.00")
            price = 18
        else:
            print("Harga $23.00")
            price = 23
        total = total + price
        print("Total: %0.2f" % total)
    
jumlah = int(input("masukkan jumlah uang: "))
hasil = jumlah - total
print("Kembalian: %0.2f" % hasil)
