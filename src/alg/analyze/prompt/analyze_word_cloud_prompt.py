SYSTEM_PROMPT = """You are the most intelligent word analyst in the world."""


USER_PROMPT = """
# Task
子どもの会話記録から，会話の中で頻繁に出てくる単語を分析してもらいます
分析結果はワードクラウドとして表示します
分析結果では，wordに欲出てくる単語を，frequencyにその単語の出現頻度（1~100, 100に近いほど頻度が大きい）を書いてください
ワードクラウドは大量に表示したいので，最低でも20個の単語を表示させてください．100個近く出力してくれるのが望ましいです．
では，始めます．


これまでの会話一覧：
{conversation}

"""
