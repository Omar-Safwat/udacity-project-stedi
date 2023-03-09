import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Custormer Trusted
CustormerTrusted_node1677591673926 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-project3/customers/trusted/"]},
    transformation_ctx="CustormerTrusted_node1677591673926",
)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi-project",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Join with Customers
JoinwithCustomers_node2 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustormerTrusted_node1677591673926,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="JoinwithCustomers_node2",
)

# Script generated for node Drop Fields
DropFields_node1677592110191 = DropFields.apply(
    frame=JoinwithCustomers_node2,
    paths=[
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithFriendsAsOfDate",
        "serialNumber",
    ],
    transformation_ctx="DropFields_node1677592110191",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1677573567831 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1677592110191,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-project3/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="AccelerometerTrusted_node1677573567831",
)

job.commit()