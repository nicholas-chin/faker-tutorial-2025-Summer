# Faker-tutorial-2025-Summer
This is a quick tutorial on generating test data using Faker python package, the tutorial python notebook can be ran on different platforms.  One of them is Databricks Free Edition.

# Databricks Free Edition
Signup for Databricks Free Edition, visit https://login.databricks.com/, click on Sign up link at the bottom if you do not have a free account yet.   

# Instruction
1. Download "Generate Test Data Tutorial 2025 Summer.ipynb" to your computer.
   - https://github.com/nicholas-chin/faker-tutorial-2025-Summer/blob/main/Generate%20Test%20Data%20Tutorial%202025%20Summer.ipynb
1. Visit https://login.databricks.com/, Login or Signup Databricks Free Edition.
   - <img width="200" height="300" alt="image" src="https://github.com/user-attachments/assets/09c874dd-6f8e-4b37-b880-ea81ddb819e2" />
4. When you are at Databricks Free Edition _Welcome to Databricks_ page, go to the left menu, click on "Workspace".
   - <img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/ca592920-0301-4931-89d4-0b37850e9915" />
5. Under Workspace, click on "Home".
   - <img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/72fe208d-2329-4119-b959-8aac2fd8b4fe" />
6. Under your email, or on the left of "Share" button, click on the "Three Dot".
   - <img width="600" height="350" alt="image" src="https://github.com/user-attachments/assets/a5bd2c9f-8149-45e2-b25f-0154702b0b7f" />
1. Click on "Import" from the "Three Dot" menu.
   - <img width="600" height="350" alt="image" src="https://github.com/user-attachments/assets/b41a2d4e-1848-46f6-9cb8-38d23619dea0" />
1. Click on "browse" button to select the downloaded python notebook from step 1.
   - <img width="200" height="300" alt="image" src="https://github.com/user-attachments/assets/7040ca6b-784a-41fc-81d8-2b5bbbfc2b6e" />
1. Open the downloaded "Generate Test Data Tutorial 2025 Summer.ipynb" file from step 1.
   - <img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/7cd88294-b1b0-4e95-9044-2f6e6ba34028" />
1. Click on "Import" button to import the python notebook file downloaded from step 1.
   - <img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/88587a81-8d78-4d46-b801-b6f2a4b0e1b2" />
1. Open the imported notebook: "Generate Test Data Tutorial 2025 Summer.ipynb"
   - <img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/623354c5-858f-4bf1-8767-2ce378ba285a" />
1. Click on "Run all cells" button to make sure all the python code is executed, so you can learn from the results.
   - <img width="700" height="1000" alt="image" src="https://github.com/user-attachments/assets/719b88de-41cb-40f9-ad0a-abb1e0b30ea6" />
1. Review and run individual cell as needed.
1. Feel free to modify the python code in cell 13 "Try it out", write it, run it, experiment and have fun!

# Number of Records
You can set the number of records needed at cell 7.

# Playground
Use cell 13 as your playground to experiment different fake providers.

# Download the Test Data
Generated Test Data can be downloaded as csv or excel file, just click on the download button below the table at the bottom of a cell.
- <img width="700" height="900" alt="image" src="https://github.com/user-attachments/assets/8ea3dfa0-1887-42c1-9d41-1c0a23198ec5" />

# Save Test Data in Unity Catalog
Since Test Data is already stored in memory as Spark DataFrame ```spark.createDataFrame(data=data,schema=schema)```, it can be used to stored the data in your own cloud storage and metadata in Unity Catalog easily.
Two steps if using spark SQL:
1. In python spark dataframe, create a temporary view that can be used in spark SQL.
   - ```df.createOrReplaceTempView("v_TestData")```
1. Use spark SQL to create a Unity Catalog table.
   ```
   %sql
   create or replace table catalog1.schema1.test_data1
   as
   select * from v_TestData;
   ```

# Closing
Thanks for reading.


