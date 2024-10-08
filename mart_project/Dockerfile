FROM python:3.12

# Poetry install karein
RUN pip install poetry

WORKDIR /app
COPY . /app/

# Required packages install karein
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

# Poetry configuration
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev 

# Expose the port
EXPOSE 8000

# Yahan 'user.user:app' ko run karne ke liye modify kiya
CMD ["poetry", "run", "uvicorn", "mart_project.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
