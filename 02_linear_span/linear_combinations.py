def vector_add(v, w):
    """Складывает два вектора покомпонентно"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def scalar_multiply(c, v):
    """Умножает вектор на скаляр"""
    return [c * v_i for v_i in v]


def linear_combination(vectors, coefficients):
    """
    Вычисляет линейную комбинацию векторов.
    
    Parameters:
    vectors: list of lists - список векторов (например, [[1, 2], [3, 4]])
    coefficients: list - список коэффициентов (например, [2, -1])
    
    Returns:
    list - результирующий вектор
    """
    # Умножаем каждый вектор на свой коэффициент
    scaled_vectors = [scalar_multiply(coef, vec) for coef, vec in zip(coefficients, vectors)]
    
    # Складываем все полученные векторы
    result = scaled_vectors[0]
    for vec in scaled_vectors[1:]:
        result = vector_add(result, vec)
    return result

# Пример использования
if __name__ == "__main__":
    # Базисные векторы
    i_hat = [1, 0]
    j_hat = [0, 1]
    
    # Коэффициенты
    coefs = [3, 2]
    
    # Линейная комбинация: 3*i_hat + 2*j_hat
    result = linear_combination([i_hat, j_hat], coefs)
    print(f"{coefs[0]}*i + {coefs[1]}*j = {result}")
    # Output: 3*i + 2*j = [3, 2]