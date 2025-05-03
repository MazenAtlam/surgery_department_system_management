from datetime import date, datetime, time

import app.models as m
from app import db


def init_db():
    """
    Initialize the database with sample data including roles, users, and phone numbers.
    """
    try:
        # Create roles first (since users depend on them)
        roles = [
            m.Role(name="admin"),
            m.Role(name="doctor"),
            m.Role(name="patient"),
        ]

        # Create a default profile picture
        default_pic = m.UploadedFile(
            file_name="default.png",
            file_type="images/png",
            file_url="https://btvfedqvariqcbjbissj.supabase.co/storage/v1/object/sign/images/default.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5Xzk5MTZiOTRmLTAxODktNDJlMi1iNWMwLWE0NmI4NTk1ZWNmZiJ9.eyJ1cmwiOiJpbWFnZXMvZGVmYXVsdC5wbmciLCJpYXQiOjE3NDYyNzI5MDksImV4cCI6MTc3NzgwODkwOX0.1MZwjbv3q3x_e7iNellhDFHkMgrHnTZUi4fKK5f3fGo",
        )
        db.session.add(default_pic)

        # Create sample users
        users = [
            m.User(
                name="Mazen Atef",
                gender="M",
                ssn="30409181700653",
                dob=date(2004, 9, 18),
                email="mazen1@gmail.com",
                password="admin1",
                role=roles[0],  # admin role
                pic=default_pic,
            ),
            m.User(
                name="Sherif Elgendy",
                gender="M",
                ssn="30404161765891",
                dob=date(2004, 9, 18),
                email="sherif2@gmail.com",
                password="admin2",
                role=roles[0],  # admin role
                pic=default_pic,
            ),
            m.User(
                name="Anas Elshiekh",
                gender="M",
                ssn="30408195158955",
                dob=date(2004, 8, 19),
                email="anas3@gmail.com",
                password="admin3",
                role=roles[0],  # admin role
                pic=default_pic,
            ),
            m.User(
                name="Ahmed Shehab",
                gender="M",
                ssn="30601012528266",
                dob=date(2006, 1, 1),
                email="ahmed3@gmail.com",
                password="admin4",
                role=roles[0],  # admin role
                pic=default_pic,
            ),
            m.User(
                name="Mostafa Ashraf",
                gender="M",
                ssn="30410021736516",
                dob=date(2004, 10, 2),
                email="mostafa5@gmail.com",
                password="admin5",
                role=roles[0],  # admin role
                pic=default_pic,
            ),
            m.User(
                name="Ahmed Hesham",
                gender="M",
                ssn="27505151354545",
                dob=date(1975, 5, 15),
                email="admin0@example.com",
                password="admin0",
                role=roles[0],  # doctor role
                pic=default_pic,
            ),
            m.User(
                name="Abdallah Darwish",
                gender="M",
                ssn="29806091725826",
                dob=date(1998, 6, 9),
                email="doctor0@example.com",
                password="doctor0",
                role=roles[1],  # doctor role
                pic=default_pic,
            ),
            m.User(
                name="Omar Hesham",
                gender="M",
                ssn="29811101721256",
                dob=date(1998, 11, 10),
                email="doctor1@example.com",
                password="doctor1",
                role=roles[1],  # doctor role
                pic=default_pic,
            ),
            m.User(
                name="Gamal Ashraf",
                gender="M",
                ssn="30350159871615",
                dob=date(2000, 10, 20),
                email="patient0@example.com",
                password="patient0",
                role=roles[2],  # patient role
                pic=default_pic,
            ),
            m.User(
                name="Jana Ahmed",
                gender="F",
                ssn="30350676528615",
                dob=date(1982, 10, 20),
                email="patient1@example.com",
                password="patient1",
                role=roles[2],  # patient role
                pic=default_pic,
            ),
            m.User(
                name="Sama Abdelrahman",
                gender="F",
                ssn="30350675612345",
                dob=date(2010, 10, 20),
                email="patient2@example.com",
                password="patient2",
                role=roles[2],  # patient role
                pic=default_pic,
            ),
        ]

        # Add all objects to session
        db.session.add_all(roles)
        db.session.add_all(users)

        db.session.commit()

        phone_numbers = [
            m.PhoneNumber(number="01095728825", user_id=users[0].id),
            m.PhoneNumber(number="01282952786", user_id=users[1].id),
            m.PhoneNumber(number="01101778044", user_id=users[2].id),
            m.PhoneNumber(number="01274316669", user_id=users[3].id),
            m.PhoneNumber(number="01288314896", user_id=users[4].id),
            m.PhoneNumber(number="01000089124", user_id=users[5].id),
            m.PhoneNumber(number="01225864595", user_id=users[6].id),
            m.PhoneNumber(number="01111125628", user_id=users[7].id),
            m.PhoneNumber(number="01515153658", user_id=users[8].id),
            m.PhoneNumber(number="01025689124", user_id=users[8].id),
        ]

        # Create Surgery Department
        surgery_dept = m.Department(
            department_name="Surgery", department_location="First Floor"
        )

        db.session.add_all(phone_numbers)
        db.session.add(surgery_dept)

        db.session.commit()

        # Create Admin Records
        admins = [
            m.Admin(
                is_superadmin=True,
                user_id=users[5].id,
            ),
            m.Admin(
                is_superadmin=False,
                user_id=users[0].id,
            ),
            m.Admin(
                is_superadmin=False,
                user_id=users[1].id,
            ),
            m.Admin(
                is_superadmin=False,
                user_id=users[2].id,
            ),
            m.Admin(
                is_superadmin=False,
                user_id=users[3].id,
            ),
            m.Admin(
                is_superadmin=False,
                user_id=users[4].id,
            ),
        ]

        doctors = [
            m.Doctor(
                years_of_experience=10,
                salary=11000,
                date_of_hire=date(2018, 11, 10),
                major="جراحة الكبد والبنكرياس والقنوات الصفراوية",
                department_id=surgery_dept.id,
                user_id=users[6].id,
            ),
            m.Doctor(
                years_of_experience=12,
                salary=13000,
                date_of_hire=date(2013, 11, 10),
                major="جراحة الغدد الصماء",
                department_id=surgery_dept.id,
                user_id=users[7].id,
            ),
        ]

        patients = [
            m.Patient(
                blood_type=m.BloodType.O_POS.value,
                user_id=users[8].id,
            ),
            m.Patient(
                blood_type=m.BloodType.A_NEG.value,
                user_id=users[9].id,
            ),
            m.Patient(
                user_id=users[10].id,
            ),
        ]

        db.session.add_all(admins)
        db.session.add_all(doctors)
        db.session.add_all(patients)

        db.session.commit()

        # Create working slots for the doctor
        working_slots = [
            m.WorkingSlot(
                doctor=doctors[0],
                day=m.DayOfWeek.SATURDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
            m.WorkingSlot(
                doctor=doctors[0],
                day=m.DayOfWeek.SUNDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
            m.WorkingSlot(
                doctor=doctors[0],
                day=m.DayOfWeek.MONDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
            m.WorkingSlot(
                doctor=doctors[1],
                day=m.DayOfWeek.TUESDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
            m.WorkingSlot(
                doctor=doctors[1],
                day=m.DayOfWeek.WEDNESDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
            m.WorkingSlot(
                doctor=doctors[1],
                day=m.DayOfWeek.THURSDAY.value,
                start_time=time(8, 0),
                end_time=time(16, 0),
            ),
        ]

        rooms = [
            m.Room(
                room_location="31001",
                department=surgery_dept,
            ),
            m.Room(
                room_location="31002",
                department=surgery_dept,
            ),
            m.Room(
                room_location="31003",
                department=surgery_dept,
            ),
            m.Room(
                room_location="31004",
                department=surgery_dept,
            ),
            m.Room(
                room_location="31005",
                department=surgery_dept,
            ),
        ]

        db.session.add_all(rooms)
        db.session.add_all(working_slots)

        db.session.commit()

        medical_devices = [
            m.MedicalDevice(
                medical_device_name="أجهزة التخدير",
                room_id=rooms[0].id,
                medical_device_price=120000,
                medical_device_state="Active",
            ),
            m.MedicalDevice(
                medical_device_name="(BIS) جهاز مراقبة عمق التخدير",
                room_id=rooms[0].id,
                medical_device_price=230000,
                medical_device_state="Active",
            ),
            m.MedicalDevice(
                medical_device_name="طاولات العمليات",
                room_id=rooms[1].id,
                medical_device_price=10000,
                medical_device_state="Active",
            ),
            m.MedicalDevice(
                medical_device_name="شفاطات جراحية",
                room_id=rooms[2].id,
                medical_device_price=130000,
                medical_device_state="Active",
            ),
            m.MedicalDevice(
                medical_device_name="طاولات العمليات",
                room_id=rooms[4].id,
                medical_device_price=10000,
                medical_device_state="In maintenance",
            ),
        ]

        dependents = [
            m.Dependent(
                patient_id=patients[1].id,
                dependent_name="Farah Ahmed",
                dependent_phone_number="01245678900",
                relationship="أخت",
            ),
            m.Dependent(
                patient_id=patients[1].id,
                dependent_name="Faris Amir",
                dependent_phone_number="01045678900",
                relationship="الزوج",
            ),
            m.Dependent(
                patient_id=patients[2].id,
                dependent_name="Abdelrahman Agour",
                dependent_phone_number="01545678900",
                relationship="الأب",
            ),
        ]

        medical_histories = [
            m.MedicalHistory(
                patient_id=patients[0].id,
                disease_name="السمنة",
            ),
            m.MedicalHistory(
                patient_id=patients[1].id,
                family_history=True,
                disease_name="البول السكري",
            ),
            m.MedicalHistory(
                patient_id=patients[1].id,
                family_history=False,
                disease_name="الضغط",
            ),
        ]

        appointments = [
            m.Appointment(
                patient_id=patients[0].id,
                doctor_id=doctors[0].id,
                appointment_date_time=datetime.now(),
                room_id=rooms[4].id,
                file_id=default_pic.id,
            ),
            m.Appointment(
                patient_id=patients[0].id,
                doctor_id=doctors[1].id,
                appointment_date_time=datetime.now(),
                room_id=rooms[1].id,
            ),
            m.Appointment(
                patient_id=patients[1].id,
                doctor_id=doctors[1].id,
                appointment_date_time=datetime.now(),
                room_id=rooms[1].id,
            ),
        ]

        db.session.add_all(appointments)
        db.session.add_all(dependents)
        db.session.add_all(medical_devices)
        db.session.add_all(medical_histories)

        # Commit the changes
        db.session.commit()

        print("Database initialized successfully with sample data.")

    except Exception as e:
        db.session.rollback()
        print(f"Error initializing database: {str(e)}")
        raise
