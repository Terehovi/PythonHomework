def printOperationTable(operation, numRows, numColumns):
    if operation(1, 1) == 2:
        print(1, end='\t')

    for row in range(1, numRows + 1):
        for column in range(1, numColumns + 1):
            if operation(1, 1) == 2:
                column -= 1
            print(operation(row, column), end='\t')
        print()

printOperationTable(lambda x, y: x * y, 6, 6)