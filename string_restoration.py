t = input()
for i in range(0,t):
    n = input()
    a = map(int, raw_input().split())
    if a[0] != 1:
        print("-1")
        continue
    ans = "a"
    all_char = "abcdefghijklmnopqrstuvwxyz"
    pos = 0
    flag = 1
    for i in range(1, n):
        if a[i] - a[i - 1] < 0 or a[i] - a[i - 1] > 1:
            flag = 0
            break
        if a[i] == a[i - 1]:
            ans += "a"
        else:
            if pos == 25:
                flag = 0
                break
            pos = pos + 1
            ans += all_char[pos]
    if flag == 1:
        print(ans)
    else:
        print(-1)
            
    
