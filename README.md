# evobandits-demo

Application example for [EvoBandits](https://github.com/EvoBandits/EvoBandits), demonstrating the use of the Genetic Multi-Armed Bandits algorithm (GMAB) for tuning a genetic algorithm.

## Installation (Windows)

The following steps are required to run the scripts, especially the optimizer comparison.

#### 1. Set up R (dependency for the IRACE package):

Install [R Version 4.4.1](https://cran.r-project.org/bin/windows/base/old/4.4.1/), the compatible 
[RTools44](https://cran.r-project.org/bin/windows/Rtools/rtools44/rtools.html), and set up the respective environment variables such as 'R_HOME'.

#### 2. Set up Python:

Install [Python 3.12](https://www.python.org/downloads/release/python-3120/), setting the environment variable on `PATH`.

#### 3. Create a virtual environment
 
```sh
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

#### 4. Install dependencies

Install several packages from PyPI using:

```sh
pip install -r requirements.txt
```

Finally, install the Python interface for irace from [iracepy-tiny](https://github.com/Saethox/iracepy-tiny).

```sh
pip install git+https://github.com/Saethox/iracepy-tiny#egg=irace
```

### Installation (macOS / unix-based systems)

Functionality on macOS and unix-based systems is currently untested and may require additional configuration.
