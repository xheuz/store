tailwindcss:
	npx tailwindcss --input ./src/css/input.css --output ./public/css/styles.css --watch --minify

build:
	python main.py

runserver:
	python -m http.server --directory public

pull_data:
	wget --output-file="/tmp/logs.csv" "https://docs.google.com/spreadsheets/d/1cZtA1ZPrW9TqoxS4RGxTRzTJnAG0kLzOHmIyGdBzxWA/export?format=csv&gid=2043408291" -O "./src/data/inventory.csv"

publish: pull_data build
	git add .
	git commit -m "updated inventory"
	git push origin main
