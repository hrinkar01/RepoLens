import subprocess
from repo.clone import cloneRepo

print("-----------------------------------------------")
print("|                                             |")
print("|            Welcome to RepoLens!             |")
print("|                                             |")
print("-----------------------------------------------")

def showRepoFiles():
    subprocess.run(['ls'], check=True)

def main():
    print("1. Clone Repository ")
    print("2. Show Repository Files ")
    query = input("Choose an option to perform: ")


    if query == "1":
        cloneRepo()
    elif query == "2":
        repo_path = input("Enter the repository path: ")
        subprocess.run(['python3', 'repo/showRepo.py', repo_path], check=True)

main()