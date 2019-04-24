a = []
b = []
c = []
dp = [[ [-1 for col in range(200)] for col in range(200)] for row in range(200)] 
def calc(cur, gold, platinum, x, y, z, n):
    if cur == n:
        return 0
    if dp[cur][gold][platinum] != -1:
        return dp[cur][gold][platinum]
    ans = 0
    diamond = cur - gold - platinum
    if gold < x:
        ans = max(ans , a[cur] + calc(cur + 1 , gold + 1, platinum, x , y , z , n))
    if platinum < y:
        ans = max(ans , b[cur] + calc(cur + 1 , gold, platinum + 1, x , y , z , n))
    if diamond < z:
        ans = max(ans , c[cur] + calc(cur + 1 , gold, platinum, x , y , z , n))
    
    dp[cur][gold][platinum] = ans
    return ans


n = input()
x,y,z = map(int, raw_input().split())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(0, n):
    a[i],b[i],c[i] = map(int, raw_input().split())

print calc(0, 0, 0, x, y, z, n)

