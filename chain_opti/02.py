def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    m = [[0] * n for _ in range(n)]  # initialize a table to store optimal costs
    s = [[0] * n for _ in range(n)]  # initialize a table to store split positions
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m, s

def print_optimal_solution(s, i, j):
    if i == j:
        return f'A{i + 1}'
    else:
        return f'({print_optimal_solution(s, i, s[i][j])}{print_optimal_solution(s, s[i][j] + 1, j)})'

def main():
    # Input: number of matrices and dimensions of matrices
    n = int(input())
    dimensions = list(map(int, input().split()))

    # Check if the input is valid
    if len(dimensions) != n + 1:
        print("Invalid input. Please provide correct number of dimensions.")
        return

    # Run the matrix chain multiplication algorithm
    m, s = matrix_chain_order(dimensions)

    # Print the optimal solution
    optimal_solution = print_optimal_solution(s, 0, n - 1)
    print(f"Optimal Solution: {optimal_solution}")

if __name__ == "__main__":
    main()
