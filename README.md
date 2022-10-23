srtgen
======

Tool to automatically generate .srt files from media files.

The result is absolute crap, but it is a good starting point to manually make a subtitle, rather than start from scratch.

Install it
----------

```bash

cd /tmp/
python3 -m venv srtgen
. srtgen/bin/activate
pip install git+https://github.com/openai/whisper.git
pip install srtgen
```

Execute it
----------

```bash

srtgen --help
```
