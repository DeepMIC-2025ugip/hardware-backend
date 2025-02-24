SYSTEM_PROMPT = """You are the most intelligent person in the world."""


USER_PROMPT = """
あなたには子どもの性格分析をしてもらいます．
子どもとAIぬいぐるみの会話一覧が与えられるので，この会話をもとに，子どもの性格，強み，弱み等の分析を行ってください．

指定したBaseModelの形式に従って出力してください．
分析する項目は多岐にわたっています．与えられた会話の情報からでは判断できない箇所は，適当なことを書くのではなく空欄としてください．


これまでの会話一覧：
{all_conversation}

"""
