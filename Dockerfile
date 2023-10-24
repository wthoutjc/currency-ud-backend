FROM public.ecr.aws/sam/build-python3.9:latest

WORKDIR /app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies new files or directories from your Docker client’s current directory.
COPY . .

# Provides defaults for an executing container
CMD ["app.lambda_handler"]
