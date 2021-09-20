# There are four general steps through which data flows within an organization.

| Collection & Ingestion     | Store & Management    | Process   |
| :------------- | :----------: | -----------: |
|  Amazon Web Services| Amazon S3   | Hadoop   |
| Google Cloud   | Hadoop| Hive  |
| Azure | Amazon Reshift | Apache Spark |

Data is stored in raw format. The next step is to prepare it, which includes "cleaning data", for instance finding missing or duplicate values, and converting data into a more organized format.

Once the data is clean and organized, it can be exploited. We explore it, visualize it, build dashboards to track changes or compare two sets of data.

Finally, once we have a good grasp of our data, we're ready to run experiments, like evaluate which article title gets the most hits, or to build predictive models, for example to forecast stock prices.

Data engineers are responsible for the first step of the process: ingesting collected data and storing it. They have a great responsibility as they lay the ground work for data analysts, data scientists and machine learning engineers. If the data is scattered around, corrupted, and difficult to access, there's not much to prepare, explore, or experiment with.

Data engineer: their job is to deliver the correct data, in the right form, to the right people, as efficiently as possible.

A data engineer's responsibilities
They ingest data from different sources, optimize the databases for analysis, and manage data corruption. Data engineers develop, construct, test, and maintain architectures such as databases and large-scale processing systems to process and handle massive amounts of data. If you're not sure what this all means, that's okay! The course will unpack all this jargon and explain the what, why, and how.

With the advent of big data,the demand for data engineers has increased. Big data can be defined as data so large you have to think about how to deal with its size, because it's difficult to process using traditional data management methods.

## The five "V"s
Big data is commonly characterized by five Vs:
volume (the quantity of data points),
variety (type and nature of the data: text, image, video, audio),
velocity (how fast the data is generated and processed),
veracity (how trustworthy the sources are),
value (how actionable the data is).
Data engineers need to take all of this into consideration.

# The Data Pipeline - Data is the new oil
Ingest
Process
Store
Need Pipelines
Automate flow from one station to the next
Provide up-to-date, accurate, relavant data

Data Pipelines Ensure Data Pipeline
Extracting
Transforming
Combining
Validating
Loading
