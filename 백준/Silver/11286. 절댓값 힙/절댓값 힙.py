import sys

def heapify_up(parent_idx, child_idx):
    if parent_idx < 1: return
    
    # 부모노드가 더 크면 swap
    if abs(heap[parent_idx]) > abs(heap[child_idx]):
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

        heapify_up(parent_idx // 2, parent_idx)
    # 절대값이 같은 경우
    elif abs(heap[parent_idx]) == abs(heap[child_idx]):
        if heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            heapify_up(parent_idx // 2, parent_idx)

    return

def heapify_down(parent_idx, child_idx):
    if child_idx >= len(heap): return

    # 왼쪽 자식이 마지막 노드일 경우
    if child_idx == len(heap) - 1:
        if (abs(heap[child_idx]) < abs(heap[parent_idx])):
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            heapify_up(parent_idx // 2, parent_idx)
        # 절대값이 같은 경우
        elif abs(heap[parent_idx]) == abs(heap[child_idx]):
            if heap[parent_idx] > heap[child_idx]:
                heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
                heapify_up(parent_idx // 2, parent_idx)
        return
    # 왼쪽 자식이 더 작은 경우
    if (abs(heap[child_idx]) < abs(heap[child_idx + 1])):
        if(abs(heap[child_idx]) < abs(heap[parent_idx])):
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            heapify_down(child_idx, child_idx * 2)
        # 절대값이 같은 경우
        elif abs(heap[parent_idx]) == abs(heap[child_idx]):
            if heap[parent_idx] > heap[child_idx]:
                heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
                heapify_down(child_idx, child_idx * 2)
    # 오른쪽 자식이 더 작은 경우
    elif (abs(heap[child_idx]) > abs(heap[child_idx + 1])):
        if (abs(heap[child_idx + 1]) < abs(heap[parent_idx])):
            heap[parent_idx], heap[child_idx + 1] = heap[child_idx + 1], heap[parent_idx]
            heapify_down(child_idx + 1, (child_idx + 1) * 2)
        # 절대값이 같은 경우
        elif abs(heap[parent_idx]) == abs(heap[child_idx + 1]):
            if heap[parent_idx] > heap[child_idx + 1]:
                heap[parent_idx], heap[child_idx + 1] = heap[child_idx + 1], heap[parent_idx]
                heapify_down(child_idx + 1, (child_idx + 1) * 2)
    # 왼쪽과 오른쪽 자식의 절대값이 같은 경우
    elif (abs(heap[child_idx]) == abs(heap[child_idx + 1])):
        if(heap[child_idx] < heap[child_idx + 1]):
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            heapify_down(child_idx, child_idx * 2)
        else:
            heap[parent_idx], heap[child_idx + 1] = heap[child_idx + 1], heap[parent_idx]
            heapify_down(child_idx + 1, (child_idx + 1) * 2)
            


def insert_min_heap(number):
    heap.append(number)

    if(len(heap) == 2): return # 요소가 1개일 때 heapify 할 필요 없음
    heapify_up(int((len(heap) - 1) / 2), len(heap) - 1)
        
def delete_min_heap():
    return_num = heap[1]
    heap[1], heap[len(heap) - 1] = heap[len(heap) - 1], heap[1] # 마지막 요소를 탑과 교환
    heap.pop() # 마지막 요소 제거
    
    if len(heap) > 2:
        heapify_down(1, 2)
        return return_num
    else: return return_num # 요소가 1개 이하일 때 heapify 할 필요 없음
    

N = int(input())

global heap
heap = []
heap.append(0) # 헷갈리니까 더미값 넣어서 인덱스 시작을 1로 계산
result = []

for _ in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(heap) == 1:
            result.append(0)
        else:
            # pop
            result.append(delete_min_heap())
    else:
        # push
        insert_min_heap(command)
        

for i in result:
    print(i)