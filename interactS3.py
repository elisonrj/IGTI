import boto3
import pandas as pd
import openpyxl

#Criar um cliente um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-elison-igti-edc",
                        "data/inventario.xlsx",
                        "data/inventario.xlsx")

df = pd.read_excel("data/inventario.xlsx")
print(df)

s3_client.upload_file("data/sample.csv",
                    "datalake-elison-igti-edc",
                    "data/sample.csv")

