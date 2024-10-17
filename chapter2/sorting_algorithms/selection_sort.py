array = [4,2,1,3]

def selection_sort(array):

    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                
        
        if array[min_index] < array[i]: 
            aux = array[i]
            array[i] = array[min_index]
            array[min_index] = aux

    return array

array_sorted = selection_sort(array)
print(array_sorted)
