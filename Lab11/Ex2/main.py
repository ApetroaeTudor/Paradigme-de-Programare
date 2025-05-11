import subprocess

my_command = "ip a | grep inet | wc -l"


commands = [comm.strip() for comm in my_command.split('|')]

print(commands)
commands_dict = {}


for comm in commands:
    # imi impart comanda in perechi command, args
    fragmented_command = comm.split(' ')
    actual_command = ""
    args = []
    for i in range(len(fragmented_command)):
        if i==0:
            actual_command = fragmented_command[i]
        else:
            if fragmented_command[i]:
                args.append(fragmented_command[i])
    commands_dict[actual_command] = args

print(commands_dict)



processes = []
for i in range(len(commands)):
    currentKey = list(commands_dict.keys())[i]
    currentValues = commands_dict.get(currentKey)
    if i == 0:
        processes.append(subprocess.Popen( [currentKey,*currentValues],stdout=subprocess.PIPE ))
    elif(i<len(commands)-1):
        processes.append(subprocess.Popen( [currentKey,*currentValues],stdin=processes[i-1].stdout,stdout=subprocess.PIPE))
    else:
        processes.append(subprocess.Popen( [currentKey,*currentValues],stdin = processes[i-1].stdout,stdout=subprocess.PIPE ))
        
        
processes[0].stdout.close()

output, _ = processes[len(processes)-1].communicate()
# astept ca procesul sa se termine, si dau unpack la output-ul scos din stdout
# aici se returneaza 2 output-ul, stdout si stderr, ma intereseaza doar de stdout

print(output.decode())
# functia decode primeste un 'byte object', aici un stream, si il converteste in string 

    
