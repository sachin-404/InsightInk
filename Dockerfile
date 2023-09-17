FROM python:3.12-rc-buster
WORKDIR /InsightInk
COPY requirements.txt /InsightInk/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /InsightInk/
RUN cd Blog && python manage.py migrate
EXPOSE 8000
CMD ["python", "Blog/manage.py", "runserver", "0.0.0.0:8000"]
