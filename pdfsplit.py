import pikepdf

# Define the input and output file paths
input_file_path = "06.-Chet-vi-chung-khoan.pdf"
output_file_path = "output.pdf"

# Define the page numbers to extract
pages_to_extract = [3, 4,10,33]

# Open the input PDF file
with pikepdf.open(input_file_path) as pdf:
    # Create a new PDF writer object
    output_pdf = pikepdf.Pdf.new()

    # Iterate over the pages to extract
    for page_number in pages_to_extract:
        # Get the page (page_number - 1 because pages are zero-indexed)
        page = pdf.pages[page_number - 1]
        
        # Append the page to the new PDF
        output_pdf.pages.append(page)

    # Save the new PDF to the output file
    output_pdf.save(output_file_path)

print("Pages extracted and saved successfully.")
