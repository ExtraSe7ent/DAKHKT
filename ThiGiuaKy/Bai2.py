def phan_tich_van_ban():
    while True:
        van_ban = input("Nhap van ban (khoang 2-3 cau): ")
        if van_ban != "":
            break
        print("Vui long nhap van ban, khong duoc de trong.")

    van_ban_sach = van_ban.lower().replace('.', '').replace(',', '').replace('!', '')
    danh_sach_tu = van_ban_sach.split()

    if len(danh_sach_tu) == 0:
        print("\nVan ban cua ban khong hop le de phan tich.")
        return
    
    tong_so_tu = len(danh_sach_tu)

    dem_tu = {}
    for tu in danh_sach_tu:
        if tu in dem_tu:
            dem_tu[tu] = dem_tu[tu] + 1
        else:
            dem_tu[tu] = 1
        
    tu_nhieu_nhat = ""
    so_lan = 0

    for tu in dem_tu:
        if dem_tu[tu] > so_lan:
            tu_nhieu_nhat = tu
            so_lan = dem_tu[tu]

    
    print(f"Van ban goc: \n>> {van_ban}\n")
    print(f"- Danh sach cac tu rieng biet: {danh_sach_tu}")
    print(f"- Tong so tu: {tong_so_tu}")
    print(f"- Tu xuat hien nhieu nhat: '{tu_nhieu_nhat}', xuat hien {so_lan} lan")

phan_tich_van_ban()