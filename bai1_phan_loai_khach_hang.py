# bai1_phan_loai_khach_hang.py
def phan_loai_khach_hang(diem_credit: int) -> str:
    """Phân hạng rủi ro tín dụng của khách hàng dựa trên điểm credit.

    Args:
        diem_credit (int): Điểm tín dụng của khách hàng (từ 300 đến 850).

    Returns:
        str: Kết quả phân hạng rủi ro tương ứng.
    """
    if not (300 <= diem_credit <= 850):
        return "Điểm tín dụng không hợp lệ (phải từ 300 đến 850)"

    if diem_credit >= 750:
        return "Rủi ro Thấp - Duyệt tự động"
    elif diem_credit >= 600:
        return "Rủi ro Trung bình - Cần thẩm định"
    else:
        return "Rủi ro Cao - Từ chối cấp tín dụng"


# --- Chạy thử nghiệm ---
if __name__ == "__main__":
    test_scores = [780, 680, 520, 200]

    for score in test_scores:
        ket_qua = phan_loai_khach_hang(score)
        print(f"Điểm {score}: {ket_qua}")
