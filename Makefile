make:
	tar -cvjSf HASYv2.tar.bz2 -T CONTENT

maint:
	pre-commit autoupdate && pre-commit run --all-files
	pip-compile -U requirements-lint.in
	pip-compile -U requirements-dev.in
	pip-compile -U setup.py

upload:
	make clean
	python setup.py sdist bdist_wheel && twine upload dist/*

clean:
	python setup.py clean --all
	pyclean .
	rm -rf hasy.egg-info dist tests/reports tests/__pycache__ lidtk.errors.log lidtk.info.log hasy/cm_analysis.html

mutation-test:
	mutmut run

mutmut-results:
	mutmut junitxml --suspicious-policy=ignore --untested-policy=ignore > mutmut-results.xml
	junit2html mutmut-results.xml mutmut-results.html

bandit:
	# Python3 only: B322 is save
	bandit -r mpu -s B322
