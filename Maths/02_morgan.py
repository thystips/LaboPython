for A in False, True:
    for B in False,True:
        nonA = not A
        nonB = not B
        nonAetnonB = nonA and nonB
        AouB = A or B
        nonAouB = not AouB

        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(A,B,nonA,nonB,nonAetnonB,AouB,nonAouB))