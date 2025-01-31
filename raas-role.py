AWSTemplateFormatVersion: '2010-09-09'
Resources:
  EC2ServiceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: MyEC2ServiceRole
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: "sts:AssumeRole"

  LambdaServiceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: MyLambdaExecutionRole
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: "sts:AssumeRole"

Outputs:
  EC2RoleARN:
    Description: "ARN of the EC2 Service Role"
    Value: !GetAtt EC2ServiceRole.Arn

  LambdaRoleARN:
    Description: "ARN of the Lambda Execution Role"
    Value: !GetAtt LambdaServiceRole.Arn
