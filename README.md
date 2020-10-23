
Парсер данных с сайта Реформа ЖКХ (http://www.reformagkh.ru) с возможностью выбора региона РФ.
Парсер выгружает наборы открытых данных в формате csv по всем регионам РФ и объединяет их в единый файл.

Пример https://www.reformagkh.ru/opendata/export/93

https://www.reformagkh.ru/opendata/export/2


Структура набора
id ID дома на Портале
region_id Субъект РФ (код ФИАС)
area_id Район (код ФИАС)
city_id Населенный пункт (код ФИАС)
street_id Улица (код ФИАС)
shortname_region Тип Субъекта РФ
formalname_region Субъект РФ (наименование)
shortname_area Тип района
formalname_area Район (наименование)
shortname_city Тип населенного пункта
formalname_city Населенный пункт (наименование)
shortname_street Тип улицы
formalname_street Улица (наименование)
house_number Номер дома
building Строение
block Корпус
letter Литера
address Адрес дома
houseguid Глобальный уникальный идентификатор дома
management_organization_id ID Управляющей организации на Портале
built_year Год постройки
exploitation_start_year Год ввода в эксплуатацию
project_type Серия, тип постройки здания
house_type Тип дома
is_alarm Факт признания дома аварийным
method_of_forming_overhaul_fund Способ формирования фонда капитального ремонта
floor_count_max Наибольшее количество этажей, ед.
floor_count_min Наименьшее количество этажей, ед.
entrance_count Количество подъездов, ед.
elevators_count Количество лифтов, ед.
energy_efficiency Класс энергетической эффективности
quarters_count Количество помещений, всего, ед.
living_quarters_count
Количество жилых помещений, ед.
unliving_quarters_count
Количество нежилых помещений, ед.
area_total
Общая площадь дома, всего, кв.м
area_residential
Общая площадь жилых помещений, кв.м
area_non_residential
Общая площадь нежилых помещений, кв.м
area_common_property
Общая площадь помещений, входящих в состав общего имущества, кв.м
area_land
Площадь земельного участка, входящего в состав общего имущества в многоквартирном доме, кв.м
parking_square
Площадь парковки в границах земельного участка, кв.м
playground
Элементы благоустройства (детская площадка)
sportsground
Элементы благоустройства (спортивная площадка)
other_beautification
Элементы благоустройства (другое)
foundation_type
Тип фундамента
floor_type
Тип перекрытий
wall_material
Материал несущих стен
basement_area
Площадь подвала по полу, кв.м
chute_type
Тип мусоропровода
chute_count
Количество мусоропроводов, ед.
electrical_type
Тип системы электроснабжения
electrical_entries_count
Количество вводов в МКД, ед.
heating_type
Тип системы теплоснабжения
hot_water_type
Тип системы горячего водоснабжения
cold_water_type
Тип системы холодного водоснабжения
sewerage_type
Тип системы водоотведения
sewerage_cesspools_volume
Объем выгребных ям, куб.м
gas_type
Тип системы газоснабжения
ventilation_type
Тип системы вентиляции
firefighting_type
Тип системы пожаротушения
drainage_type
Тип системы водостоков



License
-------
* Code - GNU GPL v2 or any later version
* Data - GNU GPL v2 or any later version
