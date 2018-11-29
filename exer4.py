"""
Pascal Ulor

"""
def fah(c):
    if c < -273.15:
        return 'Your temp is {}\N{DEGREE SIGN}C  it is not good' .format(c)
    else:
        f = (c*9/5) + 32
        return 'Your temp is {}\N{DEGREE SIGN}C you are good and'  .format(c) + str(f) +'\N{DEGREE SIGN}F'

def writer(temp, filepath):
    with open(filepath, 'w') as file:
        for c in temp:
            f = (c*9/5) + 32
            if c < -300:
                file.write("Your temp is {} " "it is not good".format(f)+"\n")
            else:
                file.write("Your temp is {} " "you are good".format(f)+"\n")




def main():
    temperatures = [10,-20,-289,100]
    with open("temperature.txt", 'w') as file:
        for item in temperatures:
            file.write(str(fah(item))+"\n")
    writer(temperatures, 'exer4.txt')
if __name__ == '__main__':
    main()
