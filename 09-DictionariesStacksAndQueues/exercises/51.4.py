# ===== Zadanie 25 =====

import queue  # moduł kolejki

customers = queue.Queue()  # kolejka klientów

ticket_number = 1  # numer biletu

while True:

    print("1. New customer")

    print("2. Serve customer")

    print("0. Exit")

    option = input("Select: ")

    if option == "1":

        customers.put(ticket_number)

        print(f"Ticket number: {ticket_number}")

        ticket_number += 1

    elif option == "2":

        if not customers.empty():

            customer = customers.get()

            print(f"Serving customer: {customer}")

        else:

            print("No customers")

    elif option == "0":

        break