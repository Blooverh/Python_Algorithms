import os

def disk_usage(path):
    """Return the number of bytes used by a file or folder or any descendents."""
    total= os.path.getsize(path) #account for direct usage
    if os.path.isdir(path):
        for filename in os.listdir(path, filename):
            childpath= os.path.join(path, filename)
            tota+= disk_usage(childpath)

    print('{0:7}'.format(total), path)
    return total
