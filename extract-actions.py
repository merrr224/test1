import json

def extract_actions_by_effect(data, effect_value):
    actions = []

    for entry in data:
        if 'Statement' in entry:
            for statement in entry['Statement']:
                if statement.get('Effect') == effect_value:
                    action = statement.get('Action')
                    if action:
                        if isinstance(action, list):
                            actions.extend(action)
                        else:
                            actions.append(action)
    
    return actions

def save_actions_to_file(actions, filename):
    with open(filename, 'w') as file:
        for action in actions:
            file.write(action + '\n')

def main():
    input_file = 'combined_policies.json'  # 入力ファイル
    allow_output_file = 'allowed_actions.txt'  # "Allow"アクションの出力ファイル
    deny_output_file = 'denied_actions.txt'  # "Deny"アクションの出力ファイル

    # JSONファイルを読み込む
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    # "Effect"が"Allow"の"Action"を抽出
    allowed_actions = extract_actions_by_effect(data, 'Allow')
    save_actions_to_file(allowed_actions, allow_output_file)
    print(f"Allowed actions have been saved to {allow_output_file}")

    # "Effect"が"Deny"の"Action"を抽出
    denied_actions = extract_actions_by_effect(data, 'Deny')
    save_actions_to_file(denied_actions, deny_output_file)
    print(f"Denied actions have been saved to {deny_output_file}")

if __name__ == "__main__":
    main()
