import pandas
from scipy.stats import norm

# dataset from http://blog.csdn.net/thither_shore/article/details/52331077
# on P84
dataset = pandas.read_csv("dataset.csv")

properties = {}

for idx, col_name in enumerate(dataset.columns):
    # remove some properties
    if idx > 0 and idx < 7:
        properties[col_name] = []

for index, row in dataset.iterrows():
    for col_name in dataset.columns:
        if col_name in properties.keys() and (not row[col_name] in properties[col_name]):
            properties[col_name].append(row[col_name])

# count label(class)
Cc = [len(dataset[dataset["Label"] == i]) for i in range(2)]
# P(c)
Pc = [(i + 1) / (sum(Cc) + 2) for i in Cc]

Pp = {}
for p in properties.keys():
    for v in properties[p]:
        Pp[v] = [(len(dataset[(dataset["Label"] == i) & (dataset[p] == v)]) + 1) / (Cc[i] + len(properties[p]))
                 for i in range(2)]

density_mean = [dataset[dataset["Label"] == i]["Density"].mean() for i in range(2)]
density_var = [dataset[dataset["Label"] == i]["Density"].std() for i in range(2)]
sugar_ratio_mean = [dataset[dataset["Label"] == i]["SugarRatio"].mean() for i in range(2)]
sugar_ratio_var = [dataset[dataset["Label"] == i]["SugarRatio"].std() for i in range(2)]

# test 1 on P151
test_1 = ["green", "curl", "heavily", "distinct", "sunken", "hard", 0.697, 0.460]
P = [1, 1]
for p in test_1[:-2]:
    P[0] *= Pp[p][0]
    P[1] *= Pp[p][1]
for i in range(2):
    P[i] *= norm.pdf(test_1[-2], loc=density_mean[i], scale=density_var[i])
    P[i] *= norm.pdf(test_1[-1], loc=density_mean[i], scale=density_var[i])
print(P)
if P[0] < P[1]:
    print(1, "Good")
else:
    print(0, "Bad")
