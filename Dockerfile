FROM python:3.7
ENV PYTHONUNBUFFERED 1

# geospacials libraries
RUN apt-get update -y && \
        apt-get install -y binutils libproj-dev gdal-bin libgeoip1 gdal-bin python-gdal

# Output version and capabilities by default.
CMD gdalinfo --version && gdalinfo --formats && ogrinfo --formats


# Requirements have to be pulled and installed here, otherwise caching won't work
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt

COPY .start-dev.sh /start-dev.sh
RUN sed -i 's/\r//' /start-dev.sh
RUN chmod +x /start-dev.sh

WORKDIR /app
