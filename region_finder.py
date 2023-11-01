import os
import pandas as pd

# Specify the directory containing the CSV files for each region
data_directory = 'data_directory'

# list of colleges
colleges_to_search = ["California Institute of Technology","Harvard University","Columbia University","Massachusetts Institute of Technology","Stanford University","Brown University","Curtis Institute of Music","University of Chicago","Yale University","Dartmouth College","Duke University","Princeton University","Amherst College","Cornell University","Johns Hopkins University","Northeastern University","Northwestern University","Pomona College","Swarthmore College","University of Pennsylvania","Vanderbilt University","Colby College","Williams College","Barnard College","Bowdoin College","Johnson C. Smith University","Rice University","University of California, Los Angeles","Claremont McKenna College","Juilliard School","Tufts University","Carnegie Mellon University","Emory University","Grinnell College","Tulane University","United States Naval Academy","University of California, Berkeley","Washington University in St. Louis","Colgate University","Georgetown University","Hamilton College","New York University","St. Andrews University","United States Military Academy at West Point","University of Southern California","Alice Lloyd College","Harvey Mudd College","Middlebury College","Pacific Oaks College","United States Air Force Academy","University of Notre Dame","Bates College","Boston University","Colorado College","Faulkner University","Haverford College","Wellesley College","Wesleyan University","United States Coast Guard Academy","Boston College","Carleton College","Davidson College","Georgia Institute of Technology","Harris-Stowe State University","University of North Carolina at Chapel Hill","Washington and Lee University","Pitzer College","University of Michigan--Ann Arbor","Franklin W. Olin College of Engineering","Rhode Island School of Design","University of Miami","University of Virginia","Vassar College","College of the Ozarks","Hillsdale College","University of California, Irvine","Wake Forest University","Webb Institute","Babson College","Cooper Union for the Advancement of Science and Art","Denison University","Smith College","University of Florida","Villanova University","University of California, San Diego","University of Richmond","Berea College","Florida State University","Kettering College","Skidmore College","University of California, Santa Barbara","University of Tampa","Case Western Reserve University","Macalester College","Scripps College","Spelman College","California Institute of the Arts","Thomas University","United States Merchant Marine Academy","Tuskegee University"]
# results dictionary
results = {}

# loop through each region (csv file) and check for matches
for filename in os.listdir(data_directory):
    if filename.endswith(".csv"):
        region = os.path.splitext(filename)[0]  # region name extracted from file name
        file_path = os.path.join(data_directory, filename)

        # read file into df
        df = pd.read_csv(file_path)

        
        for college in colleges_to_search:
            # regex to match strings
            matching_colleges = df[df['Name'].str.contains(college, case=False, na=False, regex=False)]

            # add matches
            if not matching_colleges.empty:
                for _, row in matching_colleges.iterrows():
                    results[college] = {
                        'Region': region,
                        'Campus Size': row['Campus setting']
                    }


for college, info in results.items():
    print(f"College: {college}, Region: {info['Region']}, Campus Size: {info['Campus Size']}")

print(len(results))

df = pd.DataFrame.from_dict(results, orient="index")

csv_file_path = "locations_results.csv"

#save to csv
df.to_csv(csv_file_path)

print(f"Results saved to {csv_file_path}")