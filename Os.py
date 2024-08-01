import os

print(os.getcwd())  #retrun current directory

#os.chdir(r'C:\Study\Utils\Test')
#print(os.getcwd())  #retrun current directory

# Make directory
# os.mkdir(r'C:\Study\Utils\Test1')
# Create intermadiate directories
#os.makedirs(r'C:\Study\Utils\parent_directory\child_directory')

# Remove files not directory
# os.remove(r'C:\Study\Utils\parent_directory\child_directory\Template.py')
#Removes (deletes) the directory path. The directory must be empty.
#os.rmdir(r'C:\Study\Utils\Test1')
#os.removedirs(r'C:\Study\Utils\parent_directory\child_directory')

#Renames the file or directory from src to dst.
#os.rename(r'ReadMe1.txt', 'ReadMe.txt')
#
# stats = os.stat(r'C:\Study\Utils\Template.py')
# print(stats)

#Lists all files and directories in the given directory (default is the current directory).
# contents = os.listdir(r'C:\Study\Utils')
# print("Directory Contents:", contents)

#Returns True if the path is an existing directory, False otherwise.
# is_directory = os.path.isdir(r'C:\Study\Utils')
# print("Is Directory:", is_directory)

#Returns True if the path is an existing file, False otherwise.
# is_file = os.path.isfile(r'C:\Study\Utils\ReadMe.txt')
# print("Is File:", is_file)

# #Returns True if the path exists (either file or directory), False otherwise.
# exists = os.path.exists(r'C:\Study\Utils')
# # print("Path Exists:", exists)

# #Returns the absolute path of the given path.
# absolute_path = os.path.abspath(r'C:\Study\Utils')
# print("Absolute Path:", absolute_path)


# Replaces a file or directory at dst with the file or directory at src. 
# This is similar to renaming but will replace the destination if it exists
# os.replace(r'C:\Study\Utils\ReadMe copy.txt', r'C:\Study\Utils\ReadMe.txt')
# print("File 'ReadMe.txt' replaced 'ReadMe  copy.txt'")

# #Returns the size of the file specified by path, in bytes.
# file_size = os.path.getsize(r'C:\Study\Utils\ReadMe.txt')
# print("File Size:", file_size, "bytes")

# # Join paths
# path = os.path.join('folder', 'subfolder', 'file.txt')
# print("Joined Path:", path)
