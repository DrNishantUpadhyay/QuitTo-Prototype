# QuitTo-Prototype
# 💙 QuitTo: Wellness & Recovery Web App

Welcome to the official prototype repository for **QuitTo**, a science-backed "Slow-Quit" application designed for incremental harm reduction in tobacco cessation. 

This platform bridges the gap between digital habit tracking and professional clinical support by offering a complete, dual-sided ecosystem: one interface for patients to manage their recovery, and a secure portal for healthcare providers to monitor and guide them.

---

## 🚀 Key Features & Functionality

### 👤 For Patients
* **Personalized Onboarding**: Captures baseline usage and pack costs to automatically tailor the financial and reduction targets.
* **12-Week Reduction Schedule**: A dynamic, interactive timeline guiding users to gradually reduce dependency without the shock of "cold turkey" quitting.
* **Synced Daily Tasks**: A daily habit checklist that updates in real-time based on the dentist's recommendations.
* **Health Recovery Milestones**: Educational timeline tracking the physiological healing process (from 8 hours to 1 year post-quitting) to maintain motivation.
* **Advanced Analytics**: Visualizes declining consumption trends via dynamic line charts and calculates projected financial savings.
* **QuitTo Recovery Agent**: An integrated AI chatbot available 24/7 to help patients navigate sudden cravings and stress.
* **Direct Clinical Support**: Immediate access to the Tobacco Cessation Cell (TCC) contact and location details.

### 🩺 For Healthcare Providers
* **Secure Provider Portal**: A dedicated login environment for clinical staff.
* **Patient Management Dashboard**: A centralized view of all active patients, their current addiction type, and their usage stage.
* **Clinical Record Keeping**: Interactive dialogs to seamlessly record Carbon Monoxide (CO) meter readings and detailed Case Histories (Diagnosis, Treatment Plans, Notes).
* **Dynamic Task Assignment**: Providers can remotely assign or remove specific daily tasks (e.g., "Chew nicotine gum", "Drink 2L water") for individual patients, which syncs directly to the patient's mobile view.

---

## 🛠️ Tech Stack
* **Core Framework**: Python, Streamlit
* **Data Manipulation & Visualization**: Pandas, Altair
* **UI Components**: Custom HTML/CSS, Streamlit Dialogs
* **Deployment**: Streamlit Community Cloud

---

## 👥 The Team
The QuitTo project is a fusion of medical expertise and software development:
* **Dr. Nishant Upadhyay** - Founder & Lead Developer
* **Laxmi Raj Sharma** - Co-Founder & UI/UX Lead
* **Dr. Hemant Sawhney** - TCC Incharge & Clinical Collaborator (Department of Oral Medicine and Radiology, School of Dental Sciences, Sharda University)

---

## 💻 How to Run Locally

If you want to run this prototype on your local machine:

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/DrNishantUpadhyay/QuitTo-Prototype.git](https://github.com/DrNishantUpadhyay/QuitTo-Prototype.git
   Navigate into the project directory:

2. Navigate into the project directory:
Bash
cd QuitTo-Prototype
Install the required dependencies:

3. Install the required dependencies:
Bash
pip install -r requirements.txt
Launch the Streamlit app:

Launch the Streamlit app:
4. Bash
streamlit run app.py
