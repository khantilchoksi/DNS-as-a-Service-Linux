import os
import docker
import json

#Display a normal container
def disp_container(c_name, t_id):
	curr_containers = docker.Client().containers()
	#Displaying the container
	for container in curr_containers:
		if container["Names"][0][1:] == c_name:
			print "\nContainer_name : ", c_name
			print "Status : ", container["Status"]
			print "Image : ", container["Image"]
			print "Id : ", container["Id"]
			print "Ip : ", container["NetworkSettings"]["Networks"]["bridge"]["IPAddress"]
			
#Display a dns container
"""def disp_dns_container(c_name, t_id):
	curr_containers = docker.Client().containers()
	
	#Displaying the container
	for container in curr_containers:
		if container["Names"][0][1:] == c_name:
			print "DNS container"
			print container
"""

#Display a subnet
def disp_subnet(subnet_name, t_id):
	#First display all vms in that subnet
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/vms_db.json", "r")
	
	vms = json.loads(vm_file.read())
	vm_file.close()
	
	for vm_name in vms:
		if vms[vm_name][t_id]["subnet_name"] == subnet_name:
			print "\nFound ",vm_name," to be in subnet ",subnet_name
			disp_container(vm_name, t_id)
	
	#Next display all dns vms in that subnet
	vm_file = open("/home/ece792/tenants/"+str(t_id)+"/dns_db.json", "r")
	
	vms = json.loads(vm_file.read())
	vm_file.close()
	
	for vm_name in vms:
		if vms[vm_name][t_id]["subnet_name"] == subnet_name:
			print "\nFound (dns) ",vm_name," to be in subnet ",subnet_name
			disp_container(vm_name, t_id)

	#Now display the subnet
	sub_file = open("/home/ece792/tenants/"+str(t_id)+"/subnet_db.json", "r")
	subs = json.loads(sub_file.read())
	sub_file.close()
	
	for subnet_n in subs.keys():
		#print subnet_n
		if subnet_n == subnet_name:
			print "\nSubnet name : ", subs[subnet_n][t_id]["subnet_name"]
			print "DHCP range : ", subs[subnet_n][t_id]["dhcp_range"]
			print "Subnet range : ", subs[subnet_n][t_id]["subnet_range"]
			
#Display a vpc
def disp_vpc(vpc_name, t_id):
	#First display all subnets in that vpc
	sub_file = open("/home/ece792/tenants/"+str(t_id)+"/subnet_db.json", "r")
	
	subs = json.loads(sub_file.read())
	sub_file.close()
	
	for subnet_n in subs:
		if subs[subnet_n][t_id]["vpc_name"] == vpc_name:
			print "\nFound ", subnet_n," to be in vpc ",vpc_name
			disp_subnet(subnet_n, t_id)
	
	#Now display the vpc
	vpc_file = open("/home/ece792/tenants/"+str(t_id)+"/vpc_db.json", "r")
	vpcs = json.loads(vpc_file.read())
	vpc_file.close()
	
	for vpc_n in vpcs.keys():
		#print vpc_n
		if vpc_n == vpc_name:
			print "\nVPC name : ", vpcs[vpc_name][t_id]["vpc_name"]
			print "Provider gateway : ", vpcs[vpc_name][t_id]["provider_gateway"]
			print "VPC gateway : ", vpcs[vpc_name][t_id]["vpc_gateway"]

#disp_vpc("t7vpc", "t7")
			
t_id = raw_input("Enter your tenant ID\n")
t_id = "t"+t_id

disp_type = input("Display script \nEnter (1) for VPC\n(2) for subnet\
					\n(3) for container\n")

if disp_type == 1:
	vpc_name_todisp = raw_input("Enter the vpc name\n")
	disp_vpc(vpc_name_todisp, t_id)
elif disp_type == 2:
	subnet_todisp = raw_input("Enter the sub name\n")
	disp_subnet(subnet_todisp, t_id)
elif disp_type == 3:
	container_todisp = raw_input("Enter the instance name\n")
	disp_container(container_todisp, t_id)










