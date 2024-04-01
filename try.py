import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from visualization import draw_scene, draw_path, draw_start_end

def draw_plot():
    # 获取输入并处理
    try:
        input_str = coord_text.get("1.0", tk.END)  # 从Text控件获取文本
        input_str = input_str.strip()  # 去除首尾空白字符，包括换行符
        # 假设输入格式为: x,y,z;x,y,z;x,y,z
        coord_list = np.array([list(map(float, item.split(','))) for item in input_str.split('\n')])
        
        # 绘图
        fig.clear()
        ax = fig.add_subplot(111, projection='3d')
        draw_path(coord_list, ax=ax)
        # ax = fig.add_subplot(111, projection='3d')
        # ax.scatter(coord_list[:,0], coord_list[:,1], coord_list[:,2])
        canvas.draw()
    except ValueError:
        pass  # 或者在GUI中显示错误消息



app = tk.Tk()
app.title("无人机飞行路径绘制图形界面")

left_frame = ttk.Frame(app)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = ttk.Frame(app)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=left_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# 使用Text控件替换原来的Entry控件
coord_text = tk.Text(right_frame, width=20, height=10)  # 设置Text控件的大小
coord_text.pack()
draw_button = tk.Button(right_frame, text="绘制", command=draw_plot)
draw_button.pack()


app.mainloop()
