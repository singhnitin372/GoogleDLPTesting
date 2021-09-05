from faker import Faker
import allure


@allure.step('Generating the amex credit card number list')
def amex_credit_card_generate():
    amex_credit_card_set = set()
    faker = Faker()
    for _ in range(0, 100):
        amex_credit_card_set.add(faker.credit_card_number(card_type='amex'))

    return amex_credit_card_set


@allure.step('Generating the visa credit card number list')
def visa_credit_card_generate():
    visa_credit_card_set = set()
    faker = Faker()
    for _ in range(0, 100):
        visa_credit_card_set.add(faker.credit_card_number(card_type='visa16'))

    return visa_credit_card_set


@allure.step('Generating the master credit card number list')
def master_credit_card_generate():
    master_credit_card_set = set()
    faker = Faker()
    for _ in range(0, 100):
        master_credit_card_set.add(faker.credit_card_number(card_type='mastercard'))

    return master_credit_card_set


@allure.step('Generating the email address list')
def email_generate():
    email_set = set()
    faker = Faker()
    for _ in range(0, 100):
        email_set.add(faker.email())

    return email_set


@allure.step('Generating the FullName list')
def full_name_generate():
    full_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        full_name_set.add(faker.name())

    return full_name_set


@allure.step('Generating the Last Name list')
def last_name_generate():
    last_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        last_name_set.add(faker.last_name())
    return last_name_set


@allure.step('Generating the First Name list')
def first_name_generate():
    first_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        first_name_set.add(faker.first_name())
    return first_name_set


@allure.step('Generating the IPV4 list')
def IPV4_generate():
    ipv4_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        ipv4_name_set.add(faker.ipv4())
    return ipv4_name_set


@allure.step('Generating the IPV4 Private list')
def IPV4_private_generate():
    ipv4_private_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        ipv4_private_name_set.add(faker.ipv4_private())
    return ipv4_private_name_set


@allure.step('Generating the IPV6 list')
def IPV6_generate():
    ipv6_name_set = set()
    faker = Faker()
    for _ in range(0, 100):
        ipv6_name_set.add(faker.ipv6())
    return ipv6_name_set


@allure.step('Generating the SSN Number list')
def ssn_generate():
    ssn_number_set = set()
    faker = Faker()
    for _ in range(0, 100):
        ssn_number_set.add(faker.ssn())
    return ssn_number_set


@allure.step('Generating the mac address list')
def mac_address_generate():
    mac_address_set = set()
    faker = Faker()
    for _ in range(0, 100):
        mac_address_set.add(faker.mac_address())
    return mac_address_set


@allure.step('Generating the date list')
def date_generate():
    date_set = set()
    faker = Faker()
    for _ in range(0, 100):
        date_set.add(faker.date())

    return date_set


@allure.step('Generating the datetime list')
def date_time_generate():
    date_time_set = set()
    faker = Faker()
    for _ in range(0, 100):
        date_time_set.add(str(faker.date_time()))

    return date_time_set


@allure.step('Generating the phone_number list')
def phone_number():
    phone_number_set = set()
    faker = Faker()
    for _ in range(0, 100):
        phone_number_set.add(str(faker.phone_number()).replace('.', "-"))

    return phone_number_set
