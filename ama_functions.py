import re

def clean_exit_year(year_str:str) -> None|int:
	regex = r'\d+'
	result = re.findall(regex, year_str)
	if not result:
		return None
	result = result[0]
	if len(result) == 2:
		result = "19" + result
	return int(result)

def clean_dob_dod(date_str:str) -> tuple:
	regex_death = r'Died\S\s*|DOD\S\s*'
	regex_birth = r'DOB\S\s*'
	regex_datestring = r'\d+'

	birth_year = None
	death_year = None

	result_death = re.findall(r'\d+', date_str)
	if result_death:
		print(re.findall(r'\d+', date_str))
	return (birth_year, death_year)

clean_dob_dod("Died: 04/05/1953")
