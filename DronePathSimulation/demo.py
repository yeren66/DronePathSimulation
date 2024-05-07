import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d
# from visualization import draw_scene, draw_path

global fig, ax, canvas, path_number

def init_plot_area():
    global fig, ax, canvas
    # 清空当前的图形
    fig.clear()
    # 创建一个3D子图
    ax = fig.add_subplot(111, projection='3d')
    # 设置坐标轴的限制
    ax.set_xlim([0, 150])
    ax.set_ylim([0, 150])
    ax.set_zlim([0, 150])
    # 设置坐标轴标签
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    canvas.draw()
    app.update()
    return ax

def draw_path(points, ax):
    global path_number
    x, y, z = zip(*points)
    color = ['g', 'b', 'c', 'm', 'y', 'k']
    
    # 绘制路径
    ax.plot(x, y, z, marker='o', color=color[path_number % 6])
    path_number += 1
    canvas.draw()
    app.update()

def draw_path_with_arrows(points, ax):
    global path_number
    x, y, z = zip(*points)
    color = ['g', 'b', 'c', 'm', 'y', 'k']

    # 绘制路径
    ax.plot(x, y, z, color=color[path_number % 6])

    # 在路径上添加箭头
    num_arrows = len(points) - 1
    for i in range(num_arrows):
        start_point = points[i]
        end_point = points[i + 1]
        arrow = Arrow3D([start_point[0], end_point[0]], [start_point[1], end_point[1]], [start_point[2], end_point[2]],
                        mutation_scale=20, lw=1, arrowstyle="-|>", color=color[path_number % 6])
        ax.add_artist(arrow)
    
    path_number += 1
    canvas.draw()
    app.update()

def draw_scene(matrix, ax):
    
    # 计算放大后的每个体素的位置
    # 我们创建了一个辅助的空间坐标网格，使得每个体素都能被放大到适当的位置
    filled = np.argwhere(matrix)
    for x, y, z in filled:
        # 对于矩阵中的每个非空体素，我们绘制一个以该点为中心，尺寸为10的立方体
        # 注意这里简化处理，实际上可以根据需求调整立方体的颜色和透明度等属性
        ax.bar3d(x*10, y*10, z*10, 10, 10, 10, edgecolor='gray', color=(0, 0, 0, 0), alpha=0.1)
    canvas.draw()
    app.update()

def draw_from_input(mode=0):
    global ax
    try:
        input_str = coord_text.get("1.0", tk.END).strip()
        points = np.array([list(map(float, item.split(','))) for item in input_str.split('\n') if item])
        if mode == 1:
            draw_path_with_arrows(points, ax=ax)
        else:
            draw_path(points, ax=ax)
    except ValueError:
        pass  # 处理输入错误

def draw_preset_scene(scene_id):
    matrix_size = (15, 15, 15)
    matrix = np.zeros(matrix_size, dtype=int)
    # 根据scene_id选择场景进行绘制
    if scene_id == 1:
        matrix[5:10, 5:10, 0] = 1
    elif scene_id == 2:
        matrix[0:10, 5:10, 0] = 1
    elif scene_id == 3:
        matrix[5:10, 0:10, 0] = 1
    elif scene_id == 4:
        matrix[5:10, 5:, 0] = 1

    draw_scene(matrix, ax=ax)
    # 可以添加更多的场景条件
    canvas.draw()
    app.update()


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d,  self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

    def set_3d_properties(self):
        xs, ys, zs = self._verts3d
        self._verts2d = proj3d.proj_transform(xs, ys, zs, self.axes.M)[:2]

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

        return np.min(zs)

if __name__ == '__main__':
    app = tk.Tk()
    app.title("3D绘图工具")

    # 创建左右两个Frame
    left_frame = ttk.Frame(app)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_frame = ttk.Frame(app)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=5)

    # 左侧控件，创建画布
    fig = Figure(figsize=(5, 4), dpi=200)
    canvas = FigureCanvasTkAgg(fig, master=left_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    ax = init_plot_area()
    path_number = 0

    # 右侧控件
    # 路径输入相关控件的Frame
    path_frame = ttk.Frame(right_frame)
    path_frame.pack(fill=tk.X)
    path_label = tk.Label(path_frame, text="路径输入", fg='gray')
    path_label.pack(side=tk.TOP, anchor='w')  # 'w' 代表左对齐

    coord_text = tk.Text(path_frame, width=20, height=20)
    coord_text.pack()

    buttons_frame1 = tk.Frame(path_frame)
    buttons_frame1.pack(pady=10)  # `pady`用于在按钮框架的上下添加空间，使布局更加美观

    draw_button1 = tk.Button(buttons_frame1, text="标量绘制", command=lambda: draw_from_input(0))
    draw_button1.pack(side=tk.LEFT, padx=5)
    draw_button2 = tk.Button(buttons_frame1, text="矢量绘制", command=lambda: draw_from_input(1))
    draw_button2.pack(side=tk.LEFT, padx=5)

    # 分隔路径输入和预设场景按钮
    separator = ttk.Separator(right_frame, orient='horizontal')
    separator.pack(fill='x', pady=10)

    # 预设场景按钮的Frame
    scene_frame = ttk.Frame(right_frame)
    scene_frame.pack(fill=tk.X)
    scene_label = tk.Label(scene_frame, text="预设场景", fg='gray')
    scene_label.pack(side=tk.TOP, anchor='w')  # 'w' 代表左对齐

    buttons_frame2 = tk.Frame(scene_frame)
    buttons_frame2.pack(pady=10)  # `pady`用于在按钮框架的上下添加空间，使布局更加美观

    # 预设场景按钮
    for i in range(1, 4):  # 假设有3个预设场景
        button = tk.Button(buttons_frame2, text=f"场景 {i}", command=lambda i=i: draw_preset_scene(i))
        button.pack(side=tk.LEFT, padx=5)

    # 分隔路径输入和预设场景按钮
    separator = ttk.Separator(right_frame, orient='horizontal')
    separator.pack(fill='x', pady=10)

    # 其他控件
    other_frame = ttk.Frame(right_frame)
    other_frame.pack(fill=tk.X)
    other_label = tk.Label(other_frame, text="其他", fg='gray')
    other_label.pack(side=tk.TOP, anchor='w')  # 'w' 代表左对齐

    clear_button = tk.Button(other_frame, text="清空", command=init_plot_area)
    clear_button.pack(side=tk.TOP)

    app.mainloop()
