# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv("GITHUB_PAT")


# HEADERS = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Accept": "application/vnd.github+json",
# }

# def pr(owner, repo_name):
#     REPO = f"{owner}/{repo_name}"
#     def get_prs(state="open"):
#         url = f"https://api.github.com/repos/{REPO}/pulls"
#         params = {"state": state, "per_page": 50}
#         resp = requests.get(url, headers=HEADERS, params=params)
#         resp.raise_for_status()
#         return resp.json()


#     def get_specific_pr(number):
#         url = f"https://api.github.com/repos/{REPO}/pulls/{number}"
#         resp = requests.get(url, headers=HEADERS)
#         resp.raise_for_status()
#         return resp.json()


#     def get_pr_comments(number):
#         url = f"https://api.github.com/repos/{REPO}/issues/{number}/comments"
#         resp = requests.get(url, headers=HEADERS)
#         resp.raise_for_status()
#         return resp.json()


#     def display_prs(prs):
#         if not prs:
#             print("No PRs found.")
#             return
#         print(f"\n{'#':<6} {'Title':<50} {'Author':<20} {'URL'}")
#         print("-" * 110)
#         for pr in prs:
#             print(f"#{pr['number']:<5} {pr['title'][:48]:<50} {pr['user']['login']:<20} {pr['html_url']}")
#         print(f"\nTotal: {len(prs)}")


#     def display_specific_pr(pr):
#         comments = get_pr_comments(pr['number'])

#         print("\n" + "=" * 110)
#         print(f"PR #{pr['number']} — {pr['title']}")
#         print("=" * 110)
#         print(f"Author       : {pr['user']['login']}")
#         print(f"State        : {pr['state']}")
#         print(f"Created      : {pr['created_at'][:10]}")
#         print(f"Updated      : {pr['updated_at'][:10]}")
#         print(f"Merged       : {pr['merged_at'][:10] if pr['merged_at'] else 'Not merged'}")
#         print(f"Branch       : {pr['head']['label']} → {pr['base']['label']}")
#         print(f"Commits      : {pr['commits']}")
#         print(f"Changed Files: {pr['changed_files']}")
#         print(f"Additions    : +{pr['additions']}")
#         print(f"Deletions    : -{pr['deletions']}")
#         print(f"Comments     : {pr['comments']}")
#         print(f"URL          : {pr['html_url']}")

#         labels = [l['name'] for l in pr['labels']]
#         print(f"Labels       : {', '.join(labels) if labels else 'None'}")

#         assignees = [a['login'] for a in pr['assignees']]
#         print(f"Assignees    : {', '.join(assignees) if assignees else 'None'}")

#         print(f"\n--- Description ---")
#         print(pr['body'] if pr['body'] else "No description provided.")

#         if comments:
#             print(f"\n--- Comments ({len(comments)}) ---")
#             for c in comments:
#                 print(f"\n[{c['user']['login']} — {c['created_at'][:10]}]")
#                 print(c['body'])

#         print("\n" + "=" * 110)


#     if __name__ == "__main__":
#         print("\n1. View all PRs")
#         print("2. View specific PR")
#         choice = input("Enter choice [1/2]: ").strip()

#         if choice == "1":
#             state = input("State [open/closed/all] (default: open): ").strip() or "open"
#             print(f"\nFetching {state} PRs for {REPO} ...")
#             prs = get_prs(state)
#             display_prs(prs)

#         elif choice == "2":
#             number = input("Enter PR number: ").strip()
#             print(f"\nFetching PR #{number} for {REPO} ...")
#             pr = get_specific_pr(number)
#             display_specific_pr(pr)

#         else:
#             print("Invalid choice.")
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_PAT")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_prs(REPO, state="open"):
    url = f"https://api.github.com/repos/{REPO}/pulls"
    params = {"state": state, "per_page": 50}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()


def get_specific_pr(REPO, number):
    url = f"https://api.github.com/repos/{REPO}/pulls/{number}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def get_pr_comments(REPO, number):
    url = f"https://api.github.com/repos/{REPO}/issues/{number}/comments"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def display_prs(prs):
    if not prs:
        print("No PRs found.")
        return
    print(f"\n{'#':<6} {'Title':<50} {'Author':<20} {'URL'}")
    print("-" * 110)
    for item in prs:
        print(f"#{item['number']:<5} {item['title'][:48]:<50} {item['user']['login']:<20} {item['html_url']}")
    print(f"\nTotal: {len(prs)}")


def display_specific_pr(REPO, pr):
    comments = get_pr_comments(REPO, pr['number'])
    print("\n" + "=" * 110)
    print(f"PR #{pr['number']} — {pr['title']}")
    print("=" * 110)
    print(f"Author       : {pr['user']['login']}")
    print(f"State        : {pr['state']}")
    print(f"Created      : {pr['created_at'][:10]}")
    print(f"Updated      : {pr['updated_at'][:10]}")
    print(f"Merged       : {pr['merged_at'][:10] if pr['merged_at'] else 'Not merged'}")
    print(f"Branch       : {pr['head']['label']} → {pr['base']['label']}")
    print(f"Commits      : {pr['commits']}")
    print(f"Changed Files: {pr['changed_files']}")
    print(f"Additions    : +{pr['additions']}")
    print(f"Deletions    : -{pr['deletions']}")
    print(f"Comments     : {pr['comments']}")
    print(f"URL          : {pr['html_url']}")
    labels = [l['name'] for l in pr['labels']]
    print(f"Labels       : {', '.join(labels) if labels else 'None'}")
    assignees = [a['login'] for a in pr['assignees']]
    print(f"Assignees    : {', '.join(assignees) if assignees else 'None'}")
    print(f"\n--- Description ---")
    print(pr['body'] if pr['body'] else "No description provided.")
    if comments:
        print(f"\n--- Comments ({len(comments)}) ---")
        for c in comments:
            print(f"\n[{c['user']['login']} — {c['created_at'][:10]}]")
            print(c['body'])
    print("\n" + "=" * 110)


def pr(owner, repo_name):
    REPO = f"{owner}/{repo_name}"
    print("\n1. View all PRs")
    print("2. View specific PR")
    choice = input("Enter choice [1/2]: ").strip()

    if choice == "1":
        state = input("State [open/closed/all] (default: open): ").strip() or "open"
        print(f"\nFetching {state} PRs for {REPO} ...")
        prs = get_prs(REPO, state)
        display_prs(prs)

    elif choice == "2":
        number = input("Enter PR number: ").strip()
        print(f"\nFetching PR #{number} for {REPO} ...")
        result = get_specific_pr(REPO, number)
        display_specific_pr(REPO, result)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    pr(owner, repo_name)