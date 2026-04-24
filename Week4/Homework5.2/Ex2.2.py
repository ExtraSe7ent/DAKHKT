gen = (x for x in range(16) if x % 3 == 0)

first = next(gen)
print(f"Giá trị đầu tiên lấy được là: {first}")

second = next(gen)
print(f"Giá trị thứ hai lấy được là: {second}") 
