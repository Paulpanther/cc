# https://codeforces.com/problemset/problem/1393/D
# Rejected because of timeout on test 8, we assume that is a problem with python
# and not our solution as the best possible solution is in O(n*m)
# and our solution is in O(2*n*m + c) = O(n*m)

m,n = [int(x) for x in input().split(" ")]

a = []
# Pre: 0-Border for array
a.append([0] * (n + 2))
for _ in range(m):
    row = list(input())
    a.append([0] + row + [0])
a.append([0] * (n + 2))


values = [[0] * (n + 2) for _ in range(m + 2)]

for r_i, row in enumerate(a):
    for c_i, color in enumerate(row):
        # Not in 0-Border
        if r_i != 0 and c_i != 0 and r_i != m +1 and c_i != n + 1:
            a_color = a[r_i][c_i - 1]
            b_color = a[r_i - 1][c_i]

            a_value  = values[r_i][c_i - 1]
            b_value = values[r_i - 1][c_i]

            values[r_i][c_i] = min(a_value, b_value) + 1

            if a_color != color or b_color != color:
                values[r_i][c_i] = 1

value_sum = 0

for r_i in reversed(range(len(a))):
    row = a[r_i]
    for c_i in reversed(range(len(row))):
        color = row[c_i]
        # Not in 0-Border
        if r_i != 0 and c_i != 0 and r_i != m +1 and c_i != n + 1:
            a_color = a[r_i][c_i + 1]
            b_color = a[r_i + 1][c_i]

            a_value  = values[r_i][c_i + 1]
            b_value = values[r_i + 1][c_i]

            values[r_i][c_i] = min(a_value, b_value, values[r_i][c_i] - 1) + 1

            if a_color != color or b_color != color:
                values[r_i][c_i] = 1

            value_sum += values[r_i][c_i]

print(value_sum)

