import random
import logging

__log = logging.getLogger(__name__)
__log.setLevel(logging.INFO)


def reduce(minuend: float, subtrahend: float) -> float:
    print(f'Successfully run {__log}')
    result = minuend - subtrahend + random.randint(1, 10)
    __log.info(f'Execution result: {result}')
    return result
