# hw2_promo_code.py

# 1.Nhập dữ liệu đầu vào
ho_ten = input("Nhập họ và tên: ")
nam_sinh = input("Nhập năm sinh: ")

# 2. Xử lí dữ liệu: Tạo mă ưu đăi
cac_tu = ho_ten.split()
ten = cac_tu[-1]
ten_ngan = ten[0:4].upper()
ma_uu_dai = f"{ten_ngan}-{nam_sinh}-VIP"

# 3. Xuất kết quả
print("\n---MĂ PHÁT SINH ƯU ĐĂI---")
print(f"Mă ưu đăi: ", ma_uu_dai)

