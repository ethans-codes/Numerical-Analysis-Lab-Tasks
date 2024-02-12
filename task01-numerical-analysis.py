# Function to add two matrices

def SumMatrices(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Function to multiply two matrices
def MultMatrices(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Main program
if __name__ == '__main__':
    # User input for the size of matrices
    n = int(input("Please enter the size of matrices: "))
    # Initializing matrices A and B
    A = [[0 for i in range(n)] for j in range(n)]
    B = [[0 for i in range(n)] for j in range(n)]

    # Initializing matrix A
    print("~~~~~~~~~~~~~~INITIALIZING MATRIX A:\nPlease enter values")
    for i in range(n):
        for j in range(n):
            A[i][j]=float(input(f"for row R{i+1} column C{j+1}: "))

    # Initializing matrix B
    print("\n~~~~~~~~~~~~~~INITIALIZING MATRIX B:\nPlease enter values")
    for i in range(n):
        for j in range(n):
            B[i][j]=float(input(f"for row R{i+1} column C{j+1}: "))

    # Printing the matrices
    print("\n~~~~~~~~~~~~~~The Results:")
    print(f"The Matrix A is: {A}\nThe Matrix B is: {B}")

    # Adding matrices A and B
    C= SumMatrices(A, B, n)
    print(f"A + B = {C}")

    # Multiplying matrices A and B
    C= MultMatrices(A, B, n)
    print(f"A * B = {C}")