FROM python
COPY ./src /app
RUN apt-get update
RUN apt-get install nano
RUN pip install -r /app/requirements.txt
CMD /bin/bash