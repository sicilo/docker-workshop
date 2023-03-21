# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN EXPORT AWS_ACCESS_KEY_ID=AKIAURNT75V5ZRPNRFVY
RUN EXPORT AWS_SECRET_ACCESS_KEY=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
RUN EXPORT AWS_REGION=us-east-2

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./server.py" ]