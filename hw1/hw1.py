import clingo

def print_answer_sets(program):
    # Load the answer set program, and call the grounder
    control = clingo.Control()
    control.add("base", [], program)
    control.ground([("base", [])])
    # Define a function that will be called when an answer set is found
    # This function sorts the answer set alphabetically, and prints it
    def on_model(model):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))
    # Ask clingo to find all models (using an upper bound of 0 gives all models)
    control.configuration.solve.models = 0
    # Call the clingo solver, passing on the function on_model for when an answer set is found
    answer = control.solve(on_model=on_model)
    # Print a message when no answer set was found
    if answer.satisfiable == False:
        print("No answer sets")

    
""" EXERCISE 2 """




