# Pratac Usage Examples

This document shows how to use the new interactive features while maintaining backward compatibility.

## Backward Compatibility

The original usage still works exactly as before:

```bash
# Get schedule for Martin/Mato for current week
pratac mato

# Get schedule for Martin/Mato for next week
pratac mato 1

# Get all schedules for current week
pratac all

# Get all schedules for previous week
pratac all -1
```

## New Interactive Features

### Initialize Custom Configuration

Run the interactive setup to create your own cleaning schedule:

```bash
pratac init
```

This will prompt you for:
- Cleaning areas (default: shower, toilet, floor, kitchen)
- Participant names and optional aliases
- Start date (default: today)

Example session:
```
Pratac Interactive Setup
========================

Cleaning Areas Setup
Default areas: shower, toilet, floor, kitchen
Use default cleaning areas? (y/n): n

Enter cleaning areas (press Enter with empty input to finish):
Area 1: bathroom
Area 2: kitchen
Area 3: living room
Area 4:

Participants Setup
Participant 1 name (or press Enter to finish): Alice
Enter aliases for Alice (press Enter with empty input to finish):
  Alias: Al
  Alias:

Participant 2 name (or press Enter to finish): Bob
Enter aliases for Bob (press Enter with empty input to finish):
  Alias: Bobby
  Alias:

Participant 3 name (or press Enter to finish): Charlie
Enter aliases for Charlie (press Enter with empty input to finish):
  Alias:

Participant 4 name (or press Enter to finish):

Start Date Setup
Default start date: 2024-01-15
Use today as start date? (y/n): y

Schedule Preview (first 4 weeks):
==================================================

Week 1:
  Alice (aliases: Al): bathroom
  Bob (aliases: Bobby): kitchen
  Charlie: living room

Week 2:
  Alice (aliases: Al): kitchen
  Bob (aliases: Bobby): living room
  Charlie: bathroom

Week 3:
  Alice (aliases: Al): living room
  Bob (aliases: Bobby): bathroom
  Charlie: kitchen

Week 4:
  Alice (aliases: Al): bathroom
  Bob (aliases: Bobby): kitchen
  Charlie: living room

Configuration Summary:
Participants: Alice, Bob, Charlie
Cleaning areas: bathroom, kitchen, living room
Start date: 2024-01-15

Save this configuration? (y/n): y

Configuration saved to /Users/username/.pratac/config.json
You can now use 'pratac <person>' to get schedules!
```

### View Current Configuration

```bash
pratac config
```

Shows either your custom configuration or the default settings.

### Reset to Defaults

```bash
pratac reset
```

Removes your custom configuration and returns to the original hardcoded settings.

## Roommate Sharing

When multiple roommates run `pratac init` with the same participants and cleaning areas, they'll automatically get identical schedules because participants are sorted alphabetically before assigning positions in the rotation.

Example:
- Roommate 1 enters: Alice, Bob, Charlie
- Roommate 2 enters: Charlie, Alice, Bob
- Roommate 3 enters: Bob, Charlie, Alice

All three will get the same schedule because the participants are sorted to: Alice, Bob, Charlie before creating the rotation.

## Testing the Implementation

You can test the implementation manually:

1. **Test default behavior (no config)**:
   ```bash
   pratac mato
   pratac all
   ```

2. **Test interactive setup**:
   ```bash
   pratac init
   # Follow prompts to create custom config
   ```

3. **Test with custom config**:
   ```bash
   pratac alice  # or whatever name you entered
   pratac config  # view configuration
   ```

4. **Test reset**:
   ```bash
   pratac reset
   pratac mato  # should work with defaults again
   ```

## Configuration File Location

Custom configurations are stored in:
- Linux/macOS: `~/.pratac/config.json`
- Windows: `C:\Users\<username>\.pratac\config.json`

You can manually edit this file if needed, but use `pratac init` for the guided setup experience.