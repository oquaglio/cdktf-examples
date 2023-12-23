#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.docker.provider import DockerProvider
from imports.docker.container import Container
from imports.docker.image import Image


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        DockerProvider(self, "provider")

        docker_image = Image(self, 'nginx-latest',
                             name='nginx:latest', keep_locally=False)

        Container(self, 'nginx-cdktf', name='nginx-python-cdktf',
                  image=docker_image.name, ports=[
                      {
                          'internal': 80,
                          'external': 8000
                      }], privileged=False)


app = App()
MyStack(app, "basic-example-1")

app.synth()
