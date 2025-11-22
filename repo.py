import subprocess 

print('\n\n\t**UPDATING REPOSITORY**\n\n')    
add = subprocess.run(['git','add','.'])
if add.returncode == 0: 
    print('\n\n\t**git add successful**\n\n')    
    commit  = subprocess.run(['git','commit','-m','update'])
    if commit.returncode == 0:
        print('\n\n\t**git commit successful**\n\n')            
        push = subprocess.run(['git','push'])
        if push.returncode == 0:
            print('\n\n\t**git push successful**\n\n')    
            print('\n\n\t**REPOSITORY UPDATED**\n\n')    
        else :print('\n\n\t**git push failed**\n\n')    
    else :print('\n\n\t**git commit failed**\n\n')    
else: print('\n\n\t**git add failed**\n\n')    

