# Mostly verbatim from http://docs.ansible.com/ansible/developing_api.html#python-api-2-0
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars import VariableManager
from collections import namedtuple

Options = namedtuple('Options', [
    'connection',
    'module_path',
    'forks',
    'become',
    'become_method',
    'become_user',
    'check',
    'remote_user',
    'private_key_file',
    'ssh_common_args',
    'sftp_extra_args',
    'scp_extra_args',
    'ssh_extra_args',
    'verbosity',
])

# initialize needed objects
variable_manager = VariableManager()
loader = DataLoader()

options = Options(
    connection=None,
    module_path=None,
    forks=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    remote_user=None,
    private_key_file=None,
    ssh_common_args=None,
    sftp_extra_args=None,
    scp_extra_args=None,
    ssh_extra_args=None,
    verbosity=None,
)

passwords = dict(vault_pass='secret')

# create inventory and pass to var manager
inventory = Inventory(
    loader=loader,
    variable_manager=variable_manager,
    host_list='localhost'
)
variable_manager.set_inventory(inventory)

# create play with tasks
play_source = dict(
    name="Ansible Play",
    hosts='localhost',
    gather_facts='no',
    tasks=[
        dict(
            action=dict(module='shell', args='ls'), register='shell_out'
        ),
        dict(
            action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))
        )
    ])
play = Play().load(
    play_source,
    variable_manager=variable_manager,
    loader=loader
)

# actually run it
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback='default',
    )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()
