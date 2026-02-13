# 1. Creating DataFrame using a List
# import pandas as pd
# lst = ['Geeks', 'For', 'Geeks', 'is',
#        'portal', 'for', 'Geeks']
# df = pd.DataFrame(lst)
# print(df)


# 2. Creating DataFrame from dict of ndarray/lists
# import pandas as pd
# data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
#         'Age': [20, 21, 19, 18]}
# df = pd.DataFrame(data)
#  print(df)




# 1. Column Selection
# import pandas as pd
# data = {'Name': ['Jai', 'Prince', 'Gaurav', 'Anuj'],
#         'Age': [27, 24, 22, 32],
#         'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
# df = pd.DataFrame(data)
# print(df[['Name','Age','Address','Qualification']])


# Indexing and Selecting Data in Pandas DataFrame

# 1. Indexing a Dataframe using indexing operator []
# import pandas as pd
# data = pd.read_csv("/05-02-2026-thursday/nba.csv", index_col="Name")
# first = data["Age"]
# print(first)



# 2. Indexing a DataFrame using .loc[ ]
# import pandas as pd
# data = pd.read_csv("/05-02-2026-thursday/nba.csv", index_col="Name")
# first = data.loc["Avery Bradley"]
# second = data.loc["R.J. Hunter"]
#  print(first, "\n\n\n", second)


#  3. Indexing a DataFrame using .i loc[ ]
#  import pandas as pd
#  data = pd.read_csv("/05-02-2026-thursday/nba.csv", index_col="Name")
#  row2 = data.i loc[3]
#  print(row2)


# # Working with Missing Data


#  1. Checking for Missing Values using isnull() and notnull()
# import pandas as pd
# import numpy as np
# dict = {'First Score': [100, 90, np.nan, 95],
#          'Second Score': [30, 45, 56, np.nan],
#          'Third Score': [np.nan, 40, 80, 98]}
# df = pd.DataFrame(dict)
# print(df.isnull())



#  2. Filling Missing Values using fill na(), replace() and interpolate()
# import pandas as pd
# import numpy as np
# dict = {'First Score': [100, 90, np.nan, 95],
#        'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
# df = pd.DataFrame(dict)
# print(df.fill na(0))



# 3. Dropping Missing Values using drop na()
# import pandas as pd
# import numpy as np
# dict = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score': [52, 40, 80, 98],
#         'Fourth Score': [np.nan, np.nan, np.nan, 65]}
#  df = pd.DataFrame(dict)
#  print(df)



# Now we drop rows with at least one Nan value (Null value).
# import pandas as pd
# import numpy as np
# dict = {'First Score': [100, 90, np.nan, 95],
#        'Second Score': [30, np.nan, 45, 56],
#         'Third Score': [52, 40, 80, 98],
#         'Fourth Score': [np.nan, np.nan, np.nan, 65]}
# df = pd.DataFrame(dict)
# print(df.drop na())


#  Iterating over rows and columns


# 1. Iterating Over Rows

# 1. iter items()
# 2. iter rows()
# 3. iter tuples()
# Each method provides different ways to iterate over the rows which depends on our specific needs.


import pandas as pd
 dict = {'name': ["aparna", "pankaj", "sudhir", "Geeks"],
         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
         'score': [90, 40, 80, 98]}
 df = pd.DataFrame(dict)
print(df)










