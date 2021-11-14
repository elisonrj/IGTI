provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle do estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti"
    key    = "state/igti/edc/terraform.tfstate"
    region = "us-eats-2"
  }
}