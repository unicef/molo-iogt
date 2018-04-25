ARG MOLO_VERSION=4
FROM praekeltfoundation/molo-bootstrap:${MOLO_VERSION}-onbuild

ENV DJANGO_SETTINGS_MODULE=iogt.settings.docker \
    CELERY_APP=iogt

COPY startup /opt/startup

COPY startup/sshd_config /etc/ssh/

RUN LANGUAGE_CODE=en django-admin compilemessages && \
    django-admin collectstatic --noinput && \
    django-admin compress

CMD ["iogt.wsgi:application", "--timeout", "1800"]

# ------------------------
# SSH Server support
# ------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd

RUN chmod 755 /opt/startup/init_container.sh

EXPOSE 2222 80

ENTRYPOINT ["/opt/startup/init_container.sh"]
