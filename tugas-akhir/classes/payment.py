class Payment:
  def __init__(self, amount):
    self.amount = amount

  def pay(self):
    raise NotImplementedError("Payment method is not implemented.")


class DanaPayment(Payment):
  def pay(self):
    print(f"Dana payment of {self.amount} processed.")


class OvoPayment(Payment):
  def pay(self):
    print(f"Ovo payment of {self.amount} processed.")


class BankPayment(Payment):
  def pay(self):
    print(f"Bank payment of {self.amount} processed.")
