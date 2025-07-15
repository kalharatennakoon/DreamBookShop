import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Visualizer:
    def __init__(self):
        """Initialize Visualizer class"""
        # Set up plotting style
        plt.style.use('default')
        sns.set_palette("husl")
        # Configure matplotlib to be non-blocking
        plt.ion()  # Turn on interactive mode
    
    def display_first_records(self, df, n=30):
        if df is None:
            print("Error: No dataset provided to display.")
            return
        
        if df.empty:
            print("The dataset is empty.")
            return
        
        # print(f"\n=== Displaying First {min(n, len(df))} Records ===")
        print(f"Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"Columns: {list(df.columns)}")
        print()
        
        # Display the first n records
        display_df = df.head(n)
        print(display_df.to_string(index=True))
        
        print()
        print(f"Showing {len(display_df)} out of {len(df)} total records")
    
    def display_dataset_info(self, df):
        if df is None:
            print("Error: No dataset provided.")
            return
        
        print("\n=== Dataset Information ===")
        print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"Columns: {list(df.columns)}")
        print(f"Data types:\n{df.dtypes}")
        print(f"\nMissing values:\n{df.isnull().sum()}")
        print(f"\nBasic statistics:\n{df.describe()}")
    
    def visualize_publication_trends(self, analysis_data):
        """Create visualization for publication trends over time"""
        if analysis_data is None:
            return
        
        year_counts = analysis_data['year_counts']
        
        if year_counts.empty:
            print("No publication data available for visualization.")
            return
        
        # Print detailed data in terminal (title removed to avoid duplication)
        # print("=" * 40)
        print(f"{'Year':<8} {'Books Published':<15} {'Trend':<10}")
        print("-" * 35)
        
        years = list(year_counts.index)
        counts = list(year_counts.values)
        
        for i, (year, count) in enumerate(year_counts.items()):
            # Calculate trend indicator
            if i == 0:
                trend = "—"
            else:
                prev_count = counts[i-1]
                if count > prev_count:
                    trend = "Up"
                elif count < prev_count:
                    trend = "Down"
                else:
                    trend = "Same"
            
            print(f"{int(year):<8} {count:<15} {trend:<10}")
        
        # Print summary statistics
        print(f"\nPublication Trends Summary:")
        print(f"   Total years with publications: {analysis_data['total_years']}")
        print(f"   Most productive year: {analysis_data['most_productive_year']} ({analysis_data['most_productive_count']} books)")
        print(f"   Least productive year: {analysis_data['least_productive_year']} ({analysis_data['least_productive_count']} books)")
        print(f"   Average books per year: {year_counts.mean():.1f}")
        print(f"   Total books analyzed: {year_counts.sum()}")
        
        # Calculate trend direction
        if len(counts) > 1:
            overall_trend = "increasing" if counts[-1] > counts[0] else "decreasing" if counts[-1] < counts[0] else "stable"
            print(f"   Overall trend: {overall_trend}")
        
        # Create trend line chart visualization
        plt.figure(figsize=(14, 8))
        
        # Main trend line
        plt.plot(years, counts, marker='o', linewidth=3, markersize=8, 
                color='darkblue', markerfacecolor='lightblue', markeredgecolor='darkblue', 
                markeredgewidth=2, label='Publication Trend')
        
        # Add trend line (linear regression)
        if len(years) > 1:
            z = np.polyfit(years, counts, 1)
            p = np.poly1d(z)
            plt.plot(years, p(years), "--", alpha=0.8, color='red', linewidth=2, label='Trend Line')
        
        plt.title('Publication Trends Over Time', fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Year', fontsize=14, fontweight='bold')
        plt.ylabel('Number of Books Published', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, linestyle='--')
        plt.xticks(years, rotation=45)
        plt.legend(fontsize=12)
        
        # Add value labels on data points
        for year, count in zip(years, counts):
            plt.annotate(f'{count}', (year, count), textcoords="offset points", 
                        xytext=(0,10), ha='center', fontsize=10, fontweight='bold')
        
        # Highlight highest and lowest points
        max_idx = counts.index(max(counts))
        min_idx = counts.index(min(counts))
        
        plt.scatter(years[max_idx], counts[max_idx], color='green', s=150, alpha=0.7, label='Peak Year')
        plt.scatter(years[min_idx], counts[min_idx], color='red', s=150, alpha=0.7, label='Lowest Year')
        
        plt.tight_layout()
        plt.legend(fontsize=10)
        
        # Show plot non-blocking and automatically close after displaying
        plt.show(block=False)
        plt.pause(0.1)  # Small pause to ensure plot is displayed
        
        # Close the plot automatically after a short time
        # User can still see it but doesn't need to manually close it
        print("\nGraph displayed! (Graph will close automatically)")
    
    def visualize_top_authors(self, analysis_data):
        """Create visualization for top prolific authors"""
        if analysis_data is None:
            return
        
        author_counts = analysis_data['author_counts']
        
        if author_counts.empty:
            print("No author data available for visualization.")
            return
        
        # Print summary first (removed redundant title)
        print(f"\nTop Authors Summary:")
        for i, (author, count) in enumerate(author_counts.items(), 1):
            print(f"   {i}. {author}: {count} books")
        
        plt.figure(figsize=(12, 8))
        
        # Horizontal bar chart
        plt.subplot(2, 1, 1)
        bars = plt.barh(range(len(author_counts)), author_counts.values, color='lightcoral')
        plt.yticks(range(len(author_counts)), author_counts.index)
        plt.xlabel('Number of Books', fontsize=12)
        plt.title(f'Top {analysis_data["top_n"]} Most Prolific Authors', fontsize=14, fontweight='bold')
        plt.gca().invert_yaxis()
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                    str(author_counts.values[i]), va='center', fontsize=10)
        
        # Pie chart
        plt.subplot(2, 1, 2)
        plt.pie(author_counts.values, labels=author_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Books Among Top Authors', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGraph displayed! (Graph will close automatically)")
    
    def visualize_language_distribution(self, analysis_data):
        """Create visualization for language distribution"""
        if analysis_data is None:
            return
        
        lang_counts = analysis_data['lang_counts']
        lang_percentages = analysis_data['lang_percentages']
        
        if lang_counts.empty:
            print("No language data available for visualization.")
            return
        
        # Print summary first (removed redundant title)
        print(f"\nLanguage Distribution Summary ({analysis_data['total_books']} total books):")
        for lang, count in lang_counts.items():
            percentage = lang_percentages[lang]
            print(f"   {lang}: {count} books ({percentage}%)")
        
        plt.figure(figsize=(14, 6))
        
        # Bar chart
        plt.subplot(1, 2, 1)
        bars = plt.bar(range(len(lang_counts)), lang_counts.values, color='lightgreen', alpha=0.7)
        plt.xticks(range(len(lang_counts)), lang_counts.index, rotation=45)
        plt.xlabel('Language Code', fontsize=12)
        plt.ylabel('Number of Books', fontsize=12)
        plt.title('Language Distribution of Books', fontsize=14, fontweight='bold')
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                    str(lang_counts.values[i]), ha='center', va='bottom', fontsize=10)
        
        # Pie chart for top languages
        plt.subplot(1, 2, 2)
        top_langs = lang_counts.head(8)  # Show top 8 languages
        others_count = lang_counts.tail(len(lang_counts) - 8).sum() if len(lang_counts) > 8 else 0
        
        if others_count > 0:
            pie_data = list(top_langs.values) + [others_count]
            pie_labels = list(top_langs.index) + ['Others']
        else:
            pie_data = top_langs.values
            pie_labels = top_langs.index
        
        plt.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90)
        plt.title('Language Distribution (Pie Chart)', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGraph displayed! (Graph will close automatically)")
    
    def visualize_books_by_publisher(self, analysis_data):
        """Create visualization for books by publisher"""
        if analysis_data is None:
            return
        
        publisher_counts = analysis_data['publisher_counts']
        
        if publisher_counts.empty:
            print("No publisher data available for visualization.")
            return
        
        # Print summary first (removed redundant title)
        print(f"\nPublisher Summary:")
        print(f"   Total publishers: {analysis_data['total_publishers']}")
        print(f"   Top {analysis_data['top_n']} publishers:")
        for i, (publisher, count) in enumerate(publisher_counts.items(), 1):
            print(f"   {i}. {publisher}: {count} books")
        
        plt.figure(figsize=(14, 10))
        
        # Horizontal bar chart for better readability
        bars = plt.barh(range(len(publisher_counts)), publisher_counts.values, color='orange', alpha=0.7)
        plt.yticks(range(len(publisher_counts)), publisher_counts.index)
        plt.xlabel('Number of Books', fontsize=12)
        plt.title(f'Top {analysis_data["top_n"]} Publishers by Number of Books', fontsize=14, fontweight='bold')
        
        # Invert y-axis BEFORE setting ylabel
        plt.gca().invert_yaxis()
        
        # Set ylabel after inversion
        plt.ylabel('Publisher', fontsize=12)
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                    str(publisher_counts.values[i]), va='center', fontsize=10)
        
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGraph displayed! (Graph will close automatically)")
    
    def visualize_missing_isbn(self, analysis_data, show_graph=True):
        """Create visualization for missing ISBN analysis"""
        if analysis_data is None:
            return
        
        isbn_analysis = analysis_data['isbn_analysis']
        
        if not isbn_analysis:
            print("No ISBN data available for visualization.")
            return
        
        # Print summary first (always show this)
        isbn_cols = list(isbn_analysis.keys())
        for isbn_col in isbn_cols:
            data = isbn_analysis[isbn_col]
            print(f"\n   {isbn_col.upper()}:")
            print(f"     Total records: {data['total_records']}")
            print(f"     Present: {data['present_count']}")
            print(f"     Missing: {data['missing_count']}")
            print(f"     Missing percentage: {data['missing_percentage']:.2f}%")
        
        # Only show graph if requested
        if not show_graph:
            return
            
        # Prepare data for visualization
        missing_counts = [isbn_analysis[col]['missing_count'] for col in isbn_cols]
        present_counts = [isbn_analysis[col]['present_count'] for col in isbn_cols]
        missing_percentages = [isbn_analysis[col]['missing_percentage'] for col in isbn_cols]
        
        plt.figure(figsize=(14, 8))
        
        # Stacked bar chart
        plt.subplot(2, 2, 1)
        x_pos = range(len(isbn_cols))
        plt.bar(x_pos, present_counts, label='Present', color='lightgreen', alpha=0.7)
        plt.bar(x_pos, missing_counts, bottom=present_counts, label='Missing', color='lightcoral', alpha=0.7)
        plt.xticks(x_pos, isbn_cols, rotation=45)
        plt.ylabel('Number of Records')
        plt.title('ISBN Data Completeness', fontsize=12, fontweight='bold')
        plt.legend()
        
        # Missing percentage chart
        plt.subplot(2, 2, 2)
        bars = plt.bar(x_pos, missing_percentages, color='red', alpha=0.6)
        plt.xticks(x_pos, isbn_cols, rotation=45)
        plt.ylabel('Missing Percentage (%)')
        plt.title('Missing ISBN Percentage', fontsize=12, fontweight='bold')
        
        # Add percentage labels
        for i, bar in enumerate(bars):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f'{missing_percentages[i]:.1f}%', ha='center', va='bottom')
        
        # Pie chart for each ISBN column
        for i, isbn_col in enumerate(isbn_cols):
            plt.subplot(2, 2, 3 + i)
            data = [present_counts[i], missing_counts[i]]
            labels = ['Present', 'Missing']
            colors = ['lightgreen', 'lightcoral']
            plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title(f'{isbn_col.upper()} Distribution', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGraph displayed! (Graph will close automatically)")
    
    def visualize_books_per_year_by_language(self, analysis_data):
        """Create visualization for books per year by language"""
        if analysis_data is None:
            return
        
        year_lang_counts = analysis_data['year_lang_counts']
        
        if year_lang_counts.empty:
            print("No year-language data available for visualization.")
            return
        
        # Print summary first (removed redundant title)
        print(f"\nBooks Per Year by Language Summary (First 1000 records only):")
        for year in analysis_data['years']:
            print(f"\n   {int(year)}:")
            for lang in analysis_data['languages']:
                count = year_lang_counts.loc[year, lang]
                if count > 0:
                    print(f"     {lang}: {count} books")
        
        # Create clustered bar chart
        plt.figure(figsize=(16, 10))
        
        # Clustered bar chart
        plt.subplot(2, 1, 1)
        year_lang_counts.plot(kind='bar', ax=plt.gca(), figsize=(16, 6), width=0.8)
        plt.title('Books Published Per Year by Language - First 1000 Records (Clustered Bar Chart)', fontsize=14, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Books', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Language', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars (for readability, only show non-zero values)
        for i, year in enumerate(year_lang_counts.index):
            for j, lang in enumerate(year_lang_counts.columns):
                value = year_lang_counts.loc[year, lang]
                if value > 0:  # Only show non-zero values to avoid clutter
                    plt.text(i + (j - len(year_lang_counts.columns)/2) * 0.1, value + 1, 
                            str(value), ha='center', va='bottom', fontsize=8)
        
        # Heatmap for better visualization of patterns
        plt.subplot(2, 1, 2)
        sns.heatmap(year_lang_counts.T, annot=True, fmt='d', cmap='YlOrRd', 
                   cbar_kws={'label': 'Number of Books'})
        plt.title('Books by Year and Language - First 1000 Records (Heatmap)', fontsize=14, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Language', fontsize=12)
        
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGraph displayed! (Graph will close automatically)")
