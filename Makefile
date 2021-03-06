
PKGNAME    = rule-editor

# Directories.
VENVDIR    = $(CURDIR)/virtualenv
RESULTDIR  = $(CURDIR)/results
REQUIREDIR = $(CURDIR)/requirements

SRCCOREDIR = $(CURDIR)/source

# Commands.
VIRTUALENV = virtualenv
PIP        = $(VENVDIR)/bin/pip2
PYUIC4     = $(VENVDIR)/bin/pyuic4
PYTHON     = $(VENVDIR)/bin/python
WGET       = wget
NOSETESTS  = $(VENVDIR)/bin/nosetests
PYLINT     = $(VENVDIR)/bin/pylint
SLOCCOUNT  = sloccount

# Package
SIP  = sip-4.16.6
PYQT = PyQt-x11-gpl-4.11.3

.PHONY: clean env test pylint linecount install-app run

clean: clean-tmp
	rm -rf $(VENVDIR)
	rm -rf $(RESULTDIR)
	rm -rf $(REQUIREDIR)/$(SIP)
	rm -rf $(REQUIREDIR)/$(PYQT)

env:
	$(VIRTUALENV) $(VENVDIR)
	rm $(VENVDIR)/include/python2.7
	cp -r /usr/include/python2.7 $(VENVDIR)/include
	$(PIP) install -r req-test.txt
	$(PIP) install -r req-app.txt
	$(MAKE) install-pyqt
	$(MAKE) install-yara

install-yara:
	@echo "Installing YARA 3.3.0..."
	if [ ! -f $(REQUIREDIR)/v3.3.0.tar.gz ]; then \
	$(WGET) --directory-prefix=$(REQUIREDIR) https://github.com/plusvic/yara/archive/v3.3.0.tar.gz ;\
	fi
	cd $(REQUIREDIR) && tar xzf v3.3.0.tar.gz
	cd $(REQUIREDIR)/yara-3.3.0 && ./bootstrap.sh
	cd $(REQUIREDIR)/yara-3.3.0 && ./configure --prefix=$(VENVDIR)
	cd $(REQUIREDIR)/yara-3.3.0 && make
	cd $(REQUIREDIR)/yara-3.3.0 && make install
	cd $(REQUIREDIR)/yara-3.3.0/yara-python && $(VENVDIR)/bin/python setup.py build
	cd $(REQUIREDIR)/yara-3.3.0/yara-python && $(VENVDIR)/bin/python setup.py install
	mkdir -p $(VENVDIR)/etc
	echo "virtualenv/lib" > $(VENVDIR)/etc/ld.so.conf


install-sip:
	@echo "Installing SIP $(SIP)..."
	if [ ! -f $(REQUIREDIR)/$(SIP).zip ]; then \
	$(WGET) --directory-prefix=$(REQUIREDIR) http://sourceforge.net/projects/pyqt/files/sip/$(SIP)/$(SIP).zip ;\
	fi
	cd $(REQUIREDIR) && unzip $(SIP).zip
	. $(VENVDIR)/bin/activate && cd $(REQUIREDIR)/$(SIP) && $(PYTHON) configure.py --incdir=$(VENVDIR)/include/python2.7
	. $(VENVDIR)/bin/activate && cd $(REQUIREDIR)/$(SIP) && make
	. $(VENVDIR)/bin/activate && cd $(REQUIREDIR)/$(SIP) && make install

install-pyqt: install-sip
	@echo "Installing PyQt 4.10.3..."
	if [ ! -f $(REQUIREDIR)/PyQt-x11-gpl-4.11.3.tar.gz ]; then \
	$(WGET) --directory-prefix=$(REQUIREDIR) http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.3/PyQt-x11-gpl-4.11.3.tar.gz; \
	fi
	cd $(REQUIREDIR) && tar xzf PyQt-x11-gpl-4.11.3.tar.gz
	. $(VENVDIR)/bin/activate; cd $(REQUIREDIR)/PyQt-x11-gpl-4.11.3 && $(PYTHON) configure-ng.py
	. $(VENVDIR)/bin/activate; cd $(REQUIREDIR)/PyQt-x11-gpl-4.11.3 && make
	. $(VENVDIR)/bin/activate; cd $(REQUIREDIR)/PyQt-x11-gpl-4.11.3 && make install


test:
	$(NOSETESTS) ${SRCCOREDIR} test \
		--with-coverage --cover-package=app \
		--cover-xml --cover-xml-file=coverage.xml \qt
		--with-xunit --xunit-file=nosetests.xml

pylint:
	$(PYLINT) ${SRCCOREDIR}/app > pylint.out || /bin/true

linecount:
	 $(SLOCCOUNT) --duplicates --wide --details ${SRCCOREDIR} > sloccount.sc

compile-ui:
	$(PYUIC4) ${SRCCOREDIR}/ruleeditor/ui/mainwindow.ui > ${SRCCOREDIR}/ruleeditor/ui/mainwindow.py
	$(PYUIC4) ${SRCCOREDIR}/ruleeditor/ui/dialogNewFile.ui > ${SRCCOREDIR}/ruleeditor/ui/dialogNewFile.py
	$(PYUIC4) ${SRCCOREDIR}/ruleeditor/ui/dialogSettings.ui > ${SRCCOREDIR}/ruleeditor/ui/dialogSettings.py
	$(PYUIC4) ${SRCCOREDIR}/ruleeditor/plugins/ioceditor/IOCWidget.ui > ${SRCCOREDIR}/ruleeditor/plugins/ioceditor/IOCWidget.py


install-app: compile-ui package
	$(PIP) install --no-index $(RESULTDIR)/rule_editor-*.whl

package:
	mkdir -p $(RESULTDIR)
	cd ${SRCCOREDIR} && python setup.py bdist_wheel
	cp ${SRCCOREDIR}/dist/*.whl $(RESULTDIR)

clean-tmp:
	rm -rf $(VENVDIR)/lib/python2.7/site-packages/ruleeditor
	rm -rf $(RESULTDIR)
	rm -rf $(SRCCOREDIR)/dist
	rm -rf $(SRCCOREDIR)/build
	rm -rf $(SRCCOREDIR)/rule_editor.egg-info

run: clean-tmp install-app
	. $(VENVDIR)/bin/activate; rule-editor
