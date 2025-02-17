import sys
import subprocess as sp

import compiling
from utils import call_cmd_and_print_cmd, source

def emerge_base():
    call_cmd_and_print_cmd('emerge-webrsync')
    call_cmd_and_print_cmd('emerge --oneshot sys-apps/portage')

    call_cmd_and_print_cmd('emerge app-portage/gentoolkit')

    #print(call_cmd_and_print_cmd('eselect profile list'))
    #print('select profile:')
    #profile_choice = sp.check_output('read -t 20 CHOICE; [ -z $CHOICE ] && echo 6 || echo $CHOICE', shell=True).strip().decode()
    #call_cmd_and_print_cmd(f'eselect profile set --force {profile_choice}')
    #print(call_cmd_and_print_cmd('eselect profile list'))

    call_cmd_and_print_cmd('emerge app-portage/cpuid2cpuflags')
    call_cmd_and_print_cmd('echo "*/* $(cpuid2cpuflags)" > /etc/portage/package.use/00cpu-flags')


def install(boot_device: str):
    source('/etc/profile')
    call_cmd_and_print_cmd(f'mount {boot_device} /boot')
    emerge_base()
    compiling.compile()
    call_cmd_and_print_cmd('rc-update add dhcpcd default')
    call_cmd_and_print_cmd('rc-update add lvmetad boot')
