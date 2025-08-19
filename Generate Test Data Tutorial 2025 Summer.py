# Databricks notebook source
# MAGIC %md
# MAGIC ## Introduction
# MAGIC
# MAGIC The goal of this notebook is to demonstrate how fake Test Data can be generated using Python. I am using Databricks Free Edition because everyone with a Google or Microsoft account can sign up easily. The notebook and python packages are open source and free, it can be used in any data platform with python notebook capability or run locally on your computer.
# MAGIC
# MAGIC ## Structure of this Tutorial
# MAGIC 1. Short introduction of a Fake Story
# MAGIC 1. Quick introduction of Faker python lirary 
# MAGIC 1. Installation of Faker python library
# MAGIC 1. Quick Test Data Generation
# MAGIC 1. Customized Test Data Generation
# MAGIC 1. Try it yourself Guide
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Fake Story
# MAGIC ODP is producing an animation titled "Liberator of Data", we would like to know more about our talents, examples: number of music composers, hidden talents, etc.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Faker Python Package
# MAGIC Faker is a Python package that generates fake data. <br>
# MAGIC Example use cases: 
# MAGIC - Test Data for Proof of Concept, 
# MAGIC - Data Anonymization.
# MAGIC
# MAGIC [Faker documentation](https://faker.readthedocs.io)
# MAGIC
# MAGIC Install Faker python package:
# MAGIC `%pip install faker`
# MAGIC
# MAGIC Quick Start
# MAGIC ```
# MAGIC from faker import Faker
# MAGIC
# MAGIC # seed integer is to used to make sure same values are generated if run again
# MAGIC Faker.seed(0)
# MAGIC # locale is set to make sure data is in Canadian English format
# MAGIC fake = Faker("en_CA")
# MAGIC ```
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Installation of Faker python package
# MAGIC - click on the "Run cell" button on the top left corner of the cell below.

# COMMAND ----------

# DBTITLE 1,install faker
# MAGIC %pip install faker

# COMMAND ----------

# MAGIC %md
# MAGIC ## Variable
# MAGIC - number of rows to be generated, default is 5:
# MAGIC   - feel free to change it to number of rows that you want to generate.
# MAGIC - click on the "Run cell" button to set the variable.

# COMMAND ----------

# DBTITLE 1,NUMBER_OF_ROWS
# cell 7
NUMBER_OF_ROWS = 5

# COMMAND ----------

# MAGIC %md
# MAGIC ## Quick Test Data Generation
# MAGIC Faker python package provides a quick method called profile() to generate a list of user profiles.
# MAGIC
# MAGIC spark.createDataFrame() is used to store the generated Test Data in memory.
# MAGIC Data can be downloaded as csv or excel by clicking the button at the bottom of result.
# MAGIC
# MAGIC Or, data can be stored in Unity Catalog as delta table (not shown in this notebook).
# MAGIC
# MAGIC Click on the "Run cell" button on the top left corner of cell below to generate test data.

# COMMAND ----------

# DBTITLE 1,fake.profile()
from faker import Faker

Faker.seed(0)
fake = Faker("en_CA")

data = [fake.profile() for _ in range(NUMBER_OF_ROWS)]

df = spark.createDataFrame(data=data)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Customized Test Data Generation
# MAGIC The cell below contains python code to generate Test Data based on the requirements below:
# MAGIC
# MAGIC | Seq | Columns | Meaning | Example |
# MAGIC | :------- | :------: | -------: | -------: |
# MAGIC | 1 | Member_ID | Unique Identifier prefix with MID and six numeric from 111111 to 999999 | MID123456 |
# MAGIC | 2 | Role | 5% of chance = Director <br> 15% of chance = Music Composer <br> 20% of chance = Background Artist <br> 30% of chance = Character Design <br> 30% of chance = Voice Acting | Voice Acting |
# MAGIC | 3 | User_Name | Random Unique name without space | dhzoey |
# MAGIC | 4 | First_Name | Random Canadian English First Name | Celine |
# MAGIC | 5 | Last_Name | Random Canadian English Last Name | Myers |
# MAGIC | 6 | Birth_Date | Birth Date between Age of 18 to 65 as of this year | 1982-07-02 |
# MAGIC | 7 | SIN | Random 9 digit numeric mimic Canadian SIN | 774 564 306 |
# MAGIC | 8 | Pronounce | Random selection of either "He/Him", "She/Her", "They/Them" | They/Them |
# MAGIC | 9 | Dream_Job | Random occupation name | Fashion designer |
# MAGIC | 10 | Start_Date | A random date from yesterday to 10 years ago | 2023-08-15 |
# MAGIC | 11 | Phone_Number | A random fake Canadian phone number | (492) 411-5781 x565 |
# MAGIC | 12 | Mailing_Address | A random fake Canadian address | 408 Christopher Ville Suite 097 Johnmouth, SK J3K 9K8 |
# MAGIC | 13 | Office_Address | Random Street Address, <br> Random selection of either "Toronto", "Vaughan", or "Guelph", <br> Harcoded ON as province, <br> Random Postal Code | 58714 Mann Plaza, Toronto ON Y2M 7T6 |
# MAGIC
# MAGIC spark.createDataFrame() is used to store the generated Test Data in memory as spark DataFrame format.
# MAGIC Data can be downloaded as csv or excel by clicking the button at the bottom of result.
# MAGIC
# MAGIC Or, data can be stored in Unity Catalog as delta table (not shown in this notebook).
# MAGIC
# MAGIC Click on the "Run cell" button on the top left corner of cell below to generate test data.

# COMMAND ----------

# DBTITLE 1,Generate custom Test Data
from faker import Faker
from collections import OrderedDict

Faker.seed(0)
fake = Faker("en_CA")

schema=[
    "Member_ID",
    "Role",
    "User_Name",
    "First_Name",
    "Last_Name",
    "Birth_Date",
    "SIN",
    "Pronounce",
    "Dream_Job",
    "Start_Date",
    "Phone_Number",
    "Mailing_Address",
    "Office_Address",
]

prefix_mID = 'MID'
pronouce_choices = [("He/Him"), ("She/Her"), ("They/Them")]
role_choices = OrderedDict([
    ("Director", 0.05), 
    ("Music Composer", 0.15), 
    ("Background Artist", 0.20), 
    ("Character Design", 0.30), 
    ("Voice Acting", 0.30)
])
office_choices = OrderedDict([
    ("Toronto", 0.60), 
    ("Vaughan", 0.30), 
    ("Guelph", 0.10), 
])
data = []
for row in range(NUMBER_OF_ROWS):
    data.append(
        (
            prefix_mID + str(fake.unique.random_int(min=111111, max=999999)),
            fake.random_element(role_choices),
            fake.user_name(),
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=18, maximum_age=65),
            fake.ssn(),
            fake.random_element(pronouce_choices),
            fake.job(),
            fake.date_between(start_date='-10y',end_date='-1d'),
            fake.phone_number(),
            fake.address(), 
            "{}, {} ON {}".format(
                fake.street_address(), 
                fake.random_element(office_choices), 
                fake.postcode(),         
            ),
        )
    )
df = spark.createDataFrame(schema=schema,data=data)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Try it yourself Guide
# MAGIC
# MAGIC 1. How many records? Change the value in cell 7 
# MAGIC 1. Define your requirements. Write it down.
# MAGIC 1. In the cell below, change schema to your column names.
# MAGIC 1. In the same cell, change prefix to your own.
# MAGIC 1. In the same cell, change choices.
# MAGIC 1. In the same cell, change date.append() based on your requirement.
# MAGIC    - reference: https://faker.readthedocs.io/en/master/providers.html
# MAGIC 1. Run the cell.
# MAGIC
# MAGIC Example:
# MAGIC 1. Generate 100 rows, update cell 7, ```NUMBER_OF_ROWS = 100```
# MAGIC 1. Example of requirement
# MAGIC    | Seq | Columns | Meaning | Example |
# MAGIC    | :------- | :------: | -------: | -------: |
# MAGIC    | 1 | CID | Unique Identifier prefix with CID and six numeric from 1000 to 5000 | CID4458 |
# MAGIC    | 2 | Company | Random Company Name | Chang-Fisher |
# MAGIC    | 3 | Website | Random URL | https://www.jones.net/ |
# MAGIC    | 4 | IP_Address | Random Public IPv4 Address | 182.253.123.155 |
# MAGIC    | 5 | Geo_Latitude | Random Latitude, centre of 45.44868, within radius of 10.0 | 45.683023 |
# MAGIC    | 6 | Geo_Longitude | Random Longitude, centre of -75.44868, within radius of 10.0 | -73.076634 |
# MAGIC    | 7 | Industry | 30% of chance = Healthcare <br> 20% of chance = Tourism <br> 50% of chance = Manufacturing | Manufacturing |
# MAGIC    | 8 | Established_Date | Random Date between 25 years ago and 1 week ago | 2012-07-18 |
# MAGIC 1. Update schema to
# MAGIC    ```
# MAGIC     schema = [
# MAGIC         "CID",
# MAGIC         "Company", 
# MAGIC         "Website", 
# MAGIC         "IP_Address", 
# MAGIC         "Geo_Latitude", 
# MAGIC         "Geo_Longitude",
# MAGIC         "Industry",
# MAGIC         "Established_Date",
# MAGIC     ]
# MAGIC    ```
# MAGIC 1. Update prefix ```prefix_CID = 'CID'```
# MAGIC 1. Update choices
# MAGIC    ```
# MAGIC     industry_choices = OrderedDict([
# MAGIC         ("Healthcare", 0.30), 
# MAGIC         ("Tourism", 0.20), 
# MAGIC         ("Manufacturing", 0.50), 
# MAGIC     ])
# MAGIC    ```
# MAGIC 1. Update data.append to
# MAGIC    ```
# MAGIC     data.append(
# MAGIC         (
# MAGIC             prefix_CID + str(fake.unique.random_int(min=1000, max=5000)),
# MAGIC             fake.company(),
# MAGIC             fake.url(),
# MAGIC             fake.ipv4_public(),
# MAGIC             fake.coordinate(center=45.44868, radius=10.0),
# MAGIC             fake.coordinate(center=-75.44868, radius=10.0),
# MAGIC             fake.random_element(industry_choices),
# MAGIC             fake.date_between(start_date='-25y', end_date='-1w')
# MAGIC         )
# MAGIC      )
# MAGIC     ```
# MAGIC 1. Click on the "Run cell" button on the top left corner of cell below to generate test data.
# MAGIC 1. Feel free to modify the python code and click on "Run Cell" to learn and experiement.

# COMMAND ----------

# DBTITLE 1,try it out, feel free to modify this cell
from faker import Faker
from collections import OrderedDict

Faker.seed(0)
fake = Faker("en_CA")

schema=[
    "CID",
    "Company", 
    "Website", 
    "IP_Address", 
    "Geo_Latitude", 
    "Geo_Longitude",
    "Industry",
    "Established_Date",
]

prefix_CID = 'CID'
industry_choices = OrderedDict([
    ("Healthcare", 0.30), 
    ("Tourism", 0.20), 
    ("Manufacturing", 0.50), 
])

data = []
for row in range(NUMBER_OF_ROWS):
    data.append(
        (
            prefix_CID + str(fake.unique.random_int(min=1000, max=5000)),
            fake.company(),
            fake.url(),
            fake.ipv4_public(),
            fake.coordinate(center=45.44868, radius=10.0),
            fake.coordinate(center=-75.44868, radius=10.0),
            fake.random_element(industry_choices),
            fake.date_between(start_date='-25y', end_date='-1w')
        )
    )
            
df = spark.createDataFrame(schema=schema,data=data)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## End of the Tutorial
# MAGIC This is the end of the Tutorial, thank you for reading.