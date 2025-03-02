from scipy.optimize import linear_sum_assignment

n = int(input())
energy = [list(map(int, input().split())) for _ in range(n)]
compatibility = [list(map(int, input().split())) for _ in range(n)]

cost_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if compatibility[i][j]:
            row.append(energy[i][j])
        else:
            row.append(2 * energy[i][j])
    
    cost_matrix.append(row)

row_ind, col_ind = linear_sum_assignment(cost_matrix)
print(sum(cost_matrix[i][j] for i, j in zip(row_ind, col_ind)))
