# defines what each Package object looks like
class Package:
    def __init__(self, package_id, address, deadline, city, zipcode, weight, notes, status = "At Hub"):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.notes = notes
        self.status = status # default status given
        self.delivery_time = None # to be updated
        self.departure_time = None # to be updated

    # print out to screen in order
    def __str__(self):
        return (f"ID: {self.package_id}, Address: {self.address}, City: {self.deadline}, State: {self.city}, "
                f"Zip: {self.zipcode}, Deadline: {self.weight}, Weight: {self.notes}, "
                f"Delivery Time: {self.delivery_time}, Departure Time: {self.departure_time}, Status: {self.status}")

    # changes the package status based on time
    def package_status(self, check_time):
        if check_time is None:
            return "Error: please provide a valid time to check status."

        if self.delivery_time and check_time >= self.delivery_time:
            self.status = "Delivered"
            return f"{self.status}\tDelivered Time: {self.delivery_time}"
        elif self.departure_time and self.departure_time < check_time < self.delivery_time:
            self.status = "En Route"
            return f"Status: {self.status}"
        else:
            self.status = "At Hub"
            return f"Status: {self.status}"
