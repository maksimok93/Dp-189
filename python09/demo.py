import logging
from unrealmath.addition import add
from unrealmath.subtraction import reduce

if __name__ == '__main__':
    logger = logging.getLogger('unrealmath')

    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    logger.setLevel(logging.INFO)

    addition_filter = logging.Filter('unrealmath.addition')
    subtraction_filter = logging.Filter('unrealmath.subtraction')

    addition_handler = logging.FileHandler('addition.log')
    addition_handler.addFilter(addition_filter)
    addition_handler.setFormatter(formatter)

    subtraction_handler = logging.FileHandler('subtraction.log')
    subtraction_handler.addFilter(subtraction_filter)
    subtraction_handler.setFormatter(formatter)

    logger.addHandler(addition_handler)
    logger.addHandler(subtraction_handler)
    add(17, 23)
    reduce(13, 12)
