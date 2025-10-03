
# File Structure

```mermaid
graph LR;

A([Project Directory])
A --> B(templates)
A --> C(static)
A --> A1[database.py]
A --> A2[app.py]
A --> A3[auth.py]
A --> A4[teachers.py]
A --> A5[guardians.py]

  
B --> B1[index.html]
B --> B2[guardians.html]
B --> B3[teachers.html]
B --> B4[login.html]
B --> B5[signup.html]
B --> B6[admin.html]

C --> C1[style.css]

```



# Database Structure
```mermaid
flowchart TB

    A{Database}

    %% Core tables
    A --> B[Guardians]
    A --> C[Staff]
    A --> D[Children]
    A --> E[Logs]
    A --> F[Guardian_Child]
    A --> G[Teacher_Child]
    A --> H[Roaster]

    %% Guardians
    B --> B1[Guardian_ID]
    B --> B2[Name]
    B --> B3[PhoneNumber]
    B --> B4[Email]

    %% Staff
    C --> C1[Staff_ID]
    C --> C2[Name]
    C --> C3[ClassCode]
    C --> C4[IsAdmin]
    C --> C5[IsTeacher]

    %% Children
    D --> D1[Child_ID]
    D --> D2[Name]
    D --> D3[Birthdate]

    %% Logs
    E --> E1[Log_ID]
    E --> E2[Child_ID]
    E --> E3[DateTime]
    E --> E5[Event]
    E --> E6[SignedInBy]
    E --> E7[OfferingAmount]
	E --> E8[SignedOutBy]


    %% Guardian_Child
    F --> F1[Guardian_ID]
    F --> F2[Child_ID]

    %% Teacher_Child
    G --> G1[Staff_ID]
    G --> G2[Child_ID]
    G --> G3[StartDate]
    G --> G4[EndDate]

	%% Roaster
	H --> H1[DateTime]
	H --> H2[Curriculum]
	H --> H3[ClassCode]
	H --> H4[TeacherCode]

    %% Relationships
    F1 --> B1
    F2 --> D1

    G1 --> C1
    G2 --> D1

    E2 --> D1
    

```