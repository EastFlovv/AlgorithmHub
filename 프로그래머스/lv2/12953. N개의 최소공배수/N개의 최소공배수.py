def gcd(num1, num2):
    n1 = num1
    n2 = num2
    
    while(True):
        rest = n1 % n2
        if rest == 0:
            break
        n1 = n2
        n2 = rest
    return n2

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)

def solution(arr):
    
# 모든 수를 차례대로 진행하여 앞의 두 수를 최소 공배수로 만든다
# 이를 무한히 진행

    while(len(arr) > 1):
        num1 = arr.pop()
        num2 = arr.pop()
        
        arr.append(lcm(num1, num2))
        
    answer = arr[0]
    return answer