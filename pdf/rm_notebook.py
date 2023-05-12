import os, sys, io

print(sys.argv[1])
with open(sys.argv[1], encoding="utf8") as infile:
    data = infile.read()
with open(sys.argv[1], "w", encoding="utf8") as outfile:
    buf = io.StringIO(data)
    first_inline = False
    is_code_cell = False
    for line in buf:
        # can't comment out first inline that is always in the first cell
        if '"cell_type":' in line:
            is_code_cell = '"code"' in line

        if is_code_cell:
            if '%matplotlib inline' in line:
                if first_inline:
                    line = line.replace("%matplotlib inline", "#%matplotlib inline")
                first_inline = True

            line = line.replace("%matplotlib notebook", "#%matplotlib notebook")
            line = line.replace("time.sleep", "#time.sleep")
            line = line.replace("fig.canvas.draw", "#fig.canvas.draw")
            line = line.replace("plt.gcf().canvas.draw", "#plt.gcf().canvas.draw")
        outfile.write(line)
