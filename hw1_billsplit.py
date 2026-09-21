# bai1_hw1_billsplit.py
print("===BillSplitter===")
# Nhập dữ liệu đầu vào từ người dùng
X = float(input("Nhập tổng hóa đơn(x đồng): "))
Y = float(input("Nhập số tiền tip cho nhân viên(Y%0): "))
N = int(input("Nhập số người chia (N người): "))
# Tính tổng tiền bao gồm tiền tip cho nhân viên:
tong_tien = X + (X * Y / 100)
# Tính tổng số tiền thực tế mọi người phải trả:
tien_moi_nguoi = tong_tien / N
# Làm tron đến số nguyên (0 chữ số thập phân):
tien_moi_nguoi_lam_tron = round(tien_moi_nguoi)
#Kết quả in ra màn h́nh là:
print(f"số tiền thực tế mà mỗi người phải trả là: {tien_moi_nguoi_lam_tron}")


