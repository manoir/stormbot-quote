VERSION=$(shell grep -Po "(?<=version=([\"']))(([0-9]\.){2}(dev)?[0-9])" setup.py)
PKG_NAME=$(shell grep -Po "(?<=name=([\"']))(.*)(?=\1)" setup.py)
SDIST=dist/${PKG_NAME}-${VERSION}.tar.gz
ASC=${SDIST}.asc
REPO?=pypi

all: ${SDIST} ${ASC}

${SDIST}:
	./setup.py build sdist
	twine check ${SDIST}

${ASC}: ${SDIST}
	gpg --detach-sign --default-key 56B1766D69E513DB9E405BBB672CDD2031AAF49B -a $<

upload: ${SDIST} ${ASC}
	twine upload --repository ${REPO} --skip-existing $^

clean:
	rm -rf dist/*.tar.gz
	rm -rf dist/*.asc

.PHONY: ${SDIST}
