from django.core.management.base import BaseCommand
from core.models import FrameworkParameter
DATA={
'A':('Academic Performance & Learning Outcomes',300,[('+2 Academic Performance',20),('CIA Performance',60),('SEE Performance',70),('Attendance & Academic Discipline',30),('Course Outcome Attainment',50),('Academic Progression',50),('Remedial & Advanced Learning',20)]),
'B':('Technical Skills & Experiential Learning',200,[('Engineering Exploration (After IV Semester)',40),('Course-Based Projects',30),('Capstone / Final Year Project',50),('Technical Skills Assessment',30),('Programming & Digital Skills',20),('ODL / Self-Learning',10),('Hackathons & Technical Competitions',20)]),
'C':('Industry Exposure & Professional Development',200,[('Internship',50),('Industry Certification',30),('Industry Interaction',20),('Placement Readiness',40),('Communication Skills',20),('Career Development',20),('Entrepreneurship & Startup Initiatives',20)]),
'D':('Research, Innovation & Intellectual Development',150,[('Student Publications',30),('Paper Presentations',20),('Innovation & IIC Activities',30),('Intellectual Property',20),('Research Projects',30),('Problem-Solving & Design Thinking',20)]),
'E':('Co-Curricular & Professional Engagement',80,[('Domain Club Participation',20),('Professional Society Engagement',10),('Peer Teaching & Mentoring',10),('Leadership & Teamwork',20),('Awards & Recognitions',20)]),
'F':('Social, Cultural & Holistic Development',70,[('NSS Activities',10),('Extension & Outreach Activities',10),('Sports',10),('Cultural Activities',10),('Student Well-Being & Life Skills',20),('Environmental Responsibility',10)])}
class Command(BaseCommand):
    help='Load ACE 1000-point Student Performance Framework'
    def handle(self,*args,**kwargs):
        count=0
        for code,(cat,catmax,params) in DATA.items():
            for name,mx in params:
                FrameworkParameter.objects.update_or_create(category_code=code,name=name,defaults={'category_name':cat,'category_max':catmax,'max_points':mx});count+=1
        self.stdout.write(self.style.SUCCESS(f'Framework loaded: {count} parameters'))
