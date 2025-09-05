# evobandits-demo

Demo for [EvoBandits](https://github.com/EvoBandits/EvoBandits), showcasing the Genetic Multi-Armed Bandits (GMAB) algorithm for tuning genetic algorithms.

## Set up for Windows

Follow these steps to run the [EvoBandits demonstration](_demo.ipynb) and the [performance comparison with other libraries](_tool_comparison.ipynb).

**Note**: Running the optimization from scratch takes a very long time, especially for the performance comparison. If you simply wish to recreate the plots, you can skip the optimization process and use the cached data from the previous run.

### 1. Install R (for IRACE)

- [R 4.4.1](https://cran.r-project.org/bin/windows/base/old/4.4.1/)
- [RTools44](https://cran.r-project.org/bin/windows/Rtools/rtools44/rtools.html)
- Set environment variables (e.g., `R_HOME`)
- Follow the installation guide for [IRACE](https://github.com/MLopez-Ibanez/irace) to install the package.

### 2. Install Python

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- Add Python to `PATH`

### 3. Clone this repository and set up a virtual environment

The following commands will create a local copy of the repository and initialize a virtual environment in your current working directory.

```sh
git clone https://github.com/fwuermseher/evobandits-demo.git
cd evobandits-demo
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

### 4. Install Python dependencies

The following command installs [dependencies](requirements.txt) for evobandits-demo from PyPI. Python bindings for IRACE are installed from GitHub.

```sh
pip install -r requirements.txt
pip install git+https://github.com/Saethox/iracepy-tiny#egg=irace
```

## Setup for macOS and unix-based systems

Functionality on macOS and other Unix-based systems is currently untested and may require additional configuration.
