[![Make.fun bounty](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/firlifirrizqi/everyday-things-two-lines-makefun/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/firlifirrizqi/everyday-things-two-lines-makefun/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

# Everyday Things, Two Lines, Longer Run

A two-line explanation of one everyday thing — a toaster — for a 10-year-old, written for the [Make.fun bounty](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479).

## The entry

> A toaster is like a tiny sun trapped in a box that gives your bread a warm hug on both sides until it turns golden and crunchy.
>
> It maps the heat and the golden colour, but leaves out that a real sun never pops your toast up when it is done.

## How it works

`main.py` (standard library only) holds the two lines as constants, checks each one is a single sentence of 1–200 characters, writes them — line 1, newline, line 2, no trailing newline — to `/output/entry.txt`, then re-opens the file and verifies its content matches the two lines exactly.

## Run

```sh
python3 main.py
```

It prints the character count of each line and leaves the entry in `/output/entry.txt`.
