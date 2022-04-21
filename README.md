## HealthNet - TigerGraph based Medical triage workflow tool / bot
Healthnet is a medical chat bot useful for triaging and diagnosing various medical conditions. It is built on an extensive Tigergraph database with several analysis queries. This can also be used to build a huge knowledge graph with lab results etc to help doctors arrive at better diagnosis. It can be used for the following

- Better triaging patients based on symptoms and lab results 
- Diagnosing related diseases and disorders
- Referring to specialist doctors based on diagnosis
- Presenting precautions and first

## Architechture
![healthnet](https://user-images.githubusercontent.com/104054493/164450396-9ddff5b9-0c59-417a-8e3c-ce0373cc46c7.png)

## Graph Database schema

<img width="970" alt="Screenshot 2022-04-21 at 6 40 32 AM" src="https://user-images.githubusercontent.com/104054493/164526342-b8d7b4da-2b75-43bc-bf65-9a70015bd3fa.png">

## Usage Instructions

Information to setup the project can be found here [a link](https://github.com/akumar-c/healthnet/blob/main/healthnet.ipynb)

## What it does
It builds a graph of various medical terms, diseases, symptoms and their preventions


## Data used
We have used aggregated medical sources about various
- Diseases and conditions with ICD10 codes
- Symptoms associated with each condition
- Severity of conditions
- Specialist doctors to be referred for each disease/ condition
- Detailed description of diseases, symptoms and diagnosis
- Triage severity

We have combined all these data to form a medical triage graph database. We have also written several queries to fetch symptoms related to disease , diseases associated with a particular symptom, what specialist to refer to, ideal next course of triage action etc

## Tech Stack
TigerGraph cloud database - we have built a complete medical knowledge graph with various graph analysis queries
RASA chat bot - chat bot which is trained on the graph database model . Has several intents and actions related to medical triage workflow.

The Chatbot is hosted on a simple python HTTP server

## How we built it
Medical data from various sources were aggregated from various sources. GraphDatabase was created and populated using pyTigerGraph

All the CSV data files were loaded using various load jobs and then analysis queries were writtern
The results of these analysis queries are then accessed real time by the Chatbot using a REST API


## What's next for Healthnet - TigerGraph based Medical triage workflow
- Add data from medical tests and lab results to give personalized diagnosis to patients
- Add additional intents and entities to the chatbot to make conversation engaging and informative


## Screenshots
<img width="957" alt="Screenshot 2022-04-21 at 5 58 34 AM" src="https://user-images.githubusercontent.com/104054493/164384768-090ddce7-e9a7-4146-bc7c-98619c1d55c9.png">

<img width="1447" alt="Screenshot 2022-04-21 at 5 59 28 AM" src="https://user-images.githubusercontent.com/104054493/164384784-292f18bb-7b96-41f5-a698-2c8f3cc2b4ac.png">

<img width="971" alt="Screenshot 2022-04-21 at 6 00 20 AM" src="https://user-images.githubusercontent.com/104054493/164384807-44711a06-840f-49de-b088-1da98efd3402.png">

### Datasets used with medical ICD10 codes
<img width="811" alt="Screenshot 2022-04-21 at 06 32 35 AM" src="https://user-images.githubusercontent.com/104054493/164385022-df30addb-547b-40f9-a35e-0db05627625f.png">

<img width="709" alt="Screenshot 2022-04-21 at 06 32 46 AM" src="https://user-images.githubusercontent.com/104054493/164385041-f6ff90fa-68c0-4d90-948f-59b20e6e113c.png">


### Demo chat transcript
<img width="841" alt="Screenshot 2022-04-21 at 11 34 31 AM" src="https://user-images.githubusercontent.com/104054493/164385210-49007802-b75a-4990-8b5c-08e24b2fee26.png">


## Creating a Medical triage workflow with TigerGraph
### Set Up

```!python --version
!pip install pyTigerGraph
```

Python 2.7.16
Requirement already satisfied: pyTigerGraph in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (0.0.9.9.2)
Requirement already satisfied: requests in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (2.24.0)
Requirement already satisfied: pandas in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (1.4.2)
Requirement already satisfied: validators in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (0.18.2)
Requirement already satisfied: pyTigerDriver in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (1.0.14)
Requirement already satisfied: numpy>=1.18.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (1.22.3)
Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (2022.1)
Requirement already satisfied: python-dateutil>=2.8.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (2.8.2)
Requirement already satisfied: chardet<4,>=3.0.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (2.10)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (2020.6.20)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (1.25.10)
Requirement already satisfied: decorator>=3.4.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from validators->pyTigerGraph) (5.1.1)
Requirement already satisfied: six>=1.4.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from validators->pyTigerGraph) (1.15.0)
Exploring pyTigerGraph
!pip install pyTigerGraph
Requirement already satisfied: pyTigerGraph in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (0.0.9.9.2)
Requirement already satisfied: pyTigerDriver in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (1.0.14)
Requirement already satisfied: requests in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (2.24.0)
Requirement already satisfied: validators in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (0.18.2)
Requirement already satisfied: pandas in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pyTigerGraph) (1.4.2)
Requirement already satisfied: python-dateutil>=2.8.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (2022.1)
Requirement already satisfied: numpy>=1.18.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pandas->pyTigerGraph) (1.22.3)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (1.25.10)
Requirement already satisfied: idna<3,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (2.10)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (2020.6.20)
Requirement already satisfied: chardet<4,>=3.0.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->pyTigerGraph) (3.0.4)
Requirement already satisfied: decorator>=3.4.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from validators->pyTigerGraph) (5.1.1)
Requirement already satisfied: six>=1.4.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from validators->pyTigerGraph) (1.15.0)
import pyTigerGraph as tg # Importing

## Create a Connection

``` conn = tg.TigerGraphConnection(host="https://healthnet.i.tgcloud.io", password="tigergraph", gsqlVersion="3.0.5", useCert=True)```
# Sets up connection with GSQL
```
print(conn.gsql('ls', options=[]))
```
---- Global vertices, edges, and all graphs
Vertex Types:
Edge Types:

Graphs:
Jobs:


JSON API version: v2
Syntax version: v2

# Create Edges (published and references) and Vertices (source, article and event)
```
print(conn.gsql('''
  CREATE VERTEX condition(PRIMARY_ID name STRING, desciption STRING, icd_code STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true"
  CREATE VERTEX symptom(PRIMARY_ID name STRING, severity INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true"
  CREATE VERTEX precaution(PRIMARY_ID id STRING, description STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true"
  CREATE VERTEX specialist(PRIMARY_ID name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true"

  CREATE DIRECTED EDGE has_symptom(FROM condition, TO symptom) WITH REVERSE_EDGE="reverse_has_symptom"
  CREATE DIRECTED EDGE has_precaution(FROM condition, TO precaution) WITH REVERSE_EDGE="reverse_has_precaution"
  CREATE DIRECTED EDGE refer_to(FROM condition, TO specialist) WITH REVERSE_EDGE="reverse_refer_to"

  ''', options=[]))

print(conn.gsql('''CREATE GRAPH healthnet(condition, symptom, precaution, specialist, has_symptom, has_precaution, refer_to)''', options=[])) # Create the Graph

```
Successfully created vertex types: [condition].
Successfully created vertex types: [symptom].
Successfully created vertex types: [precaution].
Successfully created vertex types: [specialist].
Successfully created edge types: [has_symptom].
Successfully created reverse edge types: [reverse_has_symptom].
Successfully created edge types: [has_precaution].
Successfully created reverse edge types: [reverse_has_precaution].
Successfully created edge types: [refer_to].
Successfully created reverse edge types: [reverse_refer_to].
Stopping GPE GSE RESTPP
Successfully stopped GPE GSE RESTPP in 30.694 seconds
Starting GPE GSE RESTPP
Successfully started GPE GSE RESTPP in 0.098 seconds
The graph healthnet is created.


## Edit the Connect Credentials for Loading Data
```
conn.graphname = "healthnet"
conn.apiToken = conn.getToken(conn.createSecret())
```
Now we can import the CSV media rating into the graph.

## What is a ICD-10 diagnosis code?
Used for medical claim reporting in all healthcare settings, ICD-10-CM is a standardized classification system of diagnosis codes that represent conditions and diseases, related health problems, abnormal findings, signs and symptoms, injuries, external causes of injuries and diseases, and social circumstances

### Jobs for importing CSV into the graph

```
print(conn.gsql('''
CREATE LOADING JOB load_job_specialists_csv_1650501210039 FOR GRAPH healthnet {
      DEFINE FILENAME MyDataSource;
      LOAD MyDataSource TO VERTEX specialist VALUES($0) USING SEPARATOR=",", HEADER="true", EOL="\n";
    }

CREATE LOADING JOB load_job_symptom_severity_csv_1650501255514 FOR GRAPH healthnet {
      DEFINE FILENAME MyDataSource;
      LOAD MyDataSource TO VERTEX symptom VALUES($0, $1) USING SEPARATOR=",", HEADER="true", EOL="\n";
    }

CREATE LOADING JOB load_job_disease_precaution_csv_1650501525366 FOR GRAPH healthnet {
      DEFINE FILENAME MyDataSource;
      LOAD MyDataSource TO EDGE has_precaution VALUES($0, $1) USING SEPARATOR=",", HEADER="true", EOL="\n";
      LOAD MyDataSource TO EDGE has_precaution VALUES($0, $2) USING SEPARATOR=",", HEADER="true", EOL="\n";
      LOAD MyDataSource TO EDGE has_precaution VALUES($0, $3) USING SEPARATOR=",", HEADER="true", EOL="\n";
      LOAD MyDataSource TO EDGE has_precaution VALUES($0, $4) USING SEPARATOR=",", HEADER="true", EOL="\n";
    }

CREATE LOADING JOB load_job_disease_symptoms_csv_1650501655558 FOR GRAPH healthnet {
      DEFINE FILENAME MyDataSource;
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $1) USING SEPARATOR=",", HEADER="false", EOL="\n";
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $2) USING SEPARATOR=",", HEADER="false", EOL="\n";
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $3) USING SEPARATOR=",", HEADER="false", EOL="\n";
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $4) USING SEPARATOR=",", HEADER="false", EOL="\n";
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $5) USING SEPARATOR=",", HEADER="false", EOL="\n";
      LOAD MyDataSource TO EDGE has_symptom VALUES($0, $5) USING SEPARATOR=",", HEADER="false", EOL="\n";
    }

CREATE LOADING JOB load_job_disease_description_csv_1650503394334 FOR GRAPH healthnet {
      DEFINE FILENAME MyDataSource;
      LOAD MyDataSource TO VERTEX condition VALUES($0, $1, _) USING SEPARATOR=",", HEADER="true", EOL="\n";
    }

 ''', options=[]))
 
 ```
Successfully created loading jobs: [load_job_specialists_csv_1650482322027].
Successfully created loading jobs: [load_job_Symptom_severity_csv_1650482478169].
### Peek into Data Load

```
import pandas as pd

df = pd.read_csv('data/conditions.csv') print(df.head(0)) print('######') df = pd.read_csv('data/specialists.csv') print(df.head(0)) print('######') df = pd.read_csv('data/disease-symptoms.csv') print(df.head(0)) print('######') df = pd.read_csv('data/disease_description.csv') print(df.head(0)) print('######') df = pd.read_csv('data/symptom-severity.csv') print(df.head(0)) print('######') df = pd.read_csv('data/disease_precaution.csv') print(df.head(0)) print('######')
```

### Clear the Whole Graph
DANGER ZONE

```
conn.gsql('''
USE GLOBAL
DROP ALL
''')
```
'Dropping all, about 1 minute ...\nAbort all active loading jobs\nTry to abort all loading jobs on graph healthnet, it may take a while ...\n[ABORT_SUCCESS] No active Loading Job to abort.\nResetting GPE...\nSuccessfully reset GPE and GSE\nStopping GPE GSE\nSuccessfully stopped GPE GSE in 0.009 seconds\nClearing graph store...\nSuccessfully cleared graph store\nStarting GPE GSE RESTPP\nSuccessfully started GPE GSE RESTPP in 0.094 seconds\nEverything is dropped.'


## Load data

```
import json

specialist_file = "data/specialists.csv"
res = conn.uploadFile(specialist_file, fileTag='MyDataSource', jobName='load_job_specialists_csv_1650501210039')
print(json.dumps(res, indent=2))


symptoms_file = "data/symptom_severity.csv"
res = conn.uploadFile(symptoms_file, fileTag='MyDataSource', jobName='load_job_symptom_severity_csv_1650501255514')
print(json.dumps(res, indent=2))


precaution_file = "data/disease_precaution.csv"
res = conn.uploadFile(precaution_file, fileTag='MyDataSource', jobName='load_job_disease_precaution_csv_1650501525366')
print(json.dumps(res, indent=2))


disease_symptoms_file = "data/disease_symptoms.csv"
res = conn.uploadFile(disease_symptoms_file, fileTag='MyDataSource', jobName='load_job_disease_symptoms_csv_1650501655558')
print(json.dumps(res, indent=2))


disease_description_file = "data/disease_description.csv"
res = conn.uploadFile(disease_description_file, fileTag='MyDataSource', jobName='load_job_disease_description_csv_1650503394334')
print(json.dumps(res, indent=2))

```

# Steps to run chatbot


  
> Step-1: (Scroll down for detailed setup instructions)

  - cd health_bot
  
  >> Terminal-1:
  - $ rasa train
  - $ rasa run -m models --enable-api --cors "*" --debug

  >> Terminal-2:
  - $ rasa run actions
