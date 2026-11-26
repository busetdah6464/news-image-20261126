# The World in One Page — 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/busetdah6464/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/busetdah6464/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126)

One image summing up the world's news of **Thursday 26 November 2026**:
49 stories from 7 regions in a dense newspaper layout — 3 lead stories,
12 more in brief, a numbered world map, 34 one-line briefs, and a
DATE CHECK box listing what was deliberately left out and why.

Every story was first reported on 26 November 2026 (in some time zone);
see `VERIFIKASI.md` for the story list with sources.

## How it is built

`render.py` draws `entry.png` (1024×1024, Pillow, locally, from the
verified story list). `main.py` — standard library only — copies that
finished image to `/output/entry.png`, so the entry is deterministic:
two runs write the same bytes.

## Run

```sh
python3 render.py          # rebuild entry.png from the story list
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
