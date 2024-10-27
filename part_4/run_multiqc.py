import multiqc

# Load data
multiqc.parse_logs('./fastp')

# Fetch the custom data
reads = {}
for samp, data in multiqc.get_module_data(module='fastp').items():
    reads[samp] = {
      'Reads Before Filtering': data['summary']['before_filtering']['total_reads']
    }

# Add new column to the General Stats table
fastp_module = multiqc.report.modules[0]
fastp_module.general_stats_addcols(data_by_sample=reads)

# Write the report
multiqc.write_report(force=True)
