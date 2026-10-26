# Khởi tạo dữ liệu
tuoi = 25
so_du = 0.0
tien_gui = 60000000.0
lai_suat = 0.10
tang_tien_gui = 0.08
muc_tieu = 10000000000.0
nam = 0
print("-"*50)
print("===BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG===")
print("-"*50)
print(f"{'Năm':<8} | {'Tuổi':<8} | {'Số tiền gửi mới':<20} | {'Tiền lăi trong năm':<20} | {'Tổng tài sản cuối năm':>23} ")
# Vong lặp tính toán
while so_du < muc_tieu:
    nam += 1
    # Tính tiền lăi
    tien_lai = so_du * lai_suat
    # Tính số dư cuối năm
    so_du = so_du + tien_lai + tien_gui

    tuoi += 1
    # Tính tiền gửi mới
    tien_gui = tien_gui * (1 +  tang_tien_gui)
    # Tính tiền gửi mới năm sau
    tien_gui_moi = tien_gui * (1 + 0.08)
    # Tính tổng tài sản cuối năm
    tong_tai_san = so_du
    print(f"{nam:<8} | {tuoi:<8} | {tien_gui_moi:<20,.0f} VNĐ | {tien_lai:<20,.0f} VNĐ | {tong_tai_san:>23,.0f} VNĐ")
