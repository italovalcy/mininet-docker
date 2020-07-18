FROM debian:buster-slim
MAINTAINER Italo Valcy <italovalcy@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests openvswitch-switch curl iproute2 iputils-ping net-tools tcpdump x11-xserver-utils xterm iperf socat telnet

RUN apt-get -y --no-install-recommends install git-core ca-certificates patch
WORKDIR /usr/src
RUN git clone https://github.com/mininet/mininet \
  && cd mininet \
  && git checkout 2.3.0d6 \
  && sed -e 's/sudo //g' \
	 -e 's/DEBIAN_FRONTEND=noninteractive //g' \
	 -e 's/\(apt-get -y -q install\)/\1 --no-install-recommends --no-install-suggests/g' \
         -i ./util/install.sh \
  && ./util/install.sh -f \
  && PYTHON=python2 ./util/install.sh -n \
  && PYTHON=python3 ./util/install.sh -n \
  && cd .. && rm -rf mininet openflow \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 6633 6653 6640

ENTRYPOINT ["/docker-entrypoint.sh"]
