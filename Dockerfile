FROM ghcr.io/seg-way/segway-connect-system-base-destination/container:1.1.0

COPY etc/syslog-ng/conf.d /etc/syslog-ng/conf.d

COPY python /app/python
RUN . /app/.venv/bin/activate ;\
    pushd /app/python ;\
    poetry export --format requirements.txt | pip --no-cache-dir install -r /dev/stdin
