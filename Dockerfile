# 1. Base image
FROM python:3.11-slim

# 2. Ensure Streamlit writes config inside /app, not /
ENV HOME=/app

# 3. Set working directory
WORKDIR /app

# 4. Copy everything
COPY . /app

# 5. Create the Streamlit config directory
RUN mkdir -p /app/.streamlit

# 6. Write a minimal config.toml to disable CORS and set port
RUN printf "[server]\nheadless = true\nport = 7860\nenableCORS = false\n" \
     > /app/.streamlit/config.toml

# 7. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 8. Expose the port Streamlit will run on
EXPOSE 7860

# 9. Launch the app
CMD ["streamlit", "run", "app.py", "--server.port=7860"]
