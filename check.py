from yoomoney import Client
from loguru import logger

def check(client: Client, label: str) -> bool:
    history = client.operation_history(label=label)
    if history.operations == []:
        logger.debug(f"label=\"{label}\" is not found")
        return False
    elif history.operations[0].status == "success":
        logger.debug(f"label=\"{label}\" is success")
        return True
    else:
        logger.debug(f"label=\"{label}\". Status is not success")
        return False