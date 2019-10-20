class Solution:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0
        self.arr = input_array
        self.length=len(input_array)

    def Merge(self, p, q, r):
        n1 = q - p + 1
        n2 = r - q 
        L=[]
        R=[]
        for i in range(0, n1):
            L.append(self.sorting_array[p + i])
        for j in range(0, n2):
            R.append(self.sorting_array[q + 1 + j])

        i = 0
        j = 0
        L.append(float("inf"))
        R.append(float("inf"))
        for k in range(p, r+1):
            if (L[i] <= R[j]):
                self.sorting_array[k] = L[i]
                i += 1
                self.comparison_count +=1
            else:
                self.sorting_array[k] = R[j]
                j += 1
                self.comparison_count +=1

    def merge_sort(self, p, r):
        if (p < r):
            q=((p+r)//2)
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            self.Merge(p, q, r)

    def build_max_heap(self):
        length = (len(self.arr) - 1)/2
        i=int(length)
        while (i>=0):
                self.max_heapify(i)
                i=i-1

    def max_heapify(self,i):
        left_child=2*i+1
        right_child=2*i+2
        if(left_child < self.length ):
            self.comparison_count=self.comparison_count+1
        if (right_child < self.length):
            self.comparison_count=self.comparison_count+1

        if (left_child < self.length and self.arr[left_child] > self.arr[i]):
            largest = left_child
        else :
            largest = i
        if (right_child < self.length and self.arr[right_child] > self.arr[largest]):
            largest = right_child
        if (largest != i):
            self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
            self.max_heapify(largest)

    def heap_sort(self):
        sor=[0] * self.length
        self.build_max_heap()
        i=self.length - 1
        while (i >= 1):
            self.arr[i],self.arr[0] = self.arr[0],self.arr[i]
            sor[i]=self.arr[i]
            del(self.arr[i])
            i=i-1
            self.length=self.length - 1
            self.max_heapify(0)
        sor[i]=self.arr[i]
        self.sorting_array=sor 

          
    def insertion_sort(self):
        arr=self.sorting_array 
        count = 0
        for j in range (1, len(arr)):
            key=arr[j]
            i=j-1
            while (i>=0):
                if (arr[i]>key):
                    arr[i+1]=arr[i]
                    i=i-1
                    count = count + 1
                else:
                    count = count + 1
                    break
            arr[i+1]=key   
        self.sorting_array = arr
        self.comparison_count = count
        
