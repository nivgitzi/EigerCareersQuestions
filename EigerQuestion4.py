
import sys

def countMaxElement(stream, max_element=(-sys.maxsize - 1), max_count=0, current_element=None):
    if current_element == None:
        current_element = next(stream)
    if current_element == 0:
        return f'({max_element}; {max_count})'
    else:
        if current_element > max_element:
            max_element = current_element
            max_count = 1
        elif current_element == max_element:
            max_count += 1
        return countMaxElement(stream, max_element, max_count, next(stream))


print(countMaxElement(iter([1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0])))