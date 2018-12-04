import os
from time import sleep

num_vms_del = input("Enter the number of vms to delete\n")
vm_names = []

for vm in range(num_vms_del):
	vm_names.append(raw_input("Enter the vm "+str(vm+1)+" name\n"))

print "Deleting VMs\n"

for vm_name in vm_names:
	os.system("sudo virsh destroy " + vm_name)
	sleep(0.5)
	os.system("sudo virsh undefine " + vm_name)
	sleep(0.5)

num_veth_del = input("Enter the number of subnets to delete\n")
veth_names = []

netns_name = ""
if num_veth_del > 0:
	netns_name = raw_input("Enter the vpc in which they exist\n")

for veth in range(num_veth_del):
	veth_names.append(raw_input("Enter the subnet "+str(veth+1)+" name\n"))


print "Deleting subnets\n"

for veth_name in veth_names:
	os.system("sudo ip link del "+veth_name+"vif2")
	os.system("sudo virsh net-destroy "+veth_name)
	os.system("sudo ifconfig "+veth_name+" down")
	os.system("sudo brctl delbr "+veth_name)
	os.system("sudo virsh net-undefine "+veth_name)

vpc_del = raw_input("Would you like to delete the vpc ? (yes/no)\n")

if vpc_del == "yes":
	if len(netns_name) > 0:
		os.system("sudo ip netns exec provider_ns ip link del "+netns_name[:-3]+"vif2")
		os.system("sudo ip netns del "+netns_name)
	else:
		netns_name = raw_input("Enter the vpc name\n")
		os.system("sudo ip netns exec provider_ns ip link del "+netns_name[:-3]+"vif2")
		os.system("sudo ip netns del "+netns_name)
	sleep(0.5)

elif vpc_del != "no":
	print "Invalid option"

	











