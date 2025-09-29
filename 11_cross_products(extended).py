import numpy as np
import matplotlib.pyplot as plt

def ml_cross_product_demo():
    
    # Практический пример из Computer Vision
    # Нормаль к поверхности треугольника
    p1, p2, p3 = [0,0,0], [2,0,0], [0,2,0]  # Вершины треугольника в плоскости XY
    
    edge1 = np.array(p2) - np.array(p1)  # [2, 0, 0]
    edge2 = np.array(p3) - np.array(p1)  # [0, 2, 0]
    
    normal = np.cross(edge1, edge2)  # [0, 0, 4]
    
    # Визуализация
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Треугольник
    triangle = np.array([p1, p2, p3, p1])
    ax.plot(triangle[:,0], triangle[:,1], triangle[:,2], 'b-', linewidth=3, label='Треугольник')
    
    # Нормаль
    ax.quiver(1, 1, 0, normal[0], normal[1], normal[2], color='red', 
              arrow_length_ratio=0.1, linewidth=3, label='Нормаль (a × b)')
    
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.legend()
    plt.title('Векторное произведение в ML: нормаль к поверхности\n(Computer Vision)')
    plt.show()
    
    print(f"edge1: {edge1}")
    print(f"edge2: {edge2}") 
    print(f"normal: {normal} (длина = {np.linalg.norm(normal)})")
    print("→ Эта нормаль используется в 3D графике, рендеринге, computer vision")

ml_cross_product_demo()