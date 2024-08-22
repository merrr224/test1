import boto3
import json
import os

def get_customer_managed_policies():
    # boto3クライアントを作成
    iam_client = boto3.client('iam')

    # カスタマー管理ポリシーを取得
    paginator = iam_client.get_paginator('list_policies')
    response_iterator = paginator.paginate(Scope='Local')

    policies = []

    for response in response_iterator:
        for policy in response['Policies']:
            policies.append(policy)

    return policies

def get_policy_document(policy_arn, version_id):
    # ポリシードキュメントを取得
    iam_client = boto3.client('iam')
    policy_version = iam_client.get_policy_version(
        PolicyArn=policy_arn,
        VersionId=version_id
    )
    return policy_version['PolicyVersion']['Document']

def save_policy_document(policy_name, policy_document):
    # フォルダがなければ作成
    if not os.path.exists('policies'):
        os.makedirs('policies')
    
    # ポリシードキュメントをJSONファイルとして保存
    file_path = os.path.join('policies', f"{policy_name}.json")
    with open(file_path, 'w') as json_file:
        json.dump(policy_document, json_file, indent=4)

def main():
    # 全てのカスタマー管理ポリシーを取得
    policies = get_customer_managed_policies()

    for policy in policies:
        policy_arn = policy['Arn']
        default_version_id = policy['DefaultVersionId']

        # ポリシードキュメントを取得
        policy_document = get_policy_document(policy_arn, default_version_id)

        # ポリシードキュメントをJSONファイルとして保存
        save_policy_document(policy['PolicyName'], policy_document)

        print(f"Saved policy document for: {policy['PolicyName']}")

if __name__ == "__main__":
    main()
