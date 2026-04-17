def add(x):
    return x+3
def multiply(x):
    return x*2
def composite_function(f,g,x):
    return f(g(x))
num=4
result=composite_function(multiply,add,num)
print("Result:",result)
lambda_result=(lambda x:multiply(add(x)))(num)
print("Result using lambda:",lambda_result)
