# hashcheck

A small Python command-line utility for checking whether a downloaded file matches an expected SHA-256 hash.

## Current functionality

- Reads a file path from the command line.
- Computes the file's SHA-256 digest in binary mode, reading it in 8192-byte chunks.
- Prompts for an expected hash and compares it with the computed digest.
- Reports whether the hashes match. If they do not, it warns that the file may have been changed or tampered with.

## Usage

Python 3.8 or newer is recommended because the script uses the assignment expression syntax.

```bash
python main.py path/to/file
```

When prompted, enter the expected SHA-256 hash.

## Project status

This is an early-stage project consisting of a single Python script. It currently provides a direct interactive comparison and does not include argument parsing for the expected hash, support for other hash algorithms, automated tests, or package/distribution configuration.

## License

See [LICENSE](LICENSE).

---

This README was generated with the assistance of GitHub Copilot. The rest of the project's code was written by a human.
