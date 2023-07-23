FROM ghcr.io/seg-way/containers/segway-connect-system-base-destination:1.4.2

COPY etc/syslog-ng/conf.d /etc/syslog-ng/conf.d

COPY python /app/plugin
RUN . /app/.venv/bin/activate ;\
    pushd /app/plugin ;\
    poetry install
