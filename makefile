.ONESHELL:

-include .env
export

test:
	@pip -q install pytest
	@pytest
