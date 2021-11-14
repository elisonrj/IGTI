# Comentário para modificar o arquivo testar validação do terraform
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciceSpark")
    .getOrCreate()
)

# Ler os dados do enem2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter",";")
    .load("s3://datalake-elison-igti-edc/raw-data/enem/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-elison-igti-edc/staging/enem")
)