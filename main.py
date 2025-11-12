import numpy as np

def romberg_integration(f, a, b, max_level=10, tol=1e-10):
    R = np.zeros((max_level + 1, max_level + 1))
    
    h = b - a
    R[0, 0] = (h / 2) * (f(a) + f(b))
    
    for i in range(1, max_level + 1):
        h = h / 2
        sum_val = 0
        for k in range(1, 2**i, 2):
            sum_val += f(a + k * h)
        R[i, 0] = 0.5 * R[i-1, 0] + h * sum_val
        
        for j in range(1, i + 1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)
        
        if i > 0 and abs(R[i, i] - R[i-1, i-1]) < tol:
            return R[:i+1, :i+1], R[i, i]
    
    return R, R[max_level, max_level]


def print_romberg_table(R):
    rows, cols = R.shape
    
    header = "R(n,m)"
    for j in range(cols):
        if j < rows:
            header += f"\t\tm={j}"
    print(header)
    print("="*100)
    
    for i in range(rows):
        row_str = f"n={i}"
        for j in range(i + 1):
            row_str += f"\t{R[i, j]:.10f}"
        print(row_str)
    print("="*100)


def integral_1(x):
    return np.cos(x)


def integral_2(x):
    return x**2


def main():
    print("="*50)
    print("ROMBERG INTEGRATION")
    print("="*50)
    print("1. cos(x) dari 0 sampai pi/2")
    print("2. x^2 dari 0 sampai 1")
    print("3. Input sendiri")
    print("="*50)
    
    choice = input("Pilih opsi (1/2/3): ")
    
    if choice == '1':
        f = integral_1
        a = 0
        b = np.pi / 2
        func_str = "cos(x)"
        bounds_str = f"0 sampai π/2"
    elif choice == '2':
        f = integral_2
        a = 0
        b = 1
        func_str = "x^2"
        bounds_str = "0 sampai 1"
    elif choice == '3':
        func_input = input("Masukkan fungsi (gunakan x sebagai variabel, contoh: x**2, np.sin(x)): ")
        a = float(input("Masukkan batas bawah (a): "))
        b = float(input("Masukkan batas atas (b): "))
        
        f = lambda x: eval(func_input)
        func_str = func_input
        bounds_str = f"{a} sampai {b}"
    else:
        print("Pilihan tidak valid!")
        return
    
    print("="*50)
    print(f"Menghitung integral: {func_str}")
    print(f"Batas integrasi: {bounds_str}")
    print("="*50)
    
    R, result = romberg_integration(f, a, b)
    
    print("\nTabel Romberg Segitiga:")
    print_romberg_table(R)
    
    print(f"\nHasil integral: {result:.15f}")
    print("="*50)


if __name__ == "__main__":
    main()
