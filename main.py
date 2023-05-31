# This is a sample Python script.
import os.path
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class strInt():
    def __init__(self,string):
        arr = string.split(';')
        self.name = arr[0]
        self.count = (int(arr[1]) + int(arr[2]) + int(arr[3]))/3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    penis = ''
    file_path = os.path.join('C:' + os.sep, 'Users', 'mrdea', 'Downloads', 'dataset_3363_4.txt')
    my_array = []
    with open(file_path, 'r+') as inf:
        for line in inf:
            my_array.append(strInt(line))
        i = int(0)
    with open('dataResult.txt','w') as ouf:
        for count in my_array:
            ouf.write(str(count.count))
        #for j in range(len(my_array)):
            #ouf.write(str(my_array[j].count) + '\n')

        while(i < len(my_array)):
            inf.write(str(my_array[i].count))
            i += 1


    #print(my_array)
    #my_array.count()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
