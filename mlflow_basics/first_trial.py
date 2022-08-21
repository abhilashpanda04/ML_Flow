import mlflow

def calculate_nthpower(x,n):
    return x**n

if __name__=='__main__':
    

    with mlflow.start_run():
        x,n=8,4
        y=calculate_nthpower(x,n)
        mlflow.log_param('x',x)
        mlflow.log_param('n',n)
        mlflow.log_metric('y',y)

