ARG REGISTRY=ghcr.io/seg-way/containers/segway-connect-system-base-destination
ARG BASEVERSION=2.0.0
FROM $REGISTRY:$BASEVERSION as builder


RUN apk add -U --upgrade --no-cache \
    python3-dev \
    libffi-dev

COPY python /app/plugin

RUN python3 -m venv /app/.venv ;\
    . /app/.venv/bin/activate ;\
    cd /app/plugin;\
    poetry install --no-dev -n

FROM $REGISTRY:$BASEVERSION

ENV VIRTUAL_ENV=/app/.venv
COPY --from=builder /app/.venv /app/.venv
COPY etc/syslog-ng/conf.d /etc/syslog-ng/conf.d
COPY python /app/plugin

USER ${uid}:${gid}
