## Makefile for the project
## Author: Themba Mahlangu

.PHONY: help

copy_deps: ## Copy poetry dependencies to requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes
