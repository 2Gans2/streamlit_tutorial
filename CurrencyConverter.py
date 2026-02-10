#CurrencyConverter
import streamlit as st
import requests
#Делаем запрос на бесплатный API курсов валют, конвертируем ответ в словарь и забираем курсы.
@st.cache_data(ttl="1 day") #C декоратором st.cache, чтобы Streamlit выполнял запрос не при каждом обновлении страницы, а только при первом, и дальше раз в сутки. Ненужных запросов будет меньше, и приложение будет работать быстрее.
def get_rates():
    url = "https://open.er-api.com/v6/latest/RUB"
    inverse_rates = requests.get(url).json()["rates"] #Каждый курс меняем на обратный, потому что API отдает курс рубля к валюте, а не валюты к рублю.
    return {x: 1 / y for x, y in inverse_rates.items()}

st.title("Currency Converter")
col1, col2 = st.columns(2)
x = col1.number_input("", min_value=0.0, value=1.0)
rates = get_rates()
currency = col2.selectbox("Валюта", list(rates))
st.success(f'{x * rates[currency]:,.2f} RUB')
