import subprocess
from repo.clone import cloneRepo
from repo.repoExplorer.repoExplorer import repoExplorer
from trackGithub.tracker import track
print("-----------------------------------------------")
print("|                                             |")
print("|            Welcome to RepoLens!             |")
print("|                                             |")
print("-----------------------------------------------")

def main():
    print("""------------------------------------------------
|  1. Clone Repository                         |  
|  2. [Offline] Repository File Explorer       |
|  3. Github Repository Tracker                |
------------------------------------------------
             """)
    query = input("Choose an option to perform: ")


    if query == "1":
        cloneRepo()
    elif query == "2":
        repoExplorer()
    elif query == "3":
        print("Dont forget to add your Personal Access Token (PAT)")
        track()

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
        break