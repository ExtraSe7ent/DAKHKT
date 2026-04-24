def todo_list_app():
    danh_sach_todo = []
    print("     UNG DUNG GHI CHU CONG VIEC")

    while True:
        cong_viec = input("- Nhap cong viec: ").strip()
        if cong_viec.lower() == "xong" or cong_viec == "":
            break

        danh_sach_todo.append(cong_viec)

    if not danh_sach_todo:
        print("Danh sach trong.")
        return
    
    with open("todo_list.txt", "w", encoding="utf-8") as file:
        print("\nDANH SACH CONG VIEC:")

        stt = 1
        for cv in danh_sach_todo:
            dong_van_ban = f"{stt}. {cv}"
            print(dong_van_ban)
            file.write(dong_van_ban + "\n")
            stt = stt + 1

    print("\nDA LUU DANH SACH CONG VIEC!")

todo_list_app()