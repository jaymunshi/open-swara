# Open Swara (स्वर)

**The largest open-source humanized voice library** — 4,065 voice samples across 44 languages, free forever under CC-BY-SA 4.0.

## What Is Open Swara?

We collected raw AI/synthetic voice samples from 10 open-source datasets, then **humanized every single one** through our proprietary voice processing pipeline. The original synthetic artifacts — robotic tone, unnatural cadence, flat prosody — are replaced with natural-sounding speech while preserving each voice's unique timbre, pitch, and character.

The result: a massive library of natural-sounding reference voices that anyone can use for TTS, voice cloning, dubbing, audiobooks, and creative projects.

## Stats

| Metric | Count |
|--------|-------|
| Total voices | 4,065 |
| Languages | 44 |
| Native language voices | 3,454 |
| English accent voices | 611 |
| Male voices | 2,105 |
| Female voices | 1,818 |
| Unknown gender | 142 |

## Structure

```
voices/
├── english/
│   ├── male/
│   │   ├── english_male_open_swara_001.wav
│   │   └── ...
│   ├── female/
│   └── unknown/
├── german/
│   ├── male/
│   │   ├── german_male_open_swara_001.wav          ← speaking German
│   │   ├── german_male_english_open_swara_001.wav  ← speaking English with German accent
│   ├── female/
│   └── unknown/
├── french/
│   └── ...
└── ... (44 languages)
```

### File Naming

- `{language}_{gender}_open_swara_{NNN}.wav` — voice speaking in its native language
- `{language}_{gender}_english_open_swara_{NNN}.wav` — voice speaking English with native accent

## Languages

Arabic, Bulgarian, Catalan, Chinese, Czech, Danish, Dutch, English, Finnish, French, Georgian, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kazakh, Korean, Lao, Latvian, Luxembourgish, Malayalam, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Telugu, Turkish, Twi, Ukrainian, Vietnamese, Welsh

## Usage

These voices are ideal as **reference samples** for:
- Text-to-Speech (TTS) voice cloning
- Voice conversion systems
- Multilingual dubbing and localization
- Audiobook narration prototyping
- Creative and research projects

## Browsing the Catalog

```bash
# Search for German female voices
python scripts/browse_catalog.py --language german --gender female

# List all languages
python scripts/browse_catalog.py --list-languages

# Search by keyword
python scripts/browse_catalog.py --search "english_accent"
```

## License

**CC-BY-SA 4.0** — free for commercial and non-commercial use with attribution.

See [LICENSE](LICENSE) for full terms.

## Attribution

When using Open Swara voices, please credit:

> Voices from [Open Swara](https://github.com/jaymunshi/open-swara).

See [ATTRIBUTION.md](ATTRIBUTION.md) for source dataset credits.
