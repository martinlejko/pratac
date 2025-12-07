# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Pratac is a Python package for managing cleaning schedules for dorm participants across different rooms over multiple weeks. It calculates week offsets from a fixed start date (2022-09-14) and assigns cleaning tasks based on rotational scheduling.

## Development Commands

This project uses Poetry for dependency management. Key commands:

- **Install dependencies**: `poetry install`
- **Run the CLI (backward compatible)**: `poetry run pratac <person> [week_offset]` or `python -m pratac <person> [week_offset]`
- **Interactive setup**: `poetry run pratac init`
- **View configuration**: `poetry run pratac config`
- **Reset configuration**: `poetry run pratac reset`
- **Type checking**: `poetry run mypy pratac/`
- **Linting and formatting**: `poetry run ruff check pratac/` and `poetry run ruff format pratac/`
- **Run tests**: `poetry run pytest` (pytest is configured as dev dependency)
- **Build package**: `poetry build`

## Code Architecture

### Core Components

- **`__main__.py`**: Entry point with command routing and scheduling logic
  - `calculate_week_offset()`: Calculates week number from configurable start date
  - `get_schedule()`: Determines cleaning assignment based on person and week
  - `process_schedule_args()`: Handles schedule generation commands
  - `main()`: Routes commands to appropriate handlers

- **`argparser.py`**: Command-line argument parsing with backward compatibility
  - `ArgParser` class with subcommands (init, config, reset, schedule)
  - Maintains backward compatibility for `pratac <person> [offset]` usage
  - Dynamic person validation against current configuration

- **`definitions.py`**: Configuration loader with fallback to defaults
  - `get_person_offset()`: Returns person mappings from config or defaults
  - `get_room_offset()`: Returns room mappings from config or defaults
  - `get_start_date()`: Returns start date from config or default
  - Preserves original hardcoded values as fallback

- **`config.py`**: Configuration management system
  - `ConfigManager`: Handles JSON config file operations in `~/.pratac/`
  - Loads/saves participant lists, aliases, cleaning areas, start dates
  - Automatically sorts participants alphabetically for consistent roommate sharing

- **`interactive.py`**: Interactive setup and configuration management
  - `run_interactive_setup()`: Guided configuration creation
  - `show_current_config()`: Display current settings
  - `reset_config()`: Remove custom config and return to defaults

### Scheduling Algorithm

The cleaning schedule uses modular arithmetic:
1. Calculate absolute week number from start date plus offset
2. Use `(week_num + person_offset) % len(room_offset)` to determine room assignment
3. Each person rotates through rooms in the same order but offset by their person number

### Configuration System

**Dual-mode operation**:
- **Default mode**: Uses hardcoded values when no custom config exists
- **Custom mode**: Loads from `~/.pratac/config.json` when available

**Default configuration**:
- Participants: martin/mato, adam/trumtulus, dano/danko, samo/kori
- Room assignments: shower (0), toilet (1), floor (2), kitchen (3)
- Start date: "2022-09-14"

**Custom configuration features**:
- Any number of participants with optional aliases
- Any number of cleaning areas
- Configurable start date
- Alphabetical participant sorting ensures roommate schedule consistency

**Roommate sharing**: Multiple people entering the same participants in any order will get identical schedules due to automatic alphabetical sorting

## Package Distribution

- Uses both Poetry (`pyproject.toml`) and setuptools (`setup.py`) for compatibility
- Entry point: `pratac = pratac.__main__:main`
- Poetry configuration includes mypy (strict mode) and ruff (line length 120)