import pandas as pd
import sys

def match_sheets(excel_file, sheet1_name, sheet2_name, match_col1, match_col2, output_csv):
    """
    Match two Excel sheets based on a common column and export to CSV.
    
    Parameters:
    - excel_file: Path to the Excel file
    - sheet1_name: Name of the first sheet
    - sheet2_name: Name of the second sheet
    - match_col1: Column name or index to match in sheet1
    - match_col2: Column name or index to match in sheet2
    - output_csv: Output CSV file path
    """
    
    try:
        # Read both sheets
        print(f"Reading {sheet1_name}...")
        df1 = pd.read_excel(excel_file, sheet_name=sheet1_name)
        
        print(f"Reading {sheet2_name}...")
        df2 = pd.read_excel(excel_file, sheet_name=sheet2_name)
        
        print(f"\nSheet1 shape: {df1.shape}")
        print(f"Sheet2 shape: {df2.shape}")
        
        print(f"\nConverting columns to matchable string type...")
        df1[match_col1] = df1[match_col1].astype(str).str.strip()
        df2[match_col2] = df2[match_col2].astype(str).str.strip()
        
        # Perform the merge based on matching columns
        print(f"\nMatching on '{match_col1}' and '{match_col2}'...")
        matched_df = pd.merge(
            df1, 
            df2, 
            left_on=match_col1, 
            right_on=match_col2, 
            how='inner',
            suffixes=('_Sheet1', '_Sheet2')
        )
        
        # Export to CSV
        matched_df.to_csv(output_csv, index=False)
        
        print(f"\n✓ Success! Matched {len(matched_df)} rows")
        print(f"✓ Results saved to: {output_csv}")
        print(f"\nMatched columns: {list(matched_df.columns)}")
        
        return matched_df
        
    except FileNotFoundError:
        print(f"Error: File '{excel_file}' not found")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        print("Make sure sheet names and column names are correct")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Configuration - Modify these values as needed
    EXCEL_FILE = "D:\Downloads\sb.xlsx"
    SHEET1_NAME = "Sheet1"
    SHEET2_NAME = "Sheet2"
    MATCH_COLUMN_SHEET1 = "TIN"  # Can be column name or index (0, 1, 2, etc.)
    MATCH_COLUMN_SHEET2 = "PAY_REQ_TIN"  # Can be column name or index (0, 1, 2, etc.)
    OUTPUT_CSV = "matched_results.csv"
    
    # Run the matching
    match_sheets(
        excel_file=EXCEL_FILE,
        sheet1_name=SHEET1_NAME,
        sheet2_name=SHEET2_NAME,
        match_col1=MATCH_COLUMN_SHEET1,
        match_col2=MATCH_COLUMN_SHEET2,
        output_csv=OUTPUT_CSV
    )