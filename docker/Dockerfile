FROM python:3.7

ENV PYTHONUNBUFFERED=1 \
    DEV=FALSE

COPY dist/eastecho-*.tar.gz /tmp/
COPY static /opt/eastecho/static
COPY templates /opt/eastecho/templates
COPY uwsgi.ini /etc/
COPY migrate.sh /usr/local/bin/

RUN pip install uwsgi \
 && pip install /tmp/eastecho-*.tar.gz \
 && rm /tmp/eastecho-*.tar.gz \
 && adduser --no-create-home --uid 101 --system nginx
RUN mkdir /opt/eastecho/media \
 && chown -R nginx /opt/eastecho \
 && chown -R nginx /usr/local/lib/python3.7/site-packages/eastecho/site/migrations \
 && cp -R /usr/local/lib/python3.7/site-packages/django/contrib/admin/static/admin /opt/eastecho/static/admin

EXPOSE 8000
USER nginx
VOLUME /opt/eastecho

CMD ["uwsgi", "--ini", "/etc/uwsgi.ini"]
