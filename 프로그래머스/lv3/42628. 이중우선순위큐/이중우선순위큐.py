class DoublePriorityQueue():
    def __init__(self):
        self.queue = []
    
    def insert(self, value):
        self.queue.append(value)
        self.queue.sort()
        
    def del_max(self):
        self.queue.pop(len(self.queue) - 1)
        
    def del_min(self):
        self.queue.pop(0)
        
    def is_empty(self):
        return True if len(self.queue) == 0 else False
    
    def get_list(self):
        return self.queue

def solution(operations):
    
    dpq = DoublePriorityQueue()
    
    for orders in operations:
        order, num = orders.split(' ')
        num = int(num)
        
        if order == "I":
            dpq.insert(num)
        elif num == 1 and not dpq.is_empty():
            dpq.del_max()
        elif num == -1  and not dpq.is_empty():
            dpq.del_min()
            
    # print(dpq.get_list())
    # print(dpq.is_empty())
    
    answer = []
    
    
    if dpq.is_empty():
        print('empty')
        answer = [0, 0]
    else:
        dpq_list = dpq.get_list()
        answer = [dpq_list[len(dpq_list) - 1], dpq_list[0]]
    
    return answer