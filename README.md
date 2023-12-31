# Digital Ethnic Futures Lab - SCOTUS College Statement Text Analyis

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

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

ex.
* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

ex.
Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)