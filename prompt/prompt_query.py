


# Input Framework is like this:
# - Input:
# {"environment size": "100 * 100 * 100",
# "block1": (40:60, 40:60, 0:100),
# "start point": (0, 0, 0),
# "destination": (100, 100, 0)}
# Instructions: "Fly to the destination avoiding the block."
# - Output:
# {"task_cohesion": 
#     {"task_sequence": [
#         "takeOff(0, 50)", 
#         "moveCtrl(0, 0, 100)", 
#         "moveCtrl(0, 1, 100)", 
#         "flyCtrl(0, 0)"
#         ],
#     "step_instructions": [
#         "Take off to 50cm height.",
#         "Move 100cm to the x direction.",
#         "Move 100cm to the y direction.",
#         "Land."
#         ]
#     },
#     "drone_before": (0, 0, 0),
#     "drone_after": (100, 100, 0),
#     "instruction_summary": "Fly to the destination avoiding the block.",
#     "question": ""
#     }


def task1():
    prompt = """Start working. Resume from the environment below.
\"\"\"
{"environment size": "100 * 100 * 100",
"block1": (0:60, 20:40, 0:100),
"block2": (40:100, 60:80, 0:100),
"start point": (0, 0, 0),
"destination": (100, 100, 0)}
\"\"\"
The instruction is as follows:
\"\"\"
Instructions: "Fly to the destination avoiding the block."
\"\"\"
The dictionary that you return should be formatted as python dictionary. Follow these rules:
1. The first element should be takeOff() to take off.
2. The last element should be flyCtrl() to land.
3. Make sure that each element of the ["step_instructions"] explains corresponding element of the ["task_sequence"]. Refer to "FLY CONTROL CODES LIST" to understand the elements of ["task_sequence"]
4. The length of the ["step_instructions"] list must be the same as the length of the ["task_sequence"] list and the length of the ["drone_position"] list. 
5. Never left ',' at the end of the list.
6. All keys of the dictionary should be double-quoted.
7. Insert ``` at the beginning and the end of the dictionary to separate it from the rest of your response.
Adhere to the output format I defined above. Think step by step. Good luck!
"""

    return prompt

def task2():
    prompt = """Start working. Resume from the environment below.
\"\"\"
{"environment size": "100 * 100",
"block1": (0:60, 20:40),
"block2": (40:100, 60:80),
"start point": (0, 0),
"destination": (100, 100)}
\"\"\"
The instruction is as follows:
\"\"\"
Instructions: "Fly to the destination avoiding the block."
\"\"\"
The dictionary that you return should be formatted as python dictionary. Follow these rules:
1. Refer to "FLY CONTROL CODES LIST" to understand the elements of ["action_sequence"]
2. Never left ',' at the end of the list.
3. All keys of the dictionary should be double-quoted.
4. Insert ``` at the beginning and the end of the dictionary to separate it from the rest of your response.
Adhere to the output format I defined above. Think step by step. Good luck!
"""

    return prompt

if __name__ == "__main__":
    print(task2())