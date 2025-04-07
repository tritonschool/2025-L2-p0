# functions
def make_statement(statement, decoration, lines):
    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)
    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

make_statement(statement="programming", decoration="=", lines=3)
print()
make_statement(statement="programmings still fun", decoration="*", lines=2)
print()
make_statement(statement="emoji in action", decoration="🧞‍♂️", lines=1)
print()

