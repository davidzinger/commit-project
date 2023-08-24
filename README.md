1)manual actions required:
- restarting eks-stack in cloudformation requaire modifing "kubectl edit -n kube-system configmap/aws-auth" based on doc/kubeconfig.yaml file.

- role file in cloudformation dir and role KUBECTLeksROLE mantioned in doc/roles: manual lunch before pipeline created,(can be added to deploy infrastructre stage in pipeline).

2)resources:
 - ecr: commit-project-image, trafex/php-nginx.
 - vpc: eks-vpc-VPC
 - eks: my-eks-cluster
 - codecommit: commit-repo-git
 - pipeline: commit-pipe
 - roles: mentioned in doc/roles 
 - rds: database-1

3)description: 2 mission:
- the entire code is stored in codecommit.
- codepipeline deploying infrastructre(vpc and eks) via cloudformation, stacks files located in cloudformation-stacks
- eks loadbalncerurl: https://a9afdffe157f34675aa22076d878c1c4-2146649501.us-east-1.elb.amazonaws.com/ (image latest.75aaa919...random numbers, rds database-1)

4)1 mission: ecs loadbalncerurl: https://new-alb-1756785036.us-east-1.elb.amazonaws.com/ (image latest, rds database-commit-rds)


5)left to do:
- configure ssl in image.
- add test stage with ec2 modifing "kubectl edit -n kube-system configmap/aws-auth" based on doc/kubeconfig.yaml file.
- give buildproject a custom image with my requirements(js,awscli). 
- work with one rds via cloudformation with backup for recreation (backup is adds expensives).