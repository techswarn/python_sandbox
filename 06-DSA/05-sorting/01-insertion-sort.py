list = [10,9,1,5,6,7]

def insertion_sort(arr):
  
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j-=1
    print(list)
insertion_sort(list)