import pandas as pd
data = [10,2,3,45,65]
series = pd.Series(data)
print(series)


import pandas as pd 
dict = {"name": "Dhanu","place":"TVM"}
series=pd.Series(dict)
print(series)





import pandas as pd
data = [10,2,3,45,65]
series = pd.Series(data)

#acess the element seperately by using indexing
print(series[2])


#arithematic operations

series_add =  series + 10
print(series_add)


# Filter the elements in the series
filtered_series=series[series > 20]
print(filtered_series)



# Statistical methods

mean =  series.mean()
print("Mean :",mean)





# dataframe

import pandas as pd
data = {'Name ': ['Swa','Suku','Pathu'],
        'Age' : [23,24,22],
        'Place' : ['Tvm','Kzh','Kol']}

# Convert the data into dataframes
df=pd.DataFrame(data)
print (df)

print (df[['Name','Place']])


# for accessing each row frond the dataframe we need by inbuild function in pandas,iloc()
print(df.iloc[1])

print(df[df['Age']>22])

#Add a new column into the dataframe
df['stipend']=[1500,5000,5000]
print(df)

# Remove a column
df = df.drop(columns=['Age'])
print(df)

# Statitical function
#Describe() help get the summary of statics of your dataframe
print(df.describe())
