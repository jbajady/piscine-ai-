import numpy as np 
import pandas as pd


colors=np.array(["ss","ss2"])
print(colors)

d = {"col1": [0, 1, 2, 3], "col2": pd.Series([2, 3], index=[2, 3])}
res= pd.DataFrame(data=d, index=[0, 1, 2, 3])
ist = pd.Series([1, 2, 3, 4, 5])
data = {"b": 1, "a": 0, "c": 2}
s_dict = pd.Series(data)
print(s_dict )
#    col1  col2
# 0     0   NaN
# 1     1   NaN
# 2     2   2.0
# 3     3   3.0