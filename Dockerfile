# Sample Dockerfile

# Indicates that the windowsservercore image will be used as the base image.
FROM python:3.7

COPY ./* /tsbk
# Copy the requirements and install
COPY requirements.txt /requirements.txt 
RUN pip3 install -r /requirements.txt
# Expose your port
EXPOSE 80
# Set the working directory to your main file
WORKDIR "/tsbk"
# Run the Flask app like you usually do
# CMD ["python", "webservice.py", "--host", "0.0.0.0", "--port", "80"]