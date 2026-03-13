import sys 

def error_message_detail(error, error_detail:sys):
    """
    This function is used to extract detail information about the error from the system information.
    exc_tb : traceback object 
    tb_frame : Frame where error happened 
    f_code : code object of the frame
    co_filename : name of the file where error happened
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))

    return error_message

"""
Defining the exception class for the project.
This class inherits behaviour from the built-in Exception class 
and adds more functionality to it
"""
class SmartGridException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail) # calling the error_message_detail function to get the detailed error message
    
    def __str__(self):
        return self.error_message