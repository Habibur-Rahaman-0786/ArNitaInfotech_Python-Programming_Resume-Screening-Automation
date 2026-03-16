#Main Application
import customtkinter as ctk
from tkinter import filedialog
from tkinter import ttk
from resume_parser import get_resume_text
from candidate_extractor import extract_name, extract_email, extract_phone
from skill_extractor import extract_skills
from ranking_system import calculate_score
from database import create_database, insert_candidate

#Initial Theme
ctk.set_appearance_mode("light")   # light / dark / system
ctk.set_default_color_theme("blue")

#Function to Upload Resume
def upload_resume():
    files = filedialog.askopenfilenames(
        filetypes=[("Resume Files","*.pdf *.docx")]
    )

    for file in files:
        text = get_resume_text(file)

        name = extract_name(text)
        email = extract_name(text)
        phone = extract_phone(text)

        skills = extract_skills(text)
        score = calculate_score(skills)

        insert_candidate(name, email, phone, str(skills), score)

        tree.insert("", ctk.END, values=(
            name,
            email,
            phone,
            ", ".join(skills),
            str(score) + "%"
        ))

create_database()

#Function To Change Theme
def change_mode():

    if mode_switch.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

#GUI Application
app = ctk.CTk()
app.title("Resume Screening Automation")
app.geometry("1000x600")

title = ctk.CTkLabel(
    app,
    text="Resume Screening Dashboard",
    font=("Arial", 22)
)

title.pack(pady=20)

mode_switch = ctk.CTkSwitch(
    app,
    text="Dark Mode",
    command=change_mode
)

mode_switch.pack(pady=10)

upload_btn = ctk.CTkButton(
    app,
    text="Upload Resumes",
    command=upload_resume
)

upload_btn.pack(pady=10)

columns = ("Name","Email","Phone","Skills","Score")

tree = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack(fill="both", expand=True, padx=20, pady=20)

scrollbar = ttk.Scrollbar(app, orient="vertical", command=tree.yview)

tree.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")

app.mainloop()