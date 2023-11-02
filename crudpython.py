#filename: main.py

import sqlite3
from sqlite3 import Error
import os

def show_main_menu():
    print("++=========================================++")
    print("|MENU UTAMA APLIKASI MENGELOLA PROJECT & TASK|")
    print("++=========================================++")
    print("||1.||MENU PROJEK........")
    print("||2.||MENU TASK..........")
    print("++=========================================++")
    print("||0.||CLOSE PROGRAM...........")
    print("++=========================================++")
    main_menu = input(" Silahkan Pilih Menu->")
    
    # clear screen
    os.system("clear")
    
    if main_menu=="1":
        show_project_menu()
    elif main_menu=="2":
        show_task_menu()
    elif main_menu=="0":
        exit()
    else:
        print("Menu Salah!")
def show_project_menu():
    print("++=======================================++")
    print("|MENU UTAMA APLIKASI MENGELOLA PROJECT!")
    print("++=======================================++") 
    print("||1.||TAMPILKAN DATA PROJEK........||")
    print("||2.||INSERT DATA PROJEK...........||")
    print("||3.||UBAH DATA PROJEK.............||") 
    print("||4.||HAPUS DATA PROJEK............||")
    print("||CARI DATA PROJEK.................||")
    print("++========================================++")
    print("||9.||KEMBALI KE MENU UTAMA........||")
    print("||0.||CLOSE PROGRAM................||")
    print("++=======================================++")
    menu_project = input("  Silahkan Pilih Menu->")
    
    # clear screen
    os.system("clear")
    
    if menu_project =="1"
        pass
    elif menu_project =="2"
        pass
    elif menu_project =="3"
        pass
    elif menu_project =="4"
        pass
    elif menu_project =="5"
        pass
    elif menu_project =="9"
        show_main_menu()
    elif menu_project =="0"
        exit()
    else:
    print("Menu Salah!")
    show_project_menu()
    
    def show_task_menu():
        print("++=======================================++")
        print("|MENU UTAMA APLIKASI MENGELOLA TASK!")
        print("++=======================================++")
        print("||1.||TAMPILKAN DATA TASK.............||")
        print("||2.||INSERT DATA TASK................||")
        print("||3.||UBAH DATA TASK..................||")
        print("||4.||HAPUS DATA TASK.................||")
        print("||5.||CARI DATA TASK..................||")
        print("++=======================================++") 
        print("||9.||KEMBALI KE MENU UTAMA........||")
        print("||0.||CLOSE PROGRAM................||")
        print("++=======================================++")
        menu_project = input("  Silahkan Pilih Menu->")
        
    # clear screen
    os.system("clear")
    
    if menu_task =="1"
        pass
    elif menu_task =="2"
        pass
    elif menu_task =="3"
        pass
    elif menu_task =="4"
        pass
    
    