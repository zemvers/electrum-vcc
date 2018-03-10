Electrum-VCC - Lightweight Vertcoin Cash client
===============================================

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Port Maintainer: Pooler (Electrum-LTC)
  Port Maintainer: Vertcoin (Electrum-VTC)
  Language: Python
  Homepage: https://vertcoincash.org






Getting started
===============

Electrum is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python-qt4
    sudo pip2 install https://github.com/metalicjames/lyra2re-hash-python/archive/master.zip

If you downloaded the official package (tar.gz), you can run
Electrum from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum from its root directory, just do::

    ./electrum-vtc

You can also install Electrum on your system, by running this command::

    python setup.py install

This will download and install the Python dependencies used by
Electrum, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Electrum. Read the next section, "Development
Version".



Development version
===================

Check out the code from Github::

    git clone https://github.com/vertcoin/electrum-vtc.git
    cd electrum-vtc

Run install (this should install dependencies)::

    python setup.py install

Compile the icons and style files for VTC::

    sudo apt-get install pyqt4-dev-tools
    pyrcc4 icons.qrc -o gui/vtc/icons_rc.py
    pyrcc4 style.qrc -o gui/vtc/style_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-pycurl gettext
    ./contrib/make_locale




Creating Binaries
=================


To create binaries, create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum.
If you get ImportErrors, this is because the modules aren't installed or
are installed, but compressed. Uninstall/install dependencies with pip,
which always installs everything unzipped.

Mac OS X
--------

::

    # On MacPorts installs: 
    sudo python setup-release.py py2app
    
    # On Homebrew installs: 
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip
    
    sudo hdiutil create -fs HFS+ -volname "Electrum-VTC" -srcfolder dist/Electrum-VTC.app dist/electrum-vtc-VERSION-macosx.dmg

Windows
-------

See `contrib/build-wine/README` file.


Android
-------

See `gui/kivy/Readme.txt` file.
