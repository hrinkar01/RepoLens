import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_PAT")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_open_issues(REPO):
    url = f"https://api.github.com/repos/{REPO}/issues"
    params = {"state": "open", "per_page": 50}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    all_items = resp.json()
    return [i for i in all_items if "pull_request" not in i]


def has_linked_pr(REPO, issue_number):
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}/timeline"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    for event in resp.json():
        if event.get("event") == "cross-referenced":
            source = event.get("source", {})
            issue  = source.get("issue", {})
            if "pull_request" in issue:
                return True
    return False


def display_issues(issues):
    if not issues:
        print("No unlinked open issues found.")
        return
    print(f"\n{'#':<6} {'Title':<50} {'Author':<20} {'URL'}")
    print("-" * 110)
    for issue in issues:
        print(f"#{issue['number']:<5} {issue['title'][:48]:<50} {issue['user']['login']:<20} {issue['html_url']}")
    print(f"\nTotal: {len(issues)}")


def unlinked_issues(owner, repo_name):
    REPO = f"{owner}/{repo_name}"
    print(f"\nFetching open issues for {REPO} ...")
    issues = get_open_issues(REPO)
    print(f"Found {len(issues)} open issues. Checking for linked PRs (this may take a moment) ...")

    result = []
    for i, issue in enumerate(issues, 1):
        print(f"  Checking #{issue['number']} ({i}/{len(issues)}) ...", end="\r")
        if not has_linked_pr(REPO, issue['number']):
            result.append(issue)

    print(f"\nDone. {len(result)} issues have no linked PR.\n")
    display_issues(result)


if __name__ == "__main__":
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    unlinked_issues(owner, repo_name)