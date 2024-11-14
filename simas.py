def load(filename):
    with open(filename, 'r') as file:
        input_text = file.read()
    run(input_text)

def run(input_text):
    instructions = []
    boxes = {}  # Use dictionary to allow named variables like "num1"
    BOX_SIZE = 255
    current_ln = None
    lines = []
    
    def init_boxes():
        for i in range(BOX_SIZE):
            boxes[str(i)] = 0  # Initialize boxes with numeric keys as strings
    
    def filter_text():
        new_text = ""
        for current_char in input_text:
            if current_char in ["", "\r", "\n"]:
                continue
            new_text += current_char
        return new_text.split(";")
    
    def compile():
        nonlocal lines
        lines = filter_text()
        lines = [line for line in lines if line != ""]
        for line in lines:
            instructions.append(line.split(" "))
    
    def ins_add(data_type, op1, op2):
        if data_type == "num":
            # Perform addition between two named variables or a variable and a number
            if op1 in boxes and op2 in boxes:
                boxes[op1] += boxes[op2]
            elif op1 in boxes and op2.isdigit():
                boxes[op1] += int(op2)
    
    def ins_comment():
        pass
    
    def ins_print(box_idx):
        print(boxes.get(box_idx, ""), end="")  # no newline
    
    def ins_println():
        print("")  # newline
    
    def ins_printc(a_thing):
        the_thing = a_thing
        for i in range(first_ins_idx + 2, len(current_ln)):
            the_thing += " " + current_ln[i]
        print(the_thing, end="")  # no newline
    
    def ins_copy(from_idx, to_idx):
        boxes[to_idx] = boxes[from_idx]
    
    def ins_set(data_type, box_idx, new_value):
        if data_type == "in":
            # Get user input and attempt to parse it as a number if possible
            user_input = input().strip()
            try:
                # Try converting to float first to handle decimals
                boxes[box_idx] = float(user_input)
                # If it's an integer (e.g., "3.0"), convert to int for cleaner handling
                if boxes[box_idx].is_integer():
                    boxes[box_idx] = int(boxes[box_idx])
            except ValueError:
                # If conversion fails, store the input as a string
                boxes[box_idx] = user_input
        elif data_type == "num":
            # Set as float to allow for decimals
            boxes[box_idx] = float(new_value)
            if boxes[box_idx].is_integer():
                boxes[box_idx] = int(boxes[box_idx])
        elif data_type == "bool":
            boxes[box_idx] = new_value.lower() == "true"
        elif data_type == "str":
            str_value = new_value
            for i in range(first_ins_idx + 4, len(current_ln)):
                str_value += " " + current_ln[i]
            boxes[box_idx] = str_value
    
    def ins_start():
        init_boxes()
    
    def ins_sub(data_type, op1, op2):
        if data_type == "num":
            if op1 in boxes and op2 in boxes:
                boxes[op1] -= boxes[op2]
            elif op1 in boxes and op2.isdigit():
                boxes[op1] -= int(op2)
    
    def dispatcher(first_ins_idx):
        fi = current_ln[first_ins_idx]
        o1 = current_ln[first_ins_idx + 1] if len(current_ln) > first_ins_idx + 1 else None
        o2 = current_ln[first_ins_idx + 2] if len(current_ln) > first_ins_idx + 2 else None
        o3 = current_ln[first_ins_idx + 3] if len(current_ln) > first_ins_idx + 3 else None
        
        if fi == "add":
            ins_add(o1, o2, o3)
        elif fi == "comment":
            ins_comment()
        elif fi == "copy":
            ins_copy(o1, o2)
        elif fi == "print":
            ins_print(o1)
        elif fi == "printc":
            ins_printc(o1)
        elif fi == "println":
            ins_println()
        elif fi == "set":
            ins_set(o1, o2, o3)
        elif fi == "start":
            ins_start()
        elif fi == "sub":
            ins_sub(o1, o2, o3)
    
    compile()
    
    for instruction in instructions:
        current_ln = instruction
        first_ins_idx = 0
        while current_ln[first_ins_idx] == "":
            first_ins_idx += 1
        dispatcher(first_ins_idx)

# To run this, save your SIMAS code in a file, e.g., 'simas.txt', then call:
# run_from_file('simas.txt')
