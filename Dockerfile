FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["ls"]
