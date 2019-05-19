grid = [

['T','R','A','P'],
['C','A','R','D'],
['F','A','C','T'],
['D','A','R','T']

]


row_words = []
column_words = []
rows = len(grid)
columns = len(grid[0])
row_words.extend([''.join(i) for i in grid[0:] ])
column_words.extend([ ''.join(i) for i in list(map(lambda x: [grid[i][x] for i in range(rows)], range(columns)))])
print(row_words,column_words)
