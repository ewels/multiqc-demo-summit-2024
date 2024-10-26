import multiqc

# Load data
multiqc.parse_logs('./fastp')

# Write the report
multiqc.write_report(force=True)
