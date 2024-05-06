import random

def generate_instruction(instruction_type, min_length, max_length):
    length = random.randint(min_length, max_length)
    return f"{instruction_type}:{length}"

def generate_process(pid, priority, arrival):
    process_lines = [f"P{pid}:{priority}", f"arrival t:{arrival}"]  

    # Control the exe/io balance 
    num_instructions = random.randint(5, 150)
    exe_io_ratio = random.random()  # 0.0 - 1.0

    for _ in range(num_instructions):
        if random.random() < exe_io_ratio:
            process_lines.append(generate_instruction("exe", 2, 500))
        else:
            process_lines.append(generate_instruction("io", 3, 1000))

    process_lines.append("terminate")
    return process_lines

def generate_test_file(filename, num_processes):
    with open(filename, "w") as f:
        arrival = 1
        for pid in range(1000, 1000 + num_processes):
            priority = random.randint(1, 50)
            process_lines = generate_process(pid, priority, arrival)
            f.writelines("\n".join(process_lines) + "\n")
            arrival += random.randint(1, 100)

# Example Usage
generate_test_file("./giant_test.txt", 100)  # Generate file with 100 processes

