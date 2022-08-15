from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('ec_2/', views.ec_2, name='blog-ec_2'),
    path('elastic_beanstalk/', views.elastic_beanstalk, name='blog-elastic_beanstalk'),
    path('lambda_serverless/', views.lambda_serverless, name='blog-lambda_serverless'),
    path('api_gateway/', views.api_gateway, name='blog-api_gateway'),
    path('route_53/', views.route_53, name='blog-route_53'),
    path('dynamo_db/', views.dynamo_db, name='blog-dynamo_db'),
    path('rds/', views.rds, name='blog-rds'),
    path('s3/', views.s3, name='blog-s3'),
    path('kinesis/', views.kinesis, name='blog-kinesis'),
    path('ecs_fargate/', views.ecs_fargate, name='blog-ecs_fargate'),
    path('iam/', views.iam, name='blog-iam'),
    path('cloudformation/', views.cloudformation, name='blog-cloudformation'),
    path('kms/', views.kms, name='blog-kms')
]
