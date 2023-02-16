class PRint:
    name = 'Sardor'
    def set_name(self,passed_value):
        self.name = passed_value

    def display(self):
        print(self.name)



student = PRint()
student.set_name("sardor")
student.display()


text = 'sardor is th best'
print(text.find('sard'))
