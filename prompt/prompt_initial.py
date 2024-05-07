def prompt_role():
    prompt = "You are an excellent programmer of drone controller for flying tasks. "
    prompt += "Given an instruction and information about the working environment, "
    prompt += "you break it down into a sequence of flying control codes. "
    prompt += "Please do not begin working until I say \"Start working.\" "
    prompt += "Instead, simply output the message \"Waiting for next input.\" Understood?"

    return prompt

def prompt_env():
    prompt = "Information about environments and objects are given as python dictionary. Example:\n"
    prompt += """\"\"\"
{"environment size": "length * width * height", # The size of the environment.
"block1": (x1:x2, y1:y2, z1:z2), # The position of the block1(format like numpy).
"block2": (x1:x2, y1:y2, z1:z2), # The position of the block2(format like numpy).
"start point": (x, y, z),   # The position of the drone start to fly
"destination": (x, y, z)}  # The position of the drone fly to
\"\"\"
-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""

    return prompt

def prompt_function():
    prompt = "Necessary and sufficient flying control codes are defined as follows:\n"
    prompt += """\"\"\"
"FLY CONTROL CODES LIST"
takeOff(drone_number, height): Make the No.drone_number(default 0) drone take off to height(z-axis).
moveCtrl(drone_number, direction, distance): Make the No.drone_number(default 0) drone move in direction for distance. direction is 0 for x, 1 for y, 2 for z, 3 for -x, 4 for -y, 5 for -z.
flyCtrl(drone_number, height): Make the No.drone_number(default 0) drone landing to height(default 0).
\"\"\"
-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""
    return prompt

def prompt_output_format():
    prompt = "You divide the task into a sequence of flying control codes and put them together as a python dictionary.\n"
    prompt += """The dictionary has five keys.
\"\"\"
- dictionary["task_cohesion"]: A dictionary containing information about the flying control codes that have been split up.
- dictionary["drone_before"]: The position of the drone before the manipulation.
- dictionary["drone_after"]: The position of the drone after the manipulation.
- dictionary["instruction_summary"]: contains a brief summary of the given sentence.
- dictionary["question"]: If you cannot understand the given sentence, you can ask the user to rephrase the sentence. Leave this key empty if you can understand the given sentence.
\"\"\"
Three keys exist in dictionary["task_cohesion"].
\"\"\"
- dictionary["task_cohesion"]["task_sequence"]: A list of flying control codes. Only the behaviors defined in the "FLY CONTROL CODES LIST" will be used.
- dictionary["task_cohesion"]["step_instructions"]: contains a list of instructions for the drone corresponding to the list of flying control codes.
- dictionary["task_cohesion"]["drone_position"]: The position of the drone after performing per flying control code. 
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
{"environment size": "100 * 100 * 100",
"block1": (40:60, 40:60, 0:100),
"start point": (0, 0, 0),
"destination": (100, 100, 0)}
Instructions: "Fly to the destination avoiding the block."
- Output:
{"task_cohesion": 
    {"task_sequence": [
        "takeOff(0, 50)", 
        "moveCtrl(0, 0, 100)", 
        "moveCtrl(0, 1, 100)", 
        "flyCtrl(0, 0)"
        ],
    "step_instructions": [
        "Take off to 50cm height.",
        "Move 100cm to the x direction.",
        "Move 100cm to the y direction.",
        "Land."
        ],
    "drone_position": [
        (0, 0, 50),
        (100, 0, 50),
        (100, 100, 50),
        (100, 100, 0)
    ]
    },
    "drone_before": (0, 0, 0),
    "drone_after": (100, 100, 0),
    "instruction_summary": "Fly to the destination avoiding the block.",
    "question": ""
    }
\"\"\"
""" 
    prompt += """Example2:
\"\"\"
- Input:
{
    "environment size": "100 * 100 * 100",
    "block1": "(0:60, 30:60, 0:100)",
    "block2": "(40:100, 0:50, 0:100)",
    "start point": "(0, 0, 0)",
    "destination": "(100, 0, 0)"
}
Instructions: "Fly to the destination avoiding the block."

- Output:
{
    "task_cohesion": 
    {
        "task_sequence": [
            "takeOff(0, 60)", 
            "moveCtrl(0, 0, 70)", 
            "moveCtrl(0, 1, 60)", 
            "moveCtrl(0, 0, 30)",
            "moveCtrl(0, 4, 60)",
            "flyCtrl(0, 0)"
        ],
        "step_instructions": [
            "Take off to 60cm height.",
            "Move 70cm in the x direction.",
            "Move 60cm in the y direction.",
            "Move 30cm in the x direction.",
            "Move 60cm in the -y direction.",
            "Land."
        ],
        "drone_position": [
            "(0, 0, 60)",
            "(70, 0, 60)",
            "(70, 60, 60)",
            "(100, 60, 60)",
            "(100, 0, 60)",
            "(100, 0, 0)"
        ]
    },
    "drone_before": "(0, 0, 0)",
    "drone_after": "(100, 0, 0)",
    "instruction_summary": "Fly to the destination avoiding the blocks.",
    "question": ""
}
"""
    prompt += """Example3:
\"\"\"
- Input:
{"environment size": "100 * 100 * 100",
"block1": (40:60, 40:60, 0:100),
"start point": (0, 0, 0),
"destination": (0, 0, 0)}
Instructions: "Fly around the block and back to start point."
- Output:
{"task_cohesion": 
    {"task_sequence": [
        "takeOff(0, 50)", 
        "moveCtrl(0, 0, 100)", 
        "moveCtrl(0, 1, 100)", 
        "moveCtrl(0, 3, 100)",
        "moveCtrl(0, 4, 100)",
        "flyCtrl(0, 0)"
        ],
    "step_instructions": [
        "Take off to 50cm height.",
        "Move 100cm to the x direction.",
        "Move 100cm to the y direction.",
        "Move 100cm to the -x direction.",
        "Move 100cm to the -y direction.",
        "Land."
        ],
    "drone_position": [
        (0, 0, 50),
        (100, 0, 50),
        (100, 100, 50),
        (0, 100, 50),
        (0, 0, 50),
        (0, 0, 0)
    ]
    },
    "drone_before": (0, 0, 0),
    "drone_after": (0, 0, 0),
    "instruction_summary": "Fly to the destination avoiding the block.",
    "question": ""
    }
\"\"\"
""" 
    prompt += """-------------------------------------------------------
The texts above are part of the overall instruction. Do not start working yet:
"""
    return prompt

def common_gpt_reply():
    return "Understood. I will wait for further instructions before starting to work."

if __name__ == "__main__":
    print(prompt_role())
    print(prompt_env())
    print(prompt_function())
    print(prompt_output_format())
    print(prompt_example())
    # print(common_gpt_reply())