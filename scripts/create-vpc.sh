#!/bin/bash

aws cloudformation create-stack   --region us-east-1   --stack-name eks-vpc   --template-body file://cloudformation-stacks/vpc-stack.yaml
