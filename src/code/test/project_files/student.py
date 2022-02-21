from class_registration import Registration

# This class will hold information about the students classes
class Student:

    def __init__(self):
        self.intial_classes = []
        self.registration_classes = []
        
        self.student_id = 0
        self.term = 0

    ######################################################################################################################################################################################
    # GETTERS AND SETTERS #

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_initial_classes(self, initial_classes):
        self.initial_classes = initial_classes

    def set_registered_classes(self, registration_classes):
        self.registration_classes = registration_classes

    def add_classes(self, initial_classes, registration_classes):
        # get the intial class schedule and new class schedule and add it to the class variables
        self.initial_classes = initial_classes
        self.registration_classes = registration_classes

    def get_initial_classes(self):
        return self.initial_classes

    def get_registration_classes(self):
        return self.registration_classes

    def get_student_id(self):
        return self.student_id

    def set_term(self, term):
        self.term = term

    def get_term(self):
        return self.term

    #####################################################################################################################################################################################

    def calculate_dropped_classes(self):
        """
        This function is resonsible for finding out how many classes this student dropped
        """

        num_classes_dropped = 0

        for initial_class in self.initial_classes:

            if initial_class not in self.registration_classes:
                num_classes_dropped += 1
        
        return num_classes_dropped

    def calculate_faculity_chosen_classes(self, rcc_analysis):

        registration_classes = self.registration_classes
        initial_classes = self.initial_classes

        if not rcc_analysis:
            for course in initial_classes:
                assert isinstance(course, Registration), "Expected a registration object"

                if course.get_subject_code() == "RCC":
                    initial_classes.remove(course)

                for course in registration_classes:
                    assert isinstance(course, Registration), "Expected a registration object"

                if course.get_subject_code() == "RCC":
                    initial_classes.remove(course)

        num_classes_chosen = 0
        num_classes = len(registration_classes)

        for reg_class in registration_classes:
            assert isinstance(reg_class, Registration), "Expected a registration object"

            if reg_class in initial_classes:
                num_classes_chosen += 1

        return num_classes_chosen / num_classes

    def calculate_kept_class_percentage(self, rcc_analysis):
        """
        This function is responsible for finding out what percentage of classes this student kept
        """
        initial_classes = self.initial_classes
        registration_classes = self.registration_classes

        # remove the rcc courses from the lists if they are not supposed to be analyized
        if not rcc_analysis:
            for course in initial_classes:
                assert isinstance(course, Registration), "Expected a registration object"

                if course.get_subject_code() == "RCC":
                    initial_classes.remove(course)

            for course in registration_classes:
                assert isinstance(course, Registration), "Expected a registration object"

                if course.get_subject_code() == "RCC":
                    registration_classes.remove(course)

        # get the total courses after chosen analysis type
        total_courses = len(initial_classes)
        total_kept_courses = 0

        if total_courses == 0:
            return 0

        for course in initial_classes:
            if course in registration_classes:
                total_kept_courses += 1

        return total_kept_courses / total_courses

    def calculate_credit_hours_pre(self):
        num_credit_hours = 0
        initial_classes = self.initial_classes
        
        for course in initial_classes:
            assert isinstance(course, Registration), "Expected a registration object"

            num_credit_hours += float(course.get_credit_hours())

        return num_credit_hours

    def calculate_credit_hours_post(self):
        num_credit_hours = 0

        for course in self.registration_classes:
            assert isinstance(course, Registration), "Expected a registration object"

            num_credit_hours += float(course.get_credit_hours())

        return num_credit_hours

    def get_registered_classes(self):
        return len(self.initial_classes)

    def get_dropped_class_subject_code(self):
        
        dropped_classes_subject_code = []

        for course in self.initial_classes:

            if course not in self.registration_classes:
                dropped_classes_subject_code.append(course.get_subject_code())

        return dropped_classes_subject_code


    def get_added_class_subject_code(self):

        added_classes_subject_code = []

        for course in self.registration_classes:

            if course not in self.intial_classes:
                added_classes_subject_code.append(course.get_subject_code())

        return added_classes_subject_code


