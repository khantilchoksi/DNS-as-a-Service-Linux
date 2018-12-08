import os
import docker
import sys
from time import sleep

dclient = docker.from_env()
if len(sys.argv) < 2:
	print "Insufficient arguments"
	sys.exit()

cid_file = open(sys.argv[1],"r")
cids = cid_file.read()
cids = [t.strip() for t in cids.split()]


while True:
	sleep(10)
	curr_containers = docker.Client().containers(all=True)
	for container in curr_containers:
		if "Exited" in container["Status"]:
			for cid in cids:
				if cid in container["Id"]:
					print "Starting container with id ",container["Id"]
					docker.Client().start(container)





