import json
#file_path = "students.json"

class Student: #model info sv
    def __init__(self, student_id , full_name , age , sex,):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.sex = sex

    def to_dict(self): #return 1 object sv
        return {
            "student_id":self.student_id,
            "full_name":self.full_name,
            "age" :self.age,
            "sex" : self.sex
        }

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self , student):
        self.students.append(student)

    def display_student(self):
        for item in self.students:
            print(f"{item.student_id} - {item.full_name} - {item.age} - {item.sex}")

    def find_student_by_name(self , keyword):
        return [s for s in self.students if keyword.lower() == s.full_name.lower()]

    def delete_student(self, student_id):
        # self.student.pop(student_id)
        self.students = [s for s in self.students if s.student_id != student_id]

    def save_to_file(self, filename="students.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]
        except FileNotFoundError:
            print("Chưa có dữ liệu, bắt đầu mới.")

def menu():
    print("=== Student Management System ===")
    print("1. Thêm học sinh")
    print("2. Xem danh sách học sinh")
    print("3. Tìm kiếm học sinh")
    print("4. Xóa học sinh")
    print("5. Lưu dữ liệu")
    print("6. Thoát")

def main():
    manager = StudentManager()
    manager.load_from_file()

    while True:
        menu()
        choice = input('Chon chuc nang: ')

        if choice == "1":
            student_id = input('Student Id: ')
            full_name = input('Full name: ')
            age = input('Age: ')
            sex = input('Sex: ')
            student = Student(student_id, full_name, age, sex)
            manager.add_student(student)
        elif choice == "2":
            manager.display_student()
        elif choice =="3":
            keyword = input('Nhap ma sinh vien: ')
            result = manager.find_student_by_name(keyword)
            for s in result:
                print(f"{s.student_id} - {s.name} - {s.age} - {s.grade}")
        elif choice == "4":
            student_id = input('Nhap Id sinh vien can xoa: ')
            manager.delete_student(student_id)
        elif choice == "5":
            manager.save_to_file()
        elif choice == "6":
            break
        else:
            print("Lựa chọn không hợp lệ.")

main()





