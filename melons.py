"""Classes for melon orders."""


class AbstractMelonOrder(object):

    def __init__(self, species, qty, shipped = False):
        self.species = species
        self.qty = qty
        self.shipped = shipped

    def get_total(self):
        '''
        Calculate price, including tax.
        '''
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class ChristmasMixin(AbstractMelonOrder):
    """Adjust base price for Christmas melons."""

    def adjust_Christmas_melons(self):
        super(ChristmasMixin, self).get_total()
        base_price *= 1.5
        return total


class DomesticMelonOrder(ChristmasMixin, AbstractMelonOrder):
    """A melon order within the USA."""
    # self.order_type = "domestic"
    # self.tax = 0.08

    # order_type = "domestic"
    # tax = .08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

    # if species == 'Christmas melon':
    #     super(DomesticMelonOrder, self).get_total()


class InternationalMelonOrder(ChristmasMixin, AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.order_type = "international"
        self.tax = .17
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        '''Calculate price, including tax.'''

        base_price = 5
        if self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total




