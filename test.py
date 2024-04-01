import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from visualization import draw_scene, draw_path


def clear_and_draw():
    # 清空画布并绘制
    fig.clear()
    ax = fig.add_subplot(111, projection='3d')
    draw_from_input(ax)
    canvas.draw()

def incremental_draw():
    # 在现有画布上增量绘制
    ax = fig.gca(projection='3d')
    draw_from_input(ax)
    canvas.draw()

def draw_from_input(ax=None):
    try:
        input_str = coord_text.get("1.0", tk.END).strip()
        points = np.array([list(map(float, item.split(','))) for item in input_str.split('\n') if item])
        draw_path(points, ax=ax)
    except ValueError:
        pass  # 处理输入错误

def draw_preset_scene(scene_id):
    fig.clear()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([0, 150])
    ax.set_ylim([0, 150])
    ax.set_zlim([0, 150])

    # 设置坐标轴标签
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    # 根据scene_id选择场景进行绘制
    if scene_id == 1:
        # matrix = np.eye(3)  # 示例矩阵，实际应用中应替换为实际场景数据
        matrix_size = (15, 15, 15)
        matrix = np.zeros(matrix_size, dtype=int)
        matrix[5:10, 5:10, 0] = 1
        draw_scene(matrix, ax=ax)
    # 可以添加更多的场景条件
    canvas.draw()

app = tk.Tk()
app.title("3D绘图工具")

left_frame = ttk.Frame(app)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = ttk.Frame(app)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=left_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

coord_text = tk.Text(right_frame, width=40, height=10)
coord_text.pack()

draw_button = tk.Button(right_frame, text="直接绘制", command=clear_and_draw)
draw_button.pack()

incremental_button = tk.Button(right_frame, text="增量绘制", command=incremental_draw)
incremental_button.pack()

# 预设场景按钮
for i in range(1, 4):  # 假设有3个预设场景
    button = tk.Button(right_frame, text=f"场景 {i}", command=lambda i=i: draw_preset_scene(i))
    button.pack()

app.mainloop()
