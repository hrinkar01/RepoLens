import subprocess
from repo.clone import cloneRepo
from repo.repoExplorer.repoExplorer import repoExplorer

print("-----------------------------------------------")
print("|                                             |")
print("|            Welcome to RepoLens!             |")
print("|                                             |")
print("-----------------------------------------------")

def main():
    print("1. Clone Repository ")
    print("2. [Offline] Repository Explorer ")
    query = input("Choose an option to perform: ")


    if query == "1":
        cloneRepo()
    elif query == "2":
        repoExplorer()

main()