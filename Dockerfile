# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose both ports
EXPOSE 8000   
EXPOSE 8501   

# Install supervisor
RUN pip install supervisor

# Command to run both frontend and backend
CMD ["supervisord", "-c", "/app/supervisord.conf"]
