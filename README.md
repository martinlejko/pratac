# Pratac Package

Pratac is a Python package designed to help you manage cleaning schedule for different participants in various rooms over multiple weeks. It provides functionality to calculate week offsets, process arguments, and retrieve schedules for specified individuals or all participants. :)

## Installation

You can install Pratac via pip:

```bash
pip install pratac
```

## Usage

### Command Line Interface

Pratac comes with a command-line interface (CLI) to facilitate schedule management. Here's how you can use it:

```bash
pratac [-h] person [--week_offset num] 
```

- `person`: The name of the person for whom you want to retrieve the schedule. Use "all" to get schedules for all participants.

Optional arguments:

- `--week_offset`: The offset in weeks from the starting date. Default is 0. Next week is 1, previous week is -1, and so on.

### Example

To retrieve the schedule for a specific person:

```bash
pratac Mato
```

To retrieve schedules for all participants for the upcoming week:

```bash
pratac all 1
```

## Definitions File

Pratac requires a definitions file where you can specify/customize participants and rooms. Make sure to set these appropriately before using the package.

## Development

If you'd like to contribute to Pratac or report issues, you can find the project on [GitHub](https://github.com/yourusername/pratac).

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

---
