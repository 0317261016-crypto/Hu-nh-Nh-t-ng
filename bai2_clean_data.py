# bai2_clean_data.py
print("----HỆ THỐNG CRM: CHUẨN HÓA DỮ LIỆU KHÁCH HÀNG----")

# 1. Dữ liệu thô từ hệ thống
raw_name = " nGuYen VAn A "
print(f"Dữ liệu gốc: '{raw_name}'")

# 2. Xử lí dữ liệu
clean_name = raw_name.strip().title()

# 3. Xuất kết quả
print(f"Dữ liệu sạch: '{clean_name}'")
