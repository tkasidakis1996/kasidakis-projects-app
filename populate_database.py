from sqlmodel import Session, SQLModel, create_engine

from data_layer.projects_database.tables import Project

from datetime import date


# Sample data
projects = [
    Project(
        name="Coni Report",
        description="A conflict of interest analysis tool for business networks.",
        technologies_used="Python, FastAPI, MongoDB",
        start_date=date(2023, 11, 13),
        end_date=date(2024, 3, 29)
    ),
    Project(
        name="Battery Station Management System",
        description="A system for managing battery stations with microservices for both field and cloud environments. The system prototype served as a foundation for a future production-based system.",
        technologies_used="Python, Flask, gRPC, MongoDB, RabbitMQ, pytest, MariaDB, PostgreSQL, Raspberry Pi",
        start_date=date(2022, 4, 1),
        end_date=date(2022, 12, 31)
    ),
    Project(
        name="Edge Computing for Drones",
        description="An implementation of a software stack for mission execution on autonomous drones, with transparent support for task offloading. Evaluated using both a HITL/SITL setup and a simulation.",
        technologies_used="Python, UDP/IP Sockets, TCP/IP Sockets, ArduPilot,Dronekit, Linux Containers (LXDs), Pyro4, OpenCV, YOLOv3, Raspberry Pi, ns-3",
        start_date=date(2020, 9, 1),
        end_date=date(2021, 6, 30)
    )
]

engine = create_engine("sqlite:///data_layer/projects_database/projects_database.db")


SQLModel.metadata.create_all(engine)

with Session(engine) as session:

    for project in projects:

        session.add(project)
        
        session.commit()
