import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file_name = 'lightning_item'

file1 =open(dir_path+"/ia.txt",'r')
Lines = file1.readlines()

with open(dir_path+"/"+file_name+".yml",'w') as f:
    for line in Lines:
        line = line.rstrip()
        if line:
            sp = line.split(':')
            f.write(sp[1]+":\n")
            f.write("  Id: paper\n")
            f.write(f"  Model:{sp[2]}\n")
            print(line)
print("done")