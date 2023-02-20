import taipy

interface = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
"""
taipy.Gui(interface).run()
