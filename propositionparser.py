from proposition import Proposition, Variable, Constant
from logicalconnective import Negation, Conjunction, Disjunction, Conditional, Biconditional
from enum import Enum

class Symbol():
    """ Class that encapsulates a symbol string and a symbol type.
    """  
    class SymbolType(Enum):
        VARIABLE_NAME = 0,
        CONSTANT_TRUE = 1,
        CONSTANT_FALSE = 2,
        OPEN_PARANTHESIS = 3,
        CLOSE_PARANTHESIS = 4,
        NEGATION = 5,
        CONJUNCTION = 6,
        DISJUNCTION = 7,
        CONDITIONAL = 8,
        BICONDITIONAL = 9


    # dictionary containing all valid strings for each logical operation
    logical_symbol_strings = {
        SymbolType.OPEN_PARANTHESIS: set(['(']),
        SymbolType.CLOSE_PARANTHESIS: set([')']),
        SymbolType.NEGATION: set(['!', '~', '¬']),
        SymbolType.CONJUNCTION: set(['&', '∧', '^']),
        SymbolType.DISJUNCTION: set(['||', '∨']),
        SymbolType.CONDITIONAL: set(['->', '→']),
        SymbolType.BICONDITIONAL: set(['<->', '↔'])
    }

    # character length of the longest logical symbol
    logical_symbol_max_length = 3

    def __init__(self, string, type = None):
        """ Creates a symbol object. If no type is provided, this infers the type of symbol.
        """
        self.string = string
        if type is not None:
            self.type = type
        else:
            if string.isalpha():
                if string.lower() == 'true':
                    self.type = Symbol.SymbolType.CONSTANT_TRUE
                elif string.lower() == 'false':
                    self.type = Symbol.SymbolType.CONSTANT_FALSE
                else:
                    self.type = Symbol.SymbolType.VARIABLE_NAME
            else:
                for symbol_type, sym_strings in self.logical_symbol_strings.items():
                    for sym_string in sym_strings:
                        if sym_string == string:
                            self.type = symbol_type
                            break
                    else: # else excecutes when for loop does not break
                        continue
                    break

    def __str__(self):
        return self.string
 
def next_symbol(x):
    """ Given a string to parse, this extracts the left most complete symbol.
    A symbol could be a logical symbol, a paranthesis, or a variable name.
    It can consist of multiple characters.
    Params
    -----------
    x: the string to parse.
    
    Returns
    -----------
    symbol: a symbol object representing the symbol.
    string: the remaining part of the string.
    """
    # get first non-space character of string
    i = 0
    while (x[i] == ' '):
        i += 1
    first_char = x[i] 
    # if first character is letter, keep looking for letters part of a variable name
    if first_char.isalpha():
        symbol = first_char
        for j in range(i + 1, len(x)):
            if x[j].isalpha():
                # another letter found, add it symbol
                symbol += x[j]
            else:
                # non-letter found, return the symbol and the rest of the string
                return Symbol(symbol), x[j:]
        # end of string reached return symbol and empty string
        return Symbol(symbol), ''
    else:
        # look for logical symbol
        symbol = ''
        for j in range(i, len(x)):
            symbol += x[j]
            for symbol_type, symbol_strings in Symbol.logical_symbol_strings.items():
                if symbol in symbol_strings:
                    # the current symbol is a valid logical symbol, return it
                    return Symbol(symbol, symbol_type), '' if j == len(x) - 1 else x[j+1:]
                if len(symbol) > Symbol.logical_symbol_max_length:
                    raise ValueError("Invalid symbol used in proposition:", symbol)
        # end of string reached, no valid symbol found, raise Error
        raise ValueError("Invalid symbol used in proposition:", symbol)

def string_to_symbol_list(x):
    """ Parses a string into a list of symbols.
    Params
    -----------
    x: the string to parse.
    
    Returns
    -----------
    symbols: a list of symbol objects.
    """
    symbols = []
    while x is not None and x != '':
        symbol, x = next_symbol(x)
        symbols.append(symbol)
    return symbols

def symbol_list_to_proposition(L):
    """ Parses a list of ordered symbols and propositions to an proposition.
    This follows the following order of operations when building the proposition:
    1. Paranthesis
    2. Negation
    3. Conjunction
    4. Disjunction
    5. Conditional
    6. Biconditional
    
    Params
    -----------
    L: A list of ordered symbols and propositions.

    Returns
    -----------
    proposition: A proposition object representing the operations in the list.
    """

    # base cases - symbol list contains one value
    if len(L) == 1:
        if issubclass(type(L[0]), Proposition):
            return L[0]
        elif isinstance(L[0], Symbol) and L[0].type == Symbol.SymbolType.VARIABLE_NAME:
            return Variable(L[0].string)
        elif isinstance(L[0], Symbol) and L[0].type == Symbol.SymbolType.CONSTANT_TRUE:
            return Constant(True)
        elif isinstance(L[0], Symbol) and L[0].type == Symbol.SymbolType.CONSTANT_FALSE:
            return Constant(False)
        else:
            raise ValueError("Invalid Proposition String")
   
    simplified_list = []
    # first we scan for open paranthesis
    # we will create a simplified list where we condense
    # everything inside a paranthesis to a proposition
    i = 0
    while (i < len(L)):
        if isinstance(L[i], Symbol) and L[i].type == Symbol.SymbolType.OPEN_PARANTHESIS:
            # we found an opened paranthesis
            # scan for the closing paranthesis and save all symbols between
            opened_paranthesis = 1
            inner_symbols = []
            # when the closing paranthesis is found, opened_paranthesis == 0
            for j in range(i+1, len(L)):
                if L[j].type == Symbol.SymbolType.OPEN_PARANTHESIS:
                    opened_paranthesis += 1
                elif L[j].type == Symbol.SymbolType.CLOSE_PARANTHESIS:
                    opened_paranthesis -= 1
                if opened_paranthesis == 0:
                    break
                else:
                    inner_symbols.append(L[j])
            if opened_paranthesis != 0:
                raise ValueError("Mismatched Paranthesis")
            # convert the symbols between the paranthesis to a proposition recusively
            prop = symbol_list_to_proposition(inner_symbols)
            # append the proposition to the list
            simplified_list.append(prop)
            # i must be increased by 1 for the open paranthesis, 1 for the close paranthesis
            # and 1 for each symbol condensed to the proposition
            i += 2 + len(inner_symbols)
        else:
            # we did not find a paranthesis, append the symbol to the simplified list
            simplified_list.append(L[i])
            # increment i
            i += 1

    # now we have a simplified list with no paranthesis
    L = simplified_list.copy()
    # the list contains symbols and propositions
    # here we will follow order of operations

    # first we scan for negations and create a new simplified list
    simplified_list = []
    i = 0
    while (i < len(L)):
        if isinstance(L[i], Symbol) and L[i].type == Symbol.SymbolType.NEGATION:
            prop = Negation(symbol_list_to_proposition([L[i + 1]]))
            simplified_list.append(prop)
            i += 2
        else:
            simplified_list.append(L[i])
            i += 1

    # now we have a simplified list with no negations
    L = simplified_list.copy()
    # next we scan for remaining operations in order
    connectives = {
        Conjunction: Symbol.SymbolType.CONJUNCTION,
        Disjunction: Symbol.SymbolType.DISJUNCTION,
        Conditional: Symbol.SymbolType.CONDITIONAL,
        Biconditional: Symbol.SymbolType.BICONDITIONAL,
    }

    for connective, symbol_type in connectives.items():
        simplified_list = []
        i = 0
        while (i < len(L)):
            if i + 1 < len(L) and type(L[i+1]) == Symbol and L[i+1].type == symbol_type:
                expr = connective(symbol_list_to_proposition([L[i]]), symbol_list_to_proposition([L[i + 2]]))
                simplified_list.append(expr)
                i += 3
            else:
                simplified_list.append(L[i])
                i += 1
        L = simplified_list.copy()

    assert len(L) == 1, "Invalid Proposition String"
    # At this point, the list should be length 1
    # Return the propostion contained in the list
    return L[0]

def parse_proposition(x):
    """ Parses a string into an propositional calculus proposition.
    
    Parses a string into an propositional calculus proposition.
    Variable names in the the input string must only have letters and are not case-sensitive.
    Variable names may not be 'true', or 'false'. These are reserved constant values.
    The following symbols are allowed for operations
    Negation: ¬, !, ~
    Conjunction: ^, &, ∧
    Disjunction: ||, ∨
    Conditional: ->, →
    Biconditional: <->, ↔


    This follows the following order of operations when building the proposition:
    1. Paranthesis
    2. Negation
    3. Conjunction
    4. Disjunction
    5. Conditional
    6. Biconditional

    
    Params
    -----------
    x: A string representing a propositonal calculus proposition.

    Returns
    -----------
    proposition: An proposition object representing the string.
    """
    return symbol_list_to_proposition(string_to_symbol_list(x))
