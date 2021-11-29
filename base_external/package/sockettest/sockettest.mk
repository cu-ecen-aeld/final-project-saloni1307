##############################################################
#
# AESD-ASSIGNMENTS
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
SOCKETTEST_VERSION = cf13fd0b531160708d851b80155e66f030ffe31c
# Note: Be sure to reference the *ssh* repository URL here (not https) to work properly
# with ssh keys and the automated build/test system.
# Your site should start with git@github.com:
SOCKETTEST_SITE = git@github.com:cu-ecen-aeld/final-project-saloni1307.git
SOCKETTEST_SITE_METHOD = git
SOCKETTEST_GIT_SUBMODULES = YES

define SOCKETTEST_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D)/sockettest all
endef

# TODO add your writer, finder and finder-test utilities/scripts to the installation steps below
define SOCKETTEST_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/sockettest/* $(TARGET_DIR)/usr/bin/
endef

$(eval $(generic-package))