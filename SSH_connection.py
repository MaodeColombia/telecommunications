#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('<I.P.>', port=22, username='<>', password='<>',timeout=4)

entrada, salida, error = ssh_client.exec_command('show signaling sccp destination-point-code all')

for line in salida.readlines():
    print (line)


# In[ ]:
