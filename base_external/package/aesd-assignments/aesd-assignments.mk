##############################################################
#
# AESD-ASSIGNMENTS
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
AESD_ASSIGNMENTS_VERSION = d920453efbc9eb571442d2c83c96ab1a389d01ce
# Note: Be sure to reference the *ssh* repository URL here (not https) to work properly
# with ssh keys and the automated build/test system.
# Your site should start with git@github.com:
AESD_ASSIGNMENTS_SITE = git@github.com:cu-ecen-aeld/final-project-Mich2899.git
AESD_ASSIGNMENTS_SITE_METHOD = git
AESD_ASSIGNMENTS_GIT_SUBMODULES = YES

define AESD_ASSIGNMENTS_BUILD_CMDS
#	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D) all
endef

# TODO add your writer, finder and finder-test utilities/scripts to the installation steps below
define AESD_ASSIGNMENTS_INSTALL_TARGET_CMDS
	$(INSTALL) -d 0755 $(@D)/ $(TARGET_DIR)/etc/project
	$(INSTALL) -m 0755 $(@D)/car.py $(TARGET_DIR)/etc/project/
	$(INSTALL) -m 0755 $(@D)/setdate.sh $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 0755 $(@D)/setdate-start-stop $(TARGET_DIR)/etc/init.d/S97setdate

endef

$(eval $(generic-package))
