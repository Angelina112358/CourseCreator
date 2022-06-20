FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000
RUN mkdir /creator
WORKDIR /creator
COPY requirements.txt /creator/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /creator/
ADD . /CourseCreator/
CMD python3 manage.py runserver 0.0.0.0:$PORT