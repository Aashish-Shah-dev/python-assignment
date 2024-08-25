import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.attendance = []

    def add_attendance(self, date, status):
        self.attendance.append((date, status))

    def view_attendance(self):
        if not self.attendance:
            return "No attendance records found."
        return "\n".join([f"Date: {date}, Status: {status}" for date, status in self.attendance])


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("CLASS TRACK")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.students = {}
        self.notices = []  # Initialize notices list
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.current_user = None

        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="CLASS TRACK", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        login_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        login_frame.pack(pady=10)

        user_type_label = tk.Label(login_frame, text="Select User Type:", font=("Arial", 12, "bold"), bg="#fff")
        user_type_label.grid(row=0, column=0, pady=10)

        self.user_type = tk.StringVar()
        admin_rb = tk.Radiobutton(login_frame, text="Admin", variable=self.user_type, value="admin", font=("Arial", 10), bg="#fff")
        student_rb = tk.Radiobutton(login_frame, text="Student", variable=self.user_type, value="student", font=("Arial", 10), bg="#fff")
        admin_rb.grid(row=0, column=1, pady=10)
        student_rb.grid(row=0, column=2, pady=10)

        username_label = tk.Label(login_frame, text="Username/Student ID:", font=("Arial", 12, "bold"), bg="#fff")
        username_label.grid(row=1, column=0, pady=10)
        self.username_entry = tk.Entry(login_frame, font=("Arial", 12), width=20)
        self.username_entry.grid(row=1, column=1, columnspan=2, pady=10)

        password_label = tk.Label(login_frame, text="Password (Admin only):", font=("Arial", 12, "bold"), bg="#fff")
        password_label.grid(row=2, column=0, pady=10)
        self.password_entry = tk.Entry(login_frame, show='*', font=("Arial", 12), width=20)
        self.password_entry.grid(row=2, column=1, columnspan=2, pady=10)

        login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), bg="#4CAF50", fg="#fff", command=self.login)
        login_button.grid(row=3, column=0, columnspan=3, pady=20)

    def login(self):
        user_type = self.user_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if user_type == "admin":
            if self.authenticate_admin(username, password):
                self.current_user = "admin"
                self.admin_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid admin credentials.")
        elif user_type == "student":
            if self.authenticate_student(username):
                self.current_user = username
                self.student_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid student ID.")
        else:
            messagebox.showerror("Login Failed", "Please select a user type.")

    def authenticate_admin(self, username, password):
        return username == self.admin_username and password == self.admin_password

    def authenticate_student(self, student_id):
        return student_id in self.students

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def admin_menu(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Admin Menu", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        menu_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        menu_frame.pack(pady=10)

        add_student_button = tk.Button(menu_frame, text="Add Student", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.add_student_screen)
        add_student_button.grid(row=0, column=0, pady=10, padx=20)

        view_student_button = tk.Button(menu_frame, text="View Student", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.view_student_screen)
        view_student_button.grid(row=1, column=0, pady=10, padx=20)

        delete_student_button = tk.Button(menu_frame, text="Delete Student", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.delete_student_screen)
        delete_student_button.grid(row=2, column=0, pady=10, padx=20)

        list_students_button = tk.Button(menu_frame, text="List Students", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.list_students_screen)
        list_students_button.grid(row=3, column=0, pady=10, padx=20)

        record_attendance_button = tk.Button(menu_frame, text="Record Attendance", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.record_attendance_screen)
        record_attendance_button.grid(row=4, column=0, pady=10, padx=20)

        add_notice_button = tk.Button(menu_frame, text="Add Notice", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.add_notice_screen)
        add_notice_button.grid(row=5, column=0, pady=10, padx=20)

        logout_button = tk.Button(menu_frame, text="Logout", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.logout)
        logout_button.grid(row=6, column=0, pady=10, padx=20)

    def student_menu(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Student Menu", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        menu_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        menu_frame.pack(pady=10)

        view_details_button = tk.Button(menu_frame, text="View My Details", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.view_my_details)
        view_details_button.pack(pady=10)

        view_attendance_button = tk.Button(menu_frame, text="View My Attendance", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.view_my_attendance)
        view_attendance_button.pack(pady=10)

        view_notices_button = tk.Button(menu_frame, text="View Notices", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.view_notices)
        view_notices_button.pack(pady=10)

        logout_button = tk.Button(menu_frame, text="Logout", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.logout)
        logout_button.pack(pady=10)

    def add_student_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Add Student", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        form_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Student ID:", font=("Arial", 12, "bold"), bg="#fff").grid(row=0, column=0, pady=10)
        self.student_id_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.student_id_entry.grid(row=0, column=1, pady=10)

        tk.Label(form_frame, text="Name:", font=("Arial", 12, "bold"), bg="#fff").grid(row=1, column=0, pady=10)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=10)

        tk.Label(form_frame, text="Age:", font=("Arial", 12, "bold"), bg="#fff").grid(row=2, column=0, pady=10)
        self.age_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.age_entry.grid(row=2, column=1, pady=10)

        tk.Label(form_frame, text="Major:", font=("Arial", 12, "bold"), bg="#fff").grid(row=3, column=0, pady=10)
        self.major_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.major_entry.grid(row=3, column=1, pady=10)

        add_button = tk.Button(form_frame, text="Add Student", font=("Arial", 14), bg="#4CAF50", fg="#fff", command=self.add_student)
        add_button.grid(row=4, column=0, columnspan=2, pady=20)

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_student(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        major = self.major_entry.get()

        if student_id and name and age and major:
            if student_id not in self.students:
                self.students[student_id] = Student(student_id, name, age, major)
                messagebox.showinfo("Success", "Student added successfully!")
                self.admin_menu()
            else:
                messagebox.showerror("Error", "Student ID already exists.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def view_student_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="View Student", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        form_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Enter Student ID:", font=("Arial", 12, "bold"), bg="#fff").grid(row=0, column=0, pady=10)
        self.view_student_id_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.view_student_id_entry.grid(row=0, column=1, pady=10)

        view_button = tk.Button(form_frame, text="View", font=("Arial", 14), bg="#2196F3", fg="#fff", command=self.view_student)
        view_button.grid(row=1, column=0, columnspan=2, pady=20)

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.grid(row=2, column=0, columnspan=2, pady=10)

    def view_student(self):
        student_id = self.view_student_id_entry.get()
        if student_id in self.students:
            student = self.students[student_id]
            details = f"ID: {student.student_id}\nName: {student.name}\nAge: {student.age}\nMajor: {student.major}"
            messagebox.showinfo("Student Details", details)
        else:
            messagebox.showerror("Error", "Student not found.")

    def delete_student_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Delete Student", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        form_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Enter Student ID:", font=("Arial", 12, "bold"), bg="#fff").grid(row=0, column=0, pady=10)
        self.delete_student_id_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.delete_student_id_entry.grid(row=0, column=1, pady=10)

        delete_button = tk.Button(form_frame, text="Delete", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.delete_student)
        delete_button.grid(row=1, column=0, columnspan=2, pady=20)

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.grid(row=2, column=0, columnspan=2, pady=10)

    def delete_student(self):
        student_id = self.delete_student_id_entry.get()
        if student_id in self.students:
            del self.students[student_id]
            messagebox.showinfo("Success", "Student deleted successfully.")
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Student not found.")

    def list_students_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="List of Students", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        list_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        list_frame.pack(pady=10)

        students_list = "\n".join([f"{student.student_id} - {student.name}" for student in self.students.values()])

        if not students_list:
            students_list = "No students found."

        students_label = tk.Label(list_frame, text=students_list, font=("Arial", 12), bg="#fff")
        students_label.pack()

        back_button = tk.Button(list_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.pack(pady=10)

    def record_attendance_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Record Attendance", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        form_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Student ID:", font=("Arial", 12, "bold"), bg="#fff").grid(row=0, column=0, pady=10)
        self.attendance_student_id_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.attendance_student_id_entry.grid(row=0, column=1, pady=10)

        tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12, "bold"), bg="#fff").grid(row=1, column=0, pady=10)
        self.attendance_date_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.attendance_date_entry.grid(row=1, column=1, pady=10)

        tk.Label(form_frame, text="Status (Present/Absent):", font=("Arial", 12, "bold"), bg="#fff").grid(row=2, column=0, pady=10)
        self.attendance_status_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.attendance_status_entry.grid(row=2, column=1, pady=10)

        record_button = tk.Button(form_frame, text="Record Attendance", font=("Arial", 14), bg="#4CAF50", fg="#fff", command=self.record_attendance)
        record_button.grid(row=3, column=0, columnspan=2, pady=20)

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def record_attendance(self):
        student_id = self.attendance_student_id_entry.get()
        date = self.attendance_date_entry.get()
        status = self.attendance_status_entry.get()

        if student_id in self.students:
            self.students[student_id].add_attendance(date, status)
            messagebox.showinfo("Success", "Attendance recorded successfully!")
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Student not found.")

    def add_notice_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Add Notice", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        form_frame = tk.Frame(self.root, bg="#fff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Notice Text:", font=("Arial", 12, "bold"), bg="#fff").grid(row=0, column=0, pady=10)
        self.notice_text_entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
        self.notice_text_entry.grid(row=0, column=1, pady=10)

        add_notice_button = tk.Button(form_frame, text="Add Notice", font=("Arial", 14), bg="#4CAF50", fg="#fff", command=self.add_notice)
        add_notice_button.grid(row=1, column=0, columnspan=2, pady=20)

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 14), bg="#f44336", fg="#fff", command=self.admin_menu)
        back_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_notice(self):
        notice_text = self.notice_text_entry.get()

        if notice_text:
            self.notices.append(notice_text)
            messagebox.showinfo("Success", "Notice added successfully!")
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Notice text cannot be empty.")

    def view_my_details(self):
        student = self.students[self.current_user]
        details = f"ID: {student.student_id}\nName: {student.name}\nAge: {student.age}\nMajor: {student.major}"
        messagebox.showinfo("My Details", details)

    def view_my_attendance(self):
        student = self.students[self.current_user]
        attendance_records = student.view_attendance()
        messagebox.showinfo("My Attendance", attendance_records)

    def view_notices(self):
        if self.notices:
            notices_text = "\n".join(self.notices)
            messagebox.showinfo("Notices", notices_text)
        else:
            messagebox.showinfo("Notices", "No notices available.")

    def logout(self):
        self.current_user = None
        self.login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
