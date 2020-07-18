# Mininet Docker Image

Mininet with OpenFlow and OpenVSwitch in a Docker container. Available resources:
- Supports Python2 and Python3
- Can be used to run mn directly, as well as run a OS command and download a script to run with arguments (thanks to https://github.com/ciena/mininet-docker) - see usage below
- Light-weight docker image based on Debian slim and include tools such as tcpdump, iperf, socat, curl, etc

## Usage

After pull or build the image, you can run:

	docker run --privileged italovalcy/mininet:2.3.0d6 --topo single,3

You can also run using a topology file:

	docker run --privileged --name mn1 -d italovalcy/mininet:2.3.0d6 /usr/bin/tail -f /dev/null
	docker cp mytopo.py mn1:/
	docker exec -it mn1 python3 /mytopo.py

Help:
```
prompt$ docker run --privileged italovalcy/mininet:2.3.0d6 --help
docker run italovalcy/mininet [options]
    -h, --help                    display help information
    /path/program ARG1 .. ARGn    execute the specfified local program
    URL ARG1 .. ARGn              download script from URL and execute it
    --ARG1 .. --ARGn              execute mininet with these arguments
```
