def main():
    mat_1 = []
    mat_2 = []
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    print("Enter the elements of the matrix 1:")
    input_mat(mat_1, row, col)
    print("Enter the elements of the matrix 2:")
    input_mat(mat_2, row, col)
    print("Original Matrix 1:")
    print_mat(mat_1, row, col)
    print("Original Matrix 2:")
    print_mat(mat_2, row, col)
    add_mat(mat_1, mat_2, row, col)

def input_mat(mat, row, col):
    for i in range(row):
        l = []
        for j in range(col):
            l.append(int(input(f"Enter the {j + 1} element of {i + 1} row: ")))
        mat.append(l)

def print_mat(mat, row, col):
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end = " ")
        print()

def add_mat(mat_1, mat_2, row, col):
    print("Addition Matrix:")
    for i in range(row):
        for j in range(col):
            print(mat_1[i][j] + mat_2[i][j], end = " ")
        print()

if __name__ == "__main__":
    main()