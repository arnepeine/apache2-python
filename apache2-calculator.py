# Calculate APACHE II Score
# 02/2018 / Arne Peine
# APACHE II ("Acute Physiology And Chronic Health Evaluation II") is a severity-of-disease classification system (Knaus et al., 1985), one of several ICU scoring systems. It is applied within 24 hours of admission of a patient to an intensive care unit (ICU): an integer score from 0 to 71 is computed based on several measurements; higher scores correspond to more severe disease and a higher risk of death. The first APACHE model was presented by Knaus et al. in 1981.
# Note: The data used should be from the initial 24 hours in the ICU, worst value should be used.
# Reference: Reference. Knaus WA Draper EA et al. APACHE II: A severity of disease classification system. Critical Care Medicine. 1985



# 1. Required Variables and explanations

# 1.1. Acute Physiology Score
# Variables are defined like this -
# Body temperature, expects float: temperature 
# Mean arterial blood pressure, expects integer: abp 
# Mean heartbeats per minute, expects integer: heart_bpm
# Respiratory rate per minute, expects integer: respiratory_rate

# Oxygenation: The APACHEII uses different inputs, depending on the fraction of inspired oxygen
# For a FiO2 > 0.5, the algorithm uses the AaDO2 (calculated like this: AaDO2 (mmHG) = pAO2 - paO2)
# The function calculate_aado2 can also be used (see below)

# For FiO2 >0.5 record AaDO2
# For FiO2 <0.5 record only PaO2 (arterial partial pressure of O2):  oxygenation 

# Blood ph level, expects float: ph 
# Blood serum sodium level in mMol/l, expects float: sodium 
# Blood serium potassium level in mMol/l, expects float: potassium 
# Acute renal injury present? 1 for yes, 0 for no, expects integer: aki
# Blood serum creatinine levels in mg/100ml, expects float: creatinine 
# Hematocrit in %, expects float: hematocrit
# White blood count (total/mm^3) in 1000s, expects float: wbc 
# Glasgow Coma Scale, expects integer: gcs 

## 2. Functions
# in_range() calculates whether a value is within the limits
# calculate_single_scores() calcuates values for a single value, e.g. calculate_single_scores (80, "abp") calculates the single score for a mean arterial blood pressure of 80
# calulate_apache2_physiology() calculates Acute Physiology Score
# chronic_health_score() calculates CHS
# calculate_apache2_final() combines all calculations above. Query like this: calculate_apache2_final(abp,temperature,heart_bpm,respiratory_rate,oxygenation,ph,sodium,potassium,hematocrit,wbc,age,scd,aki,creatinine,gcs) e.g. calculate_apache(60,37,90,20,300,7.7,190,7,50,22,44,"NO NSCD",1,7,15).

def in_range (lowerlimit, upperlimit, value):
    return lowerlimit <= value <= upperlimit
       
def calculate_single_scores (value, selector):
    
    # APACHEII Ranges
    
    if selector is "abp":
        value_ranges = ([160,300,4],[130,159,3],[110,129,2],[70,109,0],[50,69,2],[0,49,4])
    elif selector is "temperature":
        value_ranges = ([41,50,4],[39,40.9,3],[38.5,38.9,1],[36,38.9,0],[34,35.9,1],[32,33.9,2],[30,31.9,3],[19,29.9,4])
    elif selector is "heart_bpm":
        value_ranges = ([180,300,4],[140,179,3],[110,139,2],[70,109,0],[55,69,2],[40,45,4],[0,49,4])
    elif selector is "respiratory_rate":
        value_ranges = ([50,100,4],[35,49,3],[25,34,2],[12,24,0],[10,11,1],[6,9,2],[0,5,4])
    elif selector is "oxygenation": # see explanation!
        value_ranges = ([500,1000,4],[350,499,3],[200,349,2],[70,200,0],[61,70,1],[55,60,3],[0,55,4])
    elif selector is "ph":
        value_ranges = ([7.7,9.0,4],[7.6,7.69,3],[7.5,7.59,1],[7.33,7.49,0],[7.25,7.32,2],[7.15,7.24,3],[5,7.15,4])
    elif selector is "sodium":
        value_ranges = ([180,300,4],[160,179,3],[155,159,2],[150,154,1],[130,149,0],[120,129,2],[111,119,3],[50,110,4])
    elif selector is "potassium":
        value_ranges = ([7,9,4],[6,6.9],[5.5,5.9],[3.5,5.4,0],[3,3.4,1],[2.5,2.9,2],[2.5,2,4])
    #elif selector is "creatinine":
     #   value_ranges = ([3.5,30,4],[2,3.4,3],[1.5,1.9,2],[0.6,1.4,0],[0,0.6,2])
    elif selector is "hematocrit":
        value_ranges = ([60,100,4],[50,59.9,2],[46,49.9,1],[30,45.9,0],[20,29.9,2],[0,20,4])
    elif selector is "wbc":
        value_ranges = ([40,100,4],[20,39.9,2],[15,19.9,1],[3,14.9,0],[1,2.9,2],[0,1,4]) 
    elif selector is "age":
        value_ranges = ([18,44,0],[45,54,2],[55,64,3],[65,74,5],[75,120,6]) 
    else:
        value_ranges = 0
        
    for value_range in value_ranges:
        if in_range(value_range[0], value_range[1], value):
            return int(value_range[2])

def calculate_apache2_physiology(abp,temperature,heart_bpm,respiratory_rate,oxygenation,ph,sodium,potassium,hematocrit,wbc,age):
    args = list(locals().values())
    #print(args)
    list_of_scores = []
    selectors = list(reversed(["abp","temperature","heart_bpm","respiratory_rate","oxygenation","ph","sodium","potassium","hematocrit","wbc", "age"]))
    for arg, selector in zip(args, selectors):
        #print(selector, arg)
        result = calculate_single_scores(arg, selector)
        list_of_scores.append(result)
    return(sum(list_of_scores))

#This function accepts a total of 6 values for adressing Chronic Health Points and surgery status
#value="RO NSCD">elective postoperative, no SCD (Severe Chronic Diseases, see list)
#value="RO SCD">elective postoperative, SCD present
#value="NO NSCD">no surgery, no SCD
#value="NO SCD">no surgery, SCD present
#value="EO NSCD">emergency postoperative, no SCD
#value="EO SCD">emergency postoperative, SCD present

def chronic_health_score(value):

    if value == "RO NSCD":
        result = "0"
    elif value == "RO SCD":
        result = "2"
    elif value == "EO NSCD":
        result = "0"
    elif value == "EO SCD":
        result = "5"
    elif value == "NO NSCD":
        result = "0"
    elif value == "NO SCD":
        result = "5"   
    return(result)
        
def calculate_apache2_final(abp,temperature,heart_bpm,respiratory_rate,oxygenation,ph,sodium,potassium,hematocrit,wbc,age,scd,aki,creatinine,gcs):
    args = list(locals().values())
    physiology = calculate_apache2_physiology(abp,temperature,heart_bpm,respiratory_rate,oxygenation,ph,sodium,potassium,hematocrit,wbc,age)
    health_points = int(chronic_health_score(scd))
    # Double points for acute kidney injury
    if aki == 0:
        value_ranges = ([3.5,30,4],[2,3.4,3],[1.5,1.9,2],[0.6,1.4,0],[0,0.6,2])
    else:
        value_ranges = ([3.5,30,8],[2,3.4,6],[1.5,1.9,4],[0.6,1.4,0],[0,0.6,4])
    
    for value_range in value_ranges:
        if in_range(value_range[0], value_range[1], creatinine):
            creatinine_points = int(value_range[2])
    gcs_final = 15 - gcs
    final_score = int(physiology)+int(health_points)+int(creatinine_points)+gcs_final
    return(final_score)
  
print(calculate_apache(60,37,90,20,300,7.7,190,7,50,22,44,"NO NSCD",1,7,15)) // should be 28
