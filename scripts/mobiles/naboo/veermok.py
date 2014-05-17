import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	templates = Vector()
	templates.add('object/mobile/shared_veermok_hue.iff')
	mobileTemplate.setCreatureName('veermok')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setLevel(19)
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('veermok', mobileTemplate)
	