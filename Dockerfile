# Use the AWS Lambda Python 3.12 base image
FROM public.ecr.aws/lambda/python:3.12

# Set the working directory inside the container
WORKDIR /var/task

# Copy the application files
COPY lambda_app/ lambda_app/
COPY pyproject.toml poetry.lock ./
# Write Docker commands to package your Python application with its dependencies
# so that it can

# tips: a python 'requirements.txt' file to insall the Python dependencies with pip
# can be generated using 'poetry export --without-hashes > lambda_app/requirements.txt'
# before building the image with 'docker build ...'
# Install dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi
# Set CMD so that the entry point of the lambda is the 'lambda_handler' function.
# problem / actual app.py inside lambda_app
CMD ["lambda_app.app.lambda_handler"]