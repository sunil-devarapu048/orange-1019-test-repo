AWSTemplateFormatVersion: '2010-09-09'
Resources:
  AttachPoliciesToEC2Role:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: AttachPoliciesToEC2
      Roles:
        - MyEC2ServiceRole  # Ensure this role already exists
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action:
              - s3:ListBucket
              - s3:GetObject
            Resource: "*"

  AttachPoliciesToLambdaRole:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: AttachPoliciesToLambda
      Roles:
        - MyLambdaExecutionRole  # Ensure this role already exists
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action:
              - logs:CreateLogGroup
              - logs:CreateLogStream
              - logs:PutLogEvents
            Resource: "*"

  EC2AttachManagedPolicies:
    Type: AWS::IAM::RolePolicyAttachment
    Properties:
      RoleName: MyEC2ServiceRole
      PolicyArn: arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess  # AWS managed policy

  LambdaAttachManagedPolicies:
    Type: AWS::IAM::RolePolicyAttachment
    Properties:
      RoleName: MyLambdaExecutionRole
      PolicyArn: arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole  # AWS managed policy
