from src.data.data_loader import load_jobs
from src.nlp.skill_extractor import extract_skills


def main():

    jobs = load_jobs()

    print("=" * 70)
    print("JOB DESCRIPTION SKILL EXTRACTION")
    print("=" * 70)

    for _, job in jobs.iterrows():

        extracted = extract_skills(job["description"])

        print(f"\nJob ID      : {job['job_id']}")
        print(f"Job Title   : {job['job_title']}")
        print(f"Company     : {job['company']}")

        print("Skills      :")

        for skill in extracted:
            print(f"  ✓ {skill}")

        print(f"Total Skills: {len(extracted)}")


if __name__ == "__main__":
    main()