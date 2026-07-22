from typing import Literal

COLUMN_MAPPING = {
    "agency": "Agency",
    "agency_type": "Agency Type",
    "distribution_channel": "Distribution Channel",
    "product_name": "Product Name",
    "destination": "Destination",
    "duration": "Duration",
    "net_sales": "Net Sales",
    "commission": "Commission",
    "age": "Age",
    "is_refund": "Is Refund",
    "suspected_fraud": "Suspected Fraud",
    "commission_rate": "Commission Rate",
}


AgencyType = Literal['C2B', 'EPX', 'JZI', 'CWT', 'LWC', 'ART', 'CSR', 'SSI', 
                    'RAB', 'KML', 'TST', 'TTW', 'JWT', 'ADM', 'CCR', 'CBH']

AgencyCategory = Literal['Airlines', 'Travel Agency']

Channel = Literal['Online', 'Offline']

ProductName = Literal[
    'Annual Silver Plan', 'Cancellation Plan', 'Basic Plan', '2 way Comprehensive Plan',
    'Bronze Plan', '1 way Comprehensive Plan', 'Rental Vehicle Excess Insurance',
    'Single Trip Travel Protect Gold', 'Silver Plan', 'Value Plan', '24 Protect',
    'Annual Travel Protect Gold', 'Comprehensive Plan', 'Ticket Protector',
    'Travel Cruise Protect', 'Single Trip Travel Protect Silver',
    'Individual Comprehensive Plan', 'Gold Plan', 'Annual Gold Plan',
    'Child Comprehensive Plan', 'Premier Plan', 'Annual Travel Protect Silver',
    'Single Trip Travel Protect Platinum', 'Annual Travel Protect Platinum',
    'Spouse or Parents Comprehensive Plan', 'Travel Cruise Protect Family'
]

Destination = Literal[
    'SINGAPORE', 'MALAYSIA', 'INDIA', 'UNITED STATES', 'KOREA, REPUBLIC OF',
    'THAILAND', 'GERMANY', 'JAPAN', 'INDONESIA', 'VIET NAM', 'AUSTRALIA', 'FINLAND',
    'UNITED KINGDOM', 'SRI LANKA', 'SPAIN', 'HONG KONG', 'MACAO', 'CHINA',
    'UNITED ARAB EMIRATES', 'IRAN, ISLAMIC REPUBLIC OF', 'TAIWAN, PROVINCE OF CHINA',
    'POLAND', 'CANADA', 'OMAN', 'PHILIPPINES', 'GREECE', 'BELGIUM', 'TURKEY',
    'BRUNEI DARUSSALAM', 'DENMARK', 'SWITZERLAND', 'NETHERLANDS', 'SWEDEN', 'MYANMAR',
    'KENYA', 'CZECH REPUBLIC', 'FRANCE', 'RUSSIAN FEDERATION', 'PAKISTAN', 'ARGENTINA',
    'TANZANIA, UNITED REPUBLIC OF', 'SERBIA', 'ITALY', 'CROATIA', 'NEW ZEALAND',
    'PERU', 'MONGOLIA', 'CAMBODIA', 'QATAR', 'NORWAY', 'LUXEMBOURG', 'MALTA',
    "LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'ISRAEL', 'SAUDI ARABIA', 'AUSTRIA',
    'PORTUGAL', 'NEPAL', 'UKRAINE', 'ESTONIA', 'ICELAND', 'BRAZIL', 'MEXICO',
    'CAYMAN ISLANDS', 'PANAMA', 'BANGLADESH', 'TURKMENISTAN', 'BAHRAIN', 'KAZAKHSTAN',
    'TUNISIA', 'IRELAND', 'ETHIOPIA', 'NORTHERN MARIANA ISLANDS', 'MALDIVES',
    'SOUTH AFRICA', 'VENEZUELA', 'COSTA RICA', 'JORDAN', 'MALI', 'CYPRUS', 'MAURITIUS',
    'LEBANON', 'KUWAIT', 'AZERBAIJAN', 'HUNGARY', 'BHUTAN', 'BELARUS', 'MOROCCO',
    'ECUADOR', 'UZBEKISTAN', 'CHILE', 'FIJI', 'PAPUA NEW GUINEA', 'ANGOLA',
    'FRENCH POLYNESIA', 'NIGERIA', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
    'NAMIBIA', 'GEORGIA', 'COLOMBIA', 'SLOVENIA', 'EGYPT', 'ZIMBABWE', 'BULGARIA',
    'BERMUDA', 'URUGUAY', 'GUINEA', 'GHANA', 'BOLIVIA', 'TRINIDAD AND TOBAGO',
    'VANUATU', 'GUAM', 'UGANDA', 'JAMAICA', 'LATVIA', 'ROMANIA',
    'REPUBLIC OF MONTENEGRO', 'KYRGYZSTAN', 'GUADELOUPE', 'ZAMBIA', 'RWANDA',
    'BOTSWANA', 'GUYANA', 'LITHUANIA', 'GUINEA-BISSAU', 'SENEGAL', 'CAMEROON',
    'TIBET', 'SAMOA', 'PUERTO RICO', 'TAJIKISTAN', 'ARMENIA',
    "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'FAROE ISLANDS', 'DOMINICAN REPUBLIC',
    'MOLDOVA, REPUBLIC OF', 'BENIN', 'REUNION'
]
