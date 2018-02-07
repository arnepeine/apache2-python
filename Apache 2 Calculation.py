
# coding: utf-8

# In[19]:


# Calculate APACHE II Score
# 02/2018 / Arne Peine
# Required variables for APACHE II calculation
# APACHE II ("Acute Physiology And Chronic Health Evaluation II") is a severity-of-disease classification system (Knaus et al., 1985), one of several ICU scoring systems. It is applied within 24 hours of admission of a patient to an intensive care unit (ICU): an integer score from 0 to 71 is computed based on several measurements; higher scores correspond to more severe disease and a higher risk of death. The first APACHE model was presented by Knaus et al. in 1981.

# 1. Required Variables and reference ranges

# Body temperature, requires float
temperature = 0 

# Mean arterial blood pressure, requires integer
arterial_mean_pressure = 0

# Mean heartbeats per minute, requires integer
heart_bpm = 0 

# Respiratory rate per minute, requires integer
respiratory_rate = 0

# Oxygenation: The APACHEII uses different inputs, depending on the fraction of inspired oxygen
# For a FiO2 > 0.5, the algorithm uses the AaDO2 (calculated like this: AaDO2 (mmHG) = pAO2 - paO2)
# The function calculate_aado2 can also be used (see below)

# For FiO2 >0.5 record AaDO2
# For FiO2 <0.5 record only PaO2 (arterial partial pressure of O2)

oxygenation = 0

# Blood ph level, requires float
ph = 0

# Blood serum sodium level in mMol/l, requires float
sodium = 0

# Blood serium potassium level in mMol/l, requires float
potassium = 0

# Acute renal failure present? 1 for yes, 0 for no, requires integer
acute_renal_failure = 0

# Blood serum creatinine levels in mg/100ml, requires float
creatinine = 0

# Hematocrit in %, requires float
hematocrit = 0

# White blood count (total/mm^3) in 1000s, requires float
wbc = 0

# Glasgow Coma Scale, requires integer
gcs = 0



# 2. Score calculation

def calc_temperature (temperature):
    calculated_temperature_score = "Error"
    if  temperature >= 41:
        calculated_temperature_score = 4
    elif 39 > temperature < 40.9:
        calculated_temperature_score = 3
    elif 38.5 > temperature < 38.9:
        calculated_temperature_score = 1
    elif 36 > temperature < 38.4:
        calculated_temperature_score = 0        
    elif 34 > temperature < 35.9:
        calculated_temperature_score = 1        
    elif 32 > temperature < 33.9:
        calculated_temperature_score = 2        
    elif 30 > temperature < 31.9:
        calculated_temperature_score = 3        
    elif temperature <= 31.9:
        calculated_temperature_score = 4
    
    return(calculated_temperature_score)



print(calc_temperature(38.9))
    
    

