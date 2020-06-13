FROM python:3.8.2-buster
LABEL maintainer=sguilfoil1@gmail.com
WORKDIR /opt/network
COPY . .
RUN apt-get update \
    && apt-get install zlib1g-dev vim libxml2-dev libxslt-dev python-dev --no-install-recommends --assume-yes \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/networktocode/ntc-ansible --recursive \
    && python -m pip install --requirement requirements.txt --no-cache \
    && python ntc-ansible/setup.py install \
    && ansible-galaxy install -r requirements.yml
