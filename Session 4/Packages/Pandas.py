import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df, '\n')

print('Maximum Age is: ', df["Age"].max())


#Read/Write Tabular
'''
titanic = pd.read_csv("titanic.csv")

print(titanic, '\n')

print(titanic.max(), '\n')
'''

#head/tail/info methods
'''
print(titanic.head(2), '\n')
print(titanic.tail(2), '\n')
print(titanic.info(), '\n')
'''