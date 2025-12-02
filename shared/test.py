import pandas as pd

# read csv
df = pd.read_csv(
    "../results/pure/2001 - space fractions/2001 - space fractions extended.csv"
)

# drop columns Requirement, Description
df = df.drop(columns=["Requirement", "Description"])

# save here csv
df.to_csv("./test.csv", index=False)
