from __future__ import print_function
import fileinput
for line in fileinput.input():
    meta = {
        fileinput.filename(),
        fileinput.filelineno(),
        fileinput.fileno(),
        fileinput.isfirstline()}
    print(*meta, end=" ")
    #print(line, end=" ")
