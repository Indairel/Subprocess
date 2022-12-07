import subprocess

with open('output.txt', 'w') as f:
    p = subprocess.run(['ls',  '-la'], stdout=f, text=True)

# print(p.returncode)  # returncode returns if there is any error

print(p.stdout)
