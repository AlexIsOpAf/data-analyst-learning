

- [Overview](#overview)
- [What is a data analyst](#what-is-a-data-analyst)
  - [What are some common data analyst responsibilities?](#what-are-some-common-data-analyst-responsibilities)
    - [Producing reports](#producing-reports)
    - [Spotting patterns](#spotting-patterns)
    - [Collaborating with others](#collaborating-with-others)
    - [Collecting data and setting up infrastructure](#collecting-data-and-setting-up-infrastructure)
  - [Skills & Technologies does a data analyst need to know](#skills--technologies-does-a-data-analyst-need-to-know)
    - [Types of data analytics](#types-of-data-analytics)
    - [Skills to acquire as a DA](#skills-to-acquire-as-a-da)
  - [How to become competitive as a DA](#how-to-become-competitive-as-a-da)
    - [Creating a portfolio](#creating-a-portfolio)
    - [Acquiring Certifications](#acquiring-certifications)
    - [Exposure to the cloud](#exposure-to-the-cloud)
    - [Exposure to good software development practices (Version control, System design etc)](#exposure-to-good-software-development-practices-version-control-system-design-etc)
- [Stage 1: Understanding What Data is](#stage-1-understanding-what-data-is)
- [Stage 2: Excel 101](#stage-2-excel-101)
  - [Stage 2.0: What is excel?](#stage-20-what-is-excel)
  - [Stage 2.1: Data Filters](#stage-21-data-filters)
  - [Stage 2.2: Functions](#stage-22-functions)
  - [Stage 2.3: Formulas](#stage-23-formulas)
  - [Stage 2.4: Charts and plots](#stage-24-charts-and-plots)
  - [Stage 2.5: Pivot table & Transpose](#stage-25-pivot-table--transpose)
  - [Stage 2.6: Vlookup](#stage-26-vlookup)
  - [Stage 2.7: VBA macros](#stage-27-vba-macros)
  - [Stage 2.8: Hands-on look](#stage-28-hands-on-look)
- [Stage 3: Databases & SQL](#stage-3-databases--sql)
  - [Stage 3.1: SQL Project](#stage-31-sql-project)
- [Stage 4: Tableau](#stage-4-tableau)
- [Stage 5: Python](#stage-5-python)
  - [Why is Python good for Data analysis](#why-is-python-good-for-data-analysis)
    - [Data Mining](#data-mining)
    - [Data Processing and Modelling](#data-processing-and-modelling)
    - [Data Visualization](#data-visualization)
  - [Python: Intro to Python (Entry)](#python-intro-to-python-entry)
  - [Python: Python I](#python-python-i)
- [Stage 6: Auxiliary](#stage-6-auxiliary)
  - [Stage 6.1: JSON Overview](#stage-61-json-overview)
    - [Why should I use JSON?](#why-should-i-use-json)
  - [Stage 6.2: Data-warehousing principles and best practices (e.g. Dimensional Modelling, Cube Design)](#stage-62-data-warehousing-principles-and-best-practices-eg-dimensional-modelling-cube-design)
  - [Stage 6.3: A/B testing implementation](#stage-63-ab-testing-implementation)
  - [Stage 6.4: AWS & the cloud](#stage-64-aws--the-cloud)
  - [Stage 6.5: Statistics](#stage-65-statistics)



**Q: For jobs, How much should I know and is excel really a need?**

**A: "It really depends on the position. For the most part it's Data Analyst positions that call for knowledge of Excel, some Data Analyst positions don't use Python or R at all. Hypothetically a Data Analyst shouldn't need Excel because they can do everything that Excel can do using Python/R/SQL but in practice Excel is the application of choice for non-technical people to look at data so some basic knowledge of it is necessary for communication purposes."**.

**Q: If I go through everything here, am I guranteed a job?**

**A: "Anybody can learn the technical skills of data analysis if they have the time and apply themselves, so companies try to pick and choose the people best for their organization. Companies are always changing and trying to do things better, and a big part of data analysis is reporting your findings to people that don’t understand the data analysis. So if you can be open minded, kind, open to change, and a self starter, your skillset can get you a job tomorrow."**.


![Imgur](data-science.jpeg)

## Overview

This roadmap is a high level overview of skills you should strive for to become a valued data analyst. Due to the fact I do not work within the data analyst world, some of materials covering advanced techniques will be outsourced to peer-reviewed sources. I will attempt to make the programming section as rigorous as possible to ensure you are comfortable with ETL & various mutations of data to fit your usecase. I will also try and verify the validity of the content in here with experienced analysts.

I will also try to expose you to the cloud so you can showcase something original on your CV that will give you the edge over candidates.

I'm also going to push to start reguarly watching Data Analyst channels here are some:

-   [Chandoo](https://www.youtube.com/channel/UC8uU_wruBMHeeRma49dtZKA)
-   [Alex the Analyst](https://www.youtube.com/channel/UC7cs8q-gJRlGwj4A8OmCmXg)
-   [Ali](https://www.youtube.com/channel/UCaDh-eU-lds_d9kS976vBVw)
-   [Kyle (Data scientist but some of the content overlaps)](https://www.youtube.com/channel/UCr6_XCxMLXWGguWZi_93n7w)

Use these channels to take "Active breaks" use a different part of your brain.

![Imgur](0_wN5ZfViulNrCZe0f.jpeg)

## What is a data analyst

**Credit to [Kirsten Slyter](https://www.rasmussen.edu/student-life/blogs/author-archives/kirsten-slyter/) for producing invaluable insight into the data analyst role.**

Generally speaking, a data analyst will retrieve and gather data, organize it and use it to reach meaningful conclusions. "Data analysts’ work varies depending on the type of data that they’re working with (sales, social media, inventory, etc.) as well as the specific client project," says Stephanie Pham, analyst for Porter Novelli.

Companies in nearly every industry can benefit from the work of data analysts, from healthcare providers to retail stores to fast food chains. The insights that data analysts bring to an organization can be valuable to employers who want to know more about the needs of their consumer or end user.

Regardless of which industry they work in, data analysts can expect to spend their time developing systems for collecting data and compiling their findings into reports that can help improve their company.

Analysts can be involved in any part of the analysis process. In a data analyst role, you could be included in everything from setting up an analytics system to providing insights based on the data you collect—you may even be asked to train others in your data-collection system

### What are some common data analyst responsibilities?

#### Producing reports
"As an analyst, I spend a significant amount of time producing and maintaining both internal and client-facing reports," says Casey Pearson, marketing analyst at Delphic Digital. Those reports give management insights about new trends on the horizon as well as areas the company may need to improve upon.

Writing up a report isn’t as simple as throwing numbers onto a blank page and sending it to your manager. "Successful data analysts understand how to create narratives with data," says Jess Kendra, manager of analytics at Porter Novelli. "To remain valuable, the reports, answers and insights that data analysis provides have to be understood by the next decision-maker, who frequently is not an analyst."

#### Spotting patterns
The most effective data analysts are able to use data to tell a story. In order to produce a meaningful report, a data analyst first has to be able to see important patterns in the data. "At the base level, data is used to find trends and insights that we can use to make recommendations to our clients," Pham says.

Reporting in regular increments, such as weekly, monthly or quarterly, is important since it helps an analyst notice significant patterns. "They all contribute to an overarching time frame where we can see trends over time," Pham adds.

#### Collaborating with others
Surprised to see this on the list? The word "analyst" might make you think of someone working apart from the rest of the company, but that’s far from the truth. The wide variety of data analyst roles and responsibilities means you’ll collaborate across many other departments in your organization including marketers, executives and salespeople. You’ll also likely collaborate closely with those who work in data science like data architects and database developers.

Being able to communicate well is important. "Your success is dependent on your ability to work with people—the people you are gathering the research questions from, peers you collaborate with to execute the work and the people you deliver the final presentation to," Kendra says.

#### Collecting data and setting up infrastructure
Perhaps the most technical aspect of an analyst’s job is collecting the data itself. This often means working together with web developers to optimize data collection, according to Pearson.

Streamlining this data collection is key for data analysts. They work to develop routines that can be automated and easily modified for reuse in other areas. Analysts keep a handful of specialized software and tools in their arsenal to help them accomplish this.

![Imgur](data-analytics-vs-data-science.jpeg)

### Skills & Technologies does a data analyst need to know

#### Types of data analytics

At its core, data analytics is about answering questions and making decisions. And just as there are different types of questions, there are also different types of data analytics depending on what you’re hoping to accomplish. While there’s no set-in-stone glossary of these types of data analytics, the folks at ScienceSoft do an excellent job breaking this work down into four primary areas:2

-   Descriptive analytics answers, "What happened?"
-   Diagnostic analytics answers, "Why did something happen?"
-   Predictive analytics answers, "What is likely to happen?"
-   Prescriptive analytics answers, "What action should be taken?"


Data analysts can tailor their work and solution to fit the scenario. For instance, if a manufacturer is plagued with delays and unplanned stoppages, a diagnostic analytics approach could help identify what exactly is causing these delays. From there, other forms of analysis can be used for fixing these issues.

#### Skills to acquire as a DA

**High Level Skills**

-   Have moderate math and statistical skills
-   Have a strong business acumen
-   Have moderate computer science / coding skills
-   Develop key performance indicators
-   Create visualizations of the data
-   Utilize business intelligence and analytics tools


**Technical Skills**

-   Python
-   Databases (SQL/MongoDB/Cassandra etc)
-   R
-   Tableau or PowerBI
-   Excel
-   AWS (BI tools and how to use them.. Redshift etc)

[How to become a Data analyst](https://www.youtube.com/watch?v=2reMI_i24P4&ab_channel=KrishNaikKrishNaikVerified)

### How to become competitive as a DA

#### Creating a portfolio
Creating 1 or 2 extremely well built projects to showcase in your portfolio. Having this on your CV shows to an employer that you are a self starter and are passionate about a role

[Project Ideas for Your Data Analytics Portfolio](https://careerfoundry.com/en/blog/data-analytics/data-analytics-portfolio-project-ideas/)

Start thinking about what kind of project you want to build as your "Main" project. The project that when recruiters or hiring managers bring up in an interview you are proud to explain your design, implementation and what you would change given a chance to re-do. 

#### Acquiring Certifications

Focused at established Institutions (Goldman Sachs, Morgan Stanley etc..)

In order of urgency:

- Google Data Analytics Professional
- [AWS Certified Cloud Practitioner](https://www.youtube.com/watch?v=3hLmDS179YE)
- [AWS Solutions Architect: Associate](https://learn.cantrill.io/p/aws-certified-solutions-architect-associate-saa-c02)
- [AWS Specialty: Data Analytics](https://www.reddit.com/r/AWSCertifications/comments/hsag0q/just_passed_the_aws_data_analytics_specialty_cert/)
- CFA

#### Exposure to the cloud

Cloud computing is becoming increasingly vital for not just the software developers but in the field of big data analytics: cloud computing makes expanding computing power and deploying data solutions much easier and is therefore handy for data scientists who are digging into large datasets.

Each of the three major cloud providers has a set of powerful tools for data scientists:

-   For AWS, widely known tools include Redshift, EC2, EMR, S3, Data Pipeline and Database Migration Service. Customers include Standard Chartered Bank and S&P Global Ratings (financial services), Skyscanner (travel & hospitality), Nielsen (marketing & advertising), Royal Dutch Shell (energy) and The Guardian (media).
  </br>

-   Microsoft Azure, on the other hand, provides AzureSQL, DocumentDB, AzureTable and AzureBlob for data storage purposes, HDinsight as a HortonWorks distribution of Hadoop (including Hive, MapReduce, Spark,etc.) and AzureML for an easy implementation of machine learning algorithms. A plus of using Azure is that all tools mentioned above could be integrated with Microsoft Excel and Power BI – making results easier to visualise and more accessible for individuals with different technical skills. Customers of its data-related services in the UK include Concentra, NEL and Presence Orb.
  </br>

-   Widely used services for GCP include Google BigQuery for data collection and exploration, Vision/Speech/Translate/Natural Language API for data extraction and transformation, Cloud Dataprep, Cloud Dataflow and Apache Beam for data cleansing, Data Studio for visualization, and Tensorflow for machine learning purposes. Customers in Europe include HSBC (financial services), Sky UK and ITV (media), Philips (manufacturing), and AB InBev, Burger King, Ferrero and Morrisons (retail and consumer goods)


#### Exposure to good software development practices (Version control, System design etc)

*SECTION SOON*

## Stage 1: Understanding What Data is

You should be aware of the core fundamentals of what data is. How to present data, what contributes to a great visualisation, You will unlock the critical thinking portion of your brain on this topic.


[Review the Google DA Course 1 & 2](https://www.coursera.org/professional-certificates/google-data-analytics?utm_source=gg&utm_medium=sem&utm_campaign=15-GoogleDataAnalytics-ROW&utm_content=15-GoogleDataAnalytics-ROW&campaignid=12566515400&adgroupid=117869292685&device=c&keyword=google%20data%20analytics&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=507290840627&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Go6W35DpZV9ykk45xg46fwyy0apeXHMHvcWN6TowX741u6sJwM3cEaAkL3EALw_wcB#courses)

Note: The faster you go through the google content, the less it costs. Make sure you take notes and really understand. I will not be able to verify your knowledge on this so you have the responsibility to go through this with a fine tooth comb. Any terms you do not understand, google it, research it, digest it and move on.


## Stage 2: Excel 101

Again, this is not my domain, I'm highlighting what is to be required for you at minimum to be competitive in London, you should strive to understand these topics as much as possible. You have to be able to explain this to a normal person.

I have attached a csv file named:
*annual-enterprise-survey-2019-financial-year-provisional-csv.csv* 

for practical use when attempting stages 2.1 through to 2.7

Some of the lectures/videos will overlap and that is fine, what matters is you understand every single detail. Sometimes having different perspectives can help cement concepts. Make sure you understand them. If you do not, google, research and digest.

Use this [book](https://www.programmer-books.com/wp-content/uploads/2018/12/Excel-2019-Bible-1.pdf) as a reference for solidifying your knowledge. You do not need to go through it linearly, just visit the content page and flick through to the section you need.



### Stage 2.0: What is excel?
[Welcome to excel](https://www.youtube.com/watch?v=rwbho0CgEAE&ab_channel=codebasicscodebasicsVerified)

### Stage 2.1: Data Filters
-   [Review the excel filter basics](https://www.youtube.com/watch?v=wMlTDXPEjag)
-   [Review the excel advanced filter](https://www.youtube.com/watch?v=VqQACB_69SQ)
### Stage 2.2: Functions
-   [Review the excel functions lecture](https://www.youtube.com/watch?v=Jl0Qk63z2ZY)
-   [Review the additional excel functions video](https://www.youtube.com/watch?v=_EWcAR_Hkvg&ab_channel=LeilaGharaniLeilaGharani)
### Stage 2.3: Formulas
-   [Review the excel formulas lecture](https://www.youtube.com/watch?v=y1126PQ5zRU&ab_channel=LeilaGharani)
-   [Review the additional excel formula lecture](https://www.youtube.com/watch?v=ShBTJrdioLo&ab_channel=TheOrganicChemistryTutor)
-   [Review the excel advanced formula lecture](https://www.youtube.com/watch?v=F2AD24ETgaE&ab_channel=TeachExcelTeachExcel)
### Stage 2.4: Charts and plots
-   [Review the introduction to charts and plots](https://www.youtube.com/watch?v=TfkNkrKMF5c&ab_channel=TechnologyforTeachersandStudentsTechnologyforTeachersandStudents)
-   [Review the additional charts lecture](https://www.youtube.com/watch?v=DAU0qqh_I-A&ab_channel=LeilaGharaniLeilaGharani)
-   [Review the excel charts lecture](https://www.youtube.com/watch?v=8g9DK5noi1s&ab_channel=LeilaGharaniLeilaGharaniVerified)
### Stage 2.5: Pivot table & Transpose
-   [Review the excel pivot table lecture](https://www.youtube.com/watch?v=qu-AK0Hv0b4)
-   [Review the excel transpose lecture](https://www.youtube.com/watch?v=yYVokk0NdiI&ab_channel=LeilaGharaniLeilaGharaniVerified)
-   [Review the additional transpose lecture](https://www.youtube.com/watch?v=YiC-z_FH7SU&ab_channel=TechnologyforTeachersandStudentsTechnologyforTeachersandStudents)
### Stage 2.6: Vlookup
-   [Review the excel VLOOKUP lecture - important!](https://www.youtube.com/watch?v=d3BYVQ6xIE4&ab_channel=ExcelCampus-JonExcelCampus-Jon)
### Stage 2.7: VBA macros
It is not necessary for you to go through all of this in one sitting. Make sure you can answer these questions before you move on.. What are macros? What is VBA? What is object oriented programming? What is the use in VBA macros?

If you can answer these questions then move on - We will visit this later after the programming module

[VBA macros - very important](https://www.youtube.com/watch?v=G05TrN7nt6k&ab_channel=LearnitTrainingLearnitTraining)

### Stage 2.8: Hands-on look
- Visit [this website](https://docs.google.com/spreadsheets/u/0/?ftv=1)
- Select Annual budget
  
Go through the various other sheets in the annual budget and play around, find out how it works, change values, This is going to add an engineer's mindset to your repertoire.

When done:

- Go back and Select Monthly budget

Again.. Understand how things work, change the values, play around with it, delete things, look at the formulas/functions.. but make sure you understand what is going on.

You can choose to replicate the excel visualisation if you'd like to cement your knowledge, or you can move on.

![Imgur](database-157334670-5c29939d46e0fb0001edf766.jpeg)

## Stage 3: Databases & SQL

This stage is going to be extremely important because this is a Data analyst's bread and butter, you should know how to leverage database technologies. You will often feel you are repeating content, this is done on purpose so you can digest the content naturally.

there are naturally more advanced features of SQL, You should have an idea of them for e.g: VIEWS

Your checklist before you can confidently move on:

- [ ] Understanding the basics of Relational Databases (Tables,records,primary keys,attributes,foreign keys)
- [ ] Understanding the SQL Commands and their distinctions (CREATE,DROP,ALTER,TRUNCATE,INSERT,UPDATE,DELETE,GRANT,REVOKE,SELECT)
- [ ] Knowledge of Joins (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN)
- [ ] Advanced SQL (UNION, UNION ALL, INTERSECT, MINUS, LIMIT, TOP, CASE, DECODE, AUTO-INCREMENT, IDENTITY)

[Review the SQL lecture - extremely important!!!](https://www.youtube.com/watch?v=HXV3zeQKqGY) Unfortunately you will need to go through this content in it's entirety.

[Review the Google DA Course 3, 4 & 5](https://www.coursera.org/professional-certificates/google-data-analytics?utm_source=gg&utm_medium=sem&utm_campaign=15-GoogleDataAnalytics-ROW&utm_content=15-GoogleDataAnalytics-ROW&campaignid=12566515400&adgroupid=117869292685&device=c&keyword=google%20data%20analytics&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=507290840627&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Go6W35DpZV9ykk45xg46fwyy0apeXHMHvcWN6TowX741u6sJwM3cEaAkL3EALw_wcB#courses)


### Stage 3.1: SQL Project

Using your newly acquired skills, You should be able to set up a SQL workspace, ingest the .csv data given earlier and perform operations you've learned about

Go through this example SQL [video](https://www.youtube.com/watch?v=qfyynHBFOsM) and make sure that when you are completing it, You are writing notes and really digesting the material. Alex is an excellent analyst, understand his thought process and it will help you later on down the line.

When you're done with this project, you can add it to your portfolio - github, but it will not be in your CV.

## Stage 4: Tableau

Just as SQL is a data analysts bread and butter, so is having a way to visualise data and tell a story. Tableau is a way to give insight to your data or trend you are pushing, You are telling a story.

[Review the Google DA Course 6](https://www.coursera.org/professional-certificates/google-data-analytics?utm_source=gg&utm_medium=sem&utm_campaign=15-GoogleDataAnalytics-ROW&utm_content=15-GoogleDataAnalytics-ROW&campaignid=12566515400&adgroupid=117869292685&device=c&keyword=google%20data%20analytics&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=507290840627&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Go6W35DpZV9ykk45xg46fwyy0apeXHMHvcWN6TowX741u6sJwM3cEaAkL3EALw_wcB#courses)

[Review the Tableau course by Edureka](https://www.youtube.com/watch?v=aHaOIvR00So&ab_channel=BharatiDWConsultancyBharatiDWConsultancy)

Again; go through this [video](https://www.youtube.com/watch?v=QILNlRvJlfQ) for practical experience. You can add it to your portfolio but it will not be in your CV


## Stage 5: Python

Credit to **Dawid Karczewski**

Python is an interpreted, general-purpose, high-level language with an object-oriented approach. The language is used for API development, Artificial Intelligence, web development, Internet of Things, etc. 

The part of why Python has become so popular is because it is widely used among data scientists. It is one of the easiest languages to learn and has impressive libraries and works perfectly for every stage of data science. 

So the short answer to the question of whether Python is good for data analysis is yes.


I will also be setting up small python projects so you can understand how to think like a programmer from translating my requirements into code. The solutions will be annotated.

### Why is Python good for Data analysis

Python works well on every stage of data analysis. It is the Python libraries that were designed for data science that are so helpful. Data mining, data processing, and modeling along with data visualization are the 3 most popular ways of how Python is being used for data analysis. 

#### Data Mining

A data engineer uses libraries such as Scrapy and BeautifulSoup for data mining Python-based approach. With the help of Scrapy, one can build special programs that can collect structured data from the web. It is also widely used for collecting data from APIs. 

BeautifulSoup is used when one can not retrieve data from APIs: it scrapes data and arranges in the preferable format. 

![BeautifulSoup in action, scraping data from the Web](https://stackabuse.s3.amazonaws.com/media/parsing-html-with-beautifulsoup-in-python-4.gif)


#### Data Processing and Modelling

Two main libraries are used at this stage: NumPy and Pandas. NumPy (Numerical Python) is used for arranging big data sets and makes math operations and their vectorization on arrays easier. Pandas offers two data structures: series (a list of items) and data frames (a table with multiple columns). This library converts data to the data frame allowing you to delete or add new columns to it and perform various operations. 

![A linear regression modelling in NumPy](https://lh6.googleusercontent.com/xuSK3mWUr0WuOgOYqNR_sthvqX7pyVwXZrBB6-FwkWlAQsFyRWTFgFiFQmiGq7k-ZdMaub7rnmDWpyzxk2umxY6c0icxX5sKYjK65Itj58ulpeAhHszGFMoKNi1wedffgYjuKGSM)


#### Data Visualization

Matplotlib and Seaborn are widely used for Python data visualization. It means that they help to convert long lists of numbers into easy-to-understand graphics, histograms, pie charts, heatmaps, etc. 

Of course, there are way more libraries than we have mentioned. Python offers numerous tools for data analysis projects and can assist during any task within the process. 

![Matplotlib is just one of many Python libraries supporting data visualisation](https://lh5.googleusercontent.com/7GQF9jq6dPwSDaWINfOQm8krOq34I4Pq1o3R8_UDd3SvgnVO959crbM0FiAdh833ZHbVgYjsGkHNZmCFlYXSAyEZ0o4dezmKmdoUkn8HmLWlOwK5UuzotaCH-wSypjcDk5NlYd1A)

![Imgur](./Nemo_hero.jpeg)

### Python: Intro to Python (Entry)

Our immediate checklist will look something like:

- [ ] [Installing Python & PyCharm](https://www.youtube.com/watch?v=rfscVS0vtbw&t=105s)
- [ ] [Setup & Hello World](https://www.youtube.com/watch?v=rfscVS0vtbw&t=400s)
- [ ] [What are static & dynamic programming languages](https://www.youtube.com/watch?v=S5hoGPYitNQ)
- [ ] [Variables & Data types](https://www.youtube.com/watch?v=rfscVS0vtbw&t=906s)
- [ ] [Working with Strings](https://www.youtube.com/watch?v=rfscVS0vtbw&t=1623s)
- [ ] [Working with Numbers](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s)

</br>

**Quiz**
<details>
  <summary>1. In python a variable must be declared before it is assigned a value (True or False)?</summary>
  True
</details>
<details>
  <summary>2. What is the syntax that assigns the value 100 to the variable x</summary>
  x = 100
</details>
<details>
  <summary>3. In python a variable may be assigned a value of one type and then later assigned a value of a different type (True or False)?</summary>
  True
</details>
<details>
  <summary>4. What is the name of the data type, when its values are True or False. For e.g: x = False?</summary>
  Boolean/Bool
</details>


### Python: Python I

Note: For static typed languages like C++ or Java, Arrays or lists are homogeneous.. Meaning all the values that exists within that container must be of same type. For dynamic typed languages such as Python or Ruby, You can have heterogeneous Arrays/Lists.

Homogeneous = [1,2,3,4,5]
Heterogeneous = ["Alex", "Jason", 3, 2, 1]

- [ ] [Data Structures & Algorithms](https://www.youtube.com/watch?v=bum_19loj9A&ab_channel=freeCodeCamp.orgfreeCodeCamp.orgVerified)
    - [ ] [Lists - Overview](https://www.youtube.com/watch?v=pmN9ExDf3yQ&ab_channel=CSDojoCSDojoVerified)
      - [ ] [Lists](https://www.youtube.com/watch?v=rfscVS0vtbw&t=3790s)
      - [ ] [Lists Functions](https://www.youtube.com/watch?v=rfscVS0vtbw&t=4244s)
    - [ ] [Tuple](https://www.youtube.com/watch?v=rfscVS0vtbw&t=4737s)
    - [ ] [Dictionaries](https://www.youtube.com/watch?v=rfscVS0vtbw&t=7637s)
- [ ] [IF statements](https://www.youtube.com/watch?v=rfscVS0vtbw&t=6006s)
- [ ] [Functions](https://www.youtube.com/watch?v=rfscVS0vtbw&t=5055s)
- [ ] [Return Statement](https://www.youtube.com/watch?v=rfscVS0vtbw&t=5651s)
- [ ] [For loop](https://www.youtube.com/watch?v=rfscVS0vtbw&t=9164s)
- [ ] [Modules & Pip](https://www.youtube.com/watch?v=rfscVS0vtbw&t=12493s)


**Tasks**

You should know how to leverage your command line by now, But just to make sure..

Install pytest using pip:
```
pip install -U pytest
```

Check you have installed the correct version:
```
$ pytest --version
pytest 6.2.4
```



**Question:**

Given a list of integers. Define through python, a running total of the sum. Update the list with the running sum and **return** the updated list from the solution function.

<details>
  <summary>Example</summary>
    Input: nums = [1,2,3,4]
    </br>
    Output: [1, 3, 6, 10]
    </br>
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
</details>

<details>
  <summary>Example2</summary>
    Input: nums = [3,1,2,10,1]
    </br>
    Output: [3,4,6,16,17]
</details>

</br>

When you are done with the task, run this command to check your work

```
pytest Python-I/PythonI-template.py
```

If you have done this task correctly you should get a similar output

<details>
  <summary>Example</summary>

  ```
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.7.3, pytest-6.2.4, py-1.10.0, pluggy-0.12.0
rootdir: /Users/XenaDatabase/Documents
collected 1 item                                                                                                                          

PythonI-sol.py .                                                                                                                    [100%]

============================================================ 1 passed in 0.01s ============================================================
  ```
</details>




## Stage 6: Auxiliary

These are additional skills and resources that aren't necessarily core to a data analyst, but a fundamental understanding gives you perspective and increases your chances at landing a job

### Stage 6.1: JSON Overview

**Credit to [Josh Fruhlinger](https://www.infoworld.com/author/Josh-Fruhlinger/)
Credit to [Costas Andreou](https://medium.com/@costasandreou?source=post_page-----a53c3b88cc0--------------------------------)**

JavaScript Object Notation is a schema-less, text-based representation of structured data that is based on key-value pairs and ordered lists. Although JSON is derived from JavaScript, it is supported either natively or through libraries in most major programming languages. JSON is commonly, but not exclusively, used to exchange information between web clients and web servers. 

Over the last 15 years, JSON has become ubiquitous on the web. Today it is the format of choice for almost every publicly available web service, and it is frequently used for private web services as well.


#### Why should I use JSON?

It is believed that the first major company to begin offering services and therefore popularising the adoption of JSON, was Yahoo in 2005¹. It is now believed that JSON is the most used data format.

The top reasons people use JSON are:

-   Very easy to read, write and manipulate
-   It’s very fast to transfer over the network
-   Supported by all major browsers, backend tech stacks
-   You will most likely work with JSON when working with unstructured data

```json
{
  "firstName": "Jonathan",
  "lastName": "Freeman",
  "address": "Crestwell 109th Street",
  "isWriter": true,
  "worksWith": ["Spantree Technology Group", "InfoWorld"],
  "pets": [
    {
      "name": "Lilly",
      "type": "Raccoon"
    }
  ]
}
```

### Stage 6.2: Data-warehousing principles and best practices (e.g. Dimensional Modelling, Cube Design)
### Stage 6.3: A/B testing implementation
### Stage 6.4: AWS & the cloud
### Stage 6.5: Statistics
