################################################################################
#
# python-tk
#
################################################################################

PYTHON_TK_VERSION = 0.1.0
PYTHON_TK_SOURCE = tk-$(PYTHON_TK_VERSION).tar.gz
PYTHON_TK_SITE = https://files.pythonhosted.org/packages/a0/81/742b342fd642e672fbedecde725ba44db44e800dc4c936216c3c6729885a
PYTHON_TK_SETUP_TYPE = setuptools
PYTHON_TK_LICENSE = Apache-2.0

$(eval $(python-package))
