letter = '''  Dear <|Name|>,
       You are selected!
        <|Date|> ''' 
print(letter.replace("<|Name|>", "Preet").replace(" <|Date|>","08 aug 2024"))# we can chaining in .replace funcation