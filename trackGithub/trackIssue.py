import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_PAT")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_issues(REPO, state="open"):
    url = f"https://api.github.com/repos/{REPO}/issues"
    params = {"state": state, "per_page": 50}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    all_items = resp.json()
    return [i for i in all_items if "pull_request" not in i]


def get_specific_issue(REPO, number):
    url = f"https://api.github.com/repos/{REPO}/issues/{number}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def get_issue_comments(REPO, number):
    url = f"https://api.github.com/repos/{REPO}/issues/{number}/comments"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def display_issues(issues):
    if not issues:
        print("No issues found.")
        return
    print(f"\n{'#':<6} {'Title':<50} {'Author':<20} {'URL'}")
    print("-" * 110)
    for item in issues:
        print(f"#{item['number']:<5} {item['title'][:48]:<50} {item['user']['login']:<20} {item['html_url']}")
    print(f"\nTotal: {len(issues)}")


def display_specific_issue(REPO, issue):
    comments = get_issue_comments(REPO, issue['number'])
    print("\n" + "=" * 110)
    print(f"Issue #{issue['number']} — {issue['title']}")
    print("=" * 110)
    print(f"Author       : {issue['user']['login']}")
    print(f"State        : {issue['state']}")
    print(f"Created      : {issue['created_at'][:10]}")
    print(f"Updated      : {issue['updated_at'][:10]}")
    print(f"Closed       : {issue['closed_at'][:10] if issue['closed_at'] else 'Not closed'}")
    print(f"Comments     : {issue['comments']}")
    print(f"URL          : {issue['html_url']}")
    labels = [l['name'] for l in issue['labels']]
    print(f"Labels       : {', '.join(labels) if labels else 'None'}")
    assignees = [a['login'] for a in issue['assignees']]
    print(f"Assignees    : {', '.join(assignees) if assignees else 'None'}")
    print(f"\n--- Description ---")
    print(issue['body'] if issue['body'] else "No description provided.")
    if comments:
        print(f"\n--- Comments ({len(comments)}) ---")
        for c in comments:
            print(f"\n[{c['user']['login']} — {c['created_at'][:10]}]")
            print(c['body'])
    print("\n" + "=" * 110)


def issue(owner, repo_name):
    REPO = f"{owner}/{repo_name}"
    print("\n1. View all Issues")
    print("2. View specific Issue")
    choice = input("Enter choice [1/2]: ").strip()

    if choice == "1":
        state = input("State [open/closed/all] (default: open): ").strip() or "open"
        print(f"\nFetching {state} issues for {REPO} ...")
        issues = get_issues(REPO, state)
        display_issues(issues)

    elif choice == "2":
        number = input("Enter Issue number: ").strip()
        print(f"\nFetching Issue #{number} for {REPO} ...")
        result = get_specific_issue(REPO, number)
        if "pull_request" in result:
            print("That number is a PR, not an issue. Use trackPR.py instead.")
        else:
            display_specific_issue(REPO, result)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    issue(owner, repo_name)