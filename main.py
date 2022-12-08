import subprocess

# with open('output.txt', 'w') as f:
#     p = subprocess.run(['ls', '-la'], stdout=f, text=True)

# print(p.returncode)  # returncode returns if there is any error

# p = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)

p = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)

print(p.stdout)

# if p.returncode != 0

# pt = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p.stdout)
#
# print(pt.stdout)
