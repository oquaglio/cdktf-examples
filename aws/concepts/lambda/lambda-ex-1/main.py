from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
import zipfile, os

# from imports.aws.vpc import Vpc
from imports.terraform_aws_modules.aws import Vpc
from imports.aws.lambda_function import LambdaFunction
from imports.aws.s3_bucket import S3Bucket
from imports.aws.sns_topic import SnsTopic
from imports.aws.lambda_function import LambdaFunction
from imports.aws.iam_role import IamRole


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "Aws", region="ap-southeast-2")

        Vpc(
            self,
            "CustomVpc",
            name="cdktf-examples-lambda-ex-1-vpc",
            cidr="10.0.0.0/16",
            azs=["ap-southeast-2a", "ap-southeast-2b"],
            public_subnets=["10.0.1.0/24", "10.0.2.0/24"],
        )
        SnsTopic(self, "Topic", display_name="cdktf-examples-lambda-ex-1-sns-topic")
        role = IamRole(
            self,
            "Role",
            name="cdktf-examples-lambda-ex-1-lambda-role",
            assume_role_policy="""{
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "sts:AssumeRole",
                            "Principal": {
                                "Service": "lambda.amazonaws.com"
                            },
                            "Effect": "Allow",
                            "Sid": ""
                        }
                    ]
                }""",
        )

        # Specify the source directory containing your Lambda function code
        source_directory = "lambda-code"

        # Specify the output file path for the ZIP file
        output_zip_file = "lambda-code/lambda_function.zip"

        # Create a ZIP file containing the Lambda function code
        with zipfile.ZipFile(output_zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Recursively add all files and subdirectories in the source directory to the ZIP file
            for root, dirs, files in os.walk(source_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, source_directory))

        LambdaFunction(
            self,
            "Lambda",
            function_name="cdktf-examples-lambda-ex-1-lambda-function",
            role=role.arn,
            handler="index.handler",
            runtime="python3.6",
            filename=output_zip_file,
        )


app = App()
MyStack(app, "cdktf-examples-lambda-ex-1")

app.synth()
