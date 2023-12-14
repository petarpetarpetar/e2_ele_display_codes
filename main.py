in_path = "input.txt"
out_path = "out.txt"

masks = {
    'a':0b10000000,
    'f':0b01000000,
    'b':0b00100000,
    'e':0b00010000,
    'd':0b00001000,
    '_':0b00000100,
    'c':0b00000010,
    'g':0b00000001
}

with open(out_path, "w") as out:
    with open(in_path, "r") as inp:
        lines = inp.readlines()

    for line in lines:
        code = 0
        for key, value in masks.items():
            if key in line.split(' ')[1]:
                code |= value

        temp = '0'*(10-len(bin(code)))+bin(code)[2:]
        final = temp.replace('0', '2').replace('1','0').replace('2','1')
        out.write(f" 0b{final} // {line.split(' ')[0]}\n")