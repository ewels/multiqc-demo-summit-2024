import multiqc
import sqlite3

# Load data
multiqc.parse_logs('./fastp')

# Fetch from database
metadata = {}
cx = sqlite3.connect("metadata.db")
for row in cx.cursor().execute("select * from metadata"):
    metadata[row[0]] = {
        'Input DNA (ng)': row[1],
        'Sample Origin': row[2]
    }

# Add data to report
metadata_module = multiqc.BaseMultiqcModule()
metadata_module.general_stats_addcols(data_by_sample=metadata)
multiqc.report.modules.append(metadata_module)

# Write the report
multiqc.write_report(force=True)
