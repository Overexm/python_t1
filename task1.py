def combination(arr,s1=''):
    if len(arr) ==  0:
        print(s1)
    
    for i in range(len(arr)):
      L=s1+arr[i]
      S=arr[0:i]+arr[i+1:]
      combination(S,L)
        
        
permu=['a','b','c']
combination(permu)