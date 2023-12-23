from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput, S3Backend

# from cdktf_cdktf_provider_aws import AwsProvider
from imports.aws.provider import AwsProvider


# from imports.aws import S3Backend, DynamoDBTable
from imports.aws.dynamodb_table import DynamodbTable
from imports.aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="ap-southeast-2")

        # create resources
        s3_backend_bucket = S3Bucket(
            self,
            "s3_backend_bucket",
            bucket="cdktf-s3-as-backend-state",
        )

        dynamodb_lock_table = DynamodbTable(
            self,
            "dynamodb-lock-table",
            name="cdktf-s3-as-backend-state-lock",
            hash_key="LockID",
            attribute=[{"name": "LockID", "type": "S"}],
            billing_mode="PAY_PER_REQUEST",
        )

        # Output the resource ids for reference
        TerraformOutput(self, "bucket-id", value=s3_backend_bucket.id)
        TerraformOutput(self, "bucket", value=s3_backend_bucket.bucket)
        TerraformOutput(self, "dynamo-table-id", value=dynamodb_lock_table.id)

        s3_backend = S3Backend(
            self,
            bucket="cdktf-s3-as-backend-state",
            key="s3-as-backend.tfstate",
            region="ap-southeast-2",
            encrypt=True,
            dynamodb_table="cdktf-s3-as-backend-state-lock",
        )

        # Configure the backend.
        # self.add_override("terraform.backend", {"s3": s3_bucket.get_backend()})
        # self.add_override("terraform.required_version", ">= 0.14")
        # self.add_override("terraform.lock", {"dynamodb": dynamodb_table.get_lock()})
        # s3_backend.add_override("depends_on", [s3_backend_bucket.fqn])


app = App()
MyStack(app, "s3-as-backend")
app.synth()
