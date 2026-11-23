#!/usr/bin/env python3
"""Check the text that must stay the same in two places.

1. The writing skills in sower-writer/skills/ against their source: every file that
   sower-writer/SOURCE.json records exists with its recorded sha256, no skill folder there holds a
   file the record lacks, every skill folder there is one the record names (the plugin's skills
   are copies only), and the record names exactly the skills that scripts/copy-writer-skills.py
   lists. Given a checkout of the source repository, the record is also compared with the commit it
   names: every recorded file has the recorded content there, and the commit holds no file in those
   skills' folders that the record lacks. Without a checkout, that comparison is NOT CHECKED, and
   the run says so.
2. The four rules that the two quality checks share, in sower-review/agents/quality-check-quick.md
   and quality-check-deep.md, are word for word the same in both files: three bullets, and the
   whole instruction on reading a change.

Exit codes: 0, everything compared and equal; 1, a difference; 2, no difference found, but the copies
were not compared with their source because no checkout was given.

Usage: python3 scripts/check-copies.py [path to the source checkout]
"""
import ast
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "sower-writer", "skills")
RECORD = os.path.join(ROOT, "sower-writer", "SOURCE.json")
QUICK = os.path.join(ROOT, "sower-review", "agents", "quality-check-quick.md")
DEEP = os.path.join(ROOT, "sower-review", "agents", "quality-check-deep.md")
COPY_SCRIPT = os.path.join(ROOT, "scripts", "copy-writer-skills.py")
SHARED_BULLETS = [
    "No verification step the project has ruled out.",
    "Frozen text is not drift.",
    "A suspected defect is named, not chased:",
]
# The first words of the instruction on reading a change; it is compared from here to its paragraph's end.
SHARED_INSTRUCTION = "For every path that `git status --short` lists"


def sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def copied_skills():
    """The list of copied skills stands in one place, the copy script. It is read from the source, not run."""
    with open(COPY_SCRIPT, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "SKILLS" for t in node.targets):
            return sorted(ast.literal_eval(node.value))
    sys.exit("scripts/copy-writer-skills.py has no SKILLS list")


def check_copies(src):
    fails = []
    with open(RECORD, encoding="utf-8") as fh:
        record = json.load(fh)
    recorded = record["files"]
    for rel, digest in sorted(recorded.items()):
        path = os.path.join(TARGET, *rel.split("/"))
        if not os.path.isfile(path):
            fails.append("missing: " + rel)
        elif sha256(path) != digest:
            fails.append("differs from the record: " + rel)
    skills = sorted({rel.split("/")[0] for rel in recorded})
    expected = copied_skills()
    for name in expected:
        if name not in skills:
            fails.append("a skill the copy script lists is not in the record: " + name + "/")
    for name in skills:
        if name not in expected:
            fails.append("a skill in the record that the copy script does not list: " + name + "/")
    for name in sorted(os.listdir(TARGET)):
        if os.path.isdir(os.path.join(TARGET, name)) and name not in skills:
            fails.append("a skill folder the record does not name: " + name + "/")
    for skill in skills:
        for dirpath, _, names in os.walk(os.path.join(TARGET, skill)):
            for name in names:
                rel = os.path.relpath(os.path.join(dirpath, name), TARGET).replace(os.sep, "/")
                if rel not in recorded:
                    fails.append("not in the record: " + rel)
    if src:
        commit = record["commit"]
        for rel, digest in sorted(recorded.items()):
            shown = subprocess.run(["git", "-C", src, "show", f"{commit}:skills/{rel}"], capture_output=True)
            if shown.returncode != 0:
                fails.append(f"not in {commit[:12]}: {rel}")
            elif hashlib.sha256(shown.stdout).hexdigest() != digest:
                fails.append(f"the record differs from {commit[:12]}: {rel}")
        in_source = set()
        for skill in expected:
            listed = subprocess.run(["git", "-C", src, "ls-tree", "-r", "--name-only", "-z", commit, "--", "skills/" + skill],
                                    capture_output=True)
            names = [n[len("skills/"):] for n in listed.stdout.decode().split("\0") if n]
            if listed.returncode != 0 or not names:
                fails.append(f"cannot list skills/{skill}/ at {commit[:12]}")
            in_source.update(names)
        for rel in sorted(in_source - set(recorded)):
            fails.append(f"in {commit[:12]} but not in the record: {rel}")
    if src:
        print(f"copies: {len(recorded)} files recorded from {record['commit'][:12]}, compared with the source "
              f"({len(in_source)} files in its {len(expected)} folders)")
    else:
        print(f"copies: {len(recorded)} files compared with their record only; "
              f"NOT CHECKED against the source: give a checkout of {record['source']} as the argument")
    return fails


def check_shared_rules():
    def read(path):
        with open(path, encoding="utf-8") as fh:
            return fh.read()

    def bullets(text):
        return {m.group(1): m.group(0).strip() for m in re.finditer(r"^- \*\*(.+?)\*\*.*$", text, re.M)}

    def change_instruction(text):
        if text.count(SHARED_INSTRUCTION) != 1:
            return None
        start = text.index(SHARED_INSTRUCTION)
        end = text.find("\n", start)
        return text[start:] if end < 0 else text[start:end]

    quick, deep = read(QUICK), read(DEEP)
    fails = []
    for name in SHARED_BULLETS:
        a, b = bullets(quick).get(name), bullets(deep).get(name)
        if a is None or a != b:
            fails.append("shared rule differs: " + name)
    a, b = change_instruction(quick), change_instruction(deep)
    if a is None or a != b:
        fails.append("shared rule differs: the instruction on reading a change")
    print(f"shared rules: {len(SHARED_BULLETS) + 1} compared")
    return fails


def main():
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    src = sys.argv[1] if len(sys.argv) == 2 else None
    fails = check_copies(src) + check_shared_rules()
    for line in fails:
        print("FAIL " + line)
    if fails:
        print(f"{len(fails)} failed")
        sys.exit(1)
    if not src:
        print("NOT CHECKED: no difference from the record, but the copies were not compared with their source")
        sys.exit(2)
    print("OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
