""""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.

lista = [1,1,1]
"""
def all_equal(array):
    if array == []:
            return True
    else:
        try:
            
            new_array = array[0]
            index = 0
            while new_array == array[index]:
                index += 1
                try:
                    if array[index]:
                        continue
                except:
                    break
    
            if index == len(array):
                return True
            else:
                return False
        except:
            return False
all_equal(lista)
