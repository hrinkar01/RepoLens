import subprocess

print("-----------------------------------------------")
print("|            Welcome to RepoLens!             |")
print("-----------------------------------------------")


print("Please enter the GitHub repository URL you want to clone:")
repo_url = input("Repository URL: ")
print("Cloning the repository...")
subprocess.run(['git', 'clone', repo_url], check=True)
print("Repository cloned successfully!")

