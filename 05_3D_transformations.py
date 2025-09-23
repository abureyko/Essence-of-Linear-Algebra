import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def demonstrate_3d_transformation(matrix_3x3: np.ndarray, title: str= ""):
    fig = plt.figure(figsize=(10,5))

    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(ax1, np.eye(3), 'Исходный куб')
    
    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(ax2, matrix_3x3, f'После преобразования: {title}')

    plt.tight_layout()
    plt.show()

def plot_cube(ax, transformation_matrix, title):
    # Вершины единичного куба
    vertices = np.array([
        [0,0,0], [1,0,0], [1,1,0], [0,1,0],
        [0,0,1], [1,0,1], [1,1,1], [0,1,1]
    ]).T

    # Ребра куба
    edges = [
        [0,1], [1,2], [2,3], [3,0],  # низ
        [4,5], [5,6], [6,7], [7,4],  # верх
        [0,4], [1,5], [2,6], [3,7]   # боковые
    ]
    
    transformed_vertices = transformation_matrix @ vertices
    # Рисуем ребра
    for edge in edges:
        ax.plot3D(*transformed_vertices[:, edge], color='blue', alpha=0.6)
    
    # Базисные векторы i, j, k
    i_hat = transformation_matrix @ [1,0,0]
    j_hat = transformation_matrix @ [0,1,0] 
    k_hat = transformation_matrix @ [0,0,1]
    
    ax.quiver(0,0,0, i_hat[0], i_hat[1], i_hat[2], color='red', lw=2)
    ax.quiver(0,0,0, j_hat[0], j_hat[1], j_hat[2], color='green', lw=2)
    ax.quiver(0,0,0, k_hat[0], k_hat[1], k_hat[2], color='blue', lw=2)
    
    ax.set_title(title)
    ax.set_xlim([-2,2])
    ax.set_ylim([-2,2])
    ax.set_zlim([-2,2])


def rotation_x(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotation_y(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def scale_3d(sx, sy, sz):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, sz]
    ])

if __name__ == '__main__':
    demonstrate_3d_transformation(rotation_x(np.pi/4), 'Поворот вокруг X на 45°')
    demonstrate_3d_transformation(rotation_y(np.pi/3), 'Поворот вокруг Y на 60°')
    demonstrate_3d_transformation(scale_3d(1.5, 0.5, 2), 'Масштабирование')

