import numpy as np

def change_basis(vectors, old_basis, new_basis):
    """
    Преобразует векторы из старого базиса в новый базис
    
    Parameters:
    vectors: матрица векторов (каждый столбец - вектор в старом базисе)  
    old_basis: матрица старого базиса (столбцы - базисные векторы)
    new_basis: матрица нового базиса (столбцы - базисные векторы)
    
    Returns:
    vectors_in_new_basis: векторы в новом базисе
    """
    transition = np.linalg.inv(new_basis) @ old_basis
    return transition @ vectors.T
    
    

# Старый базис (стандартный)
old_basis = np.eye(2)  # [[1,0],[0,1]]

# Новый базис (базис Дженнифер)
new_basis = np.array([[2, 1],   # b1
                      [1, 2]])  # b2

# Векторы в старом базисе
vectors = np.array([[5, 3],    # v1
                    [1, 4]])   # v2 (каждый столбец - вектор)

# Преобразование
result = change_basis(vectors, old_basis, new_basis)
print("Векторы в новом базисе:")
print(result)