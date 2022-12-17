import sys

line = sys.stdin.readline()

while line!='':
    for segment in ['. ','? ','! ']:
        line = line.replace(segment[0]+' ',segment[0]+'\n')

    sys.stdout.write(line)
    line = sys.stdin.readline()