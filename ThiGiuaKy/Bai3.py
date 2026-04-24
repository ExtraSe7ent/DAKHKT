def tinh_bmi():
    print("     TINH CHI SO BMI")
    
    while True:
        try:
            can_nang_str = input("Nhap can nang cua ban (kg): ").strip()
            can_nang = float(can_nang_str)
            if can_nang <= 0:                                          
                print("\nCan nang phai lon hon 0. Vui long nhap lai.")  
                continue                                               
            break
        except ValueError:
            print("\nSAI DINH DANG. Vui long nhap dung gia tri (VD: 65 hoac 1.75).")

    while True:
        try:
            chieu_cao_str = input("Nhap chieu cao cua ban (m): ").strip()
            chieu_cao = float(chieu_cao_str)
            if chieu_cao <= 0:                                         
                print("\nChieu cao phai lon hon 0. Vui long nhap lai.")  
                continue                                                
            bmi = can_nang / (chieu_cao ** 2)
            break
        except ValueError:
            print("\nSAI DINH DANG. Vui long nhap dung gia tri (VD: 65 hoac 1.75).")
        except ZeroDivisionError:
            print("\nChieu cao khong the bang 0. Vui long nhap gia tri lon hon 0.")
            
    print(f"\n=> Chi so BMI cua ban la: {bmi:.1f}")
    
    if bmi < 18.5:
        print("=> Ket qua: Gay")
    elif 18.5 <= bmi <= 24.9:
        print("=> Ket qua: Binh thuong")
    else:
        print("=> Ket qua: Thua can")

tinh_bmi()