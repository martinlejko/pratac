#!/usr/bin/env python3
"""
Simple test script to verify the implementation works correctly.
"""

import sys
import os
import tempfile
import json
from pathlib import Path

# Add the pratac directory to the path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pratac'))

def test_default_behavior():
    """Test that default behavior still works."""
    print("Testing default behavior...")

    from pratac.definitions import get_person_offset, get_room_offset, get_start_date

    person_offset = get_person_offset()
    room_offset = get_room_offset()
    start_date = get_start_date()

    # Verify default values
    assert start_date == "2022-09-14", f"Expected '2022-09-14', got '{start_date}'"
    assert len(room_offset) == 4, f"Expected 4 rooms, got {len(room_offset)}"
    assert 0 in room_offset, "Missing room offset 0"
    assert room_offset[0] == "shower", f"Expected 'shower', got '{room_offset[0]}'"

    # Check persons
    assert ("martin", "mato") in person_offset, "Martin/Mato not found in person_offset"
    assert person_offset[("martin", "mato")] == 0, "Martin/Mato should have offset 0"

    print("✓ Default behavior works correctly")

def test_config_creation():
    """Test creating and loading a custom configuration."""
    print("Testing custom configuration...")

    from pratac.config import ConfigManager

    # Create a temporary config
    config_manager = ConfigManager()
    original_config_file = config_manager.config_file

    # Use a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        config_manager.config_file = Path(temp_dir) / "test_config.json"

        test_config = {
            "participants": ["Alice", "Bob", "Charlie"],
            "participant_aliases": {"Alice": ["Al"], "Bob": ["Bobby"]},
            "cleaning_areas": ["bathroom", "kitchen", "living_room"],
            "start_date": "2024-01-01"
        }

        # Save and load config
        config_manager.save_config(test_config)
        loaded_config = config_manager.load_config()

        assert loaded_config == test_config, "Config save/load failed"

        # Test person offset generation
        person_offset = config_manager.get_person_offset()
        assert len(person_offset) == 4, f"Expected 4 entries (3 people + 'all'), got {len(person_offset)}"

        # Verify alphabetical sorting
        sorted_participants = sorted(test_config["participants"])
        expected_offsets = {
            ("alice", "al"): 0,  # Alice comes first alphabetically
            ("bob", "bobby"): 1,  # Bob comes second
            ("charlie",): 2,      # Charlie comes third (no aliases)
            "all": 3
        }

        for key, expected_offset in expected_offsets.items():
            assert key in person_offset, f"Missing key: {key}"
            assert person_offset[key] == expected_offset, f"Wrong offset for {key}: expected {expected_offset}, got {person_offset[key]}"

        # Test room offset
        room_offset = config_manager.get_room_offset()
        expected_rooms = {0: "bathroom", 1: "kitchen", 2: "living_room"}
        assert room_offset == expected_rooms, f"Room offset mismatch: {room_offset}"

        # Test start date
        start_date = config_manager.get_start_date()
        assert start_date == "2024-01-01", f"Start date mismatch: {start_date}"

    print("✓ Custom configuration works correctly")

def test_schedule_calculation():
    """Test that schedule calculation works with both default and custom configs."""
    print("Testing schedule calculation...")

    from pratac.__main__ import calculate_week_offset, get_schedule
    from datetime import datetime

    # Test with a known date calculation
    # Using the default start date of 2022-09-14
    # and testing that week 0 gives us expected results

    # Mock the current date to a known value for consistent testing
    import pratac.__main__ as main_module
    original_datetime = main_module.datetime

    class MockDateTime:
        @staticmethod
        def strptime(date_string, format_string):
            return original_datetime.strptime(date_string, format_string)

        @staticmethod
        def now():
            # Return a fixed date: 2022-09-21 (one week after start)
            return original_datetime(2022, 9, 21)

    main_module.datetime = MockDateTime

    try:
        week_offset = calculate_week_offset(0)
        assert week_offset == 1, f"Expected week offset 1, got {week_offset}"

        # Test schedule generation (just verify it doesn't crash)
        import io
        import contextlib

        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            get_schedule("mato", week_offset)

        output = captured_output.getvalue()
        assert "mato" in output.lower(), "Schedule output should contain person name"
        assert str(week_offset) in output, "Schedule output should contain week number"

    finally:
        # Restore original datetime
        main_module.datetime = original_datetime

    print("✓ Schedule calculation works correctly")

def main():
    """Run all tests."""
    print("Running implementation tests...\n")

    try:
        test_default_behavior()
        test_config_creation()
        test_schedule_calculation()

        print("\n✅ All tests passed! Implementation is working correctly.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()