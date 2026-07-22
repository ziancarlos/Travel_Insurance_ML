import traceback


def handle_http_exception(error):
    return {
        "message": error.description,
    }, error.code
    
def validation_exception(error):
    errors = []

    for err in error.errors():
        errors.append({
            "field": ".".join(map(str, err["loc"])),
            "message": err["msg"]
        })
        
    return {
        "message": "Validation failed",
        "errors": errors
    }, 400
    
def ise_exception(error):
    traceback.print_exc()

    return {
        "message": "Internal server error",
                "error": str(error)  # only for development

    }, 500