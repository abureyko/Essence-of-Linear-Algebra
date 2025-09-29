import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])
w = np.array([2, 2])

# Вычислим скалярное произведение
dot_product = np.dot(v, w)
print(f"Скалярное произведение v и w: {dot_product}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Субплот 1: Геометрическая интерпретация (Проекция)
ax1.set_xlim(-1, 4)
ax1.set_ylim(-1, 4)
ax1.set_aspect('equal')
ax1.set_title('Геометрия: Скалярное произведение = (Длина проекции) * (Длина w)')

# Отобразим векторы
ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'v {v}', width=0.015)
ax1.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'w {w}', width=0.015)

# ВЫЧИСЛЯЕМ ПРОЕКЦИЮ вектора v на w
# Формула проекции: proj_w(v) = ( (v·w) / (w·w) ) * w
proj_scalar = dot_product / np.dot(w, w) # скаляр, показывающий "сколько w" в проекции
v_proj_on_w = proj_scalar * w

# Отображаем проекцию
ax1.quiver(0, 0, v_proj_on_w[0], v_proj_on_w[1], angles='xy', scale_units='xy', scale=1, color='green', label=f'Проекция v на w', width=0.01)

# Показываем пунктирную линию от v к проекции (перпендикуляр)
ax1.plot([v[0], v_proj_on_w[0]], [v[1], v_proj_on_w[1]], 'k--', alpha=0.7, label='Перпендикуляр')

ax1.legend()
ax1.text(0.5, -0.5, f'v · w = {dot_product}', fontsize=12, bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))
ax1.text(0.5, -0.8, f'Длина проекции = {np.linalg.norm(v_proj_on_w):.2f}', fontsize=10)

# Субплот 2: Дуальность - Линейное преобразование к 1D
ax2.set_xlim(-1, 9)
ax2.set_ylim(-1, 4)
ax2.set_aspect('equal')
ax2.set_title('Дуальность: w как линейное преобразование (1x2 матрица)')

# Отобразим исходные векторы
ax2.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'v {v}', width=0.015)
ax2.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'w {w} (преобразователь)', width=0.015)

# Покажем числовую прямую (1D пространство), на которое мы проецируем
ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax2.axhline(y=0.1, color='k', linestyle='-', alpha=0.1) # Чтобы прямая была заметнее

# Ключевой момент дуальности: вектор w можно рассматривать как матрицу-строку [w1, w2]
# Эта матрица задает линейное преобразование из 2D в 1D.
# Результат преобразования вектора v этой матрицей - это число на числовой прямой.

# Преобразуем v с помощью "матрицы" w.
# Это и есть скалярное произведение! v · w = [w1, w2] * [v1; v2] (матричное умножение 1x2 на 2x1)
result_1d = dot_product # Наше число на прямой

# Визуализируем результат на числовой прямой
ax2.plot(result_1d, 0, 'go', markersize=10, label=f'Результат преобразования: {result_1d}')
ax2.quiver(0, 0, result_1d, 0, angles='xy', scale_units='xy', scale=1, color='green', width=0.02, alpha=0.7)

# Соединяем точку v с результатом на прямой, чтобы показать "сжатие" измерения
ax2.plot([v[0], result_1d], [v[1], 0], 'k--', alpha=0.5)

ax2.legend()

plt.tight_layout()
plt.show()