import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data_onehot = pd.DataFrame(index=data.index, columns=['robot', 'human'])
data_onehot = data_onehot.fillna(0)
for i in range(len(data)):
    if data.loc[i, 'whoAmI'] == 'robot':
        data_onehot['robot'][i] = 1
    elif data.loc[i, 'whoAmI'] == 'human':
        data_onehot['human'][i] = 1
print(data_onehot.head())
