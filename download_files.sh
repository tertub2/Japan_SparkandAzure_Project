scp -i myVm_key.pem -rp azureuser@20.197.230.71:home/azureuser/output src/output

mv azureuser/output/* src/output

