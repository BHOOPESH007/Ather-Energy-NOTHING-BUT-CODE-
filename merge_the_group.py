def merge_the_group(size, array, query_size, query_list):
    groupToArray= [[i] for i in array]
    for one in query_list:
        if one[0]==1:
            X=one[1]
            Y=one[2]
            groupToArray[Y-1], groupToArray[X-1] = groupToArray[Y-1]+groupToArray[X-1], groupToArray[Y-1]+groupToArray[X-1]
        elif one[0]==2:
            X=one[1]
            print max(groupToArray[X-1])-min(groupToArray[X-1])

N=input()
array=map(int, raw_input().split(' '))
query_size=input()
query_list=[]
for i in range(query_size):
    query=map(int, raw_input().split(' '))
    query_list.append(query)
    
merge_the_group(N, array, query_size, query_list)
