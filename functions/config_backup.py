# global variables

import pandas as pd
import numpy as np
import spacy
import nltk
import os
from nltk.corpus import stopwords


job_categories = ['Data_Engineer', 'Data_Analyst', 'Data_Scientist', 'Business_Analyst', 'Business_Intelligence', 'Others']

# A list of technical skills that are needed in general
technical_skills = [
    'python','r','c','c++','java','hadoop','scala','flask','pandas',
    'spark','scikit','numpy','php','sql','mysql','css','mongodb','nltk',
    'keras','pytorch','tensorflow','linux','ruby','javascript','django',
    'react','reactjs','ai','artificial intelligence','ui', 'skicit',
    'tableau','power bi','machine learning','frontend','big data',
    'data mining','data warehousing','data visualization','data engineering',
    'data modeling','data governance','data analytics','statistical analysis',
    'natural language processing', 'computer vision','deep learning',
    'data preprocessing','etl','data quality management','excel','vba','gcp']
# A list of soft skills that are needed in general
combined_soft_skills = [
    "Communication", "Critical Thinking", "Creativity","Adaptability", "Teamwork", "Attention to Detail",
    "Time Management", "Emotional Intelligence", "Empathy","Conflict Resolution", "Decision-Making", "Leadership",
    "Problem-Solving", "Ethical Judgment", "Flexibility","Customer Service", "Negotiation", "Innovation",
    "Persuasion", "Resilience", "Collaboration", "Networking","Conflict Management", "Cultural Sensitivity", "Stress Management",
    "Self-Motivation", "Open-Mindedness", "Information Presentation","Risk Management", "Active Listening"
]

# Comprehensive list of all skills aggregated from the dataset
skills=['A/B Testing', 'Adaptability', 'Agile Methodologies', 'AI Ethics', 'AI Explainability', 'AI Fairness',
        'API Integration', 'Attention to Detail', 'Big Data', 'Business Acumen', 'Business Analysis',
        'Business Intelligence', 'Change Management', 'Classification', 'Client Management', 'Cloud Computing',
        'Clustering', 'Collaboration', 'Communication', 'Conflict Resolution', 'Containers', 'Creative Problem-Solving',
        'Creative Thinking', 'Critical Thinking', 'Dashboard Creation', 'Dashboard', 'Data Analysis',
        'Data Analytics', 'Data Architecture', 'Data Auditing', 'Data Augmentation', 'Data Catalog', 'Data Cleaning',
        'Data Cleansing', 'Data Collection', 'Data Driven', 'Data Engineering', 'Data Ethics', 'Data Exploration',
        'Data Governance', 'Data Imputation', 'Data Integration', 'Data Interpretation', 'Data Lake',
        'Data Lake Management', 'Data Lineage', 'Data Management', 'Data Manipulation', 'Data Migration', 'Data Mining',
        'Data Modeling', 'Data Monetization', 'Data Normalization', 'Data Pipelines', 'Data Preprocessing', 'Data Privacy',
        'Data Profiling', 'Data Quality', 'Data Reporting', 'Data Reshaping', 'Data Science',
        'Data Scrubbing', 'Data Security', 'Data Stewardship', 'Data Storytelling', 'Data Strategy', 'Data Testing',
        'Data Transformation', 'Data Validation', 'Data Visualization', 'Data Warehousing',
        'Data Wrangling', 'Database Design', 'Database Management', 'Data-Driven',
        'Decision-Making', 'Deep Learning', 'Dimensionality Reduction', 'Distributed Computing', 'Django', 'Docker',
        'Domain Knowledge', 'EDA', 'Ensemble', 'Ethical', 'ETL', 'Excel', 'Experimental Design',
        'FastAPI', 'Feature Engineering', 'Feature Scaling', 'Feature Selection', 'flask', 'Frameworks', 'GDPR',
        'Geospatial Analysis', 'Git', 'Gradient Boosting', 'Hadoop', 'Hypothesis Testing', 'Informatica', 'Interpersonal Skills',
        'Kanban', 'Leadership', 'Libraries', 'Machine Learning', 'Mathematics', 'Matplotlib', 'ML', 'Model Deployment',
        'Model Interpretation', 'Natural Language Processing ', 'NLP', 'nltk', 'NoSQL', 'Numpy', 'Pandas', 'Power BI',
        'Predictive Modeling', 'Presentation', 'Privacy compliance', 'Problem Definition', 'Problem Solving',
        'Project Management', 'Project Planning', 'Python', 'PyTorch', 'Quantitative Analysis', 'Query Optimization',
        'R', 'Random Forest', 'Regression Analysis', 'Reinforcement Learning', 'Requirements Gathering',
        'Sampling Techniques', 'Scikit-learn', 'Scrum', 'spacy', 'Spark', 'SQL', 'Stakeholder Management', 'Statistical Analysis',
        'Statistical Testing', 'Statistical Thinking', 'Strategic Thinking', 'Supervised Learning', 'Tableau', 'Teamwork',
        'TensorFlow', 'Text Processing', 'Time Management', 'Time Series',
        'Unsupervised Learning','vba', 'Version Control ', 'Web Scraping', 'Seaborn', 'XGBoost',
]

# meaningless words that should be manually removed
remove_words = ['data','year','least','working','business',
        'tool','position','related','strong','field',
        'minimum','good','salary','work','using','industry',
        'processing','hn','kinh','nghi','experience','relevant'
    ]

file_path_train = os.path.join('dataset', 'Data_Jobs.csv')
file_path_deploy = os.path.join('dataset', 'data_job_new.csv')


nlp = spacy.load('en_core_web_md')
df = pd.read_csv(file_path_deploy)
test = pd.read_csv(file_path_train)

from textblob import Word

def preprocess_dataframe(dataframe, remove_outliers=False):
    # Function for preprocessing job descriptions
    dataframe['Job_Description'] = dataframe['Job_Description'].astype(str)
    dataframe['Job_Title'] = dataframe['Job_Title'].astype(str)
    dataframe = dataframe.dropna(subset=['Job_Description'])

    # Lower case
    dataframe['Job_Description'] = dataframe['Job_Description'].apply(lambda x: " ".join(x.lower() for x in x.split()))

    # Remove tabulation and punctuation
    dataframe['Job_Description'] = dataframe['Job_Description'].str.replace('[^\w\s]',' ')

    # Remove digits
    dataframe['Job_Description'] = dataframe['Job_Description'].str.replace('\d+', '')

    # Remove stop words
    stop = stopwords.words('english')
    dataframe['Job_Description'] = dataframe['Job_Description'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

    # Lemmatization
    dataframe['Job_Description'] = dataframe['Job_Description'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

    if remove_outliers==True:

        # Limit years of experience to a maximum of 10

        dataframe['YOE'] = dataframe['YOE'].apply(lambda x: min(x, 10))
        # Remove the outlier jobs that have Est_Salary larger than $8,000
        dataframe['Est_Salary'] = dataframe['Est_Salary'].apply(lambda x: min(x, 8000))


    return dataframe  # Return the processed DataFrame


