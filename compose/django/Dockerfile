# Base image
FROM python:3.12 as build

RUN apt-get update && apt-get install -y build-essential curl libpq-dev
ENV VIRTUAL_ENV=/opt/venv \
PATH="/opt/venv/bin:$PATH"

ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh
COPY requirements/requirements.txt .
RUN /root/.local/bin/uv venv /opt/venv && \
/root/.local/bin/uv pip install --no-cache -r requirements.txt


# App image
FROM python:3.12-slim-bookworm
COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y \
# psycopg2 dependencies
libpq-dev \
# Translations dependencies
gettext \
curl \
lsof \
# cleaning up unused files
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*


ARG APPHOME=/app
WORKDIR ${APPHOME}

EXPOSE 8080

RUN mkdir -p ~/bin
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/bin

COPY compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY . ${APPHOME}

ENTRYPOINT [ "/entrypoint" ]
