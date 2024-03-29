﻿# Digital Ethnic Futures Lab - SCOTUS College Statement Text Analyis

## Description

This repository contains multiple programs intended to analyze the statements released by select colleges on SCOTUS's ruling on affirmative action.

* 'statement_to_csv.py' utilizes the Google Sheets API to read in data from a column and transform its' contents into individual csv files, stored in folder 'csv_files'
* 'region_finder.py' tags region information and campus size using data from folder 'data_directory' for specified colleges and transforms it into a csv file 'locations_results.csv'
* the 'tfidf' directory contains programs intended to perform term frequency inverse document frequency analysis on our corpus, while the 'sentiment' directory contains programs intended to perform sentiment analysis

## Getting Started
* 'statement_to_csv' depends on a 'credentials.json' file which is not included in this repository for security reasons. This code does not need to be run as the results are stored in 'csv_files'

* 'region_finder' can be ran from the home directory 

* 'tfidf_analysis' needs to be ran from the tfidf directory, and 'vader_sentiment' needs to be run from the sentiment directory

### Dependencies

* This repository deploys 'pandas', 'os', 'vaderSentiment', 'sklearn', 'numpy', 'altair', 'csv', and the 'googleapiclient' packages.
