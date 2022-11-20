import logging
import numpy as np
import matplotlib.pyplot as plt
import cantera as ct
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Simulation triggered')
    # Aqui me faltaria hacer que esto fuera parametrizable y pasarlo por un posteo de un PowerAutomate
    a = 100
    b = 50
    c = 0
    t = 0.1
    k1 = 0.008
    k2 = 0.002
    for i in range(50):
        print("A Component : " + a ,"B Component : " + b ,"c Component : " + c)
        a = a + (k2 * c - k1 * a * b ) * t
        b = b + (k2 * c - k1 * a* b ) * t
        c = c + (2 * k1 * a *b - k2 * c) * t
        # Aqui me faltaria enchufar un INSERT SQL en la base de datos Azure SQL que tendria volando 

    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
