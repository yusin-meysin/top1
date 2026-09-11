# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: CourseSchedule
def main():
    import argparse
    parser = argparse.ArgumentParser(description="CourseSchedule CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list", help="list items")
    p_list.add_argument("--type", choices=["course", "lecture", "room", "instructor", "attendance"], default="course")

    p_add = sub.add_parser("add", help="add item")
    p_add.add_argument("--type", required=True, choices=["course", "lecture", "room", "instructor", "attendance"])
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--json", default=None)

    p_show = sub.add_parser("show", help="show item")
    p_show.add_argument("--id", required=True)

    p_delete = sub.add_parser("delete", help="delete item")
    p_delete.add_argument("--id", required=True)

    args = parser.parse_args()
    if args.cmd == "list":
        for item in data:
            if isinstance(item, dict) and item.get("type") == args.type:
                print(item)
    elif args.cmd == "add":
        if args.json:
            item = json.loads(args.json)
        else:
            item = {"type": args.type, "name": args.name}
        if item in data:
            print("already exists")
        else:
            data.append(item)
            print("added")
    elif args.cmd == "show":
        for item in data:
            if isinstance(item, dict) and item.get("id") == args.id:
                print(item)
    elif args.cmd == "delete":
        for i, item in enumerate(data):
            if isinstance(item, dict) and item.get("id") == args.id:
                data.pop(i)
                print("deleted")
                break
        else:
            print("not found")

if __name__ == "__main__":
    main()
