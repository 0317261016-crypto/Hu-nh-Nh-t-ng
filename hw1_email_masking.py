# hw1_email_masking.py
# 1. Nhập dữ iệu đầu vào
email = input("Nhập một địa chỉ email: ")
# 2. Dùng split() để tách phần đăng nhập và tên miền
usename, domain = email.split("@")
# 3. Trích xuất kí tự 
first_three = usename[0:3]
# 4. Ghép kí tự 
masked_email = first_three + "***@" + domain
# Xuất kết quả
print("\n---BẢO MẬT THÔNG TIN CẢU KHÁCH HÀNG---")
print("Email sao khi bảo mật: ",masked_email)
