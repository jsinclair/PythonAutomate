def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for data in tableData[i]:
            if colWidths[i] < len(data):
                colWidths[i] = len(data)
    
    for j in range(len(tableData[0])):
        row = ''
        for i in range(len(tableData)):
            if i > 0:
                row += " "
            row += tableData[i][j].rjust(colWidths[i])
        print(row)
            

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
printTable(tableData)