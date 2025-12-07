#!/usr/bin/env python3
"""
Manual test script to verify the new commands work.
"""

import sys
import os

# Add the pratac directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Mock sys.argv for testing
original_argv = sys.argv

def test_init_command():
    print("Testing 'pratac init' command...")
    sys.argv = ['pratac', 'init']

    try:
        from pratac.argparser import ArgParser
        parser = ArgParser()
        args = parser.parse_args()
        print(f"✓ Arguments parsed successfully: {args}")
        print(f"  Command: {args.command}")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    finally:
        sys.argv = original_argv

def test_config_command():
    print("Testing 'pratac config' command...")
    sys.argv = ['pratac', 'config']

    try:
        from pratac.argparser import ArgParser
        parser = ArgParser()
        args = parser.parse_args()
        print(f"✓ Arguments parsed successfully: {args}")
        print(f"  Command: {args.command}")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    finally:
        sys.argv = original_argv

def test_backward_compatibility():
    print("Testing backward compatibility 'pratac mato'...")
    sys.argv = ['pratac', 'mato']

    try:
        from pratac.argparser import ArgParser
        parser = ArgParser()
        args = parser.parse_args()
        print(f"✓ Arguments parsed successfully: {args}")
        print(f"  Command: {args.command}")
        print(f"  Person: {args.person}")
        print(f"  Week offset: {args.week_offset}")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    finally:
        sys.argv = original_argv

def test_backward_compatibility_with_offset():
    print("Testing backward compatibility 'pratac mato 1'...")
    sys.argv = ['pratac', 'mato', '1']

    try:
        from pratac.argparser import ArgParser
        parser = ArgParser()
        args = parser.parse_args()
        print(f"✓ Arguments parsed successfully: {args}")
        print(f"  Command: {args.command}")
        print(f"  Person: {args.person}")
        print(f"  Week offset: {args.week_offset}")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    finally:
        sys.argv = original_argv

def main():
    print("Manual testing of pratac commands\n")

    tests = [
        test_init_command,
        test_config_command,
        test_backward_compatibility,
        test_backward_compatibility_with_offset
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! The argparser is working correctly.")
    else:
        print("❌ Some tests failed. Check the implementation.")

if __name__ == "__main__":
    main()