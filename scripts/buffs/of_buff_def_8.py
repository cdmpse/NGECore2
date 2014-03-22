import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_dodge', 4)
	core.skillModService.addSkillMod(actor, 'constitution_modified', 60)
	core.skillModService.addSkillMod(actor, 'combat_critical_hit_reduction', 9)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_dodge', 4)
	core.skillModService.deductSkillMod(actor, 'constitution_modified', 60)
	core.skillModService.deductSkillMod(actor, 'combat_critical_hit_reduction', 9)
	return