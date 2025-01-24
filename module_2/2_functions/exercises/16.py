from collections import Counter

FREE_EMAIL_DOMAINS = [
    'gmail.com',
    'yandex.ru',
    'hotmail.com',
    'yahoo.com',
]


def get_domain(email: str) -> str:
    for i in range (0, len(email)):
        if email[i] == "@":
            return email[i+1::]


def get_free_domains_count(email_addresses: list) -> dict:
    email_dict = {}
    for email in email_addresses:
        email_sufix = get_domain(email)
        if email_sufix in FREE_EMAIL_DOMAINS:
            email_dict.setdefault(email_sufix, []).append(email)
    keys = email_dict.keys()
    result = {}
    for key in keys:
        result.setdefault(key, len(email_dict[key]))
    return result


# better version
def get_domain_(email: str) -> str:
    # Use split to extract domain directly
    return email.split('@')[1]

def get_free_domains_count_(email_addresses: list) -> dict:
    email_dict = {}
    for email in email_addresses:
        email_suffix = get_domain(email)
        if email_suffix in FREE_EMAIL_DOMAINS:
            email_dict[email_suffix] = email_dict.get(email_suffix, 0) + 1
    return email_dict


def main():
    emails = [
        'info@gmail.com',
        'info@yandex.ru',
        'info@hotmail.com',
        'mk@host.com',
        'support@hexlet.io',
        'key@yandex.ru',
        'sergey@gmail.com',
        'vovan@gmail.com',
        'vovan@hotmail.com',
    ]
    print(get_free_domains_count(emails))


if __name__ == "__main__":
    main()


# Реализуйте функцию get_free_domains_count(), которая принимает на вход список email-адресов, а возвращает словарь с количеством email-адресов для каждого бесплатного домена. Список бесплатных доменов хранится в константе FREE_EMAIL_DOMAINS.

# Пример использования:

# from emails import get_free_domains_count

# emails = [
#     'info@gmail.com',
#     'info@yandex.ru',
#     'info@hotmail.com',
#     'mk@host.com',
#     'support@hexlet.io',
#     'key@yandex.ru',
#     'sergey@gmail.com',
#     'vovan@gmail.com',
#     'vovan@hotmail.com',
# ]

# print(get_free_domains_count(emails))
# # => {
# # =>   'gmail.com': 3,
# # =>   'yandex.ru': 2,
# # =>   'hotmail.com': 2,
# # => }
# Другие примеры смотрите в модуле с тестами.