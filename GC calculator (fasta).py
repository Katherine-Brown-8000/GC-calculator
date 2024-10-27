file_name = r"C:\Users\username\Downloads\sequence_name.fa"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        sequence = "".join([line.strip() for line in content if not line.startswith('>')])
        return sequence

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
print(f"The GC percent of your sequence is: {gc_content}")
