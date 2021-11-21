   ################################################################################
#
# face_recognition_models
#
################################################################################

FACE_RECOGNITION_MODELS_VERSION = 0.3.0
FACE_RECOGNITION_MODELS_SOURCE = face_recognition_models-0.3.0.tar.gz
FACE_RECOGNITION_MODELS_SITE = https://files.pythonhosted.org/packages/cf/3b/4fd8c534f6c0d1b80ce0973d01331525538045084c73c153ee6df20224cf
FACE_RECOGNITION_MODELS_LICENSE = Apache License
FACE_RECOGNITION_MODELS_LICENSE_FILES = LICENSE
FACE_RECOGNITION_MODELS_DEPENDENCIES:=
FACE_RECOGNITION_MODELS_SETUP_TYPE:= distutils

$(eval $(python-package))