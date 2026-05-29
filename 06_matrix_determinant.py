import numpy as np
import matplotlib.pyplot as plt
from plot_helpers import save_lesson_figure

def demonstrate_determinant(matrix : np.ndarray, title:str = "", filename: str = "06_matrix_determinant.png"):
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4))

     # Исходный единичный квадрат
    square = np.array([[0,1,1,0,0],
                      [0,0,1,1,0]])
    
    # Преобразованный квадрат
    transformed_square = matrix @ square

    # Площади
    area_original = 1.0  # единичный квадрат
    area_transformed = abs(np.linalg.det(matrix))

    # 1. Исходный квадрат 
    ax1.plot(square[0, :], square[1, :], 'bo-', linewidth=2)
    ax1.fill(square[0, :], square[1, :], alpha=0.3)
    ax1.set_title(f'Исходная площадь: {area_original}')
    ax1.set_aspect('equal')
    ax1.grid(True)

    # 2. Преобразованный квадрат
    ax2.plot(transformed_square[0, :], transformed_square[1, :], 'r+-', linewidth=2)
    ax2.fill(transformed_square[0, :], transformed_square[1, :], alpha=0.3)
    ax2.set_title(f'Новая площадь: {area_transformed:.2f}\nОпределитель: {np.linalg.det(matrix):.2f}')
    ax2.set_aspect('equal')
    ax2.grid(True)
    
    plt.suptitle(f'{title}\nМатрица: {matrix[0]}, {matrix[1]}')
    save_lesson_figure(fig, __file__, filename)
    plt.show()

if __name__ == '__main__':
    # Экспериментируем с разными матрицами
    matrices = {
        "Растяжение 2x": np.array([[2, 0], [0, 2]]),
        "Сжатие по Y": np.array([[1, 0], [0, 0.5]]),
        "Поворот 45°": np.array([[0.7, -0.7], [0.7, 0.7]]),
        "Сдвиг": np.array([[1, 0.5], [0, 1]]),
        "Вырожденная": np.array([[1, 2], [2, 4]])  # det = 0
    }

    filenames = {
        "Растяжение 2x": "06_det_scale_2x.png",
        "Сжатие по Y": "06_det_compress_y.png",
        "Поворот 45°": "06_det_rotation.png",
        "Сдвиг": "06_det_shear.png",
        "Вырожденная": "06_det_singular.png",
    }

    for name, matrix in matrices.items():
        demonstrate_determinant(matrix, name, filenames[name])
