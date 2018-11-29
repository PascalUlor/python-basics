file=open("fruits.txt", 'r')
content=file.read()
print(content)

content=file.readlines()
print(content)

file.seek(0)
content=file.readlines()
print(content)

# content=[i.rstrip("\n") for i in content]
content=[len(i.rstrip("\n")) for i in content]
print(content)

file.close()

file=open("myfile.txt", 'w')
file.write("Line1\n")
l = ['pear\n', 'apple\n', 'orange\n', 'mandarin\n', 'watermelon\n', 'pomegranate\n']
for item in l:
    file.write(item)
file.close()
