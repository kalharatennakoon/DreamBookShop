import pandas as pd

class Analyzer:
    def __init__(self):
        """Initialize Analyzer class"""
        pass
    
    def limit_dataset(self, df, n=None):
        """Limit dataset to first n records for analysis. If n is None, use all records."""
        if df is None or df.empty or n is None:
            return df
        return df.head(n)
    
    def analyze_publication_trends(self, df):
        """Analyze publication trends over time"""
        # Use all records for analysis
        df = self.limit_dataset(df, n=None)
        
        # Check for different possible column names for publication date
        date_columns = ['publication_date', 'publication date', 'date', 'year']
        date_col = None
        
        for col in date_columns:
            if col in df.columns:
                date_col = col
                break
        
        if date_col is None:
            return None, f"Publication date column not found in dataset! Available columns: {list(df.columns)}"
        
        # Handle different data types for dates
        years = None
        
        # Check if the column is already numeric (years)
        if df[date_col].dtype in ['int64', 'float64']:
            years = df[date_col]
        else:
            # Try to extract years from date strings
            try:
                years = pd.to_datetime(df[date_col], errors='coerce').dt.year
            except:
                # Try to extract 4-digit years from strings
                year_pattern = df[date_col].astype(str).str.extract(r'(\d{4})')
                years = pd.to_numeric(year_pattern[0], errors='coerce')
        
        if years is None:
            return None, f"Could not extract years from {date_col} column"
        
        # Filter out unrealistic years (e.g., before 1800 or after current year + 5)
        current_year = pd.Timestamp.now().year
        valid_years = years[(years >= 1800) & (years <= current_year + 5)]
        
        year_counts = valid_years.value_counts().sort_index()
        
        # Remove NaN years
        year_counts = year_counts.dropna()
        
        if year_counts.empty:
            return None, f"No valid publication years found in the data"
        
        analysis_data = {
            'year_counts': year_counts,
            'total_years': len(year_counts),
            'most_productive_year': year_counts.idxmax() if not year_counts.empty else None,
            'most_productive_count': year_counts.max() if not year_counts.empty else 0,
            'least_productive_year': year_counts.idxmin() if not year_counts.empty else None,
            'least_productive_count': year_counts.min() if not year_counts.empty else 0
        }
        
        return analysis_data, None
    
    def analyze_top_authors(self, df, top_n=5):
        """Analyze top most prolific authors"""
        # Use all records for analysis
        df = self.limit_dataset(df, n=None)
        
        # Check for different possible column names for authors
        author_columns = ['authors', 'author', 'writer', 'book_author']
        author_col = None
        
        for col in author_columns:
            if col in df.columns:
                author_col = col
                break
        
        if author_col is None:
            return None, f"Authors column not found in dataset! Available columns: {list(df.columns)}"
        
        author_counts = df[author_col].value_counts().head(top_n)
        
        analysis_data = {
            'author_counts': author_counts,
            'top_n': top_n
        }
        
        return analysis_data, None
    
    def analyze_language_distribution(self, df):
        """Analyze language distribution of books"""
        # Use all records for analysis
        df = self.limit_dataset(df, n=None)
        
        # Check for different possible column names for language
        language_columns = ['language_code', 'language', 'lang', 'book_language']
        lang_col = None
        
        for col in language_columns:
            if col in df.columns:
                lang_col = col
                break
        
        if lang_col is None:
            return None, f"Language column not found in dataset! Available columns: {list(df.columns)}"
        
        lang_counts = df[lang_col].value_counts()
        total_books = len(df)
        
        # Calculate percentages
        lang_percentages = (lang_counts / total_books * 100).round(1)
        
        analysis_data = {
            'lang_counts': lang_counts,
            'lang_percentages': lang_percentages,
            'total_books': total_books
        }
        
        return analysis_data, None
    
    def analyze_books_by_publisher(self, df, top_n=20):
        """Analyze number of books by publisher"""
        # Use all records for analysis
        df = self.limit_dataset(df, n=None)
        
        # Check for different possible column names for publisher
        publisher_columns = ['publisher', 'book publisher', 'book_publisher', 'publishing_house']
        publisher_col = None
        
        for col in publisher_columns:
            if col in df.columns:
                publisher_col = col
                break
        
        if publisher_col is None:
            return None, f"Publisher column not found in dataset! Available columns: {list(df.columns)}"
        
        publisher_counts = df[publisher_col].value_counts().head(top_n)
        total_publishers = df[publisher_col].nunique()
        
        analysis_data = {
            'publisher_counts': publisher_counts,
            'total_publishers': total_publishers,
            'top_n': top_n
        }
        
        return analysis_data, None
    
    def analyze_missing_isbn(self, df):
        """Analyze missing ISBN data"""
        # Use all records for analysis
        df = self.limit_dataset(df, n=None)
        
        isbn_columns = [col for col in df.columns if 'isbn' in col.lower()]
        
        if not isbn_columns:
            return None, "No ISBN columns found in dataset!"
        
        total_records = len(df)
        isbn_analysis = {}
        
        for isbn_col in isbn_columns:
            # Count both null values and empty strings as missing
            missing_count = df[isbn_col].isnull().sum() + (df[isbn_col] == '').sum()
            missing_percentage = (missing_count / total_records) * 100
            present_count = total_records - missing_count
            
            isbn_analysis[isbn_col] = {
                'total_records': total_records,
                'present_count': present_count,
                'missing_count': missing_count,
                'missing_percentage': missing_percentage
            }
        
        analysis_data = {
            'isbn_analysis': isbn_analysis,
            'total_records': total_records
        }
        
        return analysis_data, None
    
    def analyze_books_per_year_by_language(self, df):
        """Analyze books published per year categorized by language"""
        # Use only the first 1000 records for analysis
        df = self.limit_dataset(df, n=1000)
        
        # Check for publication date column
        date_columns = ['publication_date', 'publication date', 'date', 'year']
        date_col = None
        for col in date_columns:
            if col in df.columns:
                date_col = col
                break
        
        # Check for language column
        language_columns = ['language_code', 'language', 'lang', 'book_language']
        lang_col = None
        for col in language_columns:
            if col in df.columns:
                lang_col = col
                break
        
        if date_col is None or lang_col is None:
            missing_cols = []
            if date_col is None:
                missing_cols.append("publication date")
            if lang_col is None:
                missing_cols.append("language")
            return None, f"{' and '.join(missing_cols)} column(s) not found in dataset! Available columns: {list(df.columns)}"
        
        # Handle different data types for dates (same logic as publication trends)
        years = None
        
        # Check if the column is already numeric (years)
        if df[date_col].dtype in ['int64', 'float64']:
            years = df[date_col]
        else:
            # Try to extract years from date strings
            try:
                years = pd.to_datetime(df[date_col], errors='coerce').dt.year
            except:
                # Try to extract 4-digit years from strings
                year_pattern = df[date_col].astype(str).str.extract(r'(\d{4})')
                years = pd.to_numeric(year_pattern[0], errors='coerce')
        
        if years is None:
            return None, f"Could not extract years from {date_col} column"
        
        # Filter out unrealistic years
        current_year = pd.Timestamp.now().year
        valid_mask = (years >= 1800) & (years <= current_year + 5)
        
        # Create a temporary dataframe with year and language
        temp_df = pd.DataFrame({
            'year': years,
            'language': df[lang_col]
        })
        
        # Filter by valid years and remove NaN
        temp_df = temp_df[valid_mask].dropna()
        
        if temp_df.empty:
            return None, "No valid year-language data found"
        
        # Group by year and language
        year_lang_counts = temp_df.groupby(['year', 'language']).size().unstack(fill_value=0)
        
        analysis_data = {
            'year_lang_counts': year_lang_counts,
            'years': sorted(year_lang_counts.index) if not year_lang_counts.empty else [],
            'languages': list(year_lang_counts.columns) if not year_lang_counts.empty else []
        }
        
        return analysis_data, None
