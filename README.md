# Everybody Codes

This repository contains my pure [Python](https://www.python.org/) solutions
to [everybody.codes](https://everybody.codes/home).

## Installation

```shell
git clone https://github.com/yoonthegoon/everybody.codes.git
cd everybody.codes
uv sync  # for dev dependencies
```

## Usage

Move your notes into the [notes](/notes) directory.

```text
.
├── README.md
├── everybody_codes
├── notes
│   ├── everybody_codes_e2025_q01_p1.txt
│   ├── everybody_codes_e2025_q01_p2.txt
│   └── everybody_codes_e2025_q01_p3.txt
├── pyproject.toml
├── scripts
└── uv.lock

```

Run solutions to each part of a quest.

```shell
python3 -m everybody_codes.e2025.q01
```

> ```text
> Fyrryn
> Elarzris
> Drakzyph
> ```

Check types, format code, sort imports.

```shell
scripts/check
```

> ```text
> Checking project for type errors
> All checks passed!
> ---
> Running formatter
> 6 files left unchanged
> ---
> Sorting imports
> All checks passed!
> ```
