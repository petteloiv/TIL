## 퀵정렬 (Quick Sort)



### 개념

```
그룹을 둘로 나눠 재귀 호출 (여기까지는 병합정렬과 같다)
그룹을 나눌 때, 기준과 비교해서 나눈 다음 각각 재귀호출해서 합친다! 

- 병합정렬과 다르게 각 부분정렬 끝나고 후처리(병합) 필요하지 않다.
- 탑다운 방식 (재귀) 구현
```



### 기본 템플릿



- 쉬운 퀵 정렬 (리스트 새로 만들어서 정렬) 

```python
def quickSort(lst):
    # 리스트 길이
    n = len(lst)

    # 리스트 길이가 1 이하일 때 => 정렬할 게 없으므로 그대로 리턴 
    if n <= 1:
        return lst

    # 기준 정하기 ; 맨 앞 값으로 정함
    pivot = lst[0]
    
    # p1 ; 피벗보다 작은 값, p2 ; 피벗보다 큰 값
    p1 = []
    p2 = []
    
    # 피벗 제외한 범위 돌기
    for i in range(1,n):
        # 피벗과 비교해 값 크면 p2, 작으면 p1에 추가
        if lst[i] > pivot:
            p2.append(lst[i])
        else:
            p1.append(lst[i])
	
    # p1, p2 다시 퀵소트 시키고 피벗은 가운데 위치하도록 만들어서 리턴 
    return quickSort(p1) + [pivot] + quickSort(p2)
```



- Hoare-Partition 알고리즘 (호어 분할 알고리즘)

```
1. 피봇 값보다 큰 값들은 오른쪽, 작은값들은 왼쪽에 위치 시킴
2. 피봇 값을 두 집합의 가운데에 위치 (i, j가 교차했을 때 피봇 <-> j 위치 swap)

```



```python
def quickSort(lst, start, end):

    # 시작 인덱스가 끝보다 같거나 크다면 (배열 길이 1) 리턴
    if start >= end:
        return lst

    # 피봇값 : 맨 앞, left (앞에서부터) ; 피봇 다음, right (뒤에서부터) ; 끝
    pivot = start
    left = start+1
    right = end

    # 앞에서부터 센 인덱스가 뒤에서부터 세는 인덱스보다 작거나 같을 때만! 
    while left <= right:
        
        # left 인덱스가 범위 안에 있고, left 인덱스 값이 피봇보다 작으면 (바꿀거 없음) 
        # 인덱스 + 1 해주면서 피봇보다 큰 값 찾기.. 찾으면 멈춘다
        while left <= end and lst[left] <= lst[pivot]:
            left += 1

        # right 인덱스가 범위 안에 있고, right 인덱스 값이 피봇보다 크면
        # 인덱스 -1 해주면서 피봇보다 작은값 찾기
        while right > start and lst[right] >= lst[pivot]:
            right -= 1

        # left 인덱스가 right보다 클 때 (교차함)
        # right 인덱스 값과 피봇 값 바꿔주기
        if left > right:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            # 그게 아니라면 left, right 값 바꿔주기
            lst[left], lst[right] = lst[right], lst[left]
	
    # 정렬되었다면 정렬된 앞부분 (피봇보다 작은 값들), 정렬된 뒷부분 (피봇보다 큰 값들)
    # 반복해가면서 정렬시키기
    quickSort(lst, start, right-1)
    quickSort(lst, right+1, end)
```



- Lomuto partition 알고리즘 (로무토 분할 알고리즘)

```python
''' Python3 implementation QuickSort using Lomuto's partition
Scheme.'''
 
''' This function takes last element as pivot, places
the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot '''
def partition(arr, low, high):
     
    # pivot
    pivot = arr[high]
     
    # Index of smaller element
    i = (low - 1)
    for j in range(low, high):
         
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
             
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
     
''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''
def quickSort(arr, low, high):
    if (low < high):
         
        ''' pi is partitioning index, arr[p] is now    
        at right place '''
        pi = partition(arr, low, high)
         
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
         
''' Function to print an array '''
def printArray(arr, size):
     
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
# Driver code
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)

```

