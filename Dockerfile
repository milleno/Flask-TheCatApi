FROM python:3.8.6
RUN python -m venv venv venv\Scripts\activate
RUN pip install --upgrade pip
COPY app.py /app.py
COPY cat_api.py /cat_api.py
COPY README.md /README.md
COPY templates /templates
COPY static /static
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python","app.py"]
