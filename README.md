# Predicting Bike Share Usage in London
URL:

This web application can be used to predict usage of city bike shares in London based on weather, date, and time input data. It uses a Flask API and hosted on AWS. It uses a gradient boosted tree model.

This [Jupyter notebook](LondonBikeshare_modelDev.ipynb) includes the code to develop the predictive model, including EDA, data processing, model training, and model evaluation.

[Google Colab](LondonBikeshare_DeepLearning.ipynb) was also used to train a deep neural network on this data in order to explore using Tensorflow in AWS, but this kind of model is ill-suited for this dataset, and was not used in the final web application.

## Web Application
### Enter data
page 1
### Receive a prediction based on input data
page 2
This value is the predicted number bike share rides that will be initiated for a given hour in London.

## Developing the Model
Data was sourced from the [Transport for London](<https://cycling.data.tfl.gov.uk/>) open cycling data. This specific dataset was cleaned by Hristo Mavrodiev and can be downloaded [here](<https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset>).

Several exploratory data analysis techniques were used to understand the dataset and determine which variables would be the most effective to predict the count of bike share rides initiated (cnt).

This scatterplot illustrates the relationship between humidity, hour of the day, and total bike share count per hour.

<img src="https://github.com/Danika-Balas/LondonBikeshare/blob/main/images/scatterplot.png" width="512" />

The heatmap below shows the correlations between each variable.
<img src="https://github.com/Danika-Balas/LondonBikeshare/blob/main/images/heatmap.png" width="512" />

Tempfeel was not selected because it is not independent from temp. The variables **temp**, **windspeed**, **hour**, and **month** were selected as predictors for total hourly rides.

## Deploying to AWS
A. Create Cloud9 env and keys for git
A. check out this repo and cd into it

B. create a python virtualenv and source it and run make all

`python3 -m venv ~/.eb`

`source ~/.eb/bin/activate`

`make all`

Note, that awsebcli is installed via requirements

C. initial new eb app

`eb init -p python-3.7 flask-continuous-delivery --region us-east-2`

To create ssh keys

`eb init`


D. Create remote eb instance

'eb create flask-continuous-delivery-env'

## References

## Future Directions
* Add more validation requirements to Flask query fields, including minimum and maximum values
* Train LSTM model in order to take advantage of time series data
