FROM ghcr.io/seg-way/segway-connect-system-base-destination/container:1.2.2

COPY etc/syslog-ng/conf.d /etc/syslog-ng/conf.d

COPY python /app/plugin
RUN . /app/.venv/bin/activate ;\
    pushd /app/plugin ;\
    poetry install
