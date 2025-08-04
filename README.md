The marketing_campaign.xlsx dataset was cleaned and preprocessed using Python, leveraging the Pandas library for data manipulation and OpenPyXL for reading Excel files. The original file contained tab-separated values embedded within a single Excel column, along with inconsistent formatting and missing headers.

To prepare the data for analysis:

The first row was extracted and set as column headers.

Column names were standardized by stripping whitespace, converting to lowercase, and replacing spaces with underscores.

Duplicate records were removed.

Numeric columns such as income and year_birth were converted to appropriate types, with missing values in income imputed using the column median.

The dt_customer column was parsed correctly as a datetime field using day-first formatting.

Text fields like education and marital_status were cleaned and standardized.

A new age column was derived from year_birth.

Optionally, scaling of numeric columns was performed using MinMaxScaler from the scikit-learn library to normalize values for downstream machine learning tasks.

The final output, cleaned_preprocessed_data.csv, is a clean, structured, and analysis-ready dataset suitable for tasks such as exploratory data analysis (EDA), predictive modeling, or dashboard visualization.
