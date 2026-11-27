"""代码片段管理器：支持增删查与按标签过滤，供代码库复用。"""
from __future__ import annotations
import json
import sys
from pathlib import Path

STORE = Path("snippets.json")

def load() -> list[dict]:
    return json.loads(STORE.read_text()) if STORE.exists() else []

def save(items: list[dict]) -> None:
    STORE.write_text(json.dumps(items, ensure_ascii=False, indent=2))

def add(name: str, code: str, tags: list[str]) -> None:
    items = load()
    items.append({"name": name, "code": code, "tags": tags})
    save(items)

def find(keyword: str) -> list[dict]:
    items = load()
    return [it for it in items if keyword in it["name"] or keyword in it["code"]]

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "add":
        add(sys.argv[2], sys.argv[3], sys.argv[4].split(","))
    elif cmd == "find":
        for it in find(sys.argv[2]):
            print(it["name"], it["tags"])
    else:
        print(load())
