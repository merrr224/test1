import json

def remove_duplicate_statements(data):
    unique_statements = []
    seen_statements = set()

    for entry in data:
        if 'Statement' in entry:
            unique_entry_statements = []
            for statement in entry['Statement']:
                # JSONをシリアライズして比較可能な文字列に変換
                statement_str = json.dumps(statement, sort_keys=True)
                if statement_str not in seen_statements:
                    seen_statements.add(statement_str)
                    unique_entry_statements.append(statement)
            
            # ユニークなステートメントだけを保持
            entry['Statement'] = unique_entry_statements

            unique_statements.append(entry)
    
    return unique_statements

def main():
    input_file = 'combined_policies.json'  # 入力ファイル
    output_file = 'deduplicated_policies.json'  # 出力ファイル

    # JSONファイルを読み込む
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    # 重複するステートメントを削除
    deduplicated_data = remove_duplicate_statements(data)

    # 結果を保存する
    with open(output_file, 'w') as json_file:
        json.dump(deduplicated_data, json_file, indent=4)

    print(f"Deduplicated JSON data has been saved to {output_file}")

if __name__ == "__main__":
    main()
