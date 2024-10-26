import multiqc

# Load data
multiqc.parse_logs('./fastp')

# Fetch the custom data
fastp_data = multiqc.get_module_data(module="fastp")
reads_before_filtering = {
    s: {
        'Reads Before Filtering': d['summary']['before_filtering']['total_reads']
    }
    for s, d in fastp_data.items()
}

# Add new column to the General Stats table
fastp_module = multiqc.report.modules[0]
fastp_module.general_stats_addcols(data_by_sample=reads_before_filtering)

# Write the report
multiqc.write_report(force=True)
