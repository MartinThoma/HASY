make:
	tar -cvjSf HASYv2.tar.bz2 -T CONTENT

upload:
	make clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

clean:
	rm -rf hasy.egg-info dist tests/reports tests/__pycache__ lidtk.errors.log lidtk.info.log hasy/cm_analysis.html
