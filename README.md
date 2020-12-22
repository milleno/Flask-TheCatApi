## The Cat Api 

API created using Flask and [The Cat API](https://thecatapi.com/)

### Usage

Create a Dockerfile file, using the following content:

```
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
```

### Installation

Generating the Container

```bash
docker image build -t python-thecatapi .
```

Running the Container
```bash
docker run -p 5000:5000 -d python-thecatapi
```

To check the result, access the url http://localhost:5000 and browse the menu

### Architecture
```
_________________app.py

_________________cat_api.py

_________________templates
├── base.html
├── breed.html
├── breeds.html
├── hat.html
├── index.html
├── log.log
└── sunglasses.html
____________________static
└── css
    └── style.css
```
### Menu - Metrics

Use the credentials u:`admin`, p:`admin` to log in.

### Screenshots

![Screenshot 1](/img/dash01.png)
![Screenshot 2](/img/dash02.png)
![Screenshot 3](/img/log01.png)

## Contributing
Milleno Matos Ferreira (millenomatos@gmail.com)
