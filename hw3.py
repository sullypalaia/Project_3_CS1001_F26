from data import CountyDemographics

# returns the sum of the 2014 population of all counties in the list
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population["2014 Population"]
    return int(total)

# returns the counties in the list that match state abbreviation
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state]


# returns the estimated population for the specified education key
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        if key in county.education:
            total += county.population["2014 Population"] * county.education[key] / 100
    return total


# returns the estimated population for the specified ethnicity key
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        if key in county.ethnicities:
            total += county.population["2014 Population"] * county.ethnicities[key] / 100
    return total


# returns the estimated population below poverty level
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        total += county.population["2014 Population"] * county.income["Persons Below Poverty Level"] / 100
    return total


# returns the percentage with the specified education
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_by_education(counties, key) / total * 100


# returns percentage with the specified ethnicity
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_by_ethnicity(counties, key) / total * 100


# returns the percentage below poverty level
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = population_total(counties)
    if total == 0:
        return 0
    return population_below_poverty_level(counties) / total * 100


# returns counties whose percentage for the specified education is above the threshold
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education[key] > threshold]


# returns counties whose percentage for the specified education is below the threshold
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education[key] < threshold]


# returns counties whose percentage for the specified ethnicity is above the threshold
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities[key] > threshold]


# returns counties whose percentage for the specified ethnicity is below the threshold
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities[key] < threshold]


# returns counties whose poverty percentage is above the threshold
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] > threshold]


# returns counties whose poverty percentage is below the threshold
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] < threshold]
