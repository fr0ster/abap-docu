# abap-docu

A suite of Python tools and a Gemini-powered agent for fetching, analyzing, and documenting legacy ABAP code via SAP’s ADT (ABAP Development Tools) REST APIs.

---

## 🔍 Overview

- **Fetch source** for ABAP classes, programs, includes, function modules, interfaces, tables, and structures.
- **Discover dependencies** (includes, interfaces, table-types, domains, function calls) and automatically retrieve their metadata.
- **Inspect where-used** lists to see where an object is referenced elsewhere.
- **Generate structured documentation** as JSON via Gemini function-calling.

---

## 🚀 Quickstart

### 1. Clone & Enter

```bash
git clone git@github.com:YahorNovik/abap-docu.git
cd abap-docu
```