import ansible_runner
import json

def main():
    path = "./hosts.yml"
    
    #get inventory 
    inventory_str, war = ansible_runner.interface.get_inventory(action="list", inventories=[path])
    inventory = json.loads(inventory_str)

    #display all 
    hosts = inventory["_meta"]["hostvars"]
    for i in hosts:
        ip = hosts[i]["ansible_host"]
        print(f"{i} has an IP of {ip}")

    #display gorup and host 
    groups = inventory["all"]["children"]
    for j in groups:
        hosts = inventory[j]["hosts"]
        print(f"These Hosts are part of {j}:")
        for host_name in hosts:
            print(f"\t{host_name}")

    #ping command 
    response, err_string, rtn_code = ansible_runner.interface.run_command(executable_cmd="ansible all:localhost -m ping")
    print(f"Response: \n{response}")

if __name__ == "__main__":
    main()
