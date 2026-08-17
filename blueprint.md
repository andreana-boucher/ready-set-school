# ✅ Phase 1 — Project & Environment Setup

**Status:** Complete

## Goal

Set up the development environment and create the basic project structure.

## Plan

- [x] Create GitHub repository
- [x] Clone repository locally
- [x] Configure Git
- [x] Create Python virtual environment
- [x] Install project dependencies
- [x] Create project folder structure
- [x] Configure `.gitignore`
- [x] Commit and push project foundation

## Outcome

Project foundation is ready for development.

---

# ✅ Phase 2 — Database & Models

**Status:** Complete

## Goal

Build the models and database structure needed to store household inventory and school supply lists.

## Plan

### Inventory Foundation

- [x] Create `SupplyItem` model
- [x] Create `RequiredItem` model
- [x] Create SQLite database
- [x] Create supplies table
- [x] Build supply CRUD
- [x] Test supply CRUD

### School List Foundation

- [x] Create `SchoolSupplyList` model
- [x] Create school lists table
- [x] Create required items table
- [x] Link required items to school lists
- [x] Build school list CRUD
- [x] Build required item CRUD
- [x] Test database relationships

## Outcome

Household inventory and school supply lists can be stored, retrieved, edited, and deleted.

---

# ✅ Phase 3 — Inventory Manager

**Status:** Complete

## Goal

Turn the existing school supply database functions into usable inventory management.

## Plan

- [x] Add existing school supplies
- [x] View all saved supplies
- [x] Edit existing supplies
- [x] Delete supplies
- [x] Track quantity
- [x] Track condition
- [x] Track colour
- [x] Track specifications
- [x] Validate inventory input
- [x] Prepare inventory functions for GUI use

## Outcome

Household school supplies can be managed through reusable application logic instead of direct database testing.

---

# ⬜ Phase 4 — School List Manager

**Status:** Not Started

## Goal

Build the application logic needed to create and manage school supply lists and their required items.

## Plan

- [ ] Create a school supply list
- [ ] View saved school supply lists
- [ ] Edit school list details
- [ ] Delete school supply lists
- [ ] Add required items to a school list
- [ ] View required items
- [ ] Edit required items
- [ ] Delete required items
- [ ] Keep required items linked to the correct school list
- [ ] Test using a real school supply list

## Outcome

School supply lists and their required items can be managed through reusable application logic and are ready to be used by the comparison engine.

---

# ⬜ Phase 5 — Comparison Engine & Shopping List

**Status:** Not Started

## Goal

Compare household inventory against school requirements and calculate exactly what still needs to be purchased.

## Plan

- [ ] Match required items with household inventory
- [ ] Compare required quantities with quantities already owned
- [ ] Match colour when relevant
- [ ] Match specifications when relevant
- [ ] Consider item condition
- [ ] Calculate missing quantities
- [ ] Generate shopping list automatically
- [ ] Show only items still needed
- [ ] Track purchased and unpurchased items
- [ ] Prepare shopping list data for printing/export

## Outcome

The app can determine what the family already has, what is still missing, and generate an accurate shopping list.

---

# ⬜ Phase 6 — GUI, Printable Output & Polish

**Status:** Not Started

## Goal

Turn the working backend into a simple desktop application that is easy to use and produces a printable shopping list.

## Plan

- [ ] Build the CustomTkinter main window
- [ ] Create app navigation
- [ ] Build inventory screen
- [ ] Build school list screen
- [ ] Build comparison screen
- [ ] Build shopping list screen
- [ ] Add forms and validation messages
- [ ] Add condition dropdowns
- [ ] Add colour and specification fields
- [ ] Add purchase tracking controls
- [ ] Create printable shopping list output
- [ ] Add Print / Export option
- [ ] Test with real family data
- [ ] Improve layout and appearance
- [ ] Complete final Version 1 testing
- [ ] Commit and push Version 1

## Outcome

Ready, Set, School! works as a complete desktop application that can manage supplies, compare requirements, and generate a usable printable shopping list.

---