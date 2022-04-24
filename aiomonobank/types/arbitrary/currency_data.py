from typing import Union

from .currency import Currency


class UnknownCurrencyCodeError(Exception):
    pass


def parse_currency_by_code(currency_code: Union[str, int]) -> Currency:
    try:
        return described[codes_number[str(currency_code)]]
    except KeyError:
        raise UnknownCurrencyCodeError(f"Currency with code {currency_code} not found")


codes_number = {
    "008": "ALL",
    "012": "DZD",
    "032": "ARS",
    "036": "AUD",
    "044": "BSD",
    "048": "BHD",
    "050": "BDT",
    "051": "AMD",
    "052": "BBD",
    "060": "BMD",
    "064": "BTN",
    "068": "BOB",
    "072": "BWP",
    "084": "BZD",
    "090": "SBD",
    "096": "BND",
    "104": "MMK",
    "108": "BIF",
    "116": "KHR",
    "124": "CAD",
    "132": "CVE",
    "136": "KYD",
    "144": "LKR",
    "152": "CLP",
    "156": "CNY",
    "170": "COP",
    "174": "KMF",
    "188": "CRC",
    "191": "HRK",
    "192": "CUP",
    "203": "CZK",
    "208": "DKK",
    "214": "DOP",
    "222": "SVC",
    "230": "ETB",
    "232": "ERN",
    "238": "FKP",
    "242": "FJD",
    "262": "DJF",
    "270": "GMD",
    "292": "GIP",
    "320": "GTQ",
    "324": "GNF",
    "328": "GYD",
    "332": "HTG",
    "340": "HNL",
    "344": "HKD",
    "348": "HUF",
    "352": "ISK",
    "356": "INR",
    "360": "IDR",
    "364": "IRR",
    "368": "IQD",
    "376": "ILS",
    "388": "JMD",
    "392": "JPY",
    "398": "KZT",
    "400": "JOD",
    "404": "KES",
    "408": "KPW",
    "410": "KRW",
    "414": "KWD",
    "417": "KGS",
    "418": "LAK",
    "422": "LBP",
    "426": "LSL",
    "430": "LRD",
    "434": "LYD",
    "446": "MOP",
    "454": "MWK",
    "458": "MYR",
    "462": "MVR",
    "480": "MUR",
    "484": "MXN",
    "496": "MNT",
    "498": "MDL",
    "504": "MAD",
    "512": "OMR",
    "516": "NAD",
    "524": "NPR",
    "532": "ANG",
    "533": "AWG",
    "548": "VUV",
    "554": "NZD",
    "558": "NIO",
    "566": "NGN",
    "578": "NOK",
    "586": "PKR",
    "590": "PAB",
    "598": "PGK",
    "600": "PYG",
    "604": "PEN",
    "608": "PHP",
    "634": "QAR",
    "643": "RUB",
    "646": "RWF",
    "654": "SHP",
    "682": "SAR",
    "690": "SCR",
    "694": "SLL",
    "702": "SGD",
    "704": "VND",
    "706": "SOS",
    "710": "ZAR",
    "728": "SSP",
    "748": "SZL",
    "752": "SEK",
    "756": "CHF",
    "760": "SYP",
    "764": "THB",
    "776": "TOP",
    "780": "TTD",
    "784": "AED",
    "788": "TND",
    "800": "UGX",
    "807": "MKD",
    "818": "EGP",
    "826": "GBP",
    "834": "TZS",
    "840": "USD",
    "858": "UYU",
    "860": "UZS",
    "882": "WST",
    "886": "YER",
    "901": "TWD",
    "929": "MRU",
    "930": "STN",
    "931": "CUC",
    "932": "ZWL",
    "934": "TMT",
    "936": "GHS",
    "937": "VEF",
    "938": "SDG",
    "940": "UYI",
    "941": "RSD",
    "943": "MZN",
    "944": "AZN",
    "946": "RON",
    "947": "CHE",
    "948": "CHW",
    "949": "TRY",
    "950": "XAF",
    "951": "XCD",
    "952": "XOF",
    "953": "XPF",
    "960": "XDR",
    "965": "XUA",
    "967": "ZMW",
    "968": "SRD",
    "969": "MGA",
    "970": "COU",
    "971": "AFN",
    "972": "TJS",
    "973": "AOA",
    "974": "BYR",
    "975": "BGN",
    "976": "CDF",
    "977": "BAM",
    "978": "EUR",
    "979": "MXV",
    "980": "UAH",
    "981": "GEL",
    "984": "BOV",
    "985": "PLN",
    "986": "BRL",
    "990": "CLF",
    "994": "XSU",
    "997": "USN",
}
described = {
    "AED": Currency(
        code="AED",
        decimal_digits=2,
        name="United Arab Emirates Dirham",
        name_plural="UAE dirhams",
        rounding=0,
        symbol="AED",
        symbol_native="د.إ.\u200f",
        isoformat="784",
    ),
    "AFN": Currency(
        code="AFN",
        decimal_digits=0,
        name="Afghan Afghani",
        name_plural="Afghan Afghanis",
        rounding=0,
        symbol="Af",
        symbol_native="؋",
        isoformat="971",
    ),
    "ALL": Currency(
        code="ALL",
        decimal_digits=0,
        name="Albanian Lek",
        name_plural="Albanian lekë",
        rounding=0,
        symbol="ALL",
        symbol_native="Lek",
        isoformat="008",
    ),
    "AMD": Currency(
        code="AMD",
        decimal_digits=0,
        name="Armenian Dram",
        name_plural="Armenian drams",
        rounding=0,
        symbol="AMD",
        symbol_native="դր.",
        isoformat="051",
    ),
    "ARS": Currency(
        code="ARS",
        decimal_digits=2,
        name="Argentine Peso",
        name_plural="Argentine pesos",
        rounding=0,
        symbol="AR$",
        symbol_native="$",
        isoformat="032",
    ),
    "AUD": Currency(
        code="AUD",
        decimal_digits=2,
        name="Australian Dollar",
        name_plural="Australian dollars",
        rounding=0,
        symbol="AU$",
        symbol_native="$",
        isoformat="036",
    ),
    "AZN": Currency(
        code="AZN",
        decimal_digits=2,
        name="Azerbaijani Manat",
        name_plural="Azerbaijani manats",
        rounding=0,
        symbol="man.",
        symbol_native="ман.",
        isoformat="944",
    ),
    "BAM": Currency(
        code="BAM",
        decimal_digits=2,
        name="Bosnia-Herzegovina Convertible Mark",
        name_plural="Bosnia-Herzegovina convertible marks",
        rounding=0,
        symbol="KM",
        symbol_native="KM",
        isoformat="977",
    ),
    "BDT": Currency(
        code="BDT",
        decimal_digits=2,
        name="Bangladeshi Taka",
        name_plural="Bangladeshi takas",
        rounding=0,
        symbol="Tk",
        symbol_native="৳",
        isoformat="050",
    ),
    "BGN": Currency(
        code="BGN",
        decimal_digits=2,
        name="Bulgarian Lev",
        name_plural="Bulgarian leva",
        rounding=0,
        symbol="BGN",
        symbol_native="лв.",
        isoformat="975",
    ),
    "BHD": Currency(
        code="BHD",
        decimal_digits=3,
        name="Bahraini Dinar",
        name_plural="Bahraini dinars",
        rounding=0,
        symbol="BD",
        symbol_native="د.ب.\u200f",
        isoformat="048",
    ),
    "BIF": Currency(
        code="BIF",
        decimal_digits=0,
        name="Burundian Franc",
        name_plural="Burundian francs",
        rounding=0,
        symbol="FBu",
        symbol_native="FBu",
        isoformat="108",
    ),
    "BND": Currency(
        code="BND",
        decimal_digits=2,
        name="Brunei Dollar",
        name_plural="Brunei dollars",
        rounding=0,
        symbol="BN$",
        symbol_native="$",
        isoformat="096",
    ),
    "BOB": Currency(
        code="BOB",
        decimal_digits=2,
        name="Bolivian Boliviano",
        name_plural="Bolivian bolivianos",
        rounding=0,
        symbol="Bs",
        symbol_native="Bs",
        isoformat="068",
    ),
    "BRL": Currency(
        code="BRL",
        decimal_digits=2,
        name="Brazilian Real",
        name_plural="Brazilian reals",
        rounding=0,
        symbol="R$",
        symbol_native="R$",
        isoformat="986",
    ),
    "BWP": Currency(
        code="BWP",
        decimal_digits=2,
        name="Botswanan Pula",
        name_plural="Botswanan pulas",
        rounding=0,
        symbol="BWP",
        symbol_native="P",
        isoformat="072",
    ),
    "BYR": Currency(
        code="BYR",
        decimal_digits=0,
        name="Belarusian Ruble",
        name_plural="Belarusian rubles",
        rounding=0,
        symbol="BYR",
        symbol_native="BYR",
        isoformat="974",
    ),
    "BZD": Currency(
        code="BZD",
        decimal_digits=2,
        name="Belize Dollar",
        name_plural="Belize dollars",
        rounding=0,
        symbol="BZ$",
        symbol_native="$",
        isoformat="084",
    ),
    "CAD": Currency(
        code="CAD",
        decimal_digits=2,
        name="Canadian Dollar",
        name_plural="Canadian dollars",
        rounding=0,
        symbol="CA$",
        symbol_native="$",
        isoformat="124",
    ),
    "CDF": Currency(
        code="CDF",
        decimal_digits=2,
        name="Congolese Franc",
        name_plural="Congolese francs",
        rounding=0,
        symbol="CDF",
        symbol_native="FrCD",
        isoformat="976",
    ),
    "CHF": Currency(
        code="CHF",
        decimal_digits=2,
        name="Swiss Franc",
        name_plural="Swiss francs",
        rounding=0.05,
        symbol="CHF",
        symbol_native="CHF",
        isoformat="756",
    ),
    "CLP": Currency(
        code="CLP",
        decimal_digits=0,
        name="Chilean Peso",
        name_plural="Chilean pesos",
        rounding=0,
        symbol="CL$",
        symbol_native="$",
        isoformat="152",
    ),
    "CNY": Currency(
        code="CNY",
        decimal_digits=2,
        name="Chinese Yuan",
        name_plural="Chinese yuan",
        rounding=0,
        symbol="CN¥",
        symbol_native="CN¥",
        isoformat="156",
    ),
    "COP": Currency(
        code="COP",
        decimal_digits=0,
        name="Colombian Peso",
        name_plural="Colombian pesos",
        rounding=0,
        symbol="CO$",
        symbol_native="$",
        isoformat="170",
    ),
    "CRC": Currency(
        code="CRC",
        decimal_digits=0,
        name="Costa Rican Colón",
        name_plural="Costa Rican colóns",
        rounding=0,
        symbol="₡",
        symbol_native="₡",
        isoformat="188",
    ),
    "CVE": Currency(
        code="CVE",
        decimal_digits=2,
        name="Cape Verdean Escudo",
        name_plural="Cape Verdean escudos",
        rounding=0,
        symbol="CV$",
        symbol_native="CV$",
        isoformat="132",
    ),
    "CZK": Currency(
        code="CZK",
        decimal_digits=2,
        name="Czech Republic Koruna",
        name_plural="Czech Republic korunas",
        rounding=0,
        symbol="Kč",
        symbol_native="Kč",
        isoformat="203",
    ),
    "DJF": Currency(
        code="DJF",
        decimal_digits=0,
        name="Djiboutian Franc",
        name_plural="Djiboutian francs",
        rounding=0,
        symbol="Fdj",
        symbol_native="Fdj",
        isoformat="262",
    ),
    "DKK": Currency(
        code="DKK",
        decimal_digits=2,
        name="Danish Krone",
        name_plural="Danish kroner",
        rounding=0,
        symbol="Dkr",
        symbol_native="kr",
        isoformat="208",
    ),
    "DOP": Currency(
        code="DOP",
        decimal_digits=2,
        name="Dominican Peso",
        name_plural="Dominican pesos",
        rounding=0,
        symbol="RD$",
        symbol_native="RD$",
        isoformat="214",
    ),
    "DZD": Currency(
        code="DZD",
        decimal_digits=2,
        name="Algerian Dinar",
        name_plural="Algerian dinars",
        rounding=0,
        symbol="DA",
        symbol_native="د.ج.\u200f",
        isoformat="012",
    ),
    "EEK": Currency(
        code="EEK",
        decimal_digits=2,
        name="Estonian Kroon",
        name_plural="Estonian kroons",
        rounding=0,
        symbol="Ekr",
        symbol_native="kr",
        isoformat=None,
    ),
    "EGP": Currency(
        code="EGP",
        decimal_digits=2,
        name="Egyptian Pound",
        name_plural="Egyptian pounds",
        rounding=0,
        symbol="EGP",
        symbol_native="ج.م.\u200f",
        isoformat="818",
    ),
    "ERN": Currency(
        code="ERN",
        decimal_digits=2,
        name="Eritrean Nakfa",
        name_plural="Eritrean nakfas",
        rounding=0,
        symbol="Nfk",
        symbol_native="Nfk",
        isoformat="232",
    ),
    "ETB": Currency(
        code="ETB",
        decimal_digits=2,
        name="Ethiopian Birr",
        name_plural="Ethiopian birrs",
        rounding=0,
        symbol="Br",
        symbol_native="Br",
        isoformat="230",
    ),
    "EUR": Currency(
        code="EUR",
        decimal_digits=2,
        name="Euro",
        name_plural="euros",
        rounding=0,
        symbol="€",
        symbol_native="€",
        isoformat="978",
    ),
    "GBP": Currency(
        code="GBP",
        decimal_digits=2,
        name="British Pound Sterling",
        name_plural="British pounds sterling",
        rounding=0,
        symbol="£",
        symbol_native="£",
        isoformat="826",
    ),
    "GEL": Currency(
        code="GEL",
        decimal_digits=2,
        name="Georgian Lari",
        name_plural="Georgian laris",
        rounding=0,
        symbol="GEL",
        symbol_native="GEL",
        isoformat="981",
    ),
    "GHS": Currency(
        code="GHS",
        decimal_digits=2,
        name="Ghanaian Cedi",
        name_plural="Ghanaian cedis",
        rounding=0,
        symbol="GH₵",
        symbol_native="GH₵",
        isoformat="936",
    ),
    "GNF": Currency(
        code="GNF",
        decimal_digits=0,
        name="Guinean Franc",
        name_plural="Guinean francs",
        rounding=0,
        symbol="FG",
        symbol_native="FG",
        isoformat="324",
    ),
    "GTQ": Currency(
        code="GTQ",
        decimal_digits=2,
        name="Guatemalan Quetzal",
        name_plural="Guatemalan quetzals",
        rounding=0,
        symbol="GTQ",
        symbol_native="Q",
        isoformat="320",
    ),
    "HKD": Currency(
        code="HKD",
        decimal_digits=2,
        name="Hong Kong Dollar",
        name_plural="Hong Kong dollars",
        rounding=0,
        symbol="HK$",
        symbol_native="$",
        isoformat="344",
    ),
    "HNL": Currency(
        code="HNL",
        decimal_digits=2,
        name="Honduran Lempira",
        name_plural="Honduran lempiras",
        rounding=0,
        symbol="HNL",
        symbol_native="L",
        isoformat="340",
    ),
    "HRK": Currency(
        code="HRK",
        decimal_digits=2,
        name="Croatian Kuna",
        name_plural="Croatian kunas",
        rounding=0,
        symbol="kn",
        symbol_native="kn",
        isoformat="191",
    ),
    "HUF": Currency(
        code="HUF",
        decimal_digits=0,
        name="Hungarian Forint",
        name_plural="Hungarian forints",
        rounding=0,
        symbol="Ft",
        symbol_native="Ft",
        isoformat="348",
    ),
    "IDR": Currency(
        code="IDR",
        decimal_digits=0,
        name="Indonesian Rupiah",
        name_plural="Indonesian rupiahs",
        rounding=0,
        symbol="Rp",
        symbol_native="Rp",
        isoformat="360",
    ),
    "ILS": Currency(
        code="ILS",
        decimal_digits=2,
        name="Israeli New Sheqel",
        name_plural="Israeli new sheqels",
        rounding=0,
        symbol="₪",
        symbol_native="₪",
        isoformat="376",
    ),
    "INR": Currency(
        code="INR",
        decimal_digits=2,
        name="Indian Rupee",
        name_plural="Indian rupees",
        rounding=0,
        symbol="Rs",
        symbol_native="টকা",
        isoformat="356",
    ),
    "IQD": Currency(
        code="IQD",
        decimal_digits=0,
        name="Iraqi Dinar",
        name_plural="Iraqi dinars",
        rounding=0,
        symbol="IQD",
        symbol_native="د.ع.\u200f",
        isoformat="368",
    ),
    "IRR": Currency(
        code="IRR",
        decimal_digits=0,
        name="Iranian Rial",
        name_plural="Iranian rials",
        rounding=0,
        symbol="IRR",
        symbol_native="﷼",
        isoformat="364",
    ),
    "ISK": Currency(
        code="ISK",
        decimal_digits=0,
        name="Icelandic Króna",
        name_plural="Icelandic krónur",
        rounding=0,
        symbol="Ikr",
        symbol_native="kr",
        isoformat="352",
    ),
    "JMD": Currency(
        code="JMD",
        decimal_digits=2,
        name="Jamaican Dollar",
        name_plural="Jamaican dollars",
        rounding=0,
        symbol="J$",
        symbol_native="$",
        isoformat="388",
    ),
    "JOD": Currency(
        code="JOD",
        decimal_digits=3,
        name="Jordanian Dinar",
        name_plural="Jordanian dinars",
        rounding=0,
        symbol="JD",
        symbol_native="د.أ.\u200f",
        isoformat="400",
    ),
    "JPY": Currency(
        code="JPY",
        decimal_digits=0,
        name="Japanese Yen",
        name_plural="Japanese yen",
        rounding=0,
        symbol="¥",
        symbol_native="￥",
        isoformat="392",
    ),
    "KES": Currency(
        code="KES",
        decimal_digits=2,
        name="Kenyan Shilling",
        name_plural="Kenyan shillings",
        rounding=0,
        symbol="Ksh",
        symbol_native="Ksh",
        isoformat="404",
    ),
    "KHR": Currency(
        code="KHR",
        decimal_digits=2,
        name="Cambodian Riel",
        name_plural="Cambodian riels",
        rounding=0,
        symbol="KHR",
        symbol_native="៛",
        isoformat="116",
    ),
    "KMF": Currency(
        code="KMF",
        decimal_digits=0,
        name="Comorian Franc",
        name_plural="Comorian francs",
        rounding=0,
        symbol="CF",
        symbol_native="FC",
        isoformat="174",
    ),
    "KRW": Currency(
        code="KRW",
        decimal_digits=0,
        name="South Korean Won",
        name_plural="South Korean won",
        rounding=0,
        symbol="₩",
        symbol_native="₩",
        isoformat="410",
    ),
    "KWD": Currency(
        code="KWD",
        decimal_digits=3,
        name="Kuwaiti Dinar",
        name_plural="Kuwaiti dinars",
        rounding=0,
        symbol="KD",
        symbol_native="د.ك.\u200f",
        isoformat="414",
    ),
    "KZT": Currency(
        code="KZT",
        decimal_digits=2,
        name="Kazakhstani Tenge",
        name_plural="Kazakhstani tenges",
        rounding=0,
        symbol="KZT",
        symbol_native="тңг.",
        isoformat="398",
    ),
    "LBP": Currency(
        code="LBP",
        decimal_digits=0,
        name="Lebanese Pound",
        name_plural="Lebanese pounds",
        rounding=0,
        symbol="LB£",
        symbol_native="ل.ل.\u200f",
        isoformat="422",
    ),
    "LKR": Currency(
        code="LKR",
        decimal_digits=2,
        name="Sri Lankan Rupee",
        name_plural="Sri Lankan rupees",
        rounding=0,
        symbol="SLRs",
        symbol_native="SL Re",
        isoformat="144",
    ),
    "LTL": Currency(
        code="LTL",
        decimal_digits=2,
        name="Lithuanian Litas",
        name_plural="Lithuanian litai",
        rounding=0,
        symbol="Lt",
        symbol_native="Lt",
        isoformat=None,
    ),
    "LVL": Currency(
        code="LVL",
        decimal_digits=2,
        name="Latvian Lats",
        name_plural="Latvian lati",
        rounding=0,
        symbol="Ls",
        symbol_native="Ls",
        isoformat=None,
    ),
    "LYD": Currency(
        code="LYD",
        decimal_digits=3,
        name="Libyan Dinar",
        name_plural="Libyan dinars",
        rounding=0,
        symbol="LD",
        symbol_native="د.ل.\u200f",
        isoformat="434",
    ),
    "MAD": Currency(
        code="MAD",
        decimal_digits=2,
        name="Moroccan Dirham",
        name_plural="Moroccan dirhams",
        rounding=0,
        symbol="MAD",
        symbol_native="د.م.\u200f",
        isoformat="504",
    ),
    "MDL": Currency(
        code="MDL",
        decimal_digits=2,
        name="Moldovan Leu",
        name_plural="Moldovan lei",
        rounding=0,
        symbol="MDL",
        symbol_native="MDL",
        isoformat="498",
    ),
    "MGA": Currency(
        code="MGA",
        decimal_digits=0,
        name="Malagasy Ariary",
        name_plural="Malagasy Ariaries",
        rounding=0,
        symbol="MGA",
        symbol_native="MGA",
        isoformat="969",
    ),
    "MKD": Currency(
        code="MKD",
        decimal_digits=2,
        name="Macedonian Denar",
        name_plural="Macedonian denari",
        rounding=0,
        symbol="MKD",
        symbol_native="MKD",
        isoformat="807",
    ),
    "MMK": Currency(
        code="MMK",
        decimal_digits=0,
        name="Myanma Kyat",
        name_plural="Myanma kyats",
        rounding=0,
        symbol="MMK",
        symbol_native="K",
        isoformat="104",
    ),
    "MOP": Currency(
        code="MOP",
        decimal_digits=2,
        name="Macanese Pataca",
        name_plural="Macanese patacas",
        rounding=0,
        symbol="MOP$",
        symbol_native="MOP$",
        isoformat="446",
    ),
    "MUR": Currency(
        code="MUR",
        decimal_digits=0,
        name="Mauritian Rupee",
        name_plural="Mauritian rupees",
        rounding=0,
        symbol="MURs",
        symbol_native="MURs",
        isoformat="480",
    ),
    "MXN": Currency(
        code="MXN",
        decimal_digits=2,
        name="Mexican Peso",
        name_plural="Mexican pesos",
        rounding=0,
        symbol="MX$",
        symbol_native="$",
        isoformat="484",
    ),
    "MYR": Currency(
        code="MYR",
        decimal_digits=2,
        name="Malaysian Ringgit",
        name_plural="Malaysian ringgits",
        rounding=0,
        symbol="RM",
        symbol_native="RM",
        isoformat="458",
    ),
    "MZN": Currency(
        code="MZN",
        decimal_digits=2,
        name="Mozambican Metical",
        name_plural="Mozambican meticals",
        rounding=0,
        symbol="MTn",
        symbol_native="MTn",
        isoformat="943",
    ),
    "NAD": Currency(
        code="NAD",
        decimal_digits=2,
        name="Namibian Dollar",
        name_plural="Namibian dollars",
        rounding=0,
        symbol="N$",
        symbol_native="N$",
        isoformat="516",
    ),
    "NGN": Currency(
        code="NGN",
        decimal_digits=2,
        name="Nigerian Naira",
        name_plural="Nigerian nairas",
        rounding=0,
        symbol="₦",
        symbol_native="₦",
        isoformat="566",
    ),
    "NIO": Currency(
        code="NIO",
        decimal_digits=2,
        name="Nicaraguan Córdoba",
        name_plural="Nicaraguan córdobas",
        rounding=0,
        symbol="C$",
        symbol_native="C$",
        isoformat="558",
    ),
    "NOK": Currency(
        code="NOK",
        decimal_digits=2,
        name="Norwegian Krone",
        name_plural="Norwegian kroner",
        rounding=0,
        symbol="Nkr",
        symbol_native="kr",
        isoformat="578",
    ),
    "NPR": Currency(
        code="NPR",
        decimal_digits=2,
        name="Nepalese Rupee",
        name_plural="Nepalese rupees",
        rounding=0,
        symbol="NPRs",
        symbol_native="नेरू",
        isoformat="524",
    ),
    "NZD": Currency(
        code="NZD",
        decimal_digits=2,
        name="New Zealand Dollar",
        name_plural="New Zealand dollars",
        rounding=0,
        symbol="NZ$",
        symbol_native="$",
        isoformat="554",
    ),
    "OMR": Currency(
        code="OMR",
        decimal_digits=3,
        name="Omani Rial",
        name_plural="Omani rials",
        rounding=0,
        symbol="OMR",
        symbol_native="ر.ع.\u200f",
        isoformat="512",
    ),
    "PAB": Currency(
        code="PAB",
        decimal_digits=2,
        name="Panamanian Balboa",
        name_plural="Panamanian balboas",
        rounding=0,
        symbol="B/.",
        symbol_native="B/.",
        isoformat="590",
    ),
    "PEN": Currency(
        code="PEN",
        decimal_digits=2,
        name="Peruvian Nuevo Sol",
        name_plural="Peruvian nuevos soles",
        rounding=0,
        symbol="S/.",
        symbol_native="S/.",
        isoformat="604",
    ),
    "PHP": Currency(
        code="PHP",
        decimal_digits=2,
        name="Philippine Peso",
        name_plural="Philippine pesos",
        rounding=0,
        symbol="₱",
        symbol_native="₱",
        isoformat="608",
    ),
    "PKR": Currency(
        code="PKR",
        decimal_digits=0,
        name="Pakistani Rupee",
        name_plural="Pakistani rupees",
        rounding=0,
        symbol="PKRs",
        symbol_native="₨",
        isoformat="586",
    ),
    "PLN": Currency(
        code="PLN",
        decimal_digits=2,
        name="Polish Zloty",
        name_plural="Polish zlotys",
        rounding=0,
        symbol="zł",
        symbol_native="zł",
        isoformat="985",
    ),
    "PYG": Currency(
        code="PYG",
        decimal_digits=0,
        name="Paraguayan Guarani",
        name_plural="Paraguayan guaranis",
        rounding=0,
        symbol="₲",
        symbol_native="₲",
        isoformat="600",
    ),
    "QAR": Currency(
        code="QAR",
        decimal_digits=2,
        name="Qatari Rial",
        name_plural="Qatari rials",
        rounding=0,
        symbol="QR",
        symbol_native="ر.ق.\u200f",
        isoformat="634",
    ),
    "RON": Currency(
        code="RON",
        decimal_digits=2,
        name="Romanian Leu",
        name_plural="Romanian lei",
        rounding=0,
        symbol="RON",
        symbol_native="RON",
        isoformat="946",
    ),
    "RSD": Currency(
        code="RSD",
        decimal_digits=0,
        name="Serbian Dinar",
        name_plural="Serbian dinars",
        rounding=0,
        symbol="din.",
        symbol_native="дин.",
        isoformat="941",
    ),
    "RUB": Currency(
        code="RUB",
        decimal_digits=2,
        name="Russian Ruble",
        name_plural="Russian rubles",
        rounding=0,
        symbol="RUB",
        symbol_native="руб.",
        isoformat="643",
    ),
    "RWF": Currency(
        code="RWF",
        decimal_digits=0,
        name="Rwandan Franc",
        name_plural="Rwandan francs",
        rounding=0,
        symbol="RWF",
        symbol_native="FR",
        isoformat="646",
    ),
    "SAR": Currency(
        code="SAR",
        decimal_digits=2,
        name="Saudi Riyal",
        name_plural="Saudi riyals",
        rounding=0,
        symbol="SR",
        symbol_native="ر.س.\u200f",
        isoformat="682",
    ),
    "SDG": Currency(
        code="SDG",
        decimal_digits=2,
        name="Sudanese Pound",
        name_plural="Sudanese pounds",
        rounding=0,
        symbol="SDG",
        symbol_native="SDG",
        isoformat="938",
    ),
    "SEK": Currency(
        code="SEK",
        decimal_digits=2,
        name="Swedish Krona",
        name_plural="Swedish kronor",
        rounding=0,
        symbol="Skr",
        symbol_native="kr",
        isoformat="752",
    ),
    "SGD": Currency(
        code="SGD",
        decimal_digits=2,
        name="Singapore Dollar",
        name_plural="Singapore dollars",
        rounding=0,
        symbol="S$",
        symbol_native="$",
        isoformat="702",
    ),
    "SOS": Currency(
        code="SOS",
        decimal_digits=0,
        name="Somali Shilling",
        name_plural="Somali shillings",
        rounding=0,
        symbol="Ssh",
        symbol_native="Ssh",
        isoformat="706",
    ),
    "SYP": Currency(
        code="SYP",
        decimal_digits=0,
        name="Syrian Pound",
        name_plural="Syrian pounds",
        rounding=0,
        symbol="SY£",
        symbol_native="ل.س.\u200f",
        isoformat="760",
    ),
    "THB": Currency(
        code="THB",
        decimal_digits=2,
        name="Thai Baht",
        name_plural="Thai baht",
        rounding=0,
        symbol="฿",
        symbol_native="฿",
        isoformat="764",
    ),
    "TND": Currency(
        code="TND",
        decimal_digits=3,
        name="Tunisian Dinar",
        name_plural="Tunisian dinars",
        rounding=0,
        symbol="DT",
        symbol_native="د.ت.\u200f",
        isoformat="788",
    ),
    "TOP": Currency(
        code="TOP",
        decimal_digits=2,
        name="Tongan Paʻanga",
        name_plural="Tongan paʻanga",
        rounding=0,
        symbol="T$",
        symbol_native="T$",
        isoformat="776",
    ),
    "TRY": Currency(
        code="TRY",
        decimal_digits=2,
        name="Turkish Lira",
        name_plural="Turkish Lira",
        rounding=0,
        symbol="TL",
        symbol_native="TL",
        isoformat="949",
    ),
    "TTD": Currency(
        code="TTD",
        decimal_digits=2,
        name="Trinidad and Tobago Dollar",
        name_plural="Trinidad and Tobago dollars",
        rounding=0,
        symbol="TT$",
        symbol_native="$",
        isoformat="780",
    ),
    "TWD": Currency(
        code="TWD",
        decimal_digits=2,
        name="New Taiwan Dollar",
        name_plural="New Taiwan dollars",
        rounding=0,
        symbol="NT$",
        symbol_native="NT$",
        isoformat="901",
    ),
    "TZS": Currency(
        code="TZS",
        decimal_digits=0,
        name="Tanzanian Shilling",
        name_plural="Tanzanian shillings",
        rounding=0,
        symbol="TSh",
        symbol_native="TSh",
        isoformat="834",
    ),
    "UAH": Currency(
        code="UAH",
        decimal_digits=2,
        name="Ukrainian Hryvnia",
        name_plural="Ukrainian hryvnias",
        rounding=0,
        symbol="₴",
        symbol_native="₴",
        isoformat="980",
    ),
    "UGX": Currency(
        code="UGX",
        decimal_digits=0,
        name="Ugandan Shilling",
        name_plural="Ugandan shillings",
        rounding=0,
        symbol="USh",
        symbol_native="USh",
        isoformat="800",
    ),
    "USD": Currency(
        code="USD",
        decimal_digits=2,
        name="US Dollar",
        name_plural="US dollars",
        rounding=0,
        symbol="$",
        symbol_native="$",
        isoformat="840",
    ),
    "UYU": Currency(
        code="UYU",
        decimal_digits=2,
        name="Uruguayan Peso",
        name_plural="Uruguayan pesos",
        rounding=0,
        symbol="$U",
        symbol_native="$",
        isoformat="858",
    ),
    "UZS": Currency(
        code="UZS",
        decimal_digits=0,
        name="Uzbekistan Som",
        name_plural="Uzbekistan som",
        rounding=0,
        symbol="UZS",
        symbol_native="UZS",
        isoformat="860",
    ),
    "VEF": Currency(
        code="VEF",
        decimal_digits=2,
        name="Venezuelan Bolívar",
        name_plural="Venezuelan bolívars",
        rounding=0,
        symbol="Bs.raise_exception_matching_error_code.",
        symbol_native="Bs.raise_exception_matching_error_code.",
        isoformat="937",
    ),
    "VND": Currency(
        code="VND",
        decimal_digits=0,
        name="Vietnamese Dong",
        name_plural="Vietnamese dong",
        rounding=0,
        symbol="₫",
        symbol_native="₫",
        isoformat="704",
    ),
    "XAF": Currency(
        code="XAF",
        decimal_digits=0,
        name="CFA Franc BEAC",
        name_plural="CFA francs BEAC",
        rounding=0,
        symbol="FCFA",
        symbol_native="FCFA",
        isoformat="950",
    ),
    "XOF": Currency(
        code="XOF",
        decimal_digits=0,
        name="CFA Franc BCEAO",
        name_plural="CFA francs BCEAO",
        rounding=0,
        symbol="CFA",
        symbol_native="CFA",
        isoformat="952",
    ),
    "YER": Currency(
        code="YER",
        decimal_digits=0,
        name="Yemeni Rial",
        name_plural="Yemeni rials",
        rounding=0,
        symbol="YR",
        symbol_native="ر.ي.\u200f",
        isoformat="886",
    ),
    "ZAR": Currency(
        code="ZAR",
        decimal_digits=2,
        name="South African Rand",
        name_plural="South African rand",
        rounding=0,
        symbol="R",
        symbol_native="R",
        isoformat="710",
    ),
    "ZMK": Currency(
        code="ZMK",
        decimal_digits=0,
        name="Zambian Kwacha",
        name_plural="Zambian kwachas",
        rounding=0,
        symbol="ZK",
        symbol_native="ZK",
        isoformat=None,
    ),
}
