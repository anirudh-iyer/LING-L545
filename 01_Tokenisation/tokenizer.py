import sys

line = sys.stdin.readline()

while line!='':
    line = line.replace(' ','\n')
    line = line.replace('.',' .')
    line = line.replace(',',' ,')
    line = line.replace(';',' ;')
    line = line.replace(':',' :')
    sys.stdout.write(line)
    line = sys.stdin.readline()