import matplotlib.pyplot as plt

n = 50
result = []
for i in range(2 * n):
    result.append({"i": i, "p": 1 - i / (2 * n)})
tmp = result[n]['p']
result[n]['p'] = result[n - 1]['p']
result[n - 1]['p'] = tmp
print([i['p'] for i in result])
sorted_result = sorted(result, key=lambda x: x['p'], reverse=True)
label = []
for i in range(2 * n):
    if i >= n:
        label.append(False)
    else:
        label.append(True)
X = []
Y = []
for i in range(2 * n):
    TP = FP = TN = FN = 0
    for j in range(2 * n):
        if j <= i:
            if label[sorted_result[j]['i']]:
                TP += 1
            else:
                FP += 1
        else:
            if label[sorted_result[j]['i']]:
                FN += 1
            else:
                TN += 1
    P = TP / (TP + FP)
    R = TP / (TP + FN)
    X.append(R)
    Y.append(P)
plt.plot(X, Y)
plt.show()
