   ################################################################################
#
# packaging
#
################################################################################

PACKAGING_VERSION = 21.3
PACKAGING_SOURCE = packaging-21.3.tar.gz
PACKAGING_SITE = https://files.pythonhosted.org/packages/df/9e/d1a7217f69310c1db8fdf8ab396229f55a699ce34a203691794c5d1cad0c
PACKAGING_LICENSE = Apache License
PACKAGING_LICENSE_FILES = LICENSE
PACKAGING_DEPENDENCIES:=
PACKAGING_SETUP_TYPE:= distutils

$(eval $(python-package))