# Mininet Docker Image

Mininet with OpenFlow and OpenVSwitch in a Docker container. Available resources:
- Supports Python2 and Python3
- Can be used to run mn directly, as well as run a OS command and download a script to run with arguments (thanks to https://github.com/ciena/mininet-docker) - see usage below
- Light-weight docker image based on Debian slim and include tools such as tcpdump, iperf, socat, curl, etc

## Usage

After pull or build the image, you can run:

```
docker run --privileged -v /lib/modules:/lib/modules italovalcy/mininet:latest /usr/local/bin/mn --topo single,3
```

The `/lib/modules` mount volume is necessary to load openvswitch Kernel module required by OVS.

Another option to execute Mininet is with:

```
docker run -d --name mn1 --privileged -v /lib/modules:/lib/modules italovalcy/mininet:latest --topo single,3
```

After running the command above, mininet will start inside tmux on the container, so that you can attach to the container and have access to Mininet's console:

```
docker exec -it mn1 bash
tmux a -t mn
```

You can also run using a topology file:

```
git clone https://github.com/italovalcy/mininet-docker
cd mininet-docker/
docker build -t italovalcy/mininet:latest .
docker run --privileged --name mn1 -d -v $(PWD)/mytopo.py:/mytopo.py italovalcy/mininet:latest file:///mytopo.py
```

Help:
```
prompt$ docker run --privileged italovalcy/mininet:latest --help
docker run italovalcy/mininet [options]
    -h, --help                    display help information
    /path/program ARG1 .. ARGn    execute the specfified local program
    URL ARG1 .. ARGn              download script from URL and execute it
    --ARG1 .. --ARGn              execute mininet with these arguments
```
