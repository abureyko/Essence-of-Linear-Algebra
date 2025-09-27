import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_non_square_transformations():
    """Визуализация преобразований между разными размерностями"""
    fig = plt.figure(figsize=(15, 5))
    
    # 1. Исходные данные в 3D
    ax1 = fig.add_subplot(131, projection='3d')
    
    # Создаем точки в 3D пространстве
    t = np.linspace(0, 2*np.pi, 20)
    x = np.cos(t)
    y = np.sin(t) 

    z = t/3
    
    ax1.scatter(x, y, z, c=z, cmap='viridis', s=50)
    ax1.set_title('Исходные данные в ℝ³')
    ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')

     # 2. Преобразование 3D → 2D (матрица 2×3)
    ax2 = fig.add_subplot(132)
    
    # Матрица проекции 3D → 2D
    A_3d_to_2d = np.array([[1, 0.5, 0],   # Столбцы - куда переходят i,j,k из 3D
                           [0, 0.5, 1]])
    
    # Преобразуем 3D точки в 2D
    points_3d = np.vstack([x, y, z])
    points_2d = A_3d_to_2d @ points_3d

    ax2.scatter(points_2d[0, :], points_2d[1, :], c=z, cmap='viridis', s=50)
    ax2.set_title('ℝ³ → ℝ² (матрица 2×3)\nРанг = 2')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')

    # 3. Преобразование 2D → 3D (матрица 3×2)  
    ax3 = fig.add_subplot(133, projection='3d')
    
    # Матрица поднятия 2D → 3D
    A_2d_to_3d = np.array([[1, 0],
                           [0, 1], 
                           [1, 1]])  # Столбцы - куда переходят i,j из 2D
    
    # Создаем 2D точки
    x_2d = np.linspace(-1, 1, 10)
    y_2d = np.linspace(-1, 1, 10)
    X, Y = np.meshgrid(x_2d, y_2d)
    
    # Преобразуем 2D точки в 3D
    points_2d_flat = np.vstack([X.ravel(), Y.ravel()])
    points_3d_transformed = A_2d_to_3d @ points_2d_flat
    
    ax3.scatter(points_3d_transformed[0, :], 
                points_3d_transformed[1, :], 
                points_3d_transformed[2, :], 
                c=points_2d_flat[0, :], cmap='viridis', alpha=0.6)
    
    ax3.set_title('ℝ² → ℝ³ (матрица 3×2)\nРанг = 2')
    ax3.set_xlabel('X'); ax3.set_ylabel('Y'); ax3.set_zlabel('Z')



    plt.tight_layout()
    plt.show()

    # Вывод свойств матриц
    print("Матрица 2×3 (ℝ³ → ℝ²):")
    print("Ранг:", np.linalg.matrix_rank(A_3d_to_2d))
    print("Форма:", A_3d_to_2d.shape)
    print("\nМатрица 3×2 (ℝ² → ℝ³):")
    print("Ранг:", np.linalg.matrix_rank(A_2d_to_3d)) 
    print("Форма:", A_2d_to_3d.shape)

visualize_non_square_transformations()