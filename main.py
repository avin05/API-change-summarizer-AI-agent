import yaml
from slack import send_to_slack
from changelog_monitor import fetch_doc, compute_hash, load_last, save_current
from summarizer import summarize_change

CONFIG_FILE = "config.yaml"

def run():
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

    for api in config["apis"]:
        name = api["name"]
        url = api["url"]
        state_file = f"snapshot_{name.replace(' ', '_').lower()}.txt"

        print(f"Checking {name}...")

        new = fetch_doc(url)
        old = load_last(state_file)

        if compute_hash(new) == compute_hash(old):
            print(f"No change for {name}")
            continue

        summary = summarize_change(old, new)
        message = (
            f"📢 *{name} API Update Detected*\n\n"
            f"{summary}\n\n"
            f"🔗 <{url}|View Docs>"
        )
        send_to_slack(message)
        save_current(new, state_file)

if __name__ == "__main__":
    run()