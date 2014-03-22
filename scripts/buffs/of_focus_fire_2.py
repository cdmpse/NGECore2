import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'combat_strikethrough_value', 3)
	core.skillModService.addSkillMod(actor, 'expertise_critical_niche_all', 20)
	core.skillModService.addSkillMod(actor, 'expertise_strikethrough_chance', 2)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'combat_strikethrough_value', 3)
	core.skillModService.deductSkillMod(actor, 'expertise_critical_niche_all', 20)
	core.skillModService.deductSkillMod(actor, 'expertise_strikethrough_chance', 2)
	return