from yoomoney import Quickpay
from loguru import logger

def get_url(receiver: str, label: str, sum: int) -> str:
    logger.debug(f"label={label}, sum={sum}")
    quickpay = Quickpay(
        receiver=receiver,
        quickpay_form="shop",
        targets="VPN subscription",
        paymentType="",
        sum=sum,
        label=label
    )
    URL = quickpay.redirected_url
    logger.debug(URL)
    return URL