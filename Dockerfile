# Step 1: Use a lightweight base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /home/data

# Step 3: Copy the Python script and text files into the container
COPY script.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

# Step 4: Create an output directory for results
RUN mkdir -p /home/data/output

# Step 5: Define the command that runs when the container starts
CMD ["python", "script.py"]

