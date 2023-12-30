import sqlalchemy
from sqlalchemy import create_engine, text, values
import os

db_connonection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connonection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result:
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


# def add_application_to_db(job_id, data):
#   with engine.connect() as conn:
#     query = text(
#         "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
#     )

#     # Check if all keys in 'data' exist
#     expected_keys = [
#         'full_name', 'email', 'linkedin_url', 'education', 'work_experience',
#         'resume_url'
#     ]
#     if not all(key in data for key in expected_keys):
#       raise ValueError("Missing keys in data dictionary")

#     # Make sure the keys match the column names exactly
#     conn.execute(
#         query,
#         job_id=job_id,
#         **data  # Pass the dictionary directly to unpack its values
#     )
