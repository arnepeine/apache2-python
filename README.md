# Calculation of the APACHE II ("Acute Physiology and Chronic Health Evaluation II") score in Python

The APACHE II ("Acute Physiology And Chronic Health Evaluation II") is a severity-of-disease classification system (Knaus et al., 1985), one of several ICU scoring systems. It is applied within 24 hours of admission of a patient to an intensive care unit (ICU): an integer score from 0 to 71 is computed based on several measurements; higher scores correspond to more severe disease and a higher risk of death. The first APACHE model was presented by Knaus et al. in 1981.
- Note: The data used should be from the initial 24 hours in the ICU, worst value should be used.
- Reference: Knaus WA Draper EA et al. APACHE II: A severity of disease classification system. Critical Care Medicine. 1985


# Instructions
- The script contains four main functions
  - in_range() calculates whether a value is within the limits
  - calculate_single_scores() calcuates values for a single value, e.g. calculate_single_scores (80, "abp") calculates the single score for a mean arterial blood pressure of 80
  - calulate_apache2_physiology() calculates the Acute Physiology Score
  - chronic_health_score() calculates the chronic health points 
  - calculate_apache2_final() combines all calculations above. Query like this: calculate_apache2_final(abp,temperature,heart_bpm,respiratory_rate,oxygenation,ph,sodium,potassium,hematocrit,wbc,age,scd,aki,creatinine,gcs) e.g. *calculate_apache(60,37,90,20,300,7.7,190,7,50,22,44,"NO NSCD",1,7,15)*


*licensed under GNU General Public License v3.0*
