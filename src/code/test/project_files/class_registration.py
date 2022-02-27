# this class will hold class information

class Registration:

    def __init__(self):
        self.crn_key = 0
        self.subject_code = 0
        self.course_number = 0
        self.section_number = 0
        self.credit_hours = 0
        self.course_year = 0
        self.competency = 0

    ######################################################################################################################################################################################
    # GETTERS AND SETTERS #

    def get_term_code(self):
        return self.term_code

    def set_term_code(self, term_code):
        self.term_code = term_code

    def get_crn_key(self):
        return self.crn_key

    def set_crn_key(self, crn_key):
        self.crn_key = crn_key

    def get_subject_code(self):
        return self.subject_code

    def set_subject_code(self, subject_code):
        self.subject_code = subject_code

    def get_course_number(self):
        return self.course_number

    def set_course_number(self, course_number):
        self.course_number = course_number

    def get_section_number(self):
        return self.section_number

    def set_section_number(self, section_number):
        self.section_number = section_number

    def get_credit_hours(self):
        return self.credit_hours

    def set_credit_hours(self, credit_hours):
        self.credit_hours = credit_hours

    def get_competency(self):
        return self.competency

    def set_competency(self, competency):
        self.competency = competency

    #####################################################################################################################################################################################

    def print_course_information(self):
        print("term code: ", self.get_term_code())
        print("crn key: ", self.get_crn_key())
        print("subject code: ", self.get_subject_code())
        print("course number: ", self.get_course_number())
        print("section number: ", self.get_section_number())
        print("credit hours: ", self.get_credit_hours())
        print("competency: ", self.get_competency())