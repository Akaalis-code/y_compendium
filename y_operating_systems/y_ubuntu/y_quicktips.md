## RANDOM STUFF :
    0)  Check the version of ubuntu you are using :
        >lsb_release -a         (Confirm its authenticity later )

    1)  Check which UBUNTU DESKTOP are you using :
        > echo $XDG_CURRENT_DESKTOP
    
    2)  Check List of all PCI connected HARDWARE :
        > lspci
    
    3)  Check for Graphics drivers :
        > lspci | grep -iE 'VGA|3D|Display'

## APT :
    Advanced Packaging Tool is a package manager in Debian-based Linux distributions
    
    To install any package 
        > sudo apt install <Package_name>

    To check all the installed packges through apt 
        > apt list --installed                                      # Gives all installed packages
        > apt list | grep -i <any_package_you_are_looking_for>      # Grep helps you filter out with the package name you are looking for

    To uninstall the apt installed package 
        > sudo apt remove <package_name>        # This only uninstalls the package but any local confguratons will stay
        > sudo apt purge <package_name>         # This will remove any pre existing config files 
        > sudo apt autoremove                   # This will remove any unused dependent libraries that were auto installed

## Vulnerabilities fix and checks :
    
## Get file or folder sizes 
    
    Use "du" command which is short for (disk usage)
    To get how to use "du" command run below command
        > du --help 
    Generally if you want to find out size of any folder run below 
        > du -sh <folder_name_or_path>        # 's' argument simplifies and summarizes the output 'h' displays size in human readable form
        > du -sh *                            # '*' is used to get sizes of all files and folders under this folder


## Different ways of running shell files :

    SET1 type of running:
        sh     my_shell_file.sh              # Uses SHEEL INTERPRETER
        bash   my_shell_file.sh              # Uses BOURNE AGAIN SHELL INTERPRETER 
        ./     myshell_file.sh               # Uses Which ever INTERPRETER was mentioned inside file using SHABANG

    SET2 type of running
        .      my_shell_file.sh
        source my_shell_file.sh

    The first set of commands where explicit mentioning of which shell interpreters to use will create new SHELL SESSIONS
    Where variables and functions defined in one SHELL SESSION will not be known to PARENT SHELL SESSION or others

    Where as in the second set , the main SHELL SESSION where the cmd is being run from , will stay as the SESSION
    for running the cmds that are inside the my_shell_file.sh



## PROCESS vs SERVICE vs DAEMONS     -->> Subject to corrections 

    PROCESS  = Any code that is running , either in background or in foreground . 
               May it be small code snippets or entire applications

    SERVICE  = A "PROCESS" whose purpose is to do some function and run continuously .
               Typically but not necessarily are expected to run in Background.
               Most SERVICES are invoked by "SYSTEM INIT" (system initialization process like SYSTEMD , SysVinit , Upstart)
               
    DAEMON   = A SERVICE which is more emphasized on running in the background like the ghost , hence the name .

## KERNEL INFO :

        To get some basic SYSTEM kernel and software info being used :

            > uname -a 

            Care full with the "Network node name" that it gives ,
            Its PII so keep it private .

## Installing VIRTUALBOX on ubuntu  :


## Installing VMWARE on ubuntu  :

    Summary : 

        Before 2023 for free usage of vmware , we were supposed to download "PLAYER" version with diminished functionalities ,
        and for full functionalities we wered supposed to install "PRO" version along wiith buying license .

        After 2023  "PRO" itself is being made available for free for non comercial use , so "PLAYER" is being discontinued .


        PRO : 
            VMware Workstation Pro : for Windows and Linux
            VMware Fusion pro : For mac
        
        PLAYER : 
            VMware Workstation Player : for Windows and Linux
            VMware Fusion player : For mac
    

    ### Installation steps :

            1)  Download the bundle file from broadcome website after creating an account .
            2)  sudo apt update 
            3)  sudo apt install build-essential
            4)  sudo apt install dkms linux-headers-$(uname -r)
                Not sure on above commands legitamacy .

            5)  chmod +x VMware-Workstation-Full-17.6.2-24409262.x86_64.bundle
                Make file runnable 



        