from data import CountyDemographics

def population_total(counties: list[CountyDemographics])->int:
    total = 0
    for county in counties:
        total += county.population["2014 Population"]
    return total

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state]

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population["2014 Population"] * county.education[key] / 100
    return total

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population["2014 Population"] * county.ethnicities[key] / 100
    return total

def population_below_poverty_level(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        total += county.population["2014 Population"] * county.income[key] / 100
    return total

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    return (100*((population_by_education(counties, key) / population_total(counties))))

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    return (100*((population_by_ethnicity(counties, key) / population_total(counties))))

def percent_by_below_poverty_level(counties: list[CountyDemographics], key: str) -> float:
    return (100*((population_below_poverty_level(counties, key)/population_total(counties))))

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    new_list= []
    for county in counties:
        if county.education[key] >= threshold:
            new_list.append(county)
    return new_list

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    new_list = []
    for county in counties:
        if county.education[key] <= threshold:
            new_list.append(county)
    return new_list

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    new_list = []
    for county in counties:
        if county.ethnicities[key] >= threshold:
            new_list.append(county)
    return new_list

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    new_list = []
    for county in counties:
        if county.ethnicities[key] <= threshold:
            new_list.append(county)
    return new_list

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    new_list = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] >= threshold:
            new_list.append(county)
    return new_list

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    new_list = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] <= threshold:
            new_list.append(county)
    return new_list
