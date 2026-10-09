# bai3_trich_xuat_du_lieu.py

# 1. Chuỗi thông tin giao dich
ma_giao_dich = "GD001-5000000-VND"

# 2. Xử lí dữ liệu
trich_xuat_ma_giao_dich = ma_giao_dich[6:13]
so_tien_giao_dich= int(trich_xuat_ma_giao_dich)
if so_tien_giao_dich <= 5000000:
    print("Giao dịch thành công")
else:
    print("Giao dịch cần xác thực OTP")
    
