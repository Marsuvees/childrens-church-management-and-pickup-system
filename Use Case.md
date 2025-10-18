## **Use Case: Manage Child Check-In and Pickup (Children’s Church App)**
### **Primary Actor:** Receptionist

---

### **Goal:**

To securely admit children into the children’s church and ensure only authorized guardians can pick them up, using a digital verification code system.

---

### **Stakeholders and Interests:**

* **Receptionist:** Needs to verify registration, log attendance, and confirm pickups efficiently.
* **Guardians:** Want a safe, smooth drop-off and pickup experience for their children.
* **Children:** Need to be safely accounted for during and after service.
* **Church Administration:** Requires accurate attendance and pickup records.

---

### **Preconditions:**

* The receptionist is logged into the system.
* The app’s registration and attendance modules are active.

---

### **Postconditions:**

* The child’s check-in and pickup are securely recorded.
* The child’s current status (e.g., *Checked-In*, *Picked-Up*) is updated in the system.
* Notifications and alerts (if any) are sent to registered guardians.

---

### **Main Flow:**

#### **A. Check-In Process**

1. Guardian and child arrive at the church reception.
2. Receptionist checks the system to confirm if both guardian and child are registered.
3. **If registered:**

   * Receptionist admits the child.
   * System logs the check-in with date, time, and receptionist ID.
   * System updates child’s status to **“Checked-In.”**

#### **B. Pickup Process**

4. When the guardian arrives to pick up the child, they **request a pickup code** (either before arrival or upon reaching the church).
5. System flags the code request and sends a unique code via SMS to the guardian’s registered phone number.
6. Guardian presents the code to the receptionist.
7. Receptionist verifies the code in the system.
8. **If code is correct:**

   * The child is called from the service area.
   * Receptionist logs the pickup.
   * System updates status to **“Picked-Up.”**

---

### **Alternative Flows:**

* **1a:** If the guardian and child are *not registered*, the receptionist:

  1. Opens **“New Registration”** form.
  2. Inputs guardian details (name, phone, relationship, ID type).
  3. Adds child details (name, age group, class).
  4. Saves registration — the system assigns them unique IDs.
  5. Continues from step 3 (check-in).

* **7a:** If the code is incorrect or no code request was made:

  1. The system **denies pickup authorization.**
  2. An **alert is sent** to all registered guardians of that child for manual verification or escalation.

---

### **Exceptions:**

* If the guardian’s phone number is inactive or missing, the system prompts manual identity confirmation.
* If network is down, receptionist performs offline check-in and syncs data later.

---

### **Frequency of Use:**

* Each Sunday or service day, for every child entering and leaving the children’s church.

---

### **Special Requirements:**

* Code verification must occur within **30 seconds** of entry.
* The system must generate **unique, time-sensitive pickup codes** (single-use only).
* Support both online and offline modes (with later data sync).
* Maintain a **full audit trail** of all check-ins, pickups, and alerts.

---

### **Key Benefits:**

* Ensures **child safety** and prevents unauthorized pickups.
* Streamlines attendance management.
* Provides real-time visibility of children’s status.
* Reduces manual paperwork and human error.

---
---

### **Primary Actor:** Administrator

---

### **Goal:**

To create and manage a weekly or service-day roster assigning teachers and receptionists to classes, and defining teaching topics for each age group.

---

### **Stakeholders and Interests:**

* **Administrator:** Needs a clear, structured plan of who’s serving and what’s being taught each service.
* **Teachers:** Need to know their assigned classes, roles, and teaching topics.
* **Receptionists:** Need clarity on when they are on duty.
* **Parents/Guardians:** Benefit indirectly through organized operations and consistent teaching quality.
* **Church Leadership:** Needs accurate staffing records and accountability.

---

### **Preconditions:**

* The administrator is logged into the app with scheduling privileges.
* Teacher and volunteer profiles are already registered in the system.
* Class age groups and capacity limits are defined (e.g., 3–5 yrs, 6–8 yrs, 9–12 yrs).

---

### **Postconditions:**

* A complete roster (teachers, receptionists, and topics) is published in the app.
* Notifications are sent to all assigned personnel.
* System updates the dashboard for the upcoming service day.

---

### **Main Flow:**

1. Administrator opens the **Roster Management** section of the app.
2. Selects the **Service Date** (e.g., “Sunday, 20th October 2025”).
3. App displays available **teachers** and **receptionists** from the volunteer list.
4. Administrator assigns:

   * Receptionist(s) for the check-in/pickup desk.
   * Teachers for each **class** (e.g., *Toddlers, Juniors, Pre-Teens*).
5. Administrator enters the **lesson topic** and **Bible verse/theme** for each class.
6. System validates that no teacher is double-booked.
7. Administrator saves the roster.
8. System automatically:

   * Updates the weekly schedule.
   * Sends **notifications** (e.g., “You’re scheduled for Toddlers Class this Sunday”).
   * Flags any unassigned roles for review.
9. Teachers can view their assignments and lesson topics in their dashboard.

---

### **Alternative Flow:**

* **4a:** If a teacher or receptionist is unavailable (marked as “On Leave”), the system suggests substitutes.
* **6a:** If scheduling conflicts exist, the system alerts the admin to adjust.
* **5a:** If the topic isn’t entered, the system prompts before saving the roster.

---

### **Exceptions:**

* Internet connection lost — roster saved locally and synced once online.
* Administrator closes the app mid-process — system auto-saves progress as a draft.

---

### **Frequency of Use:**

Weekly (typically once before each service).

---

### **Special Requirements:**

* Support recurring schedules (e.g., “Every 2nd Sunday of the month”).
* Allow exporting roster to PDF or printing.
* Enable role-based permissions (only admins can edit roster).
* Integrate topic templates or lesson plan uploads.

---

### **Key Benefits:**

* Streamlines volunteer management.
* Prevents confusion about roles or class assignments.
* Keeps all staff informed of teaching topics in advance.
* Improves operational consistency and transparency.

---

### **Integration with Other Use Case:**

* The **Receptionist** assigned via this roster is the **Primary Actor** in the “Child Check-In and Pickup” use case (CC-001).
* The **Teacher Assignments** directly influence which children are marked as present in each class.
* The **Lesson Topics** can be displayed in reports for curriculum tracking.

