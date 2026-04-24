import matplotlib.pyplot as plt

def quan_ly_kho():
    kho_hang = {'Balo': 150, 'Tui xach': 80, 'Vali': 120}
    print("     QUAN LY KHO HANG")
    
    while True:
        try:
            sl_vida_str = input("- Nhap so luong 'Vi da' moi nhap kho: ").strip()
            sl_vida = int(sl_vida_str)
            if sl_vida <= 0:                                         
                print("So luong phai lon hon 0. Vui long nhap lai.")
                continue
            break
        except ValueError:
            print("SAI DINH DANG. Vui long nhap so nguyen (VD: 50).\n")
            
    kho_hang['Vi da'] = sl_vida
    
    if kho_hang['Balo'] < 30:                                        
        print("CANH BAO: Khong du Balo de xuat kho!")
    else:
        kho_hang['Balo'] = kho_hang['Balo'] - 30
        print(f"\nDa xuat kho 30 Balo. So luong con lai: {kho_hang['Balo']}")
    
    print("\n--- DANH SACH TON KHO HIEN TAI ---")
    for mat_hang, so_luong in kho_hang.items():
        print(f"• {mat_hang}: {so_luong}")
        
    labels = list(kho_hang.keys())
    sizes = list(kho_hang.values())
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Ty trong phan tram cac mat hang trong kho")
    plt.axis('equal')
    plt.show()

quan_ly_kho()