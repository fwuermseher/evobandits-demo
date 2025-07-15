# evobandits-demo

Demo for [EvoBandits](https://github.com/EvoBandits/EvoBandits), showcasing the Genetic Multi-Armed Bandits (GMAB) algorithm for tuning genetic algorithms.

## Set up for Windows

Follow these steps to run the optimizer comparison:

### 1. Install R (for IRACE)

- [R 4.4.1](https://cran.r-project.org/bin/windows/base/old/4.4.1/)
- [RTools44](https://cran.r-project.org/bin/windows/Rtools/rtools44/rtools.html)
- Set environment variables (e.g., `R_HOME`)

### 2. Install Python

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- Add Python to `PATH`

```sh
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
pip install git+https://github.com/Saethox/iracepy-tiny#egg=irace
```

### Setup for macOS / unix-based systems

Functionality on macOS and unix-based systems is currently untested and may require additional configuration.
