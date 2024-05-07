def prompt_role():
    prompt = "You are an excellent path planner for drone flying tasks. "
    prompt += "Given an instruction and information about the 2D environment, "
    prompt += "you analyze and plan a path for the drone to fly. "
    prompt += "Please do not begin working until I say \"Start working.\" "
    prompt += "Instead, simply output the message \"Waiting for next input.\" Understood?"

    return prompt

def prompt_env():
    prompt = "Information about environments and objects are given as python dictionary. Example:\n"
    prompt += """\"\"\"
{"environment size": "length * width", # The size of the environment.
"block1": (x1:x2, y1:y2), # The position of the block1(format like numpy).
"block2": (x1:x2, y1:y2), # The position of the block2(format like numpy).
"start point": (x, y),   # The position of the drone start to fly
"destination": (x, y)}  # The position of the drone fly to
\"\"\"
-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""
    
    return prompt

def prompt_function():
    prompt = "Necessary and sufficient flying actions are defined as follows:\n"
    prompt += """\"\"\"
"FLY ACTIONS LIST"
(x, distance): Move the drone in x direction for distance.
(y, distance): Move the drone in y direction for distance.
\"\"\"
Note that distance can be negative to move in the opposite direction.
-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""
    return prompt

def prompt_output_format():
    prompt = "You divide the task into a sequence of flying actions and put them together as a python dictionary.\n"
    prompt += """The dictionary has six keys.
\"\"\"
- dictionary["task_scale"]: The scale of the task you thought, could be "easy" or "complex".
- dictionary["environment_analyse"]: A brief summary of the environment you analyzed.
- dictionary["thought_process"]: A brief summary of the thought process you used to plan the path.
- dictionary["action_sequence"]: A list of flying actions. Only the behaviors defined in the "FLY ACTIONS LIST" will be used.
- dictionary["instruction_summary"]: A brief summary of the given instruction.
- dictionary["question"]: If you cannot understand the given sentence, you can ask the user to rephrase the sentence. Leave this key empty if you can understand the given sentence.
\"\"\"
-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""

    return prompt

def prompt_example():
    prompt = "I will give you some examples of the input and the output you will generate. \n"
    prompt += """Example1:
\"\"\"
- Input:
{"environment size": "100 * 100",
"block": (40:60, 40:60),
"start point": (0, 0),
"destination": (100, 100)}
Instructions: "Fly to the destination avoiding the block."
- Output:
{
    "task_scale": "easy",
    "environment_analyse": "There is a block in the middle of the environment. The drone starts at the bottom left corner and flies to the top right corner.",
    "thought_process": "To avoid the block, the drone should fly around it. The drone should fly to the right side of the block and then fly up to the destination.",
    "action_sequence": [
        ("x", 100), 
        ("y", 100)
    ],
    "instruction_summary": "Fly to the destination avoiding the block.",
    "question": ""
}
\"\"\"
""" 
    prompt += """Example2:
\"\"\"
- Input:
{"environment size": "100 * 100",
"block": (0:60, 0:60),
"start point": (0, 100),
"destination": (100, 0)}
Instructions: "Fly to the destination avoiding the block."
- Output:
{
    "task_scale": "easy",
    "environment_analyse": "There is a block in the bottom right corner of the environment. The drone starts at the top left corner and flies to the bottom right corner.",
    "thought_process": "To avoid the block, The drone should fly to the right side of the block and then fly down to the destination.",
    "action_sequence": [
        ("x", 100), 
        ("y", -100)
    ],
    "instruction_summary": "Fly to the destination avoiding the block.",
    "question": ""
}
\"\"\"
""" 
    prompt += """Example3:
\"\"\"
- Input:
{"environment size": "100 * 100",
"block1": (40:100, 20:40),
"block2": (0:60, 60:80),
"start point": (100, 0),
"destination": (0, 100)}
Instructions: "Fly to the destination avoiding the block."
- Output:
{
    "task_scale": "easy",
    "environment_analyse": "There are two blocks in the environment. One is in the right lower corner and the other is in the left upper corner. The drone starts at the bottom right corner and flies to the top left corner.",
    "thought_process": "To avoid the block1, the drone should fly to the left side of the block1 and then fly up to the middle place. To avoid the block2, the drone should continue flying to the right side of the block2 and then fly up to the top place. Finally, the drone should fly to the left side of the destination.",
    "action_sequence": [
        ("x", -100), 
        ("y", 50), 
        ("x", 100), 
        ("y", 50),
        ("x", -100)
    ],
    "instruction_summary": "Fly to the destination avoiding the block.",
    "question": ""
}
\"\"\"
""" 
    prompt += """-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""
    return prompt

if __name__ == "__main__":
    # print(prompt_role())
    # print(prompt_env())
    # print(prompt_function())
    # print(prompt_output_format())
    print(prompt_example())