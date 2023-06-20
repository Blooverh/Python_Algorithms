import os 
print(os.path.getsize(path))
print(os.path.isdir(path))
print(os.listdir(path))

def disk_usage(path):
    total= os.path.getsize(path)
    if os.path.isdir(path):
        childpath=os.path.join(path,'fileSystem.py')
        total += disk_usage(childpath)

    print('{0:7}'.format(total), path)
    return total

disk_usage(path)