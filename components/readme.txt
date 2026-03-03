Each generator follows the same pattern:

- Takes form_data (dict)
- Replaces placeholders in LaTeX template
- Compiles PDF
- Returns (success, pdf_path_or_error)