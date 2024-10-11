def generate_parenthesis(num):
    result=[]
    def solve(op,clo,current,n):
        if op==n and clo==n:
            result.append(current)
            return
        if op<n:
            current=current+"("
            solve(op+1,clo,current,n)
        if op>clo:
            current=current+")"
            solve(op,clo+1,current,n)

    solve(0,0,"",num)
    return result

nb=3
print(generate_parenthesis(nb))


'''
op=["(","[","{"]
clo=[")","]","}"]
op[0]==clo[0]
then true
'''