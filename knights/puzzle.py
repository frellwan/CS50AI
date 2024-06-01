from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Can't be both a Knight and a Knave
    Not(And(AKnight, AKnave)),

    # Must be a Knight or a Knave
    Or(AKnight, AKnave),

    # If A is a Knight then Aknight and A Knave
    Implication(AKnight, And(AKnight, AKnave)),

    # If a is a Knave then Not(AKnight and AKnave)
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Can't be both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # Must be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # If A is a Knight then both AKnave and BKnave
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a Knave then either A not Knave or B nor Knave
    Implication(AKnave, Or(Not(AKnave), Not(BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Can't be both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # Must be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # If A is a Knight than A and B are either both Knights or Both Knaves
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # If A is a Knave than A and B are not both Knights or both Knaves
    Implication(AKnave, And(Not(And(AKnight, BKnight)), Not(And(AKnave, BKnave)))),

    # If B is a Knight than AKnight/BKnave or AKnave/BKnight
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # If B is a Knave then not AKnave or not AKnight and not AKnight or not BKnave
    Implication(BKnave, And(Not(And(AKnight, BKnave)), Not(And(AKnave, BKnight))))
    )

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Can't be both a Knight and a Knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Must be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # If A is a Knight then Aknight or AKnave
    Implication(AKnight, Or(AKnight, AKnave)),

    # If A is a Knave then not AKnight and not AKnave
    Implication(AKnave,And(Not(AKnight), Not(AKnave))),

    # If B is a Knight then AKnave and CKnave
    Implication(BKnight, And(AKnave, CKnave)),

    # If B is a Knave then not AKnave or not CKnave
    Implication(BKnave, Or(Not(AKnave), Not(CKnave))),

    # If C is a Knight thenm AKnight
    Implication(CKnight, AKnight),

    # If C is a Knave then not AKnight
    Implication(CKnave, Not(AKnight))
    )


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
