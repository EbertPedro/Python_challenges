# The general form of the Lambda function is:
# name_lambda = lambda parameters(x,y,..): Evaluation_return_value(x,y,..)

#Whith def funcion
def double(x):
    return 2 * x

#With lambda function
double_lambda = lambda x : 2 * x

double_func = double(4)
lambda_func = double_lambda(4)
print(double_func, lambda_func)

def max_xy(x, y):
    if x > y:
        return x
    else:
        return y

max_lambda = lambda x,y: x if x > y else y
print(max_xy(2,12), max_lambda(2,12))