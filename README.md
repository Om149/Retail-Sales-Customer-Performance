# Retail Sales & Customer Performance Analysis (Days 16–30)

This repository structure was prepared from the selected source workbook `Day16-30(1).docx`. Code text has been extracted from that document and separated into day-wise files. SQL statements are stored separately from Python.

## Important source and execution notes
- The files contain code documented in the workbook; they are not independently verified transcripts of every code cell previously executed.
- Code text is retained as it appears in the source. Paths, table names, columns, and variable names have not been silently corrected.
- Some workbook sections provide snippets intended to be run separately. Therefore, a combined `.py` file may require the original data files and may not execute from top to bottom without following the workbook's section order.
- Day 24 and Day 25 have no executable Python/SQL blocks in this source document. Day 29 and Day 30 provide findings/finalization content, not executable code. No replacement code has been invented for these days.
- Day 21 uses the workbook's original `OrderID`, `OrderDate`, `Product`, and `Category` SQL examples. Later days use the `InvoiceNo`-based dataset. These differences are preserved rather than reconciled.
- Day 17/18 use `01_raw/online_retail_raw.csv`; Day 19 uses `data.csv`; Day 20 uses `04_outputs/day20_analysis_ready_sales.csv`; Day 21/22 use `sales_cleaned.csv`; Day 23 uses `retail_sales.csv`; Day 26 uses `data.csv`; Day 28 uses `cleaned_sales_data_updated.csv`. Place the correct source file at the path stated in each script or update it yourself only after confirming your local setup.

## Folder guide
- Day 17: dataset loading and inspection
- Day 18: data-quality audit
- Day 19: cleaning and preprocessing
- Day 20: KPI calculation
- Day 21: SQLite loader and separate SQL queries
- Day 22: sales trend analysis
- Day 23: product/category analysis
- Day 24–25: source workbook contains no executable code blocks
- Day 26: diagnostic analysis
- Day 27–28: Power BI DAX reference and dashboard validation
- Day 29–30: written findings and finalization material only

## Requirements mentioned in the workbook
Python packages used in the documented snippets include `pandas`, `numpy`, `matplotlib`, and `scipy`. SQLite is used for the Day 21 database exercise. Install only the packages required by the script you are running.

## Source
`Day16-30(1).docx` is included so each extracted code file can be checked against the original workbook.
