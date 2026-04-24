import random
import time
from datetime import datetime

def mini_hangman():
    danh_sach_tu = ["python", "apple", "river", "macbook", "samsung"]
    tu_bi_mat = random.choice(danh_sach_tu)
    
    tu_hien_tai = ["_"] * len(tu_bi_mat)
    luot_sai_con_lai = 5
    da_doan = set()
    
    print("      TRO CHOI DOAN CHU (MINI HANGMAN)      ")
    print("--------------------------------------------")
    
    thoi_gian_bat_dau = time.time()
    
    while luot_sai_con_lai > 0 and "_" in tu_hien_tai:
        print("\nTu hien tai:", " ".join(tu_hien_tai))
        print(f"Luot sai con lai: {luot_sai_con_lai}")
        
        chu_sai = [c for c in da_doan if c not in tu_bi_mat]
        if chu_sai:
            print(f"Chu sai da doan: {', '.join(sorted(chu_sai))}")
        
        chu_doan = input("Nhap 1 chu cai: ").strip().lower()
        
        if len(chu_doan) != 1 or not chu_doan.isalpha():
            print("=> Vui long chi nhap 1 chu cai (a-z).")
            continue
        
        if chu_doan in da_doan:
            print("=> Ban da doan chu nay roi. Hay chon chu khac.")
            continue
            
        da_doan.add(chu_doan)
            
        if chu_doan in tu_bi_mat:
            print("=> CHINH XAC!")
            for i in range(len(tu_bi_mat)):
                if tu_bi_mat[i] == chu_doan:
                    tu_hien_tai[i] = chu_doan
        else:
            print("=> KHONG CHINH XAC!")
            luot_sai_con_lai -= 1
            
    thoi_gian_ket_thuc = time.time()
    thoi_gian_choi = round(thoi_gian_ket_thuc - thoi_gian_bat_dau, 1)
    thoi_diem = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n============================================")
    if "_" not in tu_hien_tai:
        thong_bao = f"THANG! Tu: '{tu_bi_mat}'. TG: {thoi_gian_choi}s. Luot sai con: {luot_sai_con_lai}."
        print(f"CHUC MUNG! Ban da doan dung tu '{tu_bi_mat}'.")
    else:
        thong_bao = f"THUA! Tu: '{tu_bi_mat}'. TG: {thoi_gian_choi}s."
        print(f"Ban da het luot. Tu bi mat la '{tu_bi_mat}'.")
        
    with open("ket_qua_hangman.txt", "a", encoding="utf-8") as file:
        file.write(f"[{thoi_diem}] {thong_bao}\n")
        
    print("\nDa luu ket qua vao file 'ket_qua_hangman.txt'.")

mini_hangman()