SYSTEM_PROMPT = """You are the most intelligent child analyst in the world."""


USER_PROMPT = """
# Task
子どもの会話記録から，その子の性格を分析してもらいます
分析する項目は，人格，強み，弱み，その他，の4項目です
この分析結果は極めて重要な使われ方をするので，それぞれの項目について，可能な限り詳しく書いてください．
具体的なエピソードを交えて描くことで，より評価の高い分析レポートとなります


これまでの会話一覧：
{conversation}

"""
