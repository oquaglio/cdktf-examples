# docker/nginx
Spin up a Docker container for Nginx.


## Setup Python Env
```SH
pyenv version
```
```SH
pyenv local 3.12.11
```
```SH
pip install pipenv
```
Create Virt Env (and install Pipfile deps):
```SH
pipenv install
```
Activate Virt Env:
```SH
pipenv shell
```

## Init
```SH
cdktf init --template="python" --local
```
Activate Virt Env:
```SH
pipenv shell
```
Install project dependencies

```shell
pipenv install
```
Generate CDK for Terraform constructs for Terraform providers and modules used in the project.

```bash
cdktf get
```

Compile and generate Terraform configuration

```bash
cdktf synth
```

The above command will create a folder called `cdktf.out` that contains all Terraform JSON configuration that was generated.

Run cdktf-cli commands

```bash
cdktf diff
cdktf deploy
```
