# Define a class to handle basic propositional logic
class PropositionalLogic:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, rule):
        """Add a rule to the knowledge base."""
        self.rules.append(rule)

    def infer(self):
        """Apply rules to infer new facts until no more facts can be inferred."""
        inferred_facts = set(self.facts)
        while True:
            new_inferences = set()
            for rule in self.rules:
                for fact in inferred_facts:
                    # Apply each rule to each known fact
                    result = rule(fact)
                    if result and result not in inferred_facts:
                        new_inferences.add(result)
            # If no new facts were inferred, stop
            if not new_inferences:
                break
            inferred_facts.update(new_inferences)
        self.facts = inferred_facts

    def query(self, fact):
        """Check if a fact is in the knowledge base."""
        return fact in self.facts


# Instantiate the logic system
logic = PropositionalLogic()

# Define facts
logic.add_fact(("Loves", "mary", "john"))  # Mary loves John

# Define rules
# If Loves(X, Y) then Loves(Y, X)
def mutual_love(fact):
    if fact[0] == "Loves":
        x, y = fact[1], fact[2]
        # Return the mutual fact
        return ("Loves", y, x)
    return None

# Add rule to logic system
logic.add_rule(mutual_love)

# Infer all possible facts based on current facts and rules
logic.infer()

# Query to check if "Loves(john, mary)" is inferred
query_result = ("Loves", "john", "mary")
print(f"Does John love Mary? {'Yes' if logic.query(query_result) else 'No'}")

# Print all inferred facts
print("Inferred Facts:", logic.facts)
