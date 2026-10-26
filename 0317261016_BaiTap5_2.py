# Khởi tạo dữ liệu
F = 1000000
c = 0.9
N = 10
y = 0.85
tong_pv_coupou = 0.0
# Tính tiền lăi coupou hằng năm
C = F * c
print(f"Tiền lăi coupou trả hằng năm: {C:,.0f} VNĐ")
# Vong lặp tính toán
for t in range(1, N + 1):
    # Tính PV coupou từng năm
    pv_c = C / ((1 + y)**t)
    tong_pv_coupou += pv_c
    # Tính mệnh giá gốc
    pv_f = F / ((1 + y)**N)
    # Tính giá trái phiếu
    gia_trai_phieu = tong_pv_coupou * pv_f
    if gia_trai_phieu > pv_f:
        print("Trái phiếu này được bán cao hơn mệnh giá (Premium)")
    elif gia_trai_phieu == pv_f:
        print("Trái phiếu này được bán đúng mệnh giá (Par)")
    else:
        print("Trái phiếu này được bán thấp hơn mệnh giá (Discount)")
# Xuất kết quả
print(f"Tổng coupou từng năm: {tong_pv_coupou:,.0f} VNĐ")
print(f"Mệnh giá gốc: {pv_f:,.0f} VNĐ")
print(f"Giá trái phiếu: {gia_trai_phieu:,.0f} VNĐ")
