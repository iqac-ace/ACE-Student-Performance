from decimal import Decimal

def performance_level(spi):
    x=float(spi or 0)
    if x>=900:return 'Exceptional'
    if x>=750:return 'Excellent'
    if x>=600:return 'Good'
    if x>=400:return 'Developing'
    return 'Needs Improvement'

def student_spi(student):
    approved = student.activities.filter(status='IQAC_APPROVED')
    by_cat={}
    for a in approved.select_related('parameter'):
        code=a.parameter.category_code
        by_cat[code]=by_cat.get(code,Decimal('0'))+a.points
    caps={'A':300,'B':200,'C':200,'D':150,'E':80,'F':70}
    scores={k:min(Decimal(str(v)), by_cat.get(k,Decimal('0'))) for k,v in caps.items()}
    total=sum(scores.values(),Decimal('0'))
    return scores,total,performance_level(total)
