import os

# print(dir(os))
print("the working directory", os.getcwd())
# os.chdir("C:\\")   #it changes the directory of all files.
# print(dir(os))

print(os.listdir("C://"))
# os.mkdir('sarika')
# os.makedirs('sarika/saksham')
# os.rename('question1.py','problem.py')

print(os.environ.get('path'))
print(os.path.join("C:/", "/harry.txt"))
print(os.path.exists('C:// sarthakwork'))
print(os.path.isfile("sarthakwork"))

