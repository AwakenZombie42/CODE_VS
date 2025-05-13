def main():
    mat = []
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    input_mat(mat, row, col)
    print_mat(mat, row, col)
    transpose(mat, row, col)

def input_mat(mat, row, col):
    for i in range(row):
        l = []
        for j in range(col):
            l.append(int(input(f"Enter the {j + 1} element of {i + 1} row: ")))
        mat.append(l)

def print_mat(mat, row, col):
    print("Original Matrix:")
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end = " ")
        print()

def transpose(mat, row, col):
    print("Transpose Matrix:")
    for i in range(row):
        for j in range(col):
            print(mat[j][i], end = " ")
        print()

if __name__ == "__main__":
    main()


'''
     j  j
[    0  1
i 0 [1, 2],
i 1 [3, 4]
]
'''