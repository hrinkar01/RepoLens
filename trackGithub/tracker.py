from .trackPR import pr
from .trackIssue import issue
from .trackCommit import commit
from .trackEvents import events
from .trackUnlinkedIssues import unlinked_issues

def track():
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    print("""
          1. Track PR
          2. Track Issues
          3. Track Issues without any linked PR
          4. Track Commits
          5. Track Events
          """)
    tquery = input("Choose an option from the above: ")
    
    if tquery == "1":
        trackPR.pr(owner, repo_name)
    elif tquery == "2":
        issue(owner, repo_name)
    elif tquery == "3":
        unlinked_issues(owner, repo_name)
    elif tquery == "4":
        commit(owner, repo_name)
    elif tquery == "5":
        events(owner, repo_name)
