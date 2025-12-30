# python-tutorials

Python tutorials using Marimo notebooks.

## Prerequisites

### Installation Guide: Python, marimo, and Git

This guide will walk you through installing Python, marimo, and Git on both Windows and macOS systems.

### Windows Installation

### Installing Python

1. Visit the official Python website at https://www.python.org/downloads/
2. Download the latest Python installer for Windows (3.8 or higher recommended)
3. Run the installer and **make sure to check the box that says "Add Python to PATH"** before clicking "Install Now"
4. Verify the installation by opening Command Prompt and running:
   ```
   python --version
   ```

### Installing Git

1. Visit https://git-scm.com/download/win
2. Download the Git installer for Windows
3. Run the installer, using the default options (or customize if you prefer)
4. Verify the installation by opening Command Prompt and running:
   ```
   git --version
   ```

### Installing marimo

1. Open Command Prompt
2. Install marimo using pip:
   ```
   pip install marimo
   ```
3. Verify the installation:
   ```
   marimo --version
   ```

## macOS Installation

### Installing Python

macOS comes with Python pre-installed, but it's often an older version. It's recommended to install a newer version:

**Option 1: Using Homebrew (Recommended)**

First, install Homebrew if you don't have it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python:

```bash
brew install python
```

**Option 2: Official Installer**

1. Visit https://www.python.org/downloads/macos/
2. Download the latest macOS installer
3. Run the installer package and follow the installation steps

Verify the installation:

```bash
python3 --version
```

### Installing Git

**Option 1: Using Homebrew (Recommended)**

```bash
brew install git
```

**Option 2: Xcode Command Line Tools**

Git comes with Xcode Command Line Tools. Install them by running:

```bash
xcode-select --install
```

**Option 3: Official Installer**

Download from https://git-scm.com/download/mac and run the installer.

Verify the installation:

```bash
git --version
```

### Installing marimo

Once Python and pip are installed:

```bash
pip3 install marimo
```

If you installed Python via Homebrew, you can also use:

```bash
pip install marimo
```

Verify the installation:

```bash
marimo --version
```

If the marimo command isn't found, you may need to add the Python bin directory to your PATH. Add this line to your `~/.zshrc` (or `~/.bash_profile` if using bash):

```bash
export PATH="$HOME/Library/Python/3.x/bin:$PATH"
```

Replace `3.x` with your Python version (e.g., `3.11`). Then reload your shell:

```bash
source ~/.zshrc  # or source ~/.bash_profile
```

## Getting Started with marimo

Once everything is installed, you can create your first marimo notebook:

```bash
marimo tutorial intro
```

Or create a new notebook:

```bash
marimo edit my_notebook.py
```

This will open marimo in your default web browser where you can start creating interactive Python notebooks!

## Python tutorial projects

- [Budget Tracker](/docs/budget_tracker.md)
