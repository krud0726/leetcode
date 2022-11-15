import collections
class Solution:
    def intToRoman1(self, num: int) -> str:
        l = [(1, 'I'), (5, 'V'),(10, 'X'),(50, 'L'),(100, 'C'),(500, 'D'),(1000, 'M'),
             (4, 'IV'), (9, 'IX'), (40, 'XL'), (90, 'XC'),(400, 'CD'),(900, 'CM')]
        v = collections.defaultdict(list)
        answer = []
        
        
        # 숫자와 문자 맵핑
        for i in l:
            v[i[0]].append(i[1])
        
        # 일의 자리부터 최대 자리 수까지 진행할 수 있도록 리스트 순서 역순으로 변경
        s_num = list(str(num))[::-1]
        
        # 일의 자리부터 최대 자리 수까지 반복 진행
        for index, val in enumerate(s_num):
            
            val = int(val)
            d = (10 ** index)
            s_temp = ''
            
            while val:
                if val <= 3:
                    s_temp += (v[d][0] * val)
                    val = 0
                elif val == 4:
                    s_temp += (v[val * d][0])
                    val = 0
                elif 5 <= val <=8:
                    s_temp += (v[5 * d][0])
                    val = val-5
                else:
                    s_temp += (v[val * d][0])
                    val = 0
                    
            answer.append(s_temp)
        
        return ''.join(answer[::-1])
    
    
    def intToRoman(self, num: int) -> str:
        i=1
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        s=""
        while num!=0:
            y=num%pow(10,i)//pow(10,i-1)
            if y==5:
                s=dic[y*pow(10,i-1)]+s
            elif y==1:
                s=dic[y*pow(10,i-1)]+s
            elif y==4:
                s=dic[1*pow(10,i-1)]+dic[5*pow(10,i-1)]+s
            elif y==9:
                s=dic[1*pow(10,i-1)]+dic[1*pow(10,i)]+s
            elif y<4:
                s=dic[pow(10,i-1)]*y+s
            elif y>5 and y<9:
                y-=5
                s=dic[5*pow(10,i-1)]+dic[pow(10,i-1)]*y+s
            num=num//pow(10,i)
            num*=pow(10,i)
            i+=1
        return s