from logging import getLogger
import zmq
from config import PUB_ADDRESS, PULL_ADDRESS

logger = getLogger(__name__)

def main():
    context = zmq.Context()

    publiser = context.socket(zmq.PUB)
    publiser.bind(PUB_ADDRESS)
    logger.info("Publisher listening on %s", PUB_ADDRESS)

    puller = context.socket(zmq.PULL)
    puller.bind(PULL_ADDRESS)
    logger.info("Puller listening on %s", PULL_ADDRESS)

    logger.info("Starting main loop")
    while True:
        msg = puller.recv()
        logger.debug("New message: %s", msg)
        publiser.send(msg)
