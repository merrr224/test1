def sort_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 行を昇順にソート
    sorted_lines = sorted(lines, key=lambda line: line.strip().lower())

    # ソートされた内容をファイルに上書き保存
    with open(filename, 'w') as file:
        file.writelines(sorted_lines)

    print(f"Sorted lines in {filename}.")

def main():
    allow_file = 'allowed_actions.txt'
    deny_file = 'denied_actions.txt'

    sort_lines_in_file(allow_file)
    sort_lines_in_file(deny_file)

if __name__ == "__main__":
    main()
