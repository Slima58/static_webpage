import os
import shutil

def copy_files_recursive(source_d, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    print(os.listdir(source_d)
    dfiles = [os.path.join(source_d, file) for file in os.listdir(source_d)] 
    for file in dfiles:
        print(file)
        if os.path.isfile(file):
            shutil.copy(file, destination)
        elif os.path.isdir(file):
            c_destination = os.path.join(destination, file.split("/")[-1])
            copy_files_recursive(file, c_destination)
        
    #return os.listdir(destination)

    #if os.path.exists(source_file):
    #    shutil.copy(source_file, destination)

        #list_files = os.listdir(source_file)
        #print(list_files)

#print(load_files(static_dir, public_dir))


#def load_files(source_d, destination):
#    if os.path.exists(destination):
#        shutil.rmtree(destination)
#        os.mkdir(destination)
#        dfiles = [os.path.join(source_d, file) for file in os.listdir(source_d)] 
#        for file in dfiles:
#            print(file)
#            if os.path.isfile(file):
#                shutil.copy(file, destination)
#            elif os.path.isdir(file):
#                c_destination = os.path.join(destination, file.split("/")[-1])
#                os.mkdir(c_destination)
#                load_files(file, c_destination)
