from helloFly import fly

# 实例化起飞控制
fh = fly()
# 起飞并上升到一定高度，以避开地面障碍
fh.takeOff(0, 10)
fh.moveCtrl(0, 5, 20)  # 向上飞行20cm，以确保高度足够避免地面障碍物

# 向北飞140cm距离，绕过障碍物区域
# 假设障碍物需要绕行的动作已在路径规划中考虑，此处直接向北飞行140cm
fh.moveCtrl(0, 1, 140)  # 0代表向北

# 向东飞140cm距离，达到目的地
fh.moveCtrl(0, 4, 140)  # 3代表向东

# 降落
fh.flyCtrl(0, 0)  # 0降落
