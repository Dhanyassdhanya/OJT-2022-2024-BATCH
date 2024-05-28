import pandas as pd
# read the csv file into the dataframe
df =  pd.read_csv('series.csv',dtype = {'Age':int,'Salary':float},
                  usecols = ['Name','Age','Place'])
print(df)



import pandas as pd
df = pd.read_csv('series.csv')
print(df)

#clean the row without empty dataframe
df_cleaned_row = df.dropna(how="all")
print(df_cleaned_row)





df_cleaned_col = df.dropna(axis=1,how="all")
print(df_cleaned_col)




df_filled_data = df.fillna(0)
print(df_filled_data)






