import numpy as np
import pandas as pd

data = np.array([[5, 22, 3], [13, 24, 6]])
df = pd.DataFrame(data, index=['A', 'B'], columns=['x', 'y', 'z'])
print(df)
