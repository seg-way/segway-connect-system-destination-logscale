FROM ghcr.io/seg-way/containers/segway-connect-system-base-destination:2.0.0-next-major.5

COPY etc/syslog-ng/conf.d /etc/syslog-ng/conf.d

COPY python /app/plugin
RUN cd /app/plugin ;\
    poetry config virtualenvs.create false ;\
    poetry install -n --no-ansi --no-dev ;\
    pip cache purge
USER ${uid}:${gid}
