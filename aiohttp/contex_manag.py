import os.path
# f = open(os.path.dirname(__file__) + '/../data.yml')

# file = open(os.path.dirname(__file__) + '/../one.txt')
# try:
#     lines = file.readlines()
# finally:
#     file.close()

with open(os.path.dirname(__file__) + '/../one.txt') as f:
    lines = f.readlines()

a = 0
