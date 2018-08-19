#!/bin/bash
trap '' EXIT INT TERM

function ssh-auto-retry()
{
 echo -e "Connecting to VM...\c"
 ((count = 40))
 while [[ ${count} -ne 0 ]]; do
   echo -e '.\c'
   ssh "$@" >/dev/null 2>&1 || (sleep 4; exit 1)
   rc=$?
   if [[ $rc -eq 0 ]]; then
     ((count = 1))
   fi
   ((count = count -1))
 done
}

function terminate() {
 trap '' EXIT INT TERM
 echo -e "\nTearing down VM..."
 aws ec2 terminate-instances --instance-ids ${id} >/dev/null 2>&1 
 exit 1
}

echo "Creating a VM for you..."
props=$(aws ec2 run-instances --count 1 --instance-type t2.micro --image-id ami-example --key-name ctf --security-group-ids sg-example --subnet-id subnet-example --no-associate-public-ip-address)

ip=$(echo ${props} | jq -r '.Instances[].PrivateIpAddress')
id=$(echo ${props} | jq -r '.Instances[].InstanceId')

trap terminate EXIT INT TERM

ssh-auto-retry -t -o StrictHostKeyChecking=no -o ConnectTimeout=1 ecorp@${ip}

exit 0