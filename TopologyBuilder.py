#!/usr/bin/python					
""" 

This script creates a star topology consisting of one switch and n hosts

@author: OC2 Laboratory, Western University

"""
																				 
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI


propag_delay = 50
bandwidth = 1

class CreateTopo(Topo):
	
	def build(self, n):
		
		s1 = self.addSwitch('s1')
				
		for h in range(1,n+1):
			
			host = self.addHost('h%s' % h)						
			d = str(propag_delay)+'ms'				
			bw = bandwidth						
			self.addLink(host, s1, bw=bw, delay=d)	  	
		
def main():

	print ('Setting up network emulation environment...')
				
	setLogLevel('info')   										# Shows Mininet info
	n = 3					  										# Number of hosts
	topo = CreateTopo(n)					
	net = Mininet(topo, link=TCLink, autoSetMacs=True)			# Using Traffic Control links to add loss
	net.start()

	h = []
	
	for i in range(1,n+1):
		h.append(net['h%s' % i])
		
	print ('Testing connectivity among hosts...')

	net.pingAll()

	print ('Network ready to run experiments!')
	
	CLI( net)
	net.stop()

	print ('Network emulation finished!')

if __name__ == "__main__":
  main()