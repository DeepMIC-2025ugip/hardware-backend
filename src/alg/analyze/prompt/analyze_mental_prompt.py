SYSTEM_PROMPT = """You are the most intelligent child analyst in the world."""


USER_PROMPT = """
# Task
子どもの会話記録から，その子の性格を分析してもらいます
分析する項目は，メンタルヘルス的な観点から，友人関係・学校生活・行為・向社会性・認知的特徴・ストレス耐性，の6項目です
それぞれについて，概要，課題，アドバイス，ポイントを考えてください
この分析結果は極めて重要な使われ方をするので，それぞれの項目について，可能な限り詳しく書いてください．
具体的なエピソードを交えて描くことで，より評価の高い分析レポートとなります

また，体の症状・精神症状・自傷行為・不眠症，の4項目について，異常がないか判定してください

これまでの会話一覧：
{conversation}
"""
