tailwindcss:
	npx tailwindcss --input ./src/css/input.css --output ./public/css/styles.css --watch --minify

build:
	python main.py

runserver:
	python -m http.server --directory public

publish: build
	git add .
	git commit -m "updated inventory"
	git push origin main
