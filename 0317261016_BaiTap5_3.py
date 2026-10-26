# Khởi tạo dữ liệu
V_goc = 20.0
# Khai báo biến 
delta_Ex = [-0.003, 0, 0.003]
delta_Ir = [-0.002, -0.001, 0.001, 0.002]
# In tiêu đề ma trận
print("-" * 50)
print("===MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ NHANH MỤC (TỶ USD)===")
print("-" * 50)
print(f"{'Thay đổi lăi xuất \ tỷ giá':<20}", end="")
for ir in range (len(delta_Ir)):
    row_str = (f"Lăi xuất {ir * 100:>5,.1f}%")
    row_value = []
# Vong lặp lồng nhau
for ex in range (len(delta_Ex)):
    print(f"{ex * 100:>5,.0f}%", end="")
    # Công thức tài chính
    V_moi = V_goc + (1 + 1.5 * ex - 2.0 * ir)
    row_value.append(f"{V_moi:>5,.2f}%")
    # In ra danh mục mới
    row_str += " | ".join(row_value)
    print(row_str)
