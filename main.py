class ResumeScreener:
    def __init__(self):
        self.resumes = []
        self.skills = []

    def load_resumes(self, resume_files):
        """ Load resumes from the given file paths."""
        for file in resume_files:
            with open(file, 'r') as f:
                self.resumes.append(f.read())

    def extract_skills(self, resume):
        """ Extract skills from a single resume."
        # Placeholder for skill extraction logic
        return [skill.strip() for skill in resume.split() if skill.isalpha()]

    def calculate_match_score(self, resume_skills):
        """ Calculate match score based on extracted skills and required skills."
        match_score = len(set(resume_skills) & set(self.skills))
        return match_score

    def screen_resumes(self, required_skills):
        """ Screen resumes against a list of required skills and return matches."
        self.skills = required_skills
        matches = []
        for resume in self.resumes:
            resume_skills = self.extract_skills(resume)
            score = self.calculate_match_score(resume_skills)
            matches.append((resume, score))
        return sorted(matches, key=lambda x: x[1], reverse=True)
