values = [1, 1, 2, 3, 4, 4, 4, 5, 6]

unique = {i: 1 for i in values}
unique = list(unique.keys())
print(unique)


import numpy as np
values = [1, 1, 2, 3, 4, 4, 4, 5, 6]
print(*np.unique(values))


import pandas as pd
values = [1, 1, 2, 3, 4, 4, 4, 5, 6]
s = pd.Series(values)
s = s.drop_duplicates()
print(s.tolist())


values = [1, 1, 2, 3, 4, 4, 4, 5, 6]
df = pd.DataFrame(values)
df.drop_duplicates(inplace=True)
print(df)

values = [1, 1, 2, 3, 4, 4, 4, 5, 6]
df = pd.DataFrame({'values': values})
print(df.drop_duplicates()['values'].tolist())
