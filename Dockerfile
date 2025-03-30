FROM python:3.12-slim

WORKDIR /myAPI
COPY . /app
COPY  requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# RUN python -m venv /venv && \
    # /venv/bin/pip install --upgrade pip &&\ 
    # /venv/bin/pip install -r requirements.txt
EXPOSE 5000

# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
