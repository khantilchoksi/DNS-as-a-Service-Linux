import os
import docker
import json

#DEL a normal container
def del_container(c_name, t_id):
	curr_containers = docker.Client().containers()
	
	#Removing the container
	for container in curr_containers:
		if container["Names"][0][1:] == c_name:
			docker.Client().remove_container(container ,force=True)
			print "Removing the container with ",c_name

	#Remove from config file
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/vms_db.json", "r")
	vms = json.loads(vm_file.read())
	vm_file.close()

	for vm_name in vms.keys():
		#print vm_name, c_name
		if vm_name == c_name:
			print "Removing ", c_name," from config file"
			del vms[vm_name]
	
	#Update config file
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/vms_db.json", "w")
	vm_file.write(json.dumps(vms))
	vm_file.close()

#DEL a dns container
def del_dns_container(c_name, t_id):
	curr_containers = docker.Client().containers()
	
	#Removing the container
	for container in curr_containers:
		if container["Names"][0][1:] == c_name:
			docker.Client().remove_container(container ,force=True)
			print "Removing the dns container with ",c_name

	#Remove from config file
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/dns_db.json", "r")
	vms = json.loads(vm_file.read())
	vm_file.close()

	for vm_name in vms.keys():
		#print vm_name, c_name
		if vm_name == c_name:
			print "Removing ",c_name," from config file"
			del vms[vm_name]
	
	#Update config file
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/dns_db.json", "w")
	vm_file.write(json.dumps(vms))
	vm_file.close()



#DEL a subnet
def del_subnet(subnet_name, t_id):
	#First delete all vms in that subnet
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/vms_db.json", "r")
	
	vms = json.loads(vm_file.read())
	vm_file.close()
	
	for vm_name in vms:
		if vms[vm_name][t_id]["subnet_name"] == subnet_name:
			print "Found ",vm_name," to be in subnet ",subnet_name
			del_container(vm_name, t_id)
	
	#Next delete all dns vms in that subnet
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/dns_db.json", "r")
	
	vms = json.loads(vm_file.read())
	vm_file.close()
	
	for vm_name in vms:
		if vms[vm_name][t_id]["subnet_name"] == subnet_name:
			print "Found dns ",vm_name," to be in subnet ",subnet_name
			del_dns_container(vm_name, t_id)

	#Now delete the subnet
	sub_file = open("/home/ece792/tenants/"+str(t_id)+"/subnet_db.json", "r")
	subs = json.loads(sub_file.read())
	sub_file.close()
	
	for subnet_n in subs.keys():
		#print subnet_n
		if subnet_n == subnet_name:
			print "Removing from config for subnet ",subnet_name
			del subs[subnet_n]
			
	sub_file = open("/home/ece792/tenants/"+str(t_id)+"/subnet_db.json", "w")
	sub_file.write(json.dumps(subs))
	sub_file.close()
	os.system("sudo ifconfig "+subnet_name+" down")
	os.system("sudo brctl delbr "+subnet_name)

#DEL a vpc
def del_vpc(vpc_name, t_id):
	#First delete all subnets in that vpc
	sub_file = open("/home/ece792/tenants/"+str(t_id)+"/subnet_db.json", "r")
	
	subs = json.loads(sub_file.read())
	sub_file.close()
	
	for subnet_n in subs:
		if subs[subnet_n][t_id]["vpc_name"] == vpc_name:
			print "Found ", subnet_n," to be in vpc ",vpc_name
			del_subnet(subnet_n, t_id)
	
	#Now delete the vpc
	vpc_file = open("/home/ece792/tenants/"+str(t_id)+"/vpc_db.json", "r")
	vpcs = json.loads(vpc_file.read())
	vpc_file.close()
	
	for vpc_n in vpcs.keys():
		#print vpc_n
		if vpc_n == vpc_name:
			print "Removing from config file for vpc ",vpc_name
			del vpcs[vpc_n]
			
	vpc_file = open("/home/ece792/tenants/"+str(t_id)+"/vpc_db.json", "w")
	vpc_file.write(json.dumps(vpcs))
	vpc_file.close()
	os.system("sudo ip netns del "+vpc_name+"_ns")

t_id = raw_input("Enter your tenant ID\n")
t_id = "t"+t_id

del_type = input("Enter (1) for VPC\n(2) for subnet\
					\n(3) for container\n")

if del_type == 1:
	vpc_name_todel = raw_input("Enter the vpc name")
	del_vpc(vpc_name_todel, t_id)
elif del_type == 2:
	subnet_todel = raw_input("Enter the sub name")
	del_subnet(subnet_todel, t_id)
elif del_type == 3:
	container_todel = raw_input("Enter the instance name")
	del_container(container_todel, t_id)
	del_dns_container(container_todel, t_id)

