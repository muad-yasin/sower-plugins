#!/usr/bin/env python3
"""Copy the five writing skills from a checkout of their source repository, at one commit,
into sower-writer/skills/, and record what was copied in sower-writer/SOURCE.json.

Usage: python3 scripts/copy-writer-skills.py <path to the source checkout> <commit>

The files are read from the commit with `git show`, never from the checkout's working tree, so
uncommitted or later changes there cannot leak into the copy. The script deletes nothing: if a
skill's folder here holds a file that the source does not have at that commit, it stops and lists
the file, which you move out by hand before running it again. Then run scripts/check-copies.py with
the same checkout as its argument.
"""
import hashlib
import json
import os
import subprocess
import sys

SKILLS = ["drafting", "line-editing", "fact-checking", "final-read", "good-news-writing"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "sower-writer", "skills")
RECORD = os.path.join(ROOT, "sower-writer", "SOURCE.json")


def git(src, *args):
    return subprocess.run(["git", "-C", src, *args], check=True, capture_output=True).stdout


def public_address(src, commit):
    repository = json.loads(git(src, "show", commit + ":package.json")).get("repository", "")
    url = repository.get("url", "") if isinstance(repository, dict) else repository
    if url.startswith("git+"):
        url = url[len("git+"):]
    if url.endswith(".git"):
        url = url[: -len(".git")]
    return url


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, ref = sys.argv[1], sys.argv[2]
    commit = git(src, "rev-parse", "--verify", ref + "^{commit}").decode().strip()

    files = {}
    for skill in SKILLS:
        names = [n for n in git(src, "ls-tree", "-r", "--name-only", commit, "--", "skills/" + skill).decode().split("\n") if n]
        if not names:
            sys.exit(f"{skill}: no such folder at {commit}")
        for name in names:
            files[name[len("skills/"):]] = git(src, "show", f"{commit}:{name}")

    extra = []
    for skill in SKILLS:
        for dirpath, _, names in os.walk(os.path.join(TARGET, skill)):
            for name in names:
                rel = os.path.relpath(os.path.join(dirpath, name), TARGET).replace(os.sep, "/")
                if rel not in files:
                    extra.append(rel)
    if extra:
        sys.exit("Not in the source at this commit; move these out by hand first:\n  " + "\n  ".join(sorted(extra)))

    for rel, data in files.items():
        path = os.path.join(TARGET, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as fh:
            fh.write(data)

    record = {
        "source": public_address(src, commit),
        "commit": commit,
        "files": {rel: hashlib.sha256(data).hexdigest() for rel, data in sorted(files.items())},
    }
    with open(RECORD, "w", encoding="utf-8") as fh:
        json.dump(record, fh, indent=2)
        fh.write("\n")
    print(f"{len(files)} files copied from {commit[:12]}; recorded in sower-writer/SOURCE.json")


if __name__ == "__main__":
    main()
