"""Keep track of borrowed items and who has them."""

import argparse
import sqlite3
from contextlib import closing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="little-loan-log.sqlite3", help="SQLite database path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List records")
    command = commands.add_parser("lend", help="Record an outstanding loan.")
    command.add_argument("item")
    command.add_argument("borrower")
    command = commands.add_parser("returned", help="Close a loan.")
    command.add_argument("item")
    args = parser.parse_args()
    try:
        with closing(sqlite3.connect(args.db)) as db, db:
            db.execute("CREATE TABLE IF NOT EXISTS items (item TEXT PRIMARY KEY, borrower TEXT NOT NULL)")
            if args.command == "list":
                for row in db.execute("SELECT item, borrower FROM items ORDER BY 1, 2"):
                    print(" | ".join(map(str, row)))
            elif args.command == "lend":
                db.execute("INSERT INTO items VALUES (?, ?)", (args.item, args.borrower))
            elif args.command == "returned":
                if not db.execute("DELETE FROM items WHERE item=?", (args.item,)).rowcount:
                    raise ValueError("No outstanding loan for this item")
    except (ValueError, sqlite3.Error) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
