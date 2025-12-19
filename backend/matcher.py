def find_solution(query):
    with open("solutions.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("#") and query.lower() in line.lower():
            code = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith("#"):
                code.append(lines[j])
                j += 1
            return {
                "description": line.strip("# ").strip(),
                "code": "".join(code)
            }
    return None
