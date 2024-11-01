#!/usr/bin/python3
"""
This example creates a multi-controller network from semi-scratch by
using the net.add*() API and manually starting the switches and controllers.
"""
import mininet.clean as Cleanup
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def ring_topo():
    """ Create AmLight network for tests """
    net = Mininet(topo=None, build=False)
    # Create the hosts
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )
    h3 = net.addHost( 'h3' )
    h4 = net.addHost( 'h4' )

    # Create the switches
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )

    # Add links between the switch and each host
    net.addLink( s1, h1 )
    net.addLink( s2, h2 )
    net.addLink( s3, h3 )
    net.addLink( s1, h4)

    # Add links between the switches
    net.addLink( s1, s2 )
    net.addLink( s2, s3 )
    net.addLink( s3, s1 )

    ctrl = net.addController('ctrl', controller=RemoteController, ip='127.0.0.1', port=6633)

    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # for CLI output
    ring_topo()
    Cleanup.cleanup()
