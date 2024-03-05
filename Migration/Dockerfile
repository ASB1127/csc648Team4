FROM python:3.8.1-slim 

ENV PYTHONUNBUFFERED 1 
EXPOSE 22 8000  
WORKDIR /app 
COPY ./requirements_v2.txt .
COPY ./src . 
RUN pip install -r requirements_v2.txt
RUN apt-get clean && apt-get update
RUN pip install markupsafe==2.0.1
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "webserver:app"]  
