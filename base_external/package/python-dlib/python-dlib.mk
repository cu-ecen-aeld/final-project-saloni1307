    ################################################################################
#
# pydrive
#
################################################################################

PYTHON_DLIB_VERSION = 19.22.1
PYTHON_DLIB_SOURCE = dlib-$(PYTHON_DLIB_VERSION).tar.gz
PYTHON_DLIB_SITE = https://files.pythonhosted.org/packages/f0/a2/ba6163c09fb427990180afd8d625bcecc5555af699c253193c35ffd48c4f
PYTHON_DLIB_LICENSE = BSD-3-Clause
PYTHON_DLIB_LICENSE_FILES = LICENSE.txt
PYTHON_DLIB_DEPENDENCIES =
PYTHON_DLIB_SETUP_TYPE = distutils
PYTHON_DLIB_INSTALL_STAGING = YES

$(eval $(python-package))
$(eval $(host-python-package))