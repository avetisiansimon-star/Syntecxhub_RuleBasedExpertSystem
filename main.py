class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions  
        self.conclusion = conclusion   


class ExpertSystem:
    def __init__(self):
        self.facts = set()   
        self.rules = []      
        self.log = []        

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, conclusion):
        self.rules.append(Rule(conditions, conclusion))

    def forward_chain(self):
        new_fact_added = True

        while new_fact_added:
            new_fact_added = False

            for rule in self.rules:

                if all(c in self.facts for c in rule.conditions):

                    
                    if rule.conclusion not in self.facts:

                        
                        self.facts.add(rule.conclusion)

                    
                        self.log.append(
                            f"IF {rule.conditions} THEN {rule.conclusion}"
                        )

                        new_fact_added = True

    def show_facts(self):
        return self.facts

    def show_log(self):
        return self.log



system = ExpertSystem()

system.add_fact("fever")
system.add_fact("cough")

system.add_rule(["fever", "cough"], "flu")
system.add_rule(["flu"], "rest_needed")
system.add_rule(["rest_needed"], "stay_home")

system.forward_chain()

print("FACTS:")
print(system.show_facts())

print("\nLOG:")
for step in system.show_log():
    print(step)