# Data-sensitivity-and-privilege-levels

Assigned problem.

Write a program using python to carry out medical data processing as follows:

    1. Program writes into and reads from a configuration file the following parameters: user
    names, hashes of passwords (MD5), user type (patient or hospital staff category),
    privilege level of each user name
    2. Program writes into and reads from a data file the following data records: personal
    details, sickness details, drug prescriptions, and lab test prescriptions, each data record is
    associated with a privilege level depending on its sensitivity.
    3. Each data record is due to an encounter with a patient
    4. Hospital staff can read or write data based on sensitivity level


Description

In this medical data processing program, I implemented 5 kinds of users as Doctors, Nurses,
Pharmacists, Lab assistants and patients. All have different privilege levels. Doctor have the
highest privilege and the patient have the lowest.


                            User                Privilege Number
                            Doctor                     1
                            Nurse                      2
                            Pharmacist                 3
                            Lab Assistant              4
                            Patient                    5


Lower privilege number is associated with the high privileged user. The data records are accessed
by the users according to that privilege number.

First, all the user details are stored in configuration file. In here passwords are encrypted with md5 encryption which is a one way data encryption.

Data are stored in data.json file.

When doctor encounters a patient, doctor takes all the information regarding the patient and
records them in the data file (data.json). At that instance, doctor creates an account for the patient also. So doctor has privilege to write data in to the data file. As the doctors are highest privileged users, they can access all the data records in the data file (data.json). Doctors can also read all the details of the patients.

Nurses only can read the sickness details, drug prescriptions and lab test prescriptions. When
nurse wants to see those details, they can enter patient id and read the accessible records. They
can’t access to the personal details of the patient.

Pharmacists only can drug details of the patient. They cannot access other details of the patient.
When they want to give medicine according to prescriptions, they can access drug prescription
details by entering patient id. At the encountering of patient by the doctor, doctor set the status of the drug details to “Not Given”. So, after pharmacist given the medicines to the patient, he/she
updates the status of the drug details to “Given”. Then doctors and nurses can check whether drugs
are given to the patient. So pharmacist have access to read and write data. But very limited

Lab assistants can only access the lab test prescription details of a particular patient by entering
the patient id. Like pharmacists can do, lab assistants also can update the status of the lab test
prescription details “Lab test done!” Then doctors and nurses can check whether lab test is done
for a particular patient. So, lab assistants have ability to read and write access, but very limited.
Patients are the lowest privileged users in this system. They only can access to their own details.
They can’t access any other record. 