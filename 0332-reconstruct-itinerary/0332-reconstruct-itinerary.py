class Solution:
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        result = []
        
        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            
            result.append(a)
            
        dfs('JFK')
        
        # 다시 뒤집어 어휘순 결과로
        return result[::-1]
    
    
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 그래프 순서대로 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        result = []
        
        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop())
            
            result.append(a)
            
        dfs('JFK')
        
        # 다시 뒤집어 어휘순 결과로
        return result[::-1]
    
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        result, stack = [], ['JFK']
        
        while stack:
            #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            
            result.append(stack.pop())
        
        # 다시 뒤집어 어휘순 결과로
        return result[::-1]