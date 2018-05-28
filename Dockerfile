FROM dh99/gpio-base

RUN apt-get update -y
RUN apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libjpeg-dev

#RUN pip install --upgrade luma.core luma.led_matrix

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]