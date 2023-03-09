import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Trusted
CustomerTrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi-project",
    table_name="customer_trusted",
    transformation_ctx="CustomerTrusted_node1",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1678178807338 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi-project",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1678178807338",
)

# Script generated for node Inner join after distinct
SqlQuery0 = """
SELECT c.*
FROM customer_trusted c 
JOIN 
    (
    SELECT DISTINCT user FROM accelerometer_trusted
    ) AS a 
ON c.email = a.user;
"""
Innerjoinafterdistinct_node1678178825568 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={
        "customer_trusted": CustomerTrusted_node1,
        "accelerometer_trusted": AccelerometerTrusted_node1678178807338,
    },
    transformation_ctx="Innerjoinafterdistinct_node1678178825568",
)

# Script generated for node Customer Curated
CustomerCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=Innerjoinafterdistinct_node1678178825568,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-project3/customers/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="CustomerCurated_node3",
)

job.commit()