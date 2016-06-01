default: README.html

README.html: README.md
	cat README.md | pandoc -f markdown_github > README.html

README.pdf: README.md
	cat README.md | pandoc -f markdown_github -o README.pdf
