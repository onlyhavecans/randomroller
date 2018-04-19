deploy:
	git push
	git push --tags
	pipenv update --dev
	rm -f dist/*
	pipenv run python setup.py sdist bdist_wheel
	gpg --detach-sign -a dist/*.tar.gz
	gpg --detach-sign -a dist/*.whl
	pipenv run twine upload dist/*

.PHONY: deploy
