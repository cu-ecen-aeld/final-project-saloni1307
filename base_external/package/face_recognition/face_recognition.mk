   ################################################################################
#
# face_recognition
#
################################################################################

FACE_RECOGNITION_VERSION = 1.3.0
FACE_RECOGNITION_SOURCE = face_recognition-1.3.0.tar.gz
FACE_RECOGNITION_SITE = https://files.pythonhosted.org/packages/6c/49/75dda409b94841f01cbbc34114c9b67ec618265084e4d12d37ab838f4fd3
FACE_RECOGNITION_LICENSE = Apache License
FACE_RECOGNITION_LICENSE_FILES = LICENSE
FACE_RECOGNITION_DEPENDENCIES:=
FACE_RECOGNITION_SETUP_TYPE:= distutils

$(eval $(python-package))