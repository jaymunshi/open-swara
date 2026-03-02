#!/usr/bin/env python3
"""Browse and search the Open Swara voice catalog."""
import json
import argparse
import sys
from pathlib import Path

CATALOG = Path(__file__).parent.parent / 'catalog.json'


def load_catalog():
    with open(CATALOG) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description='Browse Open Swara voices')
    parser.add_argument('--language', '-l', help='Filter by language name')
    parser.add_argument('--gender', '-g', choices=['male', 'female', 'unknown'], help='Filter by gender')
    parser.add_argument('--type', '-t', choices=['native', 'english_accent'], help='Filter by voice type')
    parser.add_argument('--search', '-s', help='Search voice IDs by keyword')
    parser.add_argument('--list-languages', action='store_true', help='List all languages with counts')
    parser.add_argument('--stats', action='store_true', help='Show catalog statistics')
    args = parser.parse_args()

    catalog = load_catalog()

    if args.stats:
        print(f"Open Swara v{catalog['version']}")
        print(f"Total voices: {catalog['total_voices']}")
        print(f"Languages: {catalog['total_languages']}")
        print(f"Native: {catalog['native_voices']}, English accent: {catalog['english_accent_voices']}")
        print(f"Gender: {catalog['gender_breakdown']}")
        return

    if args.list_languages:
        for lang, count in sorted(catalog['languages'].items()):
            print(f"  {lang:20s} {count:5d} voices")
        return

    voices = catalog['voices']

    if args.language:
        voices = [v for v in voices if v['language'] == args.language.lower()]
    if args.gender:
        voices = [v for v in voices if v['gender'] == args.gender]
    if args.type:
        voices = [v for v in voices if v['type'] == args.type]
    if args.search:
        voices = [v for v in voices if args.search.lower() in v['voice_id'].lower()]

    if not voices:
        print('No voices found matching criteria.')
        return

    print(f"Found {len(voices)} voices:")
    for v in voices:
        print(f"  {v['file']:70s}  {v['gender']:7s}  {v['type']:14s}  {v['duration_seconds']:.1f}s")


if __name__ == '__main__':
    main()
