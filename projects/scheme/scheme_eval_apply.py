import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    # when receive atomic type value: lookup in the env first if not find then return its original form
    # only combination are list
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # return the mapped expr and cuurent procedure
        # teaverse through all the braches by recursivly calling this function
        # return to former function by scheme_apply(expr.first, expr.rest, env)
        def scheme_eval_one_arg(expr):
            return scheme_eval(expr,env)
        expr = expr.map(scheme_eval_one_arg)
        return scheme_apply(expr.first, expr.rest, env)
        # expr.first is function name
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        l = []
        # dont need to check for env at here
        # scheme_eval will convert the given args into its proper form
        # it will raise type error when given procedure is list
        while args is not nil:
            l.append(args.first)
            args = args.rest    
        if procedure.expect_env:
            l.append(env)
        try:
            t = procedure.py_func(*l)
        except TypeError:
            raise SchemeError("incorrect number of arguments")
        return t
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # scheme suppose to be a lexical or static scope langauge
        # which means the frame of this function will not be affected by the frame where calls it
        # the frame of functions are only asscoiated with the fram where create it
        function_frame = procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, function_frame)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # the current frame is only associated with the frame where it was invoked
        function_frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, function_frame)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    # evaluate all expressions and return the last one
    t = expressions
    if t is nil:
        return 
    while t.rest is not nil:
        scheme_eval(t.first, env)
        t = t.rest
    return scheme_eval(t.first, env)       
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)
        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        while isinstance(result, Pair):
            result = unoptimized_scheme_eval(result.expr, env)
        # atom expr
        return result
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = optimize_tail_calls(scheme_eval)
