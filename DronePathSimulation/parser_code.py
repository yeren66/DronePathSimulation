import re
import ast
from visualization import draw_path, draw_scene, draw_combined
import numpy as np
drone_coordinate = (0, 0, 0) # x, y, z

def parse_takeOff(coordinate, height):
    coordinate = (coordinate[0], coordinate[1], coordinate[2] + height)
    return coordinate 


def parse_moveCtrl(coordinate, direction, distance):
    if direction == 1:
        coordinate = (coordinate[0], coordinate[1] + distance, coordinate[2])
    elif direction == 2:
        coordinate = (coordinate[0], coordinate[1] - distance, coordinate[2])
    elif direction == 3:
        coordinate = (coordinate[0] - distance, coordinate[1], coordinate[2])
    elif direction == 4:
        coordinate = (coordinate[0] + distance, coordinate[1], coordinate[2])
    elif direction == 5:
        coordinate = (coordinate[0], coordinate[1], coordinate[2] + distance)
    elif direction == 6:
        coordinate = (coordinate[0], coordinate[1], coordinate[2] - distance)
    return coordinate

def parse_flyCtrl(coordinate, mode):
    if mode == 0:
        coordinate = (coordinate[0], coordinate[1], 0)
    return coordinate


# read python file
def read_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        code_snippet = file.read()
    return code_snippet

def extract_order(code_snippet):
    variables = {}
    for line in code_snippet.split('\n'):
        if '=' in line:
            # 尝试提取变量名称和值
            try:
                var_name, expression = [x.strip() for x in line.split('=', 1)]
                # 使用ast解析数值表达式
                value = ast.literal_eval(expression)
                variables[var_name] = value
            except:
                # 忽略不能直接求值的行，如导入语句或函数调用等
                continue
    # 使用变量值替换参数中的变量并尝试计算结果
    def evaluate_expression(expr):
        # 替换变量
        for var_name, value in variables.items():
            expr = expr.replace(var_name, str(value))
        try:
            # 计算表达式的值
            return eval(expr)
        except:
            # 如果表达式不能被计算，返回原始表达式
            return expr
    pattern = r"(takeOff|moveCtrl|flyCtrl)\((.*?)\)"
    matches = re.findall(pattern, code_snippet)
    updated_matches = []
    for func, args in matches:
        # 分割参数并逐一处理
        updated_args = [evaluate_expression(arg.strip()) for arg in args.split(',')]
        updated_matches.append((func, updated_args))
    return updated_matches

def node_by_order(drone_coordinate, coordinate_list, order_list):
    coordinate_list.append(drone_coordinate)
    for order, args in order_list:
        if order == 'takeOff':
            drone_coordinate = parse_takeOff(drone_coordinate, args[1])
            coordinate_list.append(drone_coordinate)
        elif order == 'moveCtrl':
            drone_coordinate = parse_moveCtrl(drone_coordinate, int(args[1]), args[2])
            coordinate_list.append(drone_coordinate)
        elif order == 'flyCtrl':
            drone_coordinate = parse_flyCtrl(drone_coordinate, args[1])
            coordinate_list.append(drone_coordinate)

    return coordinate_list

def parse_code(file_path, drone_coordinate=(0, 0, 0), coordinate_list=[]):
    code_snippet = read_file(file_path)
    order_list = extract_order(code_snippet)
    coordinate_list = node_by_order(drone_coordinate, coordinate_list, order_list)
    return coordinate_list

if __name__ == "__main__":
    matrix_size = (15, 15, 15)
    matrix = np.zeros(matrix_size, dtype=int)
    matrix[5:10, 5:10, 0] = 1

    code_snippet = read_file('control2.py')
    order_list = extract_order(code_snippet)
    coordinate_list = []
    coordinate_list = node_by_order(drone_coordinate, coordinate_list, order_list)
    # draw_path(coordinate_list)
    draw_combined(coordinate_list, matrix)
    print(coordinate_list)
    print(order_list)
