from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def ec_2(request):
    return render(request, 'blog/ec_2.html', {'title': 'EC2 - Elastic Compute Cloud'})

def ecs_fargate(request):
    return render(request, 'blog/ecs_fargate.html', {'title': 'ECS + Fargate'})

def elastic_beanstalk(request):
    return render(request, 'blog/elastic_beanstalk.html', {'title': 'Elastic Beanstalk'})

def lambda_serverless(request):
    return render(request, 'blog/lambda.html', {'title': 'Lambda'})

def api_gateway(request):
    return render(request, 'blog/api_gateway.html', {'title': 'Api Gateway'})

def route_53(request):
    return render(request, 'blog/route_53.html', {'title': 'Route 53'})

def dynamo_db(request):
    return render(request, 'blog/dynamo_db.html', {'title': 'DynamoDB'})

def rds(request):
    return render(request, 'blog/rds.html', {'title': 'RDS'})

def s3(request):
    return render(request, 'blog/s3.html', {'title': 'S3'})

def vpc(request):
    return render(request, 'blog/vpc.html', {'title': 'VPC'})

def ecs_fargate(request):
    return render(request, 'blog/ecs_fargate.html', {'title': 'ECS - Fargate'})

def iam(request):
    return render(request, 'blog/iam.html', {'title': 'IAM'})

def cloudformation(request):
    return render(request, 'blog/cloudformation.html', {'title': 'CloudFormation'})

def kinesis(request):
    return render(request, 'blog/kinesis.html', {'title': 'Kinesis'})

def kms(request):
    return render(request, 'blog/kms.html', {'title': 'KMS'})
