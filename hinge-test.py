def decide_what_to_do(person):
    if (
        person["matched"]
        and person["is_cute"]
        and person["has_personality"]
        and person["is_adventurous"]
    ):
        return "ask her out"
    return "keep scrolling"


candidates = {
    "diya": {
        "matched": True,
        "is_cute": True,
        "has_personality": True,
        "is_adventurous": True
    },
}

for name, person in candidates.items():
    decision = decide_what_to_do(person)
    print(f"{name.title()} -> {decision}")

    if decision == "ask her out":
        date_options = {
            1: "go out for a walk",
            2: "play mini golf",
            3: "grab coffee"
        }

        date = date_options[]
        print("Date:", date)
