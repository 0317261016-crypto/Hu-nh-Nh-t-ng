# bai4_lai_xuat_tiet_kiem.py
def tinh_tong_tien_tiet_kiem(
    so_tien_goc = float, lai_xuat_nam = float, thoi_gian = float
    )-> float:
    """ Tính tổng số tiền nhận được sau một thời gian gửi tiết kiệm
    Args:
        so_tien_goc(float): Số tiền gốc ban đầu gửi vào tiết kiệm
        lai_xuat_nam(float): Lăi xuất tiết kiệm tính theo năm(ví dụ: 0.06 tương ứng 6%)
        thoi_gian(float): Thời gian gửi tiết kiệm tính bằng năm(Ví dụ 0.5 năm )
    Returns:
        float: Tổng số tiền thu được(gồm gốc và lăi)
    """
    # Ép kiểu dữ liệu sang float
    so_tien_goc = float(so_tien_goc)
    lai_xuat_nam = float(lai_xuat_nam)
    thoi_gian = float(thoi_gian)
    # Tính số tiền theo thức:
    tong_tien = so_tien_goc * (1 + lai_xuat_nam * thoi_gian)
    return tong_tien

#---Tiến hành viết code---

# 1. Khai báo biến đầu vào
so_tien_goc_ban_dau = "10000000"
lai_xuat_nam_ban_dau = "0.06"
thoi_gian_ban_dau = "2"

# 2. Xử lí dữ liệu
so_tien_goc = float(so_tien_goc_ban_dau)
lai_xuat_nam = float(lai_xuat_nam_ban_dau)
thoi_gian = float(thoi_gian_ban_dau)

# 3. Tiến hành tính toán
tong_tien = so_tien_goc * (1 + lai_xuat_nam * thoi_gian)

# 4. Xuất kết quả
print(f"Số tiên gốc : {so_tien_goc:,.0f}")
print(f"Lăi xuất năm :{lai_xuat_nam * 100:,.2f}")
print(f"Thời gian : {thoi_gian}")
print(f"Tông tiền : {tong_tien:,.0f}")
