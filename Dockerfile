FROM python:3.9.5
WORKDIR /usr/app
COPY ./ /usr/app
RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python", "redditweb.py"]
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]