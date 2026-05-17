import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_PAT")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

EVENT_TYPES = [
    "PushEvent",
    "PullRequestEvent",
    "IssuesEvent",
    "ForkEvent",
    "WatchEvent",
    "CreateEvent",
    "DeleteEvent",
    "ReleaseEvent",
]


def get_events(REPO):
    url = f"https://api.github.com/repos/{REPO}/events"
    params = {"per_page": 100}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()


def summarize_event(e):
    etype   = e['type']
    actor   = e['actor']['login']
    date    = e['created_at'][:10]
    payload = e.get('payload', {})
    summary = ""

    if etype == "PushEvent":
        commits = payload.get('commits', [])
        branch  = payload.get('ref', '').replace('refs/heads/', '')
        summary = f"Pushed {len(commits)} commit(s) to {branch}"

    elif etype == "PullRequestEvent":
        pr     = payload.get('pull_request', {})
        action = payload.get('action', '')
        summary = f"PR #{pr.get('number')} {action} — {pr.get('title', '')[:50]}"

    elif etype == "IssuesEvent":
        issue  = payload.get('issue', {})
        action = payload.get('action', '')
        summary = f"Issue #{issue.get('number')} {action} — {issue.get('title', '')[:50]}"

    elif etype == "ForkEvent":
        forkee  = payload.get('forkee', {})
        summary = f"Forked to {forkee.get('full_name', '')}"

    elif etype == "WatchEvent":
        summary = "Starred the repository"

    elif etype == "CreateEvent":
        ref_type = payload.get('ref_type', '')
        ref      = payload.get('ref', '')
        summary  = f"Created {ref_type} '{ref}'"

    elif etype == "DeleteEvent":
        ref_type = payload.get('ref_type', '')
        ref      = payload.get('ref', '')
        summary  = f"Deleted {ref_type} '{ref}'"

    elif etype == "ReleaseEvent":
        release = payload.get('release', {})
        action  = payload.get('action', '')
        summary = f"Release {action} — {release.get('tag_name', '')}"

    else:
        summary = "—"

    return actor, date, summary


def display_events(events):
    if not events:
        print("No events found.")
        return
    print(f"\n{'Type':<22} {'Actor':<20} {'Date':<12} {'Summary'}")
    print("-" * 110)
    for e in events:
        actor, date, summary = summarize_event(e)
        print(f"{e['type']:<22} {actor:<20} {date:<12} {summary}")
    print(f"\nTotal: {len(events)}")


def events(owner, repo_name):
    REPO = f"{owner}/{repo_name}"
    print("\n1. View all events")
    print("2. Filter by event type")
    choice = input("Enter choice [1/2]: ").strip()

    print(f"\nFetching events for {REPO} ...")
    all_events = get_events(REPO)

    if choice == "1":
        display_events(all_events)

    elif choice == "2":
        print("\nAvailable event types:")
        for i, et in enumerate(EVENT_TYPES, 1):
            print(f"  {i}. {et}")
        etype = input("Enter event type (e.g. PushEvent): ").strip()
        filtered = [e for e in all_events if e['type'] == etype]
        print(f"\nFiltered to {etype}:")
        display_events(filtered)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    owner = input("Enter Github Owner: ")
    repo_name = input("Enter Repository Name: ")
    events(owner, repo_name)