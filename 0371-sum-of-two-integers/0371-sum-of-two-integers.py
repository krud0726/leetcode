class Solution:
    def getSum1(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        
        result = []
        carry = 0
        sum = 0
        
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            #print("A / B : ", A, " / ", B)
            
            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            
            sum = Q2 ^ carry
            carry = Q1 | Q3
            
            result.append(str(sum))
        
        # 마지막 캐리가 1이면 1을 추가해서 붙인다. (32자리 초과)
        if carry == 1:
            result.append('1')
            
        # 초과 자릿 수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        
        # 음수 처리
        # 파이썬은 기본적으로 음수를 표현할 때, 기존의 다른 언어들과 다르게 이진수에 -(음수 기호)를 붙여 표현한다.
        # 하지만, 비트 연산(&, |, ^, ~)을 수행할 때에는 -(음수 기호)를 붙여 표현하는 것이 아닌 2의 보수를 취하여 계산한다.
        # 또한, 비트연산을 취할 때, -(음수 기호)를 사용한 비트를 취하든 2의 보수를 취하든 비트 연산의 결과는 같다.
        # 즉, 정리하면 기본적으로 파이썬은 비트를 계산할 때, 양수로 계산을 하기 때문에 비트 연산을 일부러 취하여 2의 보수 즉, 음수로 표현하는 것이다.
        # 만약, 비트 연산을 취하지 않을 경우에는 모든 값을 양수로 표현하게 될 것이다.
        # 음수를 나타내기 위해서 비트연산을 취할 뿐 다른 이유는 없다.
        if result > INT_MAX:
            result = ~(result ^ MASK)
            
            
        return result
    
    
    
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        # 자리 올림수가 0이 아닐 때까지 반복한다.
        # a = 각 비트의 합
        # b = 자리가 올려진 carry 값
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)
            
        return a
        