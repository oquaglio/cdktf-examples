import inspect
import pytest
from cdktf import Testing
from cdktf import App, TerraformStack

# The tests below are example tests, you can find more information at
# https://cdk.tf/testing


class TestMain:

    def test_my_app(self):
        assert True

    stack = TerraformStack(Testing.app(), "stack")
    #app_abstraction = MyApplicationsAbstraction(stack, "app-abstraction")
    synthesized = Testing.synth(stack)
    print(synthesized)
    print(type(synthesized))
    print(type(stack))
    print(dir(synthesized))
    print(dir(stack))
    print(stack.to_string())
    print(stack.depends_on)
    print(stack.dependencies)
    print(getattr(stack, "depends_on"))


    # Print information about the class's constructor
    sig = inspect.signature(TerraformStack.__init__)
    for param in sig.parameters.values():
        print(f"{param.name}: {param.default}")

    # Print information about the class's methods
    for name, member in inspect.getmembers(TerraformStack, inspect.ismethod):
        if name != "__init__":
            print(f"{name}: {member.__doc__}")

    # def test_should_contain_container(self):
    #    assert Testing.to_have_resource(self.synthesized, Container.TF_RESOURCE_TYPE)

    # def test_should_use_an_ubuntu_image(self):
    #    assert Testing.to_have_resource_with_properties(self.synthesized, Image.TF_RESOURCE_TYPE, {
    #        "name": "ubuntu:latest",
    #    })

    def test_check_validity(self):
       assert Testing.to_be_valid_terraform(Testing.full_synth(stack))
