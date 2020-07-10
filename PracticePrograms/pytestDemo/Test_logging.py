import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__) #to retrive the test file name

    fileHandler = logging.FileHandler('logfile.log') #where the logs are stored

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object(file location)

    logger.setLevel(logging.INFO) #set the debug level to info and only the error after
                                  # the info will be displayed and not debug levels

    logger.debug("A debug statement is executed")
    logger.info("Information messages")
    logger.warning("Something is in warning mode")
    logger.error("A major error has occured")
    logger.critical("A critical issue")