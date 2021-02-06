from functools import cmp_to_key
def compare(a,b):
        ab = str(a)+str(b)
        ba= str(b)+str(a)
        if ab < ba:
            return 1
        elif ab > ba:
            return -1
        else:
            return 0


letter_cmp_key = cmp_to_key(compare)
def largestNumber(A):
    A = sorted(A, key=letter_cmp_key)
    result = ''
    for item in A:
        result+=str(item)
    print(str(int(result)))
    return str(int(result))
    
largestNumber([0, 0, 0, 0, 0])




