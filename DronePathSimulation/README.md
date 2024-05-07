`parser_code.py` 用于解析无人机控制代码，获取无人机飞行路径

`visualization.py` 用于图像绘制，包括三部分：

1. `draw_path`用于绘制路径，基于`parser_code.py`获取的飞行路径
2. `draw_scene`用于绘制场景，使用numpy中的矩阵定义
3. `draw_start_end`用于绘制起点和终点

可使用`draw_combined`合并上述内容于一张图

在`sample.py`中存放无人机控制代码
在`main.py`进行无人机路径绘制
