# CS_Honors_Project
Honors Research Project Rollins Year 4

## Completed statistics log

1. Percentage of classes dropped

This was calculated by ...

2. Percentage of classes kept

This was calculated by ...

## Error log

Found issue with the student classes. I was not taking into account what term each class was for and ended up using a crn from the 2017 year to calculate the 2018 school year. I fixed this issue by adding the (crn,termcode) touple as the key for the courses so a student in the 201709 term would not get assigned classes from the 201809 term.