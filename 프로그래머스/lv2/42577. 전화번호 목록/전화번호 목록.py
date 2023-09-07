class node():
    def __init__(self):
        self.next = [None for _ in range(10)]
        self.end = False
        
    def end(self):
        self.end = True

def solution(phone_book):
    
# 인덱스에 따라...
# 한가지만 겹쳐도 접두어가 된다? -> x 단어 전체가 접두어가 되어야함
# 1->1->9->e
    answer = True
    
    phone_dict = {}
    
    # for phone in phone_book:
    #     for i in range(len(phone)):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        # print(f'phone1 = {phone_book[i]}, phone2 = {phone_book[i+1]}')
        if phone_book[i] in phone_book[i+1] and phone_book[i+1].index(phone_book[i]) == 0:
            answer = False
        if not answer:
            break
    
             
    
    
    
    return answer