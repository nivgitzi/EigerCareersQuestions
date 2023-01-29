import sys

def countMaxElement(CurrentNumInStream, max_element=(-sys.maxsize - 1), max_count=0):
    if CurrentNumInStream == 0:
        return f'({max_element}; {max_count})'
    if CurrentNumInStream > max_element:
        max_element = CurrentNumInStream
        max_count = 1
    elif CurrentNumInStream == max_element:
        max_count += 1
    return countMaxElement(int(input()), max_element, max_count)

print("Please enter a sequence of numbers divided by ENTER. type the number 0 as the end of your sequence: ")
print(countMaxElement(int(input())))

