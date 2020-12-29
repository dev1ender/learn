def solution(S):
    # write your code in Python 3.6
    result = ''
    counter = 1
    S = S.replace(' ','')
    S = S.replace('-','')
    for index,ch in enumerate(S):
        if(counter == 3 and len(S)- index > 3 ):
            counter = 1
            result += ch+'-'
        elif(len(S) - index == 4):
            result += S[-4:-2]+'-'+S[-2:]
            break
        else:
            result += ch
            counter += 1
    return result

def vertex(N , A ,B):
    arr = list(zip(A,B))
    obj = {}
    for item in arr:
        print(obj)
        if item[0] in obj:
            print(obj[item[0]])
            obj[item[0]] = list(obj[item[0]]).append(item[1])
        else:
            obj[item[0]] = [item[1]]
        if item[1] in obj:
            obj[item[1]] = list(obj[item[1]]).append(item[0])
        else:
            obj[item[1]] = [item[0]]
    # print(obj)
    seq = list(set(A+B))
    # print(arr,seq)
    
result =  vertex(4,[1,2,1,3],[2,4,3,4])
# print(result)
