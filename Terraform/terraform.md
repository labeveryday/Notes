# Hashicorp - Terraform Notes

Find documentation here
- https://learn.hashicorp.com/tutorials/terraform/install-cli
- ACI provider: 
    - https://registry.terraform.io/providers/CiscoDevNet/aci/latest/docs

Understanding Terraform
- Provides the ability for Infrastructure as code.
- Declarative, machine-readable definition files
- Executable documentation
- Enables collaboration
- Safe and predictable
- Safely and predictably make infrastructure changes

***

### Mac Install
- Install HashiCorp tap, this is a repo of all HashiCorp Homebrew packages
```lang-bash
brew tap hasicorp/tap
```
- Now install Terraform 
```
brew install hashicorp/tap/terraform
```
- Update Terraform
```
brew upgrade hashicorp/tap/terraform
```

***

### Terraform Commands
Validate Terraform
```
terraform validate
```

precommit validation
```
pre-commit run --all-files
```

Rewrites pre-0.13 module source code for v0.13
- You may have to update your terraform depending on the provider.
```
terraform 0.13upgrade
```


Initialize a Terraform working directory
```
terraform init
```

Generate and show an execution plan
```
terraform plan
```

Builds or changes infrastructure
```
terraform apply
```
