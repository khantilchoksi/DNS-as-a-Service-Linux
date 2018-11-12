# DNS-as-a-service  

### Linux Networking Project - Fall 2018  

Functional Documentation of Infrastructure automation:  

#### VPC CRUD:  
- Create: Tenant will upload a json file with VPC fields: VPC Name, IP CIDR Block, (provide at least one subnet inside VPC ??) and in return we will provide tenant VPC id of newly created VPC.  
- Read: List down all the VPC ids for a tenant.   
- Update:   
- Delete: Remove the VPC for the tenant. Which may force to destroy deletion of all VMs running inside the VPC?

--------------

#### Subnet CRUD: Ref: 
- Create:  
- Read:  
- Update:  
- Delete:  

----------------
#### VM Instance CRUD:
- Create:   
- Tenant / User will require to fill up a form or json file which has creation parameters like: vcpu, memory, disk size, OS type, VPC id and as result we will create VM for the user, assign IP, (and do we have to provide private key to user ?)  
    - *Command:* `sudo ansible-playbook create_vm.yaml`  
    -   Requirements: vars  
    - Automation:
        - Completely automated VM instance spin up, attach with subnet and will also get ip address from dhcp server from subnet as well as controller network.
        - Provider adming able to ssh to this new vm without any manual ssh keypair generation manual steps.

- Read:
User should be able to ssh inside the VM he/she has requested for. 
- Update:  
Tenant / User should be able to update the VPC id, i.e. putting the existing VM, add interfaces.
Tenant should be able to terminate, restart VM.
- Delete: Destroying the whole VM and free up memory.

-----------------
#### DNS Server CRUD
Create: 
Read:
Update:

-------------------
### References: 
- https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
- Cloudflare DNS: https://www.cloudflare.com/dns/
- Amazon Route 53: https://aws.amazon.com/route53/ 
- NS1 DNS: https://ns1.com/products
- Google Cloud DNS: https://cloud.google.com/dns/
- Azure DNS: https://azure.microsoft.com/en-us/services/dns/
- Rackspace Cloud DNS: https://www.rackspace.com/cloud/dns
- https://www.siteground.com/kb/private_dns/
