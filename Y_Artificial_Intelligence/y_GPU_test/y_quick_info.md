Spark can access GPU using RAPIDS --> need to study further

## OS system wide:
    
    1)  Check if system recognizes the GPU :
        > lspci | grep -iE 'VGA|3D|Display'

## PYTORCH Setup :
    1)  Create a virtual env for python using VENV and activate it .
    2)  Install pytorch :
        > pip install torch

## Pytorch GPU setup 

    1) NVIDIA driver 
        Looks like GPU cannot be recognized from VIRTUAL BOX VM s 
        REF = https://superuser.com/questions/1767605/how-to-access-gpu-from-ubuntu-22-vm-running-in-virtual-box-on-windows-10