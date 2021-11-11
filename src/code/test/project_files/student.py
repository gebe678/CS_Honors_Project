# This class will hold information about the students classes
class Student:

    def __init__(self):
        self.intial_classes = []
        self.registration_classes = []
        
        self.student_id = 0

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
