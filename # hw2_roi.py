# hw2_roi.py

# 1. Nhập tổng vốn ban đầu và tổng giá trị bán ra
initial_investment = float(input(" Nhập tổng vốn ban đâu(initial investment): "))
final_value = float(input("Nhập tổng giá trị bán ra(final value): "))

# 2. Xử lí tính toán
# Công thức tính lợi nhuận rong = giá trị bán ra - vốn ban đầu
net_profit = final_value - initial_investment
# Công thức tính ROI(%) = ( lợi nhuận rong/tổng vốn ban đầu)*100
roi = (net_profit/initial_investment)*100
# 3. Xuất kết quả
print("\n----TỶ SUẤT SINH LỜI TRÊN VỐN ĐẦU TƯ----")
print(f"Lợi nhuận rong(Net Profit): {net_profit:,.2f}")
print(f"Tỷ lệ roi(%) : {roi:,.2f}%")
