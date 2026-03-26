#exercise -level 1
'''empty_list = []

list = [1,2,5,'Gopal',23,53]

print(len(list))

print(list[0::2])

mixed_data_types = ['Gopal',21,'6ft','unmarried','Gustok']

it_companies = ['Facebook','Google','Microsoft',' Apple', 'IBM', 'Oracle','Amazon']

print(it_companies)

print(len(it_companies))

it_companies[0] = 'Vincorp'
print(it_companies)

it_companies.append('Jojoinzing')
it_companies.insert(3, 'capsule corp')

it_companies[1] = it_companies[1].upper()
print(it_companies)

it_companies = ["#! " + item for item in it_companies]
print(it_companies)

if '#! Vincorp' in it_companies:
    print('Yes it does exist')

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3])

print(it_companies[-1:-4:-1])

print(it_companies[5:6])

it_companies.pop(0)
it_companies.pop(4)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

front_end.extend(['Python','SQL'])
'''
#Exercise-level2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum = min(ages)
maximum = max(ages)

ages.extend([minimum,maximum])
print(ages)

print(ages[len(ages)//2])

sum=0
for num in ages:
    sum = sum + num
average = sum/len(ages)

range = maximum-minimum

if abs(minimum-average) == abs(maximum-average):
    print("True")
else:
    print("False")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(countries[len(countries)//2])
print(len(countries))

countries.append('czechblak')

F_half = countries[0:len(countries)//2]
print(F_half)

S_half = countries[-1:-(len(countries)//2)]
print(S_half)

new_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']




