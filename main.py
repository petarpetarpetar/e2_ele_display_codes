in_path = "input.txt"
out_path = "out.txt"

with open(out_path, "w") as out:
    with open(in_path, "r") as inp:
        lines = inp.readlines()

    for line in lines:
        code = 0b00000000
        mask = 0b10000000
        for ch in "afbed_cg":
            if ch in line.split(' ')[1]:
                code |= mask
                mask >>= 1
        out.write(f"{bin(code)} // {line.split(' ')[0]}\n")