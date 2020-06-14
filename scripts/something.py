from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import commands, networking
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(
    core={"num_workers": 100},
    inventory={
        "plugin": "nornir.plugins.inventory.ansible.AnsibleInventory",
        "options": {
            "hostsfile": f"{DIRECTORY}/../hosts.yaml"
        }
    },
    logging={
        "enabled": True,
        "level": "debug",
        "to_console": "true"
    }
)

host = nr.inventory.hosts["home-2811-sguilfoil"]
print(host.keys())
exit()

print_result(nr.run(
    task=networking.netmiko_send_command,
    command_string="show access-list",
    use_textfsm=True
))
