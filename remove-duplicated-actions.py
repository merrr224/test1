def remove_duplicate_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    unique_lines = []
    seen = set()
    duplicate_count = 0

    for line in lines:
        stripped_line = line.strip()
        if stripped_line not in seen:
            seen.add(stripped_line)
            unique_lines.append(line)
        else:
            duplicate_count += 1

    with open(filename, 'w') as file:
        file.writelines(unique_lines)

    print(f"Removed {duplicate_count} duplicate lines from {filename}")

def main():
    allow_file = 'allowed_actions.txt'
    deny_file = 'denied_actions.txt'

    remove_duplicate_lines(allow_file)
    remove_duplicate_lines(deny_file)

if __name__ == "__main__":
    main()
