   ################################################################################
#
# opencv-python
#
################################################################################

OPENCV_PYTHON_VERSION = 4.5.4.58
OPENCV_PYTHON_SOURCE = opencv-python-4.5.4.58.tar.gz
OPENCV_PYTHON_SITE = https://files.pythonhosted.org/packages/b6/82/0519fdbbcaddc0fa8c2568327a8311477315a91b4513738ee1d35f0ce715
OPENCV_PYTHON_LICENSE = Apache License
OPENCV_PYTHON_LICENSE_FILES = LICENSE
OPENCV_PYTHON_DEPENDENCIES:=
OPENCV_PYTHON_SETUP_TYPE:= distutils

$(eval $(python-package))