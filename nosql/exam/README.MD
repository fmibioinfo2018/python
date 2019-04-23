# Проект
Да се разработи **RESTFul** приложение на Python (по желание може и друг език), което да оперира върху предварително интегрирани следните данни: 
- clinical.cart.2019-02-13.tar.gz - съдържа клинични записи на пациенти във TSV формат.
- gdc_sample_sheet.2019-02-08.tsv - съдържа връзка между всеки пациент и CNV файл. Във всеки файл от clinical.cart.2019-02-13.tar.gz има поле submitter_id това поле отговаря на полето Case ID от файла gdc_sample_sheet.2019-02-08.tsv.
- cnv_segments_download_20190209.tar.gz - съдържа всички данни за Copy Number Variants - полето File ID от gdc_sample_sheet.2019-02-08.tsv отговаря на папка от архива cnv_segments_download_20190209.tar.gz.
Изтеглете файловете и ги запишете
Задачата за всички е тези данни да се ИНТЕГРИРАТ (Data integration)
След интегрирането на данните трябва да са изпълнени следните изисквания.
Да има ясно разделенение между обеkти и връзки - да бъдат в отделни таблици/колекции.
Препоръчително е да се използват NoSQL бази от данни.

### Възможен вариант за избор на бази от данни:
* Може се използва Neo4j базата от данни, за да се съхраняват в нея релацийте между обектите.
* Може се използва MongoDB за запис на всичките атрибути на обектите.
# RESTFul приложение
RESTFul приложението трябва да има следните входни точки:
- ``` /v1/patients/case_id/relations?skip=10&fetch=10 ``` 
> HTTP GET метод, който да връща като информация релациите, които са за конкретният пациент с ID case_id. Параметрките **skip** и **fetch** показват съответно бойката, от релации, която трябва да се прескочи и бойката от релации, която трябва да се върне. Във връщаният отговор трябва да се съдържа и колко е общата бройка на релацийте за пациент с ID case_id.

- ``` /v1/patients ```
> HTTP GET метод, който трябва да връща пациентите, който са интегрирани в базите от данни. Отговорът трябва да има минимум следните атрибути показани в приемрният JSON: 
```json
{ 
"morphology": "8500/3",
"ethnicity": "not hispanic or latino",
"vital_status": "alive",
"race": "american indian or alaska native",
"gender": "female",
"submitter_id": "TCGA-A2-A0T1",
"tumor_stage": "stage iiic",
"days_to_birth": "-20227.0",
"last_known_disease_status": "not reported",
"year_of_birth": "1954",
"tissue_or_organ_of_origin": "Breast, NOS",
"days_to_last_follow_up": "521.0",
"primary_diagnosis": "Infiltrating duct carcinoma, NOS",
"age_at_diagnosis": "20227",
"classification_of_tumor": "not reported",
"project_id": "TCGA-BRCA",
"prior_malignancy": "not reported",
"case_id": "02bed00f-bef7-4fb7-b243-540354990e45",
"site_of_resection_or_biopsy": "Breast, NOS",
"tumor_grade": "not reported",
"progression_or_recurrence": "not reported"
}
```

- ``` /v1/patients/case_id/proteins?skip=10&fetch=10``` 
>HTTP GET метод, който трябва да връща протеините към, който има релация избраният пациент с ID case_id. Параметрите **skip** и **fetch** показват съответно бойката, от протеини, която трябва да се прескочи и бойката от протеини, която трябва да се върне. Във връщаният отговор трябва да се съдържа и колко е общата бройка на протеини за пациент с ID case_id.

# Вариант 1:

Да се реализират допълнително следните точки за достъп:
- ```/v1/patients/case_id/proteins?attribute=value``` 
> HTTP GET метод, който да връща всички протеини,който са свързани с посочения пациент с ID case_id и имат като параметър **"attribute"** със стойност **"value"**

Пример:
```http 
/v1/patients/case_id/proteins?number=772
```

- ```/v1/patients?attribute=value&attribute=value``` 
> HTTP GET метод, който връща всички пациенти, който имат  **"attribute"** със стойност **"value"**

Пример:
```http
/v1/patients?project_id=TCGA-BRCA&age_at_diagnosis=20227
```

# Вариант 2
Да се реализират допълнително следните точки за достъп:

- ```/v1/patients/case_id/proteins``` 
> HTTP PUT метод, който да добавя нови протеини към съществуващите за конкретният пациент с ID case_id. Примерно съдържание на заявката:
```json
{
"case_id": "00331c0a-23f0-4724-9c0f-5e37f971f26f",
"number": "2550",
"ENSG": "ENSG00000000003.13"
}
```
Да се добави валидация на полето ENSG ако вече съществува такъв запис да не се добавя отново, а като резултат да се връща HTTP Response **Bad Request**

# Вариант 3
Да се реализират допълнително следните точки за достъп:

- ```/v1/patients```
> HTTP PUT метод, който тряbва да добавя нов пациент в бата/ите от данни. Като body на заявката трябва да се приемат следните атрибути показани в примерният JSON:
```json
{
"morphology": "8500/3",
"ethnicity": "not hispanic or latino",
"vital_status": "alive",
"race": "american indian or alaska native",
"gender": "female",
"submitter_id": "TCGA-A2-A0T1",
"tumor_stage": "stage iiic",
"days_to_birth": "-20227.0",
"last_known_disease_status": "not reported",
"year_of_birth": "1954",
"tissue_or_organ_of_origin": "Breast, NOS",
"days_to_last_follow_up": "521.0",
"primary_diagnosis": "Infiltrating duct carcinoma, NOS",
"age_at_diagnosis": "20227",
"classification_of_tumor": "not reported",
"project_id": "TCGA-BRCA",
"prior_malignancy": "not reported",
"case_id": "02bed00f-bef7-4fb7-b243-540354990e45",
"site_of_resection_or_biopsy": "Breast, NOS",
"tumor_grade": "not reported",
"progression_or_recurrence": "not reported"
}
```

# Вариант 4
Към интегрираните данни да се добавят и данните за афускираните Copy Number Variants от архива - **masked_cnv_segments_download_20190209.tar.gz**

Свързващото поле File ID отново се намира във gdc_sample_sheet.2019-02-08.tsv и то отговаря на папка от архива masked_cnv_segments_download_20190209.tar.gz
