FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3 \
    python3-pip \
    wget \
    bash \
    net-tools \
    netbase \
    strace \
    iproute2 \
    iputils-ping \
    pciutils \
    vim  \
    libibverbs-dev  \
    libibverbs1  \
    ethtool  \
    sudo \
    tcpdump \
    libpthread-stubs0-dev

RUN wget --no-check-certificate https://trex-tgn.cisco.com/trex/release/v3.02.tar.gz && \
    tar -zxvf v3.02.tar.gz -C / && \
    chown root:root /v3.02  && \
    rm v3.02.tar.gz

ENV PYTHONPATH=/v3.02/automation/trex_control_plane/interactive

WORKDIR /v3.02