"""
Implements the Scheme related exceptions
"""

class Sch_Error(Exception):
    """
    A type of exception to be raised if there is an error with a 
    Scheme program. This exception should never be raised directly;
    Only the subclasses of this exception are raised 
    Easier to handle as they are more specific this way.

    @param Exception: the subclass to be raised
    way to
    """