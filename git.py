import subprocess
import sys


print(sys.argv)
print(sys.argv[1])

subprocess.run(["git", "add","."])

subprocess.run(["git", "commit","-m", sys.argv[1]])

subprocess.run(["git", "push"])
