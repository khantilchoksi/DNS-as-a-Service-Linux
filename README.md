# DNS-as-a-service  

### Linux Networking Project - Fall 2018  

Functional Documentation:
Infrastructure:
VPC CRUD:
Create: Tenant will upload a json file with VPC fields: VPC Name, IP CIDR Block, (provide at least one subnet inside VPC ??) and in return we will provide tenant VPC id of newly created VPC.
Read: List down all the VPC ids for a tenant.
Update: ?
Delete: Remove the VPC for the tenant. Which may force to destroy deletion of all VMs running inside the VPC?
Subnet CRUD: Ref: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
Create:
Read:
Update:
Delete:
VM Instance CRUD:
Create: 
Tenant / User will require to fill up a form or json file which has creation parameters like: vcpu, memory, disk size, OS type, VPC id and as result we will create VM for the user, assign IP, (and do we have to provide private key to user ?)
Read:
User should be able to ssh inside the VM he/she has requested for. 
Update:
Tenant / User should be able to update the VPC id, i.e. putting the existing VM, add interfaces.
Tenant should be able to terminate, restart VM.
Delete:
Destroying the whole VM and free up memory.
DNS Server CRUD
Create: 
Read:
Update:
