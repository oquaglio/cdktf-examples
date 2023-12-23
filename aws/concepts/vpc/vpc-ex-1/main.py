#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws.provider import AwsProvider
from imports.terraform_aws_modules.aws import Vpc


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "Aws", region="ap-southeast-2")

        # define resources here
        Vpc(
            self,
            "CustomVpc",
            name="cdktf-python-aws-vpc-basic-example-1",
            cidr="10.0.0.0/16",
            azs=["ap-southeast-2a", "ap-southeast-2b"],
            public_subnets=["10.0.1.0/24", "10.0.2.0/24"],
        )


app = App()
MyStack(app, "cdktf-python-aws-vpc-ex-1")

app.synth()
