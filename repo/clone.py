import subprocess

def cloneRepo():
    repo_url = input("\nEnter the GitHub repository URL to clone: ")
    subprocess.run(['git', 'clone', repo_url], check=True)
    print("Repository cloned successfully!\n")
