# defines what each Package object looks like
class Package:
    """
        Represents a delivery package with full address, deadline, weight, and status information.

        This class stores all relevant information for a single package. The status changes from "At Hub" to "En Route"
        to "Delivered" as the package progresses through the delivery system.

        Attributes are set during initialization and updated during the delivery process to reflect any changes.
        """
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, status="At Hub"):
        """
                Initializes a new Package object with delivery information.

                The package starts with a default status of "At Hub" and no delivery/departure times.
                These attributes are updated by the delivery system as the package is loaded and delivered.
                The parameters are initialized according to the order in CSV package file.
        """


        self.package_id = package_id #1-40
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status # default status given
        self.delivery_time = None # to be updated when package is loaded onto truck in main.py
        self.departure_time = None # to be updated when package is delivered in nearest_neighbor.py

    # print out to screen in order
    def __str__(self):
        """
        Returns a human-readable string representation of the package i'm using to debug.
        """

        return (f"ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, "
                f"Zip: {self.zipcode}, Weight: {self.weight}, Deadline: {self.deadline}, Status: {self.status}, "
                f"Delivery Time: {self.delivery_time}, Departure Time: {self.departure_time}, Status: {self.status}")

