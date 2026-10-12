facts = ["rainy"]

rules = {
    "rainy": "carry_umbrella",
    "carry_umbrella": "stay_dry"
}

inferred = []

for fact in facts:
    if fact in rules:
        conclusion = rules[fact]
        inferred.append(conclusion)

        if conclusion in rules:
            inferred.append(rules[conclusion])

print("Inferred Knowledge:", inferred)
