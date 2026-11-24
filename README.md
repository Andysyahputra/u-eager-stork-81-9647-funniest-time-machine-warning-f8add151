# Funniest Time Machine Warning Label

A program that writes the funniest one-line warning label for a time
machine to `/output/entry.txt`.

The label is phrased like a genuine safety notice about meeting your
own duplicate self — with the punch saved for the last few words:

> WARNING: If you meet yourself, do not make eye contact. He knows what you did.

## Run

```sh
python3 main.py
```

The program is deterministic: it writes the same 78-character label on
every run, with no network, no secrets, and no files outside the repo
except the output file.

## License

MIT — see `LICENSE`.
