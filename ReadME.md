# 🎒 Ready, Set, School!

**Ready, Set, School!** is a Python desktop application designed to make back-to-school shopping easier by comparing the school supplies you already own against a student's required school supply list.

Instead of manually checking every pencil, binder, marker, notebook, and other supply, the application keeps track of household school-supply inventory, stores school requirements, compares the two, and generates a shopping list containing only the items that are still needed.

> **Current Version: 1.0 — Functional MVP**
>
> Version 1.0 is a functional Minimum Viable Product (MVP). The core workflow is working end-to-end, while additional usability, automation, and quality-of-life features are planned for future versions.

---

# 💡 Why I Built This

Ready, Set, School! started with a simple real-world problem:

> **Before buying more school supplies, how can I quickly figure out what we already have and what we're actually missing?**

At the beginning of a new school year, there are usually supplies left over from previous years. Some are still usable, some need replacing, and the new school supply list may require specific quantities, colours, or specifications.

Manually comparing everything can become tedious very quickly.

The idea behind Ready, Set, School! is to let the user inventory the supplies they already own, enter a student's school requirements, and have the application calculate what is actually missing.

For example:

```text
School requires:
24 HB #2 Pencils

Inventory:
10 HB #2 Pencils in Good condition

Ready, Set, School! calculates:
14 Pencils still needed
```

The project also gave me an opportunity to take concepts I have been learning in school and use them to build a practical application from the ground up.

That includes:

- Python
- Object-Oriented Programming
- Classes and objects
- Functions
- Validation
- CRUD operations
- SQLite databases
- Relational data
- Service layers
- GUI development
- Comparison logic
- Application architecture

Rather than trying to build every planned feature immediately, Version 1.0 focuses on creating a **functional MVP** with a complete core workflow.

---

# ✨ Version 1.0 Features

The current functional MVP supports:

- Adding, editing, and deleting Inventory items
- Tracking Inventory quantities
- Tracking item condition
- Recording colour, specification, and notes
- Creating and deleting School Lists
- Creating School Lists for multiple students
- Adding, editing, and deleting Required Items
- Comparing Required Items against household Inventory
- Ignoring Inventory items in `Poor` condition during comparison
- Matching requirements using:
  - Item name
  - Colour
  - Specification
- Calculating missing quantities
- Automatically generating Shopping Lists
- Maintaining separate Shopping Lists for different School Lists
- Marking Shopping Items as purchased
- Undoing purchased status
- Deleting Shopping Items
- Supporting comma-separated colours when one of each colour is required
- Storing application data in a SQLite database
- Navigating the application through a CustomTkinter GUI

---

# 🔄 Core Workflow

The core Version 1.0 workflow is:

```text
Inventory
    ↓
School List
    ↓
Required Items
    ↓
Comparison Engine
    ↓
Shopping List
```

The user first records the supplies they already own.

They then create a School List and add the supplies required by the school.

The Comparison Engine compares the Required Items against the household Inventory and calculates the missing quantities.

Those missing quantities are then used to generate the Shopping List.

---

# 🛠️ Technologies Used

Ready, Set, School! Version 1.0 uses:

- Python
- CustomTkinter
- SQLite
- Object-Oriented Programming
- Service-layer architecture
- Git
- GitHub

The project separates the application into several layers:

```text
Models
   ↓
Services
   ↓
Database
   ↓
User Interface
```

This keeps database operations, application logic, comparison logic, and GUI code separated.

---

# 📁 Project Structure

```text
ready-set-school/
│
├── assets/
│
├── data/
│   └── ready_set_school.db
│
├── models/
│   ├── __init__.py
│   ├── required_item.py
│   ├── school_supply_list.py
│   ├── shopping_item.py
│   └── supply_item.py
│
├── services/
│   ├── __init__.py
│   ├── comparison_engine.py
│   ├── database.py
│   ├── inventory_manager.py
│   ├── school_list_manager.py
│   └── shopping_list_manager.py
│
├── tests/
│
├── ui/
│   ├── __init__.py
│   ├── inventory_screen.py
│   ├── main_window.py
│   ├── school_list_screen.py
│   └── shopping_list_screen.py
│
├── .gitignore
├── blueprint.md
├── main.py
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run the Application

## 1. Clone the Repository

Clone the repository:

```bash
git clone <repository-url>
```

Then enter the project directory:

```bash
cd ready-set-school
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

### PowerShell

Activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Command Prompt

Activate it with:

```cmd
.venv\Scripts\activate
```

---

## 3. Install the Requirements

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

---

## 4. Start the Application

Run:

```bash
python main.py
```

The **Ready, Set, School!** desktop application should open.

---

# 📖 How to Use Ready, Set, School!

## Step 1 — Add Existing Supplies to Inventory

Open **Inventory** from the navigation menu.

Select:

```text
Add Supply
```

Enter information such as:

```text
Name
Quantity
Condition
Colour
Specification
Notes
```

For example:

```text
Name: Pencil
Quantity: 10
Condition: Good
Specification: HB #2
```

Inventory items can later be edited or deleted.

---

## Step 2 — Record Item Condition

Inventory items can have conditions such as:

```text
New
Good
Fair
Poor
```

Items marked as `Poor` are ignored by the comparison engine.

This prevents unusable supplies from reducing the quantity that the Shopping List says needs to be purchased.

For example:

```text
Inventory:
Pencil | Quantity: 10 | Condition: Poor

Required:
Pencil | Quantity: 24
```

The 10 poor-condition pencils will not count toward the requirement.

---

## Step 3 — Create a School List

Open:

```text
School Lists
```

Select:

```text
Add School List
```

Enter information such as:

```text
School
Grade
School Year
Student
```

For example:

```text
School: Test School
Grade: Grade 12
School Year: 2026-2027
Student: Student 1
```

The new School List will appear on the School Lists screen.

---

# 👨‍👩‍👧‍👦 Multiple Students

Version 1.0 already supports managing school requirements for multiple students.

Each School List can contain its own:

- School
- Grade
- School year
- Student name
- Required Items
- Generated Shopping List

For example:

```text
Test School | Grade 12 | 2026-2027 | Student 1

Test School 2 | Grade 12 | 2026-2027 | Student 2
```

This allows different students, schools, grades, and school years to be stored independently.

Each School List can be opened separately to manage its Required Items.

---

## Step 4 — Add Required Items

Open the appropriate School List and select:

```text
Add Required Item
```

A Required Item describes what the school says the student needs.

For example:

```text
Item Name: Pencil
Quantity Required: 24
Specification: HB #2
```

Additional information can include:

```text
Colour
Specification
Notes
```

Required Items can later be edited or deleted.

---

# 🎨 Entering Colour Requirements

Version 1.0 supports comma-separated colours, but there is an important limitation.

## One Item Required in Each Colour

If the **Quantity Required is 1**, multiple colours can be entered using commas.

For example:

```text
Item Name: Report Cover
Quantity Required: 1
Colour: Orange, Yellow, Red, Blue
Specification: 3 Prong
```

Ready, Set, School! automatically creates separate Required Items:

```text
Report Cover | Quantity: 1 | Orange | 3 Prong
Report Cover | Quantity: 1 | Yellow | 3 Prong
Report Cover | Quantity: 1 | Red | 3 Prong
Report Cover | Quantity: 1 | Blue | 3 Prong
```

This prevents the user from having to enter the same requirement repeatedly when exactly one of each colour is required.

---

## Different Quantities for Different Colours

If different colours require different quantities, **each colour must currently be entered separately**.

For example, suppose the school requires:

```text
12 Blue Ballpoint Pens
6 Black Ballpoint Pens
4 Red Ballpoint Pens
```

Enter:

```text
Item Name: Ballpoint Pen
Quantity Required: 12
Colour: Blue
```

Then:

```text
Item Name: Ballpoint Pen
Quantity Required: 6
Colour: Black
```

Then:

```text
Item Name: Ballpoint Pen
Quantity Required: 4
Colour: Red
```

Do **not** enter:

```text
Item Name: Ballpoint Pen
Quantity Required: 12
Colour: Blue, Black, Red
```

Version 1.0 cannot associate separate quantities with individual colours in a single entry.

> **Version 1.0 Rule:** Use comma-separated colours when the quantity required is `1` and one of each listed colour is needed. If different colours require different quantities, enter each colour as a separate Required Item.

---

# 🔍 How Inventory Comparison Works

The comparison engine compares Inventory against each Required Item.

It currently considers:

```text
Item Name
Colour
Specification
```

Text is normalized before comparison so capitalization does not affect matching.

For example:

```text
Pencil
pencil
PENCIL
```

are treated as the same item name.

If a Required Item specifies a colour, the Inventory item must have the matching colour.

If a Required Item specifies a specification, the Inventory item must also have the matching specification.

Inventory items with a condition of `Poor` are ignored.

---

## Comparison Example

Suppose the Required Item is:

```text
Pencil
Quantity Required: 24
Specification: HB #2
```

and Inventory contains:

```text
Pencil
Quantity: 10
Condition: Good
Specification: HB #2
```

The comparison engine calculates:

```text
24 required
- 10 owned
-----------
14 missing
```

The generated Shopping List will therefore contain:

```text
Pencil | Quantity: 14 | HB #2
```

---

## Step 5 — Generate the Shopping List

Once Required Items have been entered, open the School List and select:

```text
Generate Shopping List
```

Ready, Set, School! compares the requirements for that School List against the household Inventory.

Only missing quantities are added to the Shopping List.

---

## Step 6 — View the Shopping List

Open:

```text
Shopping List
```

Choose the appropriate School List from the dropdown.

Select:

```text
Load
```

The generated Shopping List will appear.

---

## Step 7 — Track Purchases

Shopping List items can be marked as:

```text
Mark Purchased
```

After being marked as purchased, the button changes to:

```text
Undo Purchased
```

This allows shopping progress to be tracked without immediately deleting the item.

Shopping Items can also be manually deleted.

---

# ⚠️ Version 1.0 Limitations

Version 1.0 is a **functional MVP**, not the final version of Ready, Set, School!

The core application workflow works end-to-end, but several limitations remain.

---

## 1. Different Colour Quantities Require Separate Entries

Comma-separated colours cannot currently be assigned different quantities.

For example:

```text
Blue × 12
Black × 6
Red × 4
```

must currently be entered as three separate Required Items.

---

## 2. Matching Is Based on Structured Text

The comparison engine currently compares normalized:

- Item names
- Colours
- Specifications

It does not yet perform semantic or fuzzy matching.

For example:

```text
HB Pencil
HB #2 Pencil
#2 Pencil
Wood Pencil
```

may refer to compatible supplies, but Version 1.0 may treat them as different items.

---

## 3. Specifications Need Consistent Wording

Different ways of writing the same specification may not currently match.

For example:

```text
2 inch
```

and:

```text
2"
```

may describe the same binder size to a person but are not necessarily interpreted as equivalent by the application.

Users should currently try to use consistent wording between Inventory and Required Items.

---

## 4. Inventory Is Household-Level

Inventory is currently treated as a shared household pool.

Version 1.0 supports multiple students and separate School Lists, but it does not yet intelligently allocate limited Inventory between multiple students.

For example:

```text
Inventory:
Pencil × 20

Student 1:
Requires Pencil × 15

Student 2:
Requires Pencil × 15
```

The application does not yet perform household-level allocation to determine how the 20 available pencils should be divided between the two students.

---

## 5. Shopping Lists Are Generated Per School List

Each School List currently generates its own Shopping List.

Version 1.0 does not yet combine requirements from multiple students into one household Shopping List.

---

## 6. School Supply Requirements Must Be Entered Manually

School supply requirements currently have to be entered manually through the GUI.

Version 1.0 cannot yet automatically import supply requirements from:

- Screenshots
- Images
- PDFs
- School websites
- Online school-supply lists
- Other documents

Automated importing is planned for a future version.

---

## 7. Regenerating a Shopping List Recalculates Requirements

The Shopping List is generated from the current Inventory and Required Items.

Version 1.0 is focused on generating the current missing requirements rather than maintaining a complete shopping history.

Future versions can improve synchronization between Inventory, purchases, requirements, and Shopping Lists.

---

# 🚀 Planned Future Features

Version 1.0 establishes the core application architecture and workflow.

Future development will focus on reducing manual data entry, improving household planning, and making the comparison system smarter.

---

## 📸 AI-Assisted School List Import

A major planned feature is the ability to import a school supply list from a screenshot or image using AI-assisted image analysis.

The intended workflow is:

```text
Upload Screenshot
        ↓
AI / Image Analysis
        ↓
Detect School Supply Items
        ↓
Extract Names, Quantities,
Colours and Specifications
        ↓
User Reviews Results
        ↓
Create Required Items
        ↓
Generate Shopping List
```

For example, instead of manually entering:

```text
24 HB #2 Pencils
2 Clear Glue Sticks - 40 g
1 Black Fine Tip Dry Erase Marker
1 Orange 3-Prong Report Cover
```

the user could provide a screenshot of the school supply list.

The application could identify the individual supplies and convert them into structured Required Items.

The user would review and approve the extracted information before it is saved to prevent incorrect information from being automatically added.

---

## 📄 PDF School List Import

Future versions could support school-provided PDF supply lists.

The application could extract requirements from a PDF and convert them into structured Required Items.

This would provide another option for reducing manual entry.

---

## 🌐 School Website Import

A future version could potentially assist with importing requirements from school websites or online school-supply lists.

This would further reduce the amount of manual entry required before generating a Shopping List.

---

## 🎨 Improved Colour and Quantity Entry

Future versions could support entering different quantities for multiple colours in a single form.

For example:

```text
Ballpoint Pen

Blue: 12
Black: 6
Red: 4
```

instead of requiring three separate Required Item entries.

---

## 🧠 Smarter Item Matching

Future versions could improve the Comparison Engine so it recognizes equivalent or compatible descriptions.

For example:

```text
HB #2 Pencil
#2 Pencil
HB Pencil
```

could potentially be recognized as the same type of supply.

Similar improvements could be made for specifications such as:

```text
2 inch
2"
2-inch
```

The goal would be to make comparison more flexible without incorrectly treating genuinely different supplies as equivalent.

---

## 👨‍👩‍👧‍👦 Expanded Multi-Student Support

Version 1.0 already supports creating separate School Lists for multiple students.

Future versions could expand this functionality with:

- Student profiles
- A dashboard showing all students
- Filtering by student
- Combined household Shopping Lists
- Showing which student requires each Shopping Item
- Detecting overlapping requirements between students
- Comparing household Inventory against multiple students simultaneously

---

## 📦 Household Inventory Allocation

A future Comparison Engine could allocate shared Inventory across multiple students.

For example:

```text
Inventory:
20 Pencils

Student 1 needs:
15 Pencils

Student 2 needs:
15 Pencils
```

Instead of allowing both lists to independently count the same 20 pencils, the system could calculate:

```text
Total required: 30
Total owned: 20
Total still needed: 10
```

This would allow Ready, Set, School! to work as a complete household-level back-to-school planning tool.

---

## 🛒 Combined Household Shopping List

Instead of viewing Shopping Lists only by individual School List, a future version could create one combined shopping trip.

For example:

```text
HOUSEHOLD SHOPPING LIST

Pencils × 10
Binders × 4
Glue Sticks × 2
Dry Erase Markers × 1
```

Items could also show which student or School List requires them.

---

## 📤 Export and Printing

Future versions could expand export functionality to support:

- Printable Shopping Lists
- PDF export
- CSV export
- Inventory reports
- School requirement reports
- Shopping checklists

---

## 🔄 Inventory Updates After Shopping

A future workflow could allow purchased Shopping Items to be automatically added to Inventory.

For example:

```text
Mark Purchased
      ↓
Confirm Purchase
      ↓
Add Quantity to Inventory
      ↓
Update Shopping List
```

This would connect shopping and Inventory management more closely.

---

## 🏷️ Categories

Future Inventory and Required Items could be grouped into categories such as:

```text
Writing Supplies
Paper
Binders & Organization
Art Supplies
Technology
Classroom Supplies
Clothing
Other
```

This could improve organization and Shopping List readability.

---

## 🔎 Search, Sorting, and Filtering

As Inventory and School Lists grow, future versions could include:

- Inventory search
- Required Item search
- Shopping List search
- Sorting alphabetically
- Sorting by quantity
- Filtering by student
- Filtering by category
- Filtering by purchased status
- Filtering by item condition

---

## 💾 Improved Data Management

Future versions could add:

- Database backup
- Database restore
- Data import/export
- Archived school years
- Archived School Lists
- Shopping history

---

## 🎨 GUI Improvements

The Version 1.0 interface prioritizes functionality.

Future versions could improve:

- Responsive layouts
- Item cards
- Icons
- Confirmation dialogs
- Success messages
- Error messages
- Empty-state messages
- Sorting
- Search
- Filtering
- Progress indicators
- Visual purchased-item states
- Better handling of long item descriptions

---

# 🗺️ Development Roadmap

A possible development path after Version 1.0 is:

```text
Version 1.0
Functional MVP

✓ Inventory
✓ School Lists
✓ Multiple Students
✓ Required Items
✓ Comparison Engine
✓ Missing Quantity Calculation
✓ Shopping List Generation
✓ Purchase Tracking

        ↓

Version 1.x
Usability Improvements

• Better forms
• Validation improvements
• Search and sorting
• Export / printing
• Improved colour quantities
• GUI improvements

        ↓

Version 2.0
Smarter Automation

• Screenshot import
• AI-assisted extraction
• PDF import
• Smarter item matching
• Improved specification matching

        ↓

Future
Household Planning

• Student profiles
• Household Inventory allocation
• Combined Shopping Lists
• Purchase → Inventory workflow
• Archived school years
• Shopping history
```

---

# 🔐 Privacy

The public version of this project uses fictional demonstration information.

Example test data includes:

```text
School: Test School
Student: Student 1
Grade: Grade 12
School Year: 2026-2027
```

Real student or school information should not be included in public repository screenshots, documentation, test data, or committed databases.

The SQLite database is intended to remain local and should not be committed when it contains personal information.

---

# 🧪 Current Project Status

**Version:** 1.0  
**Status:** Functional MVP

The primary workflow is operational:

```text
Create Inventory
      ✓
Create School List
      ✓
Add Required Items
      ✓
Compare Requirements to Inventory
      ✓
Calculate Missing Quantities
      ✓
Generate Shopping List
      ✓
Load Shopping List
      ✓
Mark Items Purchased
      ✓
Undo Purchased Status
      ✓
```

Version 1.0 proves the core concept:

> **Ready, Set, School! can store household school supplies, store student requirements, compare the two, and generate a Shopping List containing the missing supplies.**

The project is now at the point where future development can focus less on proving the core workflow and more on improving usability, automation, household planning, and intelligent item matching.

---

# 🎒 Ready, Set, School!

**Inventory what you have.  
Compare what you need.  
Buy only what's missing.**