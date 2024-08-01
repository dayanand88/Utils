import shutil
import os

# Copy a File
shutil.copy('source.txt', 'destination.txt')  # Copies 'source.txt' to 'destination.txt'

# Copy a File with Metadata
shutil.copy2('source.txt', 'destination.txt')  # Copies 'source.txt' to 'destination.txt' with metadata

# Copy a Directory
shutil.copytree('source_directory', 'destination_directory')  # Recursively copies 'source_directory' to 'destination_directory'

# Move a File or Directory
shutil.move('source.txt', 'destination.txt')  # Moves or renames 'source.txt' to 'destination.txt'

# Remove a Directory Tree
shutil.rmtree('directory_to_remove')  # Recursively deletes 'directory_to_remove'

# Create an Archive
shutil.make_archive('archive_name', 'zip', 'directory_to_archive')  # Creates a zip archive of 'directory_to_archive'

# Extract an Archive
shutil.unpack_archive('archive_name.zip', 'extracted_directory')  # Extracts 'archive_name.zip' to 'extracted_directory'

# Disk Usage
usage = shutil.disk_usage('/')
print("Total:", usage.total)  # Total disk space
print("Used:", usage.used)    # Used disk space
print("Free:", usage.free)    # Free disk space

# Get Terminal Size
size = shutil.get_terminal_size()
print("Terminal Size:", size)  # Prints terminal window size (columns, rows)

# Create a Temporary Directory
from tempfile import TemporaryDirectory
with TemporaryDirectory() as temp_dir:
    print("Temporary Directory:", temp_dir)  # Temporary directory created and cleaned up automatically
