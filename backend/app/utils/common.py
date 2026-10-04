from fastapi.responses import JSONResponse

def sendResponse(
    status_code: int,
    response_code: str,
    message: str,
    data: dict = None,
) -> dict:
    """
    Send a response with the given status code, message, data, and error.
    
    Args:
        status_code (int): The HTTP status code of the response.
        message (str): A message describing the response.
        data (dict, optional): Additional data to include in the response. Defaults to None.
        response_code (str): A code representing the type of response.

    Returns:
        dict: A dictionary containing the response information.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "response_code": response_code,
            "message": message,
            "data": data if data is not None else {}
        }
    )
    return response