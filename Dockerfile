#Use Alpine Linux as the docker base. 
FROM azuresdk/azure-cli-python

#Update Alpine image
RUN apk update

#Install some required thingies
RUN apk add python3
RUN pip3 install --upgrade pip

# Copy the web contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /app/requirements.txt

## I would like some ports available to the world outside this container
EXPOSE 80
EXPOSE 443

WORKDIR /app/
# Run app.py when the container launches
CMD ["python3", "app.py"]