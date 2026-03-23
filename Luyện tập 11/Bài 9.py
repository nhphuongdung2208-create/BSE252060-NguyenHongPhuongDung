def input_matrix(rows, cols):
    matrix = []
    print(f"Nhập {rows}x{cols} phần tử:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Phần tử [{i}][{j}]: ")
            if val.strip() == "": # Báo lỗi nếu trống
                raise ValueError("Lỗi: Không được để trống giá trị!")
            row.append(float(val))
        matrix.append(row)
    return matrix

try:
    r = int(input("Nhập số dòng: "))
    c = int(input("Nhập số cột: "))
    print("Nhập ma trận A:")
    A = input_matrix(r, c)
    print("Nhập ma trận B:")
    B = input_matrix(r, c)

    # Cộng ma trận
    result = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]
    print("Kết quả ma trận (A+B):", result)

except ValueError as e:
    print(e)