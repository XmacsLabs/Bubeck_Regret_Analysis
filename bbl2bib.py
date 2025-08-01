import re
import sys


def bbl_to_bib(bbl_file, bib_file):
    with open(bbl_file, "r") as f:
        content = f.read()

    entries = re.findall(
        r"\\bibitem(?:\[.*?\])?\{(.*?)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})",
        content,
        re.DOTALL,
    )

    with open(bib_file, "w") as f:
        for key, text in entries:
            text = re.sub(r"\s+", " ", text.strip())  # Clean whitespace
            f.write(f"@misc{{{key},\n  note = {{{text}}}\n}}\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bbl2bib.py input.bbl output.bib")
        sys.exit(1)
    bbl_to_bib(sys.argv[1], sys.argv[2])
