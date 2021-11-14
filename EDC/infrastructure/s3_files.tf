resource "aws_s3_bucket_object" "job_spark" {
  bucket = aws_s3_bucket.dl
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl   = "private"
  source = "../jobs/job_emr_spark.py"
  etag   = filemd5("../jobs/job_emr_spark.py")
}