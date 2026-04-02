import numpy as np 
import pandas as pd
 


data=np.array([
                ["Blue",    [1, 2],    1.1]
               ,["Red",    [3, 4],    2.2]
               ,["Pink",    [5, 6],    3.3]
               ,["Grey",    [7, 8],    4.4]
               ,["Black",[9, 10],5.5]],dtype=object)
result=pd.DataFrame(data, columns=["color","list","number"], index=[1,3,5,7,9])
print(result)
print(result.dtypes)