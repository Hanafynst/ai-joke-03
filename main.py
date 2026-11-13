import os

JOKE = (
    "I asked my coding agent to nudge a button two pixels left. "
    "It deprecated the old button, wrote a migration plan, "
    "and shipped the replacement two pixels right."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
