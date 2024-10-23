file_name = r"C:\Users\scien\Desktop\Python code files\lanbda_virus.txt"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read().strip()
        return content

seq = read_file(file_name)

def gc_calculator(seq):
    gc_count = 0
    total_bases = len(seq)

    for base in seq:
        if base in ("C", "G", "c", 'g'):
            gc_count += 1

    gc_percent = (gc_count / total_bases) * 100
    return gc_percent

gc_content = gc_calculator(seq)
print(gc_content)
