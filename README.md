# SAAMAPIArtists
Documenting Artists of Color in the SAAM Collection 


The SAAM API Artists Project extrapolates demographic data from the American Art API in the hopes of illuminating the work of under represented artists. Using the .get request I gathered information from the API (GetSAAMData.py) and transformed it into structured data (SAAMFinal.py). The next step in my project was an attempt to gather ethnicity or racial demographic data from each African American artist using their ULAN ID number. The ULAN_InfoINeed.py file gathers each artists ULAN file and searches for ethnicity information under the Nationality predicate. However, my attempts proved unsuccessful as ethnicity and nationality are conflated in the ULAN database, as American is listed as the primary nationality for almost all African American Artists. African American Artists’ race is denoted as “nationalityNonPreferred” and is therefore nested within the data structure and difficult to gather.
