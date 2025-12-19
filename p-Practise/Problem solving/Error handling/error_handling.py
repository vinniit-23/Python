"""Error handling in python"""
file = open("youtube_manager.py",'w')

try :
    file.write("print('Hello world') ")
finally :
    file.close()

with open("youtube_manager.py",'w') as file:
    file.write("print('hello from error_handling.py file')")