
data = [
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rainy', 'Mild', 'High', 'Weak', 'No'],
    ['Rainy', 'Cool', 'Normal', 'Strong', 'Yes']
]

print("Training Examples:")
for row in data:
    print(row)

hypothesis = ['0', '0', '0', '0']

for row in data:
    if row[4] == 'Yes':
        if hypothesis[0] == '0':
            hypothesis = row[:4]
        else:
            for i in range(4):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'

print("\nFinal Hypothesis:")
print(hypothesis)
