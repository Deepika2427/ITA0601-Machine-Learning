
S = ['0', '0', '0', '0']
G = [['?', '?', '?', '?']]

data = [
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Weak', 'No'],
    ['Sunny', 'Warm', 'High', 'Weak', 'Yes']
]

for row in data:
    x = row[:4]
    label = row[4]

    if label == 'Yes':
        G = [g for g in G if all(
            g[i] == '?' or g[i] == x[i]
            for i in range(4)
        )]

        if S[0] == '0':
            S = x[:]
        else:
            for i in range(4):
                if S[i] != x[i]:
                    S[i] = '?'

    else:
        new_G = []
        for g in G:
            if all(g[i] == '?' or g[i] == x[i]
                   for i in range(4)):
                for i in range(4):
                    if g[i] == '?' and S[i] != '?':
                        h = g[:]
                        h[i] = S[i]
                        if h not in new_G:
                            new_G.append(h)
            else:
                new_G.append(g)
        G = new_G

print("Specific Boundary (S):", S)
print("General Boundary (G):")
for g in G:
    print(g)
