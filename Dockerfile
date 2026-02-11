# Use Python official image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 10000

# Streamlit runs on Render's PORT variable
ENV PORT=10000

# Streamlit server startup
CMD ["streamlit", "run", "app.py", "--server.port=10000", "--server.address=0.0.0.0"]
