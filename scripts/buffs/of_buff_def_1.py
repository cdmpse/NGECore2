import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_dodge', 1)
	core.skillModService.addSkillMod(actor, 'constitution_modified', 5)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_dodge', 1)
	core.skillModService.deductSkillMod(actor, 'constitution_modified', 5)
	return