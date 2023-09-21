def transpose(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
    return table2

def show(table):
    for i in range(len(table)):
        mx_string = []
        for j in range(len(table[i])):
            mx_string.append(table[i][j])
        print (mx_string)

matrix = [[1, 2, 3], [4, 5, 6]]
show(matrix)
print("=============")
matrix2 = transpose(matrix)
show(matrix2)
