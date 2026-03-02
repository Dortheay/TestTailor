from controller.order_controller import OrderController


def main():
    controller = OrderController()

    controller.create_order("Alice", 100)
    controller.create_order("Bob", 250)

    controller.print_all_orders()


if __name__ == "__main__":
    main()