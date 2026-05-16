from trackPR import pr
from trackIssue import issue


def track():
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    print("""
          1. Track PR
          2. Track Issues
          3. Track Issues without Pr
          4. Track Commits
          5. Track Events
          """)
    tquery = input("Choose an option from the above: ")
    
    if tquery == "1":
        pr(owner, repo_name)
    elif tquery == "2":
        issue(owner, repo_name)
track()