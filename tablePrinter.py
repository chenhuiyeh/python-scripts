tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    
    colWidths = [0] * len(tableData)
    row = 0
    col = 0
    for row in range(len(tableData)):
        for col in range(len(tableData[row])):
            if len(tableData[row][col]) >= colWidths[row]:
                colWidths[row] = len(tableData[row][col])
            
    i = 0
    for i in range(len(tableData[i])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print('\n')


printTable(tableData)
