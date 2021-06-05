# Predicting Bike Share Usage in London
URL:

This web application can be used to predict usage of city bike shares in London based on weather, date, and time input data. It uses a Flask API and hosted on AWS. It uses a gradient boosted tree model.

This [Jupyter notebook](LondonBikeshare_modelDev.ipynb) includes the code to develop the predictive model, including EDA, data processing, model training, and model evaluation.

[Google Colab](LondonBikeshare_dl.ipynb) was also used to train a deep neural network on this data in order to explore using Tensorflow in AWS, but this kind of model is ill-suited for this dataset, and was not used in the final web application.

## Web Application
### Enter data
page 1
### Receive a prediction based on input data
page 2
This value is the predicted number bike share rides that will be initiated for a given hour in London.

## Developing the Model
Data was use from ___
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
