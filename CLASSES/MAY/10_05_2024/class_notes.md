# MAY, 10, 2024 - MAP/REDUCE CLASS & MOST FAMOUS FRAMEWORK

## MAP REDUCE

FRAMEWORK HADOOP WORKS ON MAP/REDUCE ALGORITHM, GATHERING RESULT ALL TOGETHER.

IT BREAKS DOWN DATA INTO SMALLER PIECES, AND USES PARALLEL PROCESSING, TIED IN A SINGLE HADOOP COMMODITY SERVER.


### HISTORY

EARLY 2000, ENGINEERS FROM GOOGLE STARTED THINKING ABOUT FUTURE SOLUTIONS.

DIVIDE AND CONQUER SPIRIT, FLOWING INTO PARALLEL PROCESSING.

TARGET IS TO REDUCE EXECUTION TIME, BY DIVING A SINGLE LARGER TASK INTO MULTIPLE SMALLER ONES. FINALLY, AT THE END, PUT IT ALL TOGETHER.


MAP REDUCE WAS AN OPEN SOURCE SOLUTION, WHICH WAS PRESENTED BY GOOGLE ENGINEERS. AFTER THAT, MANY OTHER PRIVATE COMPANIES STARTED WORKING ON PRODUCTS THAT WERE INITIALLY BASED ON OPEN SOURCE SOLUTION.

INTERESTING PAPER: "MAPREDUCE: SIMPLIFIED DATA PROCESSING ON LARGE CLUSTERS"

## HOW DOES IT WORK

### MAP

SPLIT LARGER TASK INTO SMALLER ONE.



### REDUCE

PERFORMED ON THE OUTPUT DATA FROM THE MAP TASK. REDUCES INTERMEDIATE TASKS UNTIL IT GETS INTO ONE SINGLE VALUE.

## ADVANTAGES

POWERFUL FRAMEWORK, REVOLUTIONIZED BIG DATA WORLD:

- SCALABILITY
- FAULT TOLERANCE: DUPLICATED DATA, ENSURING AVAILABILITY
- COST-EFFECTIVE: EACH SMALL TASK CAN BE PROCESSED ON A NORMAL COMPUTER, SO, HARDWARE EFFECTIVE

## MOST IMPORTANT FRAMEWORKS

- HADOOP
- SPARK
- DASK

### HADOOP

Based on the mapReduce algorithm.

Some other caracteristics:

- scalable
- cost effective
- flexible
- fault tolerant

#### Archtecture

HDFS - Hadoop distributed file systemthat supports petabytes of data and the management of related files across
machines.

Datanodes

### SPARK

Easier to use when compared to hadoop. 

Originated at Berkeley University from San Franciso (USA).

Extremely used for large ammount of data treatment and processing.

Adopeted by several big shots companies, like facebbok.

Uses RAM to store data, which is a lot more faster.

Uses mapReduce algorithms under the hood, it abstracts a lot more 

#### ADVANTAGES

- fast processing: uses RAN rather than HD.
- Flexibility: a lot of programming languages frameworks
- In-memory computing
- Real time processing

#### ARCHTECTURE

Five main components of Apache Spark:

- Apache spark core
- Spark SQL
- Spark Streaming
- Machine learning library (MLib)
- GraphX

### DASK

open source python library that enables work on arbitrarily large datasets, speed on computation.

- speed
- flexibility
- 

natively scales on numPy, Pandas and sckit-learn.

works well for medium datasets.



## LLM - Large language model