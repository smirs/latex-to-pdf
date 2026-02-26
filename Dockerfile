# Use official Python image
FROM python:3.11-slim

# Install system dependencies (needed for LaTeX)
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-science \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-xetex \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose port
EXPOSE 5000

# Run with production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]