# todotxtExtended

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

todotxtExtended is an enhanced Python script for managing tasks using an extended version of the todo.txt format. It builds upon the simplicity and flexibility of the original todo.txt system while adding powerful features for more comprehensive task management.

## Table of Contents

- [todotxtExtended](#todotxtextended)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Features](#features)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Basic Commands](#basic-commands)
  - [Creating Aliases](#creating-aliases)
    - [For Linux/macOS](#for-linuxmacos)
    - [For Windows](#for-windows)
  - [Alternative Usage Methods](#alternative-usage-methods)
  - [Extended Format](#extended-format)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

## Background

todotxtExtended is inspired by the original [todo.txt](https://github.com/todotxt/todo.txt) project, which aims to bring the power of plain text task management to the command line. This project extends the concept to include additional features that support the [Getting Things Done (GTD)](https://en.wikipedia.org/wiki/Getting_Things_Done) methodology, allowing for more detailed task tracking and management.

## Features

- **All original todo.txt features**, including priorities, projects, and contexts
- **Extended date handling**: Creation dates, due dates, and completion dates
- **Task status tracking**: Start, pause, and complete tasks
- **Recurrence**: Set tasks to repeat at specified intervals
- **Time tracking**: Record time spent on tasks
- **Enhanced filtering and sorting**: Filter and sort tasks by various criteria
- **Archiving**: Move completed tasks to a separate file
- **Comments**: Add non-task notes to your todo.txt file

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/todotxtExtended.git
   ```
2. Navigate to the project directory:
   ```
   cd todotxtExtended
   ```
3. Ensure you have Python 3.6+ installed.

## Configuration

todotxtExtended reads the `todo.txt` and `done.txt` files from a directory configured in a `.todo` file located in the user's home directory. If this file doesn't exist, the script will create it along with a default "Life" folder in the home directory.

The default configuration in the `.todo` file is as follows:

```
TODO_FILE=/path/to/home/Life/todo.txt
DONE_FILE=/path/to/home/Life/done.txt
HELP_FILE=/path/to/home/Life/todohelp.txt
```

You can customize these paths by editing the `.todo` file. For example:

```
TODO_FILE=/custom/path/todo.txt
DONE_FILE=/custom/path/done.txt
HELP_FILE=/custom/path/todohelp.txt
```

If the specified directories don't exist, the script will create them automatically.

## Usage

Run the script from the command line:

```
python todo.py [options]
```

For a full list of commands and options, use:

```
python todo.py --help
```

For an extended manual, use:

```
python todo.py --manual
```

### Basic Commands

- Add a task: `python todo.py --add "Task description @context +project #tag due:date"`
- List tasks: `python todo.py --list`
- Complete a task: `python todo.py --complete <task_id>`
- Start a task: `python todo.py --start <task_id>`
- Pause a task: `python todo.py --pause <task_id>`

## Creating Aliases

To make using todotxtExtended more convenient, you can create aliases for common commands.

### For Linux/macOS

1. Open your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, etc.) in a text editor.
2. Add the following lines:

```bash
alias todo='python /path/to/todo.py'
alias t='python /path/to/todo.py'
alias ta='python /path/to/todo.py --add'
alias tl='python /path/to/todo.py --list'
alias tc='python /path/to/todo.py --complete'
alias ts='python /path/to/todo.py --start'
alias tp='python /path/to/todo.py --pause'
```

3. Save the file and reload your shell configuration:

```bash
source ~/.bashrc  # or the appropriate file for your shell
```

### For Windows

1. Open a command prompt as an administrator.
2. Use the `doskey` command to create aliases:

```
doskey todo=python C:\path\to\todo.py $*
doskey t=python C:\path\to\todo.py $*
doskey ta=python C:\path\to\todo.py --add $*
doskey tl=python C:\path\to\todo.py --list $*
doskey tc=python C:\path\to\todo.py --complete $*
doskey ts=python C:\path\to\todo.py --start $*
doskey tp=python C:\path\to\todo.py --pause $*
```

To make these aliases permanent, you can create a batch file with these commands and add it to your Windows startup folder or run it as part of your command prompt initialization.

## Alternative Usage Methods

1. **Make the script executable (Linux/macOS):**
   
   Add a shebang line at the beginning of the script:
   ```python
   #!/usr/bin/env python3
   ```
   Then make it executable:
   ```bash
   chmod +x /path/to/todo.py
   ```
   Now you can run it directly:
   ```bash
   ./todo.py [options]
   ```

2. **Create a batch file (Windows):**
   
   Create a file named `todo.bat` in a directory in your PATH with the following content:
   ```batch
   @echo off
   python C:\path\to\todo.py %*
   ```
   Now you can use `todo` from anywhere in the command prompt.

3. **Use `python -m`:**
   
   If you add the directory containing `todo.py` to your PYTHONPATH, you can run it as a module:
   ```bash
   python -m todo [options]
   ```

These methods allow for more flexible and convenient usage of todotxtExtended across different operating systems and environments.

## Extended Format

todotxtExtended uses an extended version of the todo.txt format. Here's a brief overview:

```
(A) 2023-04-15 Call mom @phone +Family due:2023-04-16 rec:1w
```

- `(A)`: Priority
- `2023-04-15`: Creation date
- `@phone`: Context
- `+Family`: Project
- `due:2023-04-16`: Due date
- `rec:1w`: Recurrence (weekly)

Additional features:
- `[=]`: Task in progress
- `[?]`: Paused task
- `x`: Completed task (prepended)

For a full description of the format, please refer to the [todohelp.txt](todohelp.txt) file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

This project is inspired by and builds upon the work of Gina Trapani and the todo.txt community. We are grateful for their pioneering efforts in plain-text task management.

- [todo.txt](https://github.com/todotxt/todo.txt)
- [Gina Trapani](http://ginatrapani.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
