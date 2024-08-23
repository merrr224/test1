import os
import json

def load_and_combine_json_files(directory):
    combined_data = []

    # ディレクトリ内のすべてのファイルを処理
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

                # "Version"キーを除去
                if "Version" in data:
                    del data["Version"]

                combined_data.append(data)

    return combined_data

def save_combined_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    directory = 'inline_policies'  # JSONファイルが保存されているディレクトリ
    output_file = 'combined_policies.json'  # 出力するJSONファイル名

    combined_data = load_and_combine_json_files(directory)
    save_combined_json(combined_data, output_file)

    print(f"Combined JSON data has been saved to {output_file}")

if __name__ == "__main__":
    main()
