import math
import time
import random

def is_prime(n):
    """Kiểm tra số nguyên tố cơ bản để phục vụ test case."""
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return True

def generate_real_rsa_key(bits=32):
    """Sinh một khóa RSA thực tế (N = p * q) để test thử kết quả."""
    print(f"[⚙️] Đang sinh ngẫu nhiên cặp số nguyên tố lớn ({bits}-bit)...")
    primes = []
    while len(primes) < 2:
        candidate = random.getrandbits(bits // 2) | 1
        if is_prime(candidate) and candidate not in primes:
            primes.append(candidate)
    p, q = primes[0], primes[1]
    return p * q, p, q

def pythagorean_snapper(N):
    """
    THUẬT TOÁN PHÂN TÍCH HÌNH HỌC 2D TRÊN TOẠ ĐỘ THỰC TẾ
    Phương trình Fermat: x^2 - y^2 = N => y^2 + N = x^2 (Mô hình tam giác vuông Pythagoras)
    """
    print(f"[🚀] Đang quét không gian hình học cho Khóa mục tiêu N = {N}")
    start_time = time.perf_counter()
    
    # Bước 1: Xác định điểm bắt đầu từ trần căn thức (Cạnh huyền tối thiểu của tam giác)
    x = math.ceil(math.sqrt(N))
    steps = 0
    
    # Bước 2: Quét góc vector cho đến khi tọa độ 'snap' trúng số nguyên (Perfect Integer Coordinate)
    while True:
        steps += 1
        y_squared = x**2 - N
        y = math.isqrt(y_squared)
        
        # Kiểm tra điều kiện Snap: Cạnh đối y có phải là số nguyên hoàn hảo không
        if y * y == y_squared:
            elapsed_time = time.perf_counter() - start_time
            print(f"[🎯] KHỚP TỌA ĐỘ NGUYÊN! Tìm thấy điểm giao sau {steps} bước quét.")
            print(f"[⏱️] Thời gian xử lý: {elapsed_time:.6f} giây.")
            
            # Bước 3: Trích xuất kích thước gốc (Giải mã 2 số nguyên tố bí mật)
            extracted_p = x - y
            extracted_q = x + y
            return extracted_p, extracted_q, steps, elapsed_time

if __name__ == "__main__":
    print("=== BÀI KIỂM THỬ THỰC TẾ: PHẦN 1 (2D CORE) ===")
    
    # 1. Tạo dữ liệu mã hóa thật
    target_N, actual_p, actual_q = generate_real_rsa_key(bits=36)
    print(f"[🔑] Khóa công khai tạo thành N: {target_N}")
    print(f"[🔒] Kích thước bí mật gốc cần tìm: p = {actual_p}, q = {actual_q}\n")
    
    # 2. Chạy thuật toán bẻ khóa bằng Hình học Pythagoras
    p_found, q_found, steps, dt = pythagorean_snapper(target_N)
    
    # 3. Xác minh kết quả thực tế
    print("\n=== KẾT QUẢ THỰC TẾ ===")
    print(f"-> Số nguyên tố p tìm được: {p_found} (Chính xác: {p_found == actual_p or p_found == actual_q})")
    print(f"-> Số nguyên tố q tìm được: {q_found} (Chính xác: {q_found == actual_p or q_found == actual_q})")
    print(f"-> Trạng thái: {'THÀNH CÔNG 🎉' if p_found * q_found == target_N else 'THẤT BẠI ❌'}")
