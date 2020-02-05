#! python3
# Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(colWidths)):
        max = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > max:
                max = len(table[i][j])
        colWidths[i] = max + 1
   
    for i in range(len(table[0])):
        str = ''
        for j in range(len(table)):     
            str = str + table[j][i].rjust(colWidths[j])
        print(str)

printTable(tableData)
