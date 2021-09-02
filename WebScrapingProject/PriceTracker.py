import requests
from bs4 import BeautifulSoup

# URL = "https://www.flipkart.com/apple-iphone-12-black-128-gb/p/itmf1f0a58f1ecd7?pid=MOBFWBYZK3HACR72&lid=LSTMOBFWBYZK3HACR72SELGT5&marketplace=FLIPKART&q=apple+iphone+12+&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=cbb48e89-da1b-4452-bd69-72c2e82a5d31.MOBFWBYZK3HACR72.SEARCH&ppt=hp&ppn=homepage&ssid=hng5uac4dc0000001625237960802&qH=69834b9244e2e97e"

# URL = 'https://www.flipkart.com/vivo-v20-midnight-jazz-128-gb/p/itm2f3fbb0879ced?pid=MOBFVWB4GFUMPEBY&lid=LSTMOBFVWB4GFUMPEBY3EPV19&marketplace=FLIPKART&q=vivo+v20&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&fm=SEARCH&iid=3684afe5-1a83-4465-b628-f76d789c009e.MOBFVWB4GFUMPEBY.SEARCH&ppt=sp&ppn=sp&ssid=0grbkijmk00000001626701478735&qH=ea1ec0fd5bd38137'

# URL = 'https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv'

products_to_track = [
    {
        "product_url": "https://www.flipkart.com/apple-iphone-12-black-128-gb/p/itmf1f0a58f1ecd7?pid=MOBFWBYZK3HACR72&lid=LSTMOBFWBYZK3HACR72SELGT5&marketplace=FLIPKART&q=apple+iphone+12+&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=cbb48e89-da1b-4452-bd69-72c2e82a5d31.MOBFWBYZK3HACR72.SEARCH&ppt=hp&ppn=homepage&ssid=hng5uac4dc0000001625237960802&qH=69834b9244e2e97e",
        "name": "apple iphone 10",
        "target_price": 80000
    },

    {
        "product_url": "https://www.flipkart.com/vivo-v20-midnight-jazz-128-gb/p/itm2f3fbb0879ced?pid=MOBFVWB4GFUMPEBY&lid=LSTMOBFVWB4GFUMPEBY3EPV19&marketplace=FLIPKART&q=vivo+v20&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&fm=SEARCH&iid=3684afe5-1a83-4465-b628-f76d789c009e.MOBFVWB4GFUMPEBY.SEARCH&ppt=sp&ppn=sp&ssid=0grbkijmk00000001626701478735&qH=ea1ec0fd5bd38137",
        "name": "vivo v20",
        "target_price": 22000
    },

    {
        "product_url": "https://www.flipkart.com/samsung-galaxy-s10-prism-black-128-gb/p/itmfdyp6fjtxf4hv",
        "name": "samsung galaxy s10",
        "target_price": 40000

    },

    {
        "product_url": "https://www.flipkart.com/redmi-note-10-frost-white-64-gb/p/itm23973bd36fd21",
        "name": "Redmi note 10",
        "target_price": 15000
    },

    {
        "product_url": "https://www.flipkart.com/oppo-f19-pro-5g-space-silver-128-gb/p/itmd90acf0f30ad6?pid=MOBGFUZ4ARZ5SPGT&lid=LSTMOBGFUZ4ARZ5SPGT9BXTWL&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_ff206d6d-c3e7-4839-8347-93615a16b68b_4_TM3Q7Y9338_MC.MOBGFUZ4ARZ5SPGT&ppt=None&ppn=None&ssid=d6kx27cvcg0000001626713355234&otracker=clp_pmu_v2_Oppo%2BMobiles%2Babove%2B%25E2%2582%25B920K_4_4.productCard.PMU_V2_OPPO%2BF19%2BPro%252B%2B5G%2B%2528Space%2BSilver%252C%2B128%2BGB%2529_oppo-mobile-phones-store_MOBGFUZ4ARZ5SPGT_neo%2Fmerchandising_3&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Oppo%2BMobiles%2Babove%2B%25E2%2582%25B920K_LIST_productCard_cc_4_NA_view-all&cid=MOBGFUZ4ARZ5SPGT",
        "name": "Oppo F19 pro",
        "target_price": 26000
    }
]


def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})

    return product_price.getText()


result_file = open('my_result_file.txt', 'w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' - \t' + 'Available at Target Price' + ' Current Price- ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")
finally:
    result_file.close()
