import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_PAT")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_commits(REPO, branch=None, author=None, since=None, until=None):
    url = f"https://api.github.com/repos/{REPO}/commits"
    params = {"per_page": 50}
    if branch:
        params["sha"] = branch
    if author:
        params["author"] = author
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()


def get_specific_commit(REPO, sha):
    url = f"https://api.github.com/repos/{REPO}/commits/{sha}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def display_commits(commits):
    if not commits:
        print("No commits found.")
        return
    print(f"\n{'SHA':<10} {'Author':<20} {'Date':<12} {'Message'}")
    print("-" * 110)
    for c in commits:
        sha     = c['sha'][:7]
        author  = c['commit']['author']['name'][:18]
        date    = c['commit']['author']['date'][:10]
        message = c['commit']['message'].splitlines()[0][:60]
        print(f"{sha:<10} {author:<20} {date:<12} {message}")
    print(f"\nTotal: {len(commits)}")


def display_specific_commit(commit):
    info = commit['commit']
    files = commit.get('files', [])

    print("\n" + "=" * 110)
    print(f"Commit {commit['sha'][:7]} — {info['message'].splitlines()[0]}")
    print("=" * 110)
    print(f"Full SHA     : {commit['sha']}")
    print(f"Author       : {info['author']['name']} <{info['author']['email']}>")
    print(f"Date         : {info['author']['date'][:10]}")
    print(f"Committer    : {info['committer']['name']}")
    print(f"URL          : {commit['html_url']}")
    print(f"Files changed: {len(files)}")

    stats = commit.get('stats', {})
    print(f"Additions    : +{stats.get('additions', 0)}")
    print(f"Deletions    : -{stats.get('deletions', 0)}")
    print(f"Total changes: {stats.get('total', 0)}")

    print(f"\n--- Full Commit Message ---")
    print(info['message'])

    if files:
        print(f"\n--- Changed Files ({len(files)}) ---")
        for f in files:
            status = f['status'].upper()
            additions = f.get('additions', 0)
            deletions = f.get('deletions', 0)
            print(f"\n[{status}] {f['filename']}  +{additions} -{deletions}")
            if f.get('patch'):
                print(f['patch'][:500])
                if len(f.get('patch', '')) > 500:
                    print("... (truncated)")

    print("\n" + "=" * 110)


def commit(owner, repo_name):
    REPO = f"{owner}/{repo_name}"
    print("\n1. View all commits")
    print("2. View specific commit")
    choice = input("Enter choice [1/2]: ").strip()

    if choice == "1":
        branch = input("Branch name (leave blank for default): ").strip() or None
        author = input("Filter by author username (leave blank to skip): ").strip() or None
        since  = input("Since date YYYY-MM-DD (leave blank to skip): ").strip() or None
        until  = input("Until date YYYY-MM-DD (leave blank to skip): ").strip() or None
        print(f"\nFetching commits for {REPO} ...")
        commits = get_commits(REPO, branch, author, since, until)
        display_commits(commits)

    elif choice == "2":
        sha = input("Enter commit SHA: ").strip()
        print(f"\nFetching commit {sha[:7]} for {REPO} ...")
        result = get_specific_commit(REPO, sha)
        display_specific_commit(result)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    commit(owner, repo_name)