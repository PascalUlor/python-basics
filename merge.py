import datetime

filepath=['exer4.txt', 'file3.txt', 'fruits.txt']

def merge(filepath):
    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
        for item in filepath:
            with open(str(item), 'r') as f:
                file.write(f.read()+'\n')


merge(filepath)
