#!/usr/bin/env bash

print_if_verbatim(){
    if ! [ -z "$VERBOSE" ]; then
        eval "$@"
    fi
}


source /etc/profile

BOOT_PARTITION="$(lsblk | sed -n '/\/boot/ s@.*\(sd[a-z][0-9]\).*@\1@p')"

mount /dev/"${BOOT_PARTITION}" /boot

emerge-webrsync
emerge --sync
emerge --oneshot sys/apps/portage

eselect profile list

printf 'select profile: '
read profile_choice

eselect profile set "${profile_choice}"

eselect profile list

./compiling
