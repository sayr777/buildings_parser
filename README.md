
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



 <option value="2208163">Алтайский край</option>
                                                                                    <option value="2215422">Амурская область</option>
                                                                                    <option value="2216073">Архангельская область</option>
                                                                                    <option value="2220005">Астраханская область</option>
                                                                                    <option value="2220463">Белгородская область</option>
                                                                                    <option value="2222089">Брянская область</option>
                                                                                    <option value="2224825">Владимирская область</option>
                                                                                    <option value="2227349">Волгоградская область</option>
                                                                                    <option value="2228920">Вологодская область</option>
                                                                                    <option value="2236864">Воронежская область</option>
                                                                                    <option value="2280999">город Москва</option>
                                                                                    <option value="2276347">город Санкт-Петербург</option>
                                                                                    <option value="2399515">город Севастополь</option>
                                                                                    <option value="2361205">Еврейская автономная область</option>
                                                                                    <option value="2333436">Забайкальский край</option>
                                                                                    <option value="2243734">Ивановская область</option>
                                                                                    <option value="2246043">Иркутская область</option>
                                                                                    <option value="2347352">Кабардино-Балкарская Республика</option>
                                                                                    <option value="2247652">Калининградская область</option>
                                                                                    <option value="2258331">Калужская область</option>
                                                                                    <option value="2261569">Камчатский край</option>
                                                                                    <option value="2352939">Карачаево-Черкесская Республика</option>
                                                                                    <option value="2261688">Кемеровская область - Кузбасс</option>
                                                                                    <option value="2262823">Кировская область</option>
                                                                                    <option value="2267309">Костромская область</option>
                                                                                    <option value="2209858">Краснодарский край</option>
                                                                                    <option value="2211647">Красноярский край</option>
                                                                                    <option value="2272233">Курганская область</option>
                                                                                    <option value="2273507">Курская область</option>
                                                                                    <option value="2276351">Ленинградская область</option>
                                                                                    <option value="2279312">Липецкая область</option>
                                                                                    <option value="2280928">Магаданская область</option>
                                                                                    <option value="2281126">Московская область</option>
                                                                                    <option value="2287468">Мурманская область</option>
                                                                                    <option value="2361342">Ненецкий автономный округ</option>
                                                                                    <option value="2238753">Нижегородская область</option>
                                                                                    <option value="2287629">Новгородская область</option>
                                                                                    <option value="2290273">Новосибирская область</option>
                                                                                    <option value="2291899">Омская область</option>
                                                                                    <option value="2293481">Оренбургская область</option>
                                                                                    <option value="2295251">Орловская область</option>
                                                                                    <option value="2298217">Пензенская область</option>
                                                                                    <option value="2299744">Пермский край</option>
                                                                                    <option value="2213474">Приморский край</option>
                                                                                    <option value="2303372">Псковская область</option>
                                                                                    <option value="2340164">Республика Адыгея</option>
                                                                                    <option value="2347543">Республика Алтай</option>
                                                                                    <option value="2340399">Республика Башкортостан</option>
                                                                                    <option value="2345009">Республика Бурятия</option>
                                                                                    <option value="2345675">Республика Дагестан</option>
                                                                                    <option value="2247643">Республика Ингушетия</option>
                                                                                    <option value="2347799">Республика Калмыкия</option>
                                                                                    <option value="2348078">Республика Карелия</option>
                                                                                    <option value="2348894">Республика Коми</option>
                                                                                    <option value="2399489">Республика Крым</option>
                                                                                    <option value="2349746">Республика Марий Эл</option>
                                                                                    <option value="2351376">Республика Мордовия</option>
                                                                                    <option value="2360536">Республика Саха (Якутия)</option>
                                                                                    <option value="2352709">Республика Северная Осетия-Алания</option>
                                                                                    <option value="2353101">Республика Татарстан</option>
                                                                                    <option value="2356269">Республика Тыва</option>
                                                                                    <option value="2358459">Республика Хакасия</option>
                                                                                    <option value="2310204">Ростовская область</option>
                                                                                    <option value="2312245">Рязанская область</option>
                                                                                    <option value="2270853">Самарская область</option>
                                                                                    <option value="2315056">Саратовская область</option>
                                                                                    <option value="2316924">Сахалинская область</option>
                                                                                    <option value="2317157">Свердловская область</option>
                                                                                    <option value="2319070">Смоленская область</option>
                                                                                    <option value="2214158">Ставропольский край</option>
                                                                                    <option value="2323682">Тамбовская область</option>
                                                                                    <option value="2248754">Тверская область</option>
                                                                                    <option value="2325436">Томская область</option>
                                                                                    <option value="2326046">Тульская область</option>
                                                                                    <option value="2329523">Тюменская область</option>
                                                                                    <option value="2356486">Удмуртская Республика</option>
                                                                                    <option value="2331106">Ульяновская область</option>
                                                                                    <option value="2214950">Хабаровский край</option>
                                                                                    <option value="2330826">Ханты-Мансийский автономный округ</option>
                                                                                    <option value="2332121">Челябинская область</option>
                                                                                    <option value="2358750">Чеченская Республика</option>
                                                                                    <option value="2358768">Чувашская Республика</option>
                                                                                    <option value="2334262">Чукотский автономный округ</option>
                                                                                    <option value="2331019">Ямало-Ненецкий автономный округ</option>
                                                                                    <option value="2334335">Ярославская область</option>
