# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV STREAMLIT_HOME=/app

# Set working directory
WORKDIR $STREAMLIT_HOME

# Copy everything into the container
COPY . .

# Create writable .streamlit directory inside /app
RUN mkdir -p $STREAMLIT_HOME/.streamlit

# Set Streamlit config to avoid permission issues
RUN echo "\
[server]\n\
headless = true\n\
port = 7860\n\
enableCORS = false\n\
\n\
" > $STREAMLIT_HOME/.streamlit/config.toml

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
