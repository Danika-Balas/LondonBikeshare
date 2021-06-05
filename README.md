# LondonBikeshare--Deploying on AWS

## Deployment
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
