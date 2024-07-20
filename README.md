# Old-Car-Price-Predictor
The Project aims to predict the price of an old and used car by taking it's details such as it's model name, manufacturing company, year of purchase and  how much it is used.

# Dataset Details:
This dataset contains data of Quikr Cars about second hand cars . 

This data was web scrapped from their website and have data of about 1000 cars and have features like: 

Name 

Company 

Price 

Kms_driven 

Fuel_type


# Workings of the Project
  The dataset was first imported into the Jupyter notebook where it was read using pandas and converted into a Data Frame.

  The Data was then cleaned and preprocessed since it contained lots of gibberish in it such as the columns that had to be numeric sometimes contained non numerical data or had commas in between the digits. It also contained several missing values.

  Some EDA was performed, the outliers were delt with and the data skewness was somewhat normalised, and the cleaned data was exported for further use.

  Then several models were built on top of the cleaned data among which Random Forest Regressor gave the most accurate result.

  Then the model was exported to be used in website built using Flask to perform predictions on the data.
