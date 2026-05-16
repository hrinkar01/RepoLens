import subprocess
from .fileCount import counter
def repoExplorer():
    repoPath = input("Enter the repository path to view its structure: ")
    print("""
        1. View Repository File Structure
        2. About Files
        3. View File Content
""")
    
    expQuery = input("Choose an option from give above functions: ")
    

    if expQuery == "1":
        subprocess.run(['python3', 'repo/showRepo.py', repoPath], check=True)
        print("\n")

    elif expQuery == "2":
        counter(repoPath)

    elif expQuery == "3":
        file_path = input("Enter the files exact path you want to view: ")
        subprocess.run(['cat', file_path], check=True)
        print("\n")

