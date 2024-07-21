## Makefile for the project
## Author: Themba Mahlangu

.PHONY: help

copy_deps: ## Copy poetry dependencies to requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes


lint: ## lint
	ruff check .
	ruff format .


zip_template: ## Zip the template
	cd ./vanty/scaffold/template/ && zip -rX app_template.zip app_template -x ".*" -x "__MACOSX"
	rclone copy ./vanty/scaffold/template/app_template.zip r2:advantch-prod/template/
