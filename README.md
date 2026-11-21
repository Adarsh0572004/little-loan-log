# Little Loan Log

Keep track of borrowed items and who has them.

## Quick start

Use Python 3.10 or newer. All dependencies are in the standard library.

```sh
python app.py lend Atlas Mira
python app.py lend Compass Dev
python app.py list
```

The example output includes `Atlas | Mira`.

Records are saved in `little-loan-log.sqlite3` in the working directory. Use `--db PATH` before the command to choose another database. Run `python app.py --help` for the available options.
