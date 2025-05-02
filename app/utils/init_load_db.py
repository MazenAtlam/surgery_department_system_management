from datetime import datetime

import app.models as m


def init_load_db(db):
    db_changed = False
    roles = ["Patient", "Admin", "Doctor"]
    for role in roles:
        if not m.Role.query.filter_by(name=role).first():
            new_role = m.Role(name=role)
            db.session.add(new_role)
            db_changed = True

    admin_role_id = m.Role.query.filter_by(name="Admin").first().id
    admins = [
        {
            "email": "mazenatef5510@gmail.com",
            "password": "10",
            "name": "Mazen Atef",
            "ssn": "30409181700653",
            "gender": "M",
            "dob": datetime.strptime("18-9-2004", "%d-%m-%Y").date(),
            "role_id": admin_role_id,
            "is_superadmin": True,
        },
    ]
    # for admin in admins:
    #     if not m.Admin.query.filter_by(email=admin["email"]).first(): # get the admin from user table
    #         is_superadmin: bool = (
    #             admin["is_superadmin"] if "is_superadmin" in admin.keys() else False
    #         )
    #         new_admin = m.Admin(is_superadmin=is_superadmin)
    #         db.session.add(new_admin)
    #
    #         new_user = m.User(
    #             email=admin["email"],
    #             password=admin["password"],
    #             name=admin["name"],
    #             ssn=admin["ssn"],
    #             gender=admin["gender"],
    #             dob=admin["dob"],
    #             role_id=admin["role_id"],
    #             admin_id=new_admin.id,
    #         )
    #         db.session.add(new_user)
    #         db_changed = True

    if db_changed:
        db.session.commit()
