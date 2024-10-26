

# MultiQC scripts demo

> **Nextflow Summit 2024 - Barcelona**
> Phil Ewels, Thurs Oct 31, 2024

## Demo steps
1. `part_1` - In-browser run using WASM
    * Drop `fastp` and `fastqc` dirs into seqera.io/multiqc and generate a report
    * Go back and drop the `multiqc_config.yml`, run again
2. `part_2` - CLI run with custom content
    * ```bash
      multiqc .
      ```
    * Runs MultiQC in the terminal, using just `fastq`.
      Includes the _"percent magic"_ data from Custom Content into General Stats.
3. `part_3` - Python script - basic
    * ```bash
      python run_multiqc.py
      ```
    * Runs `fastp` again, but now from a script.
4. `part_4` - Python script - preprocess
    * ```bash
      python run_multiqc.py
      ```
    * Adds an extra column to General Stats, using data parsed from Fastp but not normally used.
5. `part_5` - Python script - pull data from database
    * Show the `metadata.db` database in VSCode with extension
    * ```bash
      python run_multiqc.py
      ```
    * Pulls in some data from a local mysqlite database and adds to General Stats
6. `part_6` - TODO: Jupyter Notebook
    * Version of the script as an annotated Juypter Notebook
7. `part_7` - Streamlit app
    * ```bash
      streamlit run multiqc_app.py
      ```
    * Turns script into Streamlit app
8. Seqera AI
    * ```bash
      multiqc .
      ```
    * Uses local CLI with new `ai_summary: true` config
    * Can follow link in report to continue discussion in Seqera AI


# Data

Data taken from the [nf-core/viralrecon](https://nf-co.re/viralrecon) pipeline.

```bash
aws s3 sync s3://nf-core-awsmegatests/viralrecon/results-3731dd3a32a67a2648ea22c2bd980c224abdaee2/platform_illumina/ . \
  --exclude "*.bam" \
  --exclude "*.fa" \
  --exclude "*.fasta" \
  --exclude "*.crunch" \
  --exclude "*.bai" \
  --exclude "*.gz" \
  --exclude "*.fastq" \
  --exclude "*.fq" \
  --exclude "*.pdf" \
  --exclude "*.vcf" \
  --exclude "*.tbi" \
  --exclude "*.h5" \
  --exclude "*.png" \
  --exclude "*.svg" \
  --exclude "*.tiling" \
  --exclude "*.delta" \
  --exclude "*_tmp" \
  --exclude "*configs.txt"
```
