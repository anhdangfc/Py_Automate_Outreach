#! python3
# 14_Table_Printer.py - Take the list of lists of strings
# and displays it in a well-organized table with each column right-justified
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(tableData):
    out = ''
    #colWidth = [0]*len(tableData) ## save the max width for .rjust(pad) (for 3 col)
    rowOut = [0]*len(tableData) ## two store 3 values of each row 

    ## Identify the pad of each col in output
    for c_ix in range(len(tableData)):
        len_str = list(map(lambda x: len(x), tableData[c_ix])) ## Use lambda and map. Directly without using colWidth to store value
        #colWidth[c_ix] = max(len_str)
        tableData[c_ix] = list(map(lambda x: x.rjust(max(len_str)+1), tableData[c_ix]))
    # print(tableData) ## for check/debug 

    ## Rotate row and col
    for r_ix in range(len(tableData[1])):
        for c_ix in range(len(tableData)):
            item = tableData[c_ix][r_ix]
            rowOut[c_ix] = item
            # print(item) ## for check/debug
        if c_ix == len(tableData)-1: ## The position to enter new line
            out += ''.join(rowOut) + '\n'

    ## Print output
    print(out, end = '\n')


## Test:  
print_table(tableData)